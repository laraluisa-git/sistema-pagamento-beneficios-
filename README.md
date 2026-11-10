# Sistema de Pagamento de Benefícios

## Sobre o projeto

Sistema desenvolvido em Python para demonstrar a automatização do pagamento mensal de benefícios utilizando uma regra de negócio baseada na validação de atestado de óbito por um oráculo. 

EQUIPE 5 - Disciplina Inovação em Soluções Computacionais

## Regra de negócio

O pagamento mensal somente será liberado quando não existir atestado de óbito registrado pelo oráculo.

## Funcionalidades

- Cadastro do beneficiário.
- Definição do valor do benefício.
- Consulta ao oráculo.
- Registro de atestado de óbito.
- Liberação ou bloqueio do pagamento.
- Histórico de pagamentos mensais.
- Prevenção de pagamentos duplicados.

## Conceitos utilizados

| Conceito | Implementação |
|---|---|
| Class | `PagamentoBeneficios` |
| Atributo | Nome, valor e situação do óbito |
| Método | `consultar_oraculo()` e `pagar_beneficio()` |
| If + erro | `raise ValueError` e `PermissionError` |
| Usuário | Parâmetro `usuario` |
| Dicionário / Map | `pagamentos` |
| Constructor | `__init__()` |

## Tecnologias

- Python 3
- Programação Orientada a Objetos

## Como executar

1. Instale o Python 3.
2. Abra a pasta do projeto no VS Code.
3. Abra o terminal.
4. Execute:

```bash
python main.py
```

No Windows, também pode utilizar:

```bash
py main.py
```

---

# Testes do sistema

Os testes abaixo demonstram o funcionamento das regras de negócio implementadas.

## 1. Teste: pagamento aprovado

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
```

## 2. Teste: pagamento bloqueado por óbito

**Passo 1:** Escolha novamente a opção `1` (Consultar oráculo).

Informe:

```text
Identificação do oráculo: ORACULO01
Existe atestado de óbito? s
```

Resultado esperado:

```text
ORACULO: Atestado de óbito encontrado!
```

**Passo 2:** Escolha a opção `2` (Solicitar pagamento).

Informe:

```text
Nome do beneficiário: João
Mês de referência: 12/2026
```

Resultado esperado:

```text
ERRO: Pagamento bloqueado: existe atestado de óbito.
```

O sistema impede a liberação do benefício porque existe um registro de óbito.

## 3. Teste: impedir pagamento duplicado

Execute novamente o programa.

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

O pagamento será aprovado.

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

---

## Observação

Este é um projeto acadêmico demonstrativo. O oráculo e o registro dos pagamentos são simulados localmente em Python, sem integração real com uma rede blockchain, cartório ou sistema bancário.

## Autor

Projeto desenvolvido para fins acadêmicos e de aprendizagem da disciplina de Inovação em Soluções Computacionais.# sistema-pagamento-beneficios-
