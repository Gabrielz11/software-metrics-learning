# Definição do Objetivo (Goal) em GQM

Segundo Basili, um **Objetivo (Goal)** em GQM deve obrigatoriamente ser formalizado contendo **cinco elementos estruturais**.

---

## 1. As 5 Dimensões de um Objetivo GQM

```text
ESTRUTURA DE UM GOAL GQM:
├── Objeto: O que está sendo analisado? (Produto, Processo ou Recurso)
├── Propósito: Qual a intenção da medição? (Avaliar, Controlar, Melhorar, Prever)
├── Foco de Qualidade: Qual o atributo de interesse? (Confiabilidade, Produtividade, Custo)
├── Ponto de Vista: Quem é o interessado nos resultados? (Gerente, Desenvolvedor, Cliente)
└── Contexto: Em qual ambiente ocorre a análise? (Sistema de Biblioteca, Equipe X)
```

---

## 2. Exemplo no Sistema de Biblioteca

!!! example "Objetivo Formalizado GQM"
    - **Objeto**: O processo de teste e release do *Sistema de Biblioteca*.
    - **Propósito**: Avaliar e melhorar.
    - **Foco de Qualidade**: A confiabilidade e a redução de falhas em produção.
    - **Ponto de Vista**: O Gerente de Engenharia de Software.
    - **Contexto**: O ambiente de produção da Release 1.0.

---

## 3. Você consegue responder?
1. Quais são os 5 elementos obrigatórios de uma definição de Objetivo em GQM?
2. Por que o "Ponto de Vista" é fundamental na definição do Objetivo?
3. Dê dois exemplos de "Propósito" em um Objetivo GQM.
4. Escreva um objetivo GQM formalizado para o módulo de pagamentos de uma loja virtual.
5. O que distingue o "Objeto" do "Contexto" na estrutura de Basili?

??? check "Mostrar Gabarito / Resposta"
    1. **5 Elementos do Objetivo GQM:** Objeto (*Object*), Propósito (*Purpose*), Foco de Qualidade (*Quality Focus*), Ponto de Vista (*Viewpoint*) e Contexto (*Environment/Context*).
    2. **Importância do Ponto de Vista:** Porque o conceito de qualidade ou sucesso varia de acordo com quem analisa os dados (ex: o que é prioridade para o Gerente Financeiro difere do que é prioridade para o Arquiteto de Software).
    3. **Exemplos de Propósito:** "Analisar para compreender", "Analisar para avaliar", "Analisar para melhorar" ou "Analisar para controlar".
    4. **Exemplo de Objetivo formalizado:**
       - *Analisar* o módulo de pagamentos checkout
       - *Com o propósito de* avaliar e reduzir a taxa de rejeição de transações
       - *Sob o foco de* confiabilidade e desempenho
       - *Do ponto de vista do* Gerente de Produto (PO)
       - *No contexto do* ambiente de produção da loja virtual.
    5. **Objeto vs. Contexto:** Objeto é o processo, produto ou recurso específico sendo analisado (ex: módulo de login). Contexto é o ambiente organizacional ou de execução onde esse objeto opera (ex: equipe alfa na release 2.0).

---

## 📚 Referências utilizadas
- **Basili, V. R., Caldiera, G., & Rombach, H. D.** *The Goal Question Metric Approach*, 1994.
