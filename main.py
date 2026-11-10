
# ==========================================
# SISTEMA DE PAGAMENTO DE BENEFICIOS
# Projeto academico - Python
# Disciplina: Inovacao em Solucoes Computacionais
# ==========================================

import hashlib
import json
from datetime import datetime


# ==========================================
# 1. CLASSE BLOCO - BLOCKCHAIN
# ==========================================

class Bloco:

    def __init__(self, indice, dados, hash_anterior):

        self.indice = indice
        self.dados = dados
        self.data = datetime.now().isoformat()
        self.hash_anterior = hash_anterior
        self.nonce = 0

        self.hash = self.gerar_hash()

    # Gera o hash criptografico do bloco.
    def gerar_hash(self):

        conteudo = json.dumps({
            "indice": self.indice,
            "dados": self.dados,
            "data": self.data,
            "hash_anterior": self.hash_anterior,
            "nonce": self.nonce
        }, sort_keys=True, ensure_ascii=False)

        return hashlib.sha256(
            conteudo.encode()
        ).hexdigest()

    # Executa a prova de trabalho (Proof of Work).
    def minerar(self, dificuldade=2):

        prefixo = "0" * dificuldade

        while not self.hash.startswith(prefixo):

            self.nonce += 1
            self.hash = self.gerar_hash()


# ==========================================
# 2. CLASSE BLOCKCHAIN
# ==========================================

class Blockchain:

    def __init__(self):

        self.dificuldade = 2
        self.cadeia = []

        # Cria o primeiro bloco (Genesis).
        bloco_inicial = Bloco(
            0,
            {"mensagem": "Bloco Genesis"},
            "0"
        )

        bloco_inicial.minerar(self.dificuldade)
        self.cadeia.append(bloco_inicial)

    # Retorna o ultimo bloco da cadeia.
    def ultimo_bloco(self):

        return self.cadeia[-1]

    # Adiciona um novo bloco a blockchain.
    def adicionar_bloco(self, dados):

        anterior = self.ultimo_bloco()

        novo_bloco = Bloco(
            len(self.cadeia),
            dados,
            anterior.hash
        )

        novo_bloco.minerar(self.dificuldade)
        self.cadeia.append(novo_bloco)

        return novo_bloco.hash

    # Verifica a integridade de toda a cadeia.
    def validar_cadeia(self):

        for i in range(1, len(self.cadeia)):

            atual = self.cadeia[i]
            anterior = self.cadeia[i - 1]

            # Verifica o hash do bloco.
            if atual.hash != atual.gerar_hash():
                return False

            # Verifica o encadeamento dos blocos.
            if atual.hash_anterior != anterior.hash:
                return False

            # Verifica a prova de trabalho.
            if not atual.hash.startswith(
                "0" * self.dificuldade
            ):
                return False

        return True

    # Exibe todos os blocos da blockchain.
    def exibir_cadeia(self):

        for bloco in self.cadeia:

            print("\n===================================")
            print("BLOCO:", bloco.indice)
            print("DATA:", bloco.data)
            print("DADOS:", bloco.dados)
            print("HASH:", bloco.hash)
            print("HASH ANTERIOR:", bloco.hash_anterior)
            print("NONCE:", bloco.nonce)

        print("\n===================================")


# ==========================================
# 3. CLASSE PAGAMENTO DE BENEFICIOS
# ==========================================

class PagamentoBeneficios:

    # Constructor: inicializa os dados do beneficiario.
    def __init__(self, nome, valor, oraculo):

        self.nome = nome
        self.valor = valor
        self.oraculo = oraculo

        # Atributo de estado.
        self.atestado_obito = False

        # Dicionario (MAP) de pagamentos realizados.
        self.pagamentos = {}

        # Instancia da blockchain.
        self.blockchain = Blockchain()

    # Consulta ao oraculo autorizado.
    def consultar_oraculo(self, usuario, obito):

        if usuario != self.oraculo:

            raise PermissionError(
                "Apenas o oraculo autorizado pode atualizar os dados."
            )

        self.atestado_obito = obito

        if obito:
            return "Atestado de obito encontrado!"

        else:
            return "Nenhum atestado de obito encontrado!"

    # Realiza o pagamento do beneficio.
    def pagar_beneficio(self, usuario, mes):

        if usuario != self.nome:

            raise PermissionError(
                "Somente o beneficiario pode solicitar o pagamento."
            )

        if self.atestado_obito:

            raise ValueError(
                "Pagamento bloqueado: existe atestado de obito."
            )

        if not mes:

            raise ValueError(
                "Informe um mes de referencia valido."
            )

        if mes in self.pagamentos:

            raise ValueError(
                "O beneficio deste mes ja foi pago."
            )

        # Cria os dados da transacao.
        transacao = {
            "beneficiario": self.nome,
            "valor": self.valor,
            "mes": mes,
            "status": "Pagamento aprovado"
        }

        # Registra a transacao na blockchain.
        hash_transacao = self.blockchain.adicionar_bloco(
            transacao
        )

        # Registra o pagamento no dicionario.
        self.pagamentos[mes] = self.valor

        return (
            f"Pagamento aprovado para {self.nome}!\n"
            f"Valor: R$ {self.valor:.2f}\n"
            f"Mes: {mes}\n"
            f"Hash Blockchain: {hash_transacao}"
        )


# ==========================================
# 4. PROGRAMA PRINCIPAL
# ==========================================

def iniciar_sistema():

    print("\n===================================")
    print("    PAGAMENTO DE BENEFICIOS")
    print("       COM BLOCKCHAIN")
    print("===================================")

    nome = input(
        "Nome do beneficiario: "
    ).strip()

    while not nome:

        nome = input(
            "Informe um nome valido: "
        ).strip()

    while True:

        try:

            valor = float(
                input("Valor do beneficio: R$ ").replace(",", ".")
            )

            if valor <= 0:

                print("O valor deve ser maior que zero.")
                continue

            break

        except ValueError:

            print("Digite um valor numerico valido.")

    oraculo = input(
        "Identificacao do oraculo: "
    ).strip()

    while not oraculo:

        oraculo = input(
            "Informe o identificador do oraculo: "
        ).strip()

    # Criacao do objeto utilizando o constructor.
    sistema = PagamentoBeneficios(
        nome,
        valor,
        oraculo
    )

    while True:

        print("\n========== MENU ==========")
        print("1 - Consultar oraculo")
        print("2 - Solicitar pagamento")
        print("3 - Consultar pagamentos")
        print("4 - Validar Blockchain")
        print("5 - Consultar blocos")
        print("0 - Sair")

        opcao = input(
            "Escolha uma opcao: "
        ).strip()

        if opcao == "1":

            usuario = input(
                "Identificacao do oraculo: "
            )

            resposta = input(
                "Existe atestado de obito? (s/n): "
            ).strip().lower()

            if resposta not in ("s", "n"):

                print("Digite s ou n.")
                continue

            try:

                resultado = sistema.consultar_oraculo(
                    usuario,
                    resposta == "s"
                )

                print("\nORACULO:", resultado)

            except PermissionError as erro:

                print("\nERRO:", erro)

        elif opcao == "2":

            usuario = input(
                "Nome do beneficiario: "
            )

            mes = input(
                "Mes de referencia (ex: 11/2026): "
            ).strip()

            try:

                resultado = sistema.pagar_beneficio(
                    usuario,
                    mes
                )

                print("\n", resultado)

            except (PermissionError, ValueError) as erro:

                print("\nERRO:", erro)

        elif opcao == "3":

            print("\n===== HISTORICO DE PAGAMENTOS =====")

            if not sistema.pagamentos:

                print("Nenhum pagamento realizado.")

            else:

                for mes, valor in sistema.pagamentos.items():

                    print(f"{mes}: R$ {valor:.2f}")

        elif opcao == "4":

            print("\n===== VALIDACAO BLOCKCHAIN =====")

            if sistema.blockchain.validar_cadeia():

                print("Blockchain valida!")
                print("Integridade dos blocos confirmada.")

            else:

                print("ALERTA: Blockchain comprometida!")
                print("Foi detectada uma alteracao na cadeia.")

        elif opcao == "5":

            print("\n===== HISTORICO BLOCKCHAIN =====")

            sistema.blockchain.exibir_cadeia()

        elif opcao == "0":

            print("Sistema encerrado.")
            break

        else:

            print("Opcao invalida. Tente novamente.")


# ==========================================
# 5. EXECUCAO DO PROGRAMA
# ==========================================

if __name__ == "__main__":

    iniciar_sistema()
