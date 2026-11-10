# Sistema de Pagamento de Benefícios com Blockchain

## Sobre o projeto

Sistema desenvolvido em Python para demonstrar a automatização do pagamento mensal de benefícios, utilizando uma regra de negócio baseada na validação de atestado de óbito por um oráculo e o registro das transações em uma Blockchain.

**EQUIPE 5** — Disciplina: Inovação em Soluções Computacionais.

O projeto combina Programação Orientada a Objetos (POO) com conceitos de Blockchain, permitindo registrar pagamentos em blocos encadeados e verificar a integridade dos registros por meio de hashes criptográficos.

## Regra de negócio

O pagamento mensal somente será liberado quando não existir atestado de óbito registrado pelo oráculo autorizado.

Cada pagamento aprovado é registrado em um novo bloco na Blockchain, contendo os dados da transação e a referência criptográfica ao bloco anterior.

## Funcionalidades

- Cadastro do beneficiário.
- Definição do valor do benefício.
- Consulta ao oráculo autorizado.
- Registro de atestado de óbito.
- Liberação ou bloqueio do pagamento.
- Histórico de pagamentos mensais.
- Prevenção de pagamentos duplicados.
- Criação automática do bloco Genesis.
- Registro de pagamentos em blocos.
- Geração de hashes criptográficos SHA-256.
- Encadeamento dos blocos por meio do hash anterior.
- Mineração de blocos utilizando Proof of Work.
- Validação da integridade da Blockchain.
- Consulta ao histórico completo de blocos.

## Conceitos utilizados

### Programação Orientada a Objetos

| Conceito | Implementação |
|---|---|
| Class | `PagamentoBeneficios`, `Bloco` e `Blockchain` |
| Constructor | `__init__()` |
| Atributos | Nome, valor, oráculo, pagamentos e situação do óbito |
| Métodos | `consultar_oraculo()`, `pagar_beneficio()` e `adicionar_bloco()` |
| If + erro | `raise ValueError` e `PermissionError` |
| Usuário | Parâmetro `usuario` |
| Dicionário / Map | `pagamentos` |
| Encapsulamento lógico | Organização dos dados e operações nas classes |

### Conceitos de Blockchain

| Conceito | Implementação |
|---|---|
| Bloco Genesis | Primeiro bloco da cadeia |
| Blocos | Classe `Bloco` |
| Blockchain | Classe `Blockchain` |
| Hash criptográfico | SHA-256 utilizando `hashlib` |
| Hash anterior | `hash_anterior` |
| Encadeamento | Referência entre blocos consecutivos |
| Proof of Work | Método `minerar()` |
| Nonce | Contador utilizado durante a mineração |
| Validação | Método `validar_cadeia()` |

## Tecnologias

- Python 3
- Programação Orientada a Objetos (POO)
- Biblioteca `hashlib`
- Biblioteca `json`
- Biblioteca `datetime`
- Algoritmo SHA-256
- Proof of Work

## Como executar

1. Instale o Python 3.
2. Clone o repositório ou baixe os arquivos do projeto.
3. Abra a pasta do projeto no VS Code.
4. Abra o terminal.
5. Execute:

```bash
python main.py
```

No Windows, também pode utilizar:

```bash
py main.py
```

Não é necessário instalar bibliotecas externas, pois o projeto utiliza módulos nativos do Python.

---

# Testes do sistema

Os testes abaixo demonstram o funcionamento das regras de negócio e dos mecanismos de Blockchain implementados.

## 1. Teste: pagamento aprovado e registro na Blockchain

**Dados iniciais:**

- Beneficiário: João
- Valor: R$ 1.500,00
- Oráculo: ORACULO01

**Passo 1:** No menu, escolha a opção `1` (Consultar oráculo).

Informe:

```text
Identificação do oráculo: ORACULO01
Existe atestado de óbito? n
```

Resultado esperado:

```text
ORACULO: Nenhum atestado de óbito encontrado!
```

**Passo 2:** Escolha a opção `2` (Solicitar pagamento).

Informe:

```text
Nome do beneficiário: João
Mês de referência: 11/2026
```

Resultado esperado:

```text
Pagamento aprovado para João!
Valor: R$ 1500.00
Mês: 11/2026
Hash Blockchain: [hash criptográfico gerado]
```

O sistema aprova o pagamento e registra automaticamente a transação em um novo bloco da Blockchain.

## 2. Teste: pagamento bloqueado por óbito

**Passo 1:** Escolha a opção `1` (Consultar oráculo).

Informe:

```text
Identificação do oráculo: ORACULO01
Existe atestado de óbito? s
```

Resultado esperado:

```text
ORACULO: Atestado de obito encontrado!
```

**Passo 2:** Escolha a opção `2` (Solicitar pagamento).

Informe:

```text
Nome do beneficiário: João
Mês de referência: 12/2026
```

Resultado esperado:

```text
ERRO: Pagamento bloqueado: existe atestado de obito.
```

O sistema impede a liberação do benefício e não registra uma nova transação na Blockchain.

## 3. Teste: impedir pagamento duplicado

**Passo 1:** Consulte o oráculo e informe que não existe óbito:

```text
Identificação do oráculo: ORACULO01
Existe atestado de óbito? n
```

**Passo 2:** Realize o pagamento:

```text
Nome do beneficiário: João
Mês de referência: 11/2026
```

O pagamento será aprovado e registrado na Blockchain.

**Passo 3:** Tente realizar novamente o pagamento para o mesmo mês:

```text
Nome do beneficiário: João
Mês de referência: 11/2026
```

Resultado esperado:

```text
ERRO: O beneficio deste mes ja foi pago.
```

O sistema identifica que o pagamento já foi registrado e impede uma segunda liberação para o mesmo mês.

## 4. Teste: validação da Blockchain

Após realizar um pagamento, escolha a opção `4` (Validar Blockchain).

Resultado esperado:

```text
===== VALIDACAO BLOCKCHAIN =====

Blockchain valida!
Integridade dos blocos confirmada.
```

O sistema verifica os hashes dos blocos, o encadeamento entre eles e a prova de trabalho.

## 5. Teste: consultar histórico de blocos

Escolha a opção `5` (Consultar blocos).

O sistema exibirá:

- Índice do bloco.
- Data e horário de criação.
- Dados da transação.
- Hash do bloco.
- Hash do bloco anterior.
- Nonce utilizado na mineração.

O primeiro bloco será o Genesis, seguido pelos blocos correspondentes aos pagamentos aprovados.

## 6. Exemplo de estrutura da Blockchain

```text
BLOCO 0 - GENESIS
       |
       v
BLOCO 1 - PAGAMENTO NOVEMBRO
       |
       v
BLOCO 2 - PAGAMENTO DEZEMBRO
       |
       v
BLOCO 3 - PAGAMENTO JANEIRO
```

Cada bloco contém uma referência criptográfica ao bloco anterior, formando uma cadeia encadeada.

---

## Observações e limitações

Este é um projeto acadêmico demonstrativo. A Blockchain é implementada localmente em Python, utilizando hashes SHA-256 e Proof of Work.

A implementação não possui rede descentralizada, consenso distribuído, integração com Ethereum ou execução de Smart Contracts.

Os blocos são armazenados em memória e, portanto, os registros são perdidos quando o programa é encerrado.

O oráculo também é simulado localmente, sem integração real com cartórios, bancos ou sistemas governamentais.

## Equipe

Projeto desenvolvido pela **Equipe 5**, para fins acadêmicos e de aprendizagem da disciplina de Inovação em Soluções Computacionais.
