
# ==========================================
# SISTEMA DE PAGAMENTO DE BENEFICIOS
# Projeto academico - Python
# Disciplina Inovação em Soluções Computacionais
# ==========================================

class PagamentoBeneficios:

    # 1. CONSTRUCTOR
    # Inicializa os dados do beneficiario.
    def __init__(self, nome, valor, oraculo):
        self.nome = nome
        self.valor = valor
        self.oraculo = oraculo

        # 2. ATRIBUTOS (variaveis de estado)
        self.atestado_obito = False

        # 3. DICIONARIO (MAP)
        # Armazena os pagamentos realizados.
        self.pagamentos = {}

    # 4. METODO: consulta ao oraculo
    def consultar_oraculo(self, usuario, obito):

        # 5. USUARIO COMO PARAMETRO
        if usuario != self.oraculo:
            raise PermissionError(
                "Apenas o oraculo autorizado pode atualizar os dados."
            )

        self.atestado_obito = obito

        if obito:
            return "Atestado de obito encontrado!"
        else:
            return "Nenhum atestado de obito encontrado!"

    # 6. METODO: pagamento do beneficio
    def pagar_beneficio(self, usuario, mes):

        if usuario != self.nome:
            raise PermissionError(
                "Somente o beneficiario pode solicitar o pagamento."
            )

        # 7. IF + ERRO
        if self.atestado_obito:
            raise ValueError(
                "Pagamento bloqueado: existe atestado de obito."
            )

        if mes in self.pagamentos:
            raise ValueError(
                "O beneficio deste mes ja foi pago."
            )

        # Registra o pagamento no dicionario.
        self.pagamentos[mes] = self.valor

        return (
            f"Pagamento aprovado para {self.nome}!\n"
            f"Valor: R$ {self.valor:.2f}\n"
            f"Mes: {mes}"
        )


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def iniciar_sistema():

    print("\n===================================")
    print("    PAGAMENTO DE BENEFICIOS")
    print("===================================")

    nome = input("Nome do beneficiario: ").strip()

    while not nome:
        nome = input("Informe um nome valido: ").strip()

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

    oraculo = input("Identificacao do oraculo: ").strip()

    while not oraculo:
        oraculo = input("Informe o identificador do oraculo: ").strip()

    # Criacao do objeto utilizando o constructor.
    sistema = PagamentoBeneficios(nome, valor, oraculo)

    while True:

        print("\n========== MENU ==========")
        print("1 - Consultar oraculo")
        print("2 - Solicitar pagamento")
        print("3 - Consultar pagamentos")
        print("0 - Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":

            usuario = input("Identificacao do oraculo: ")
            resposta = input(
                "Existe atestado de obito? (s/n): "
            ).strip().lower()

            if resposta not in ("s", "n"):
                print("Digite s ou n.")
                continue

            try:
                resultado = sistema.consultar_oraculo(
                    usuario, resposta == "s"
                )
                print("\nORACULO:", resultado)

            except PermissionError as erro:
                print("\nERRO:", erro)

        elif opcao == "2":

            usuario = input("Nome do beneficiario: ")
            mes = input("Mes de referencia (ex: 11/2026): ")

            try:
                resultado = sistema.pagar_beneficio(usuario, mes)
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

        elif opcao == "0":

            print("Sistema encerrado.")
            break

        else:
            print("Opcao invalida. Tente novamente.")


# Executa o programa.
if __name__ == "__main__":
    iniciar_sistema()
