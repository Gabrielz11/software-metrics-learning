# Exemplo Completo de Contagem APF: Sistema de Biblioteca

Este capítulo apresenta a contagem de Pontos de Função detalhada do *Sistema de Biblioteca* fictício.

---

## 1. Escopo e Requisitos

### Requisitos Funcionais
- RF01 — Cadastrar usuário
- RF02 — Atualizar usuário
- RF03 — Cadastrar livro
- RF04 — Realizar empréstimo
- RF05 — Registrar devolução
- RF06 — Consultar livro
- RF07 — Consultar empréstimos
- RF08 — Gerar relatório de empréstimos atrasados

---

## 2. Identificação das Funções de Dados

| Identificador | Nome | Tipo | RET | DET | Complexidade | Pontos de Função |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **ALI_01** | Tabela Usuário | ALI | 1 | 5 | Baixa | 7 PF |
| **ALI_02** | Tabela Livro | ALI | 1 | 6 | Baixa | 7 PF |
| **ALI_03** | Tabela Empréstimo | ALI | 1 | 6 | Baixa | 7 PF |
| **AIE_01** | Consulta Serasa/Crédito | AIE | 1 | 3 | Baixa | 5 PF |
| **Subtotal Dados** | | | | | | **26 PF** |

---

## 3. Identificação das Funções Transacionais

| Identificador | Nome | Tipo | FTR | DET | Complexidade | Pontos de Função |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **EE_01** | Cadastrar Usuário | EE | 1 | 3 | Baixa | 3 PF |
| **EE_02** | Atualizar Usuário | EE | 1 | 3 | Baixa | 3 PF |
| **EE_03** | Cadastrar Livro | EE | 1 | 3 | Baixa | 3 PF |
| **EE_04** | Realizar Empréstimo | EE | 3 | 2 | Média | 4 PF |
| **EE_05** | Registrar Devolução | EE | 2 | 1 | Baixa | 3 PF |
| **CE_01** | Consultar Livro | CE | 1 | 5 | Baixa | 3 PF |
| **CE_02** | Consultar Empréstimos | CE | 2 | 4 | Baixa | 3 PF |
| **SE_01** | Relatório de Atrasos | SE | 3 | 8 | Média | 5 PF |
| **Subtotal Transações** | | | | | | **27 PF** |

---

## 4. Resultado da Contagem Total

$$\text{Tamanho Funcional Total} = 26\text{ PF (Dados)} + 27\text{ PF (Transações)} = 53\text{ Pontos de Função}$$

---

## 5. Você consegue responder?
1. Quantas funções de dados e quantas funções transacionais compõem o Sistema de Biblioteca?
2. Por que a transação `Realizar Empréstimo` possui complexidade média (EE com 3 FTRs)?
3. Qual o subtotal de Pontos de Função de Dados do sistema?
4. Qual a diferença de complexidade entre `Consultar Livro` (CE) e `Relatório de Atrasos` (SE)?
5. Como os 53 PF obtidos nesta contagem auxiliam no orçamento do projeto?

---

## 📚 Referências utilizadas
- **IFPUG**. *Function Point Counting Practices Manual*, Release 4.3.1.
