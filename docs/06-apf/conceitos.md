# Conceitos Fundamentais IFPUG: Fronteira e Escopo

A correta identificação da **Fronteira da Aplicação** e do **Escopo da Contagem** é o passo inicial indispensável para garantir a repetibilidade de uma contagem APF.

---

## 1. Escopo da Contagem
O escopo define *quais* partes do software estão sendo medidas (ex: o sistema completo, apenas o módulo de relatórios ou uma solicitação de mudança específica).

## 2. Fronteira da Aplicação
A fronteira define o limite entre o software que está sendo medido e o mundo externo (usuários e outros sistemas).

```mermaid
flowchart LR
    subgraph Mundo Externo
        U[Usuário Humano]
        S[Sistema de Crédito Serasa]
    end

    subgraph Fronteira do Sistema de Biblioteca
        A1[(ALI - Usuário)]
        A2[(ALI - Livro)]
        A3[(ALI - Empréstimo)]
        T1[EE - Cadastrar Livro]
        T2[SE - Relatório Atrasos]
    end

    U -->|envia dados| T1
    T1 -->|armazena| A2
    T2 -->|lê dados de| A1
    T2 -->|lê dados de| A3
    S <-->|interface AIE| Fronteira do Sistema de Biblioteca
```

---

## 3. As Cinco Funções IFPUG

```text
FUNCTION POINT ANALYSIS (APF)
          │
          ├── Funções de Dados
          │      ├── ALI (Arquivo Lógico Interno / ILF)
          │      └── AIE (Arquivo de Interface Externa / EIF)
          │
          └── Funções de Transação
                 ├── EE (Entrada Externa / EI)
                 ├── SE (Saída Externa / EO)
                 └── CE (Consulta Externa / EQ)
```

---

## 4. Você consegue responder?
1. Qual a função da Fronteira da Aplicação em uma contagem IFPUG?
2. Como se divide a contagem de Pontos de Função entre dados e transações?
3. O que são Funções de Dados e quais suas siglas em português e inglês?
4. O que são Funções Transacionais e quais suas siglas?
5. Qual a diferença entre escopo da contagem e fronteira da aplicação?

---

## 📚 Referências utilizadas
- **IFPUG**. *Function Point Counting Practices Manual*, Release 4.3.1.
