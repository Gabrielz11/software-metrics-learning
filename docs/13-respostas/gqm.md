# Respostas: Paradigma GQM

---

### Solução do Exemplo 01 🟢
- **Objeto**: O processo de testes automatizados.
- **Propósito**: Aumentar.
- **Foco de Qualidade**: A cobertura de código.
- **Ponto de Vista**: O Líder Técnico.
- **Contexto**: O projeto Sistema de Biblioteca.

---

### Solução do Exemplo 02 🟡
- **GOAL**: Melhorar a previsibilidade de entregas das sprints sob a ótica do Scrum Master.
- **Question 1**: Quanto a quantidade de trabalho entregue varia entre sprints?
  - *Métrica 1.1*: Desvio padrão do Velocity (Story Points/sprint)
  - *Métrica 1.2*: Percentual de histórias completadas vs planejadas (%)
- **Question 2**: Quanto o escopo flutua após o início da sprint?
  - *Métrica 2.1*: Quantidade de pontos adicionados pós-Sprint Planning
  - *Métrica 2.2*: Quantidade de pontos removidos pós-Sprint Planning

---

### Solução do Exemplo 03 🔴
```mermaid
flowchart TD
    G[GOAL: Reduzir o custo de manutenção corretiva pós-release de sistemas legados sob a ótica da Diretoria de TI no ambiente corporativo]
    G --> Q1[Q1: Qual o volume financeiro e horas gastas em correções de bugs pós-release?]
    G --> Q2[Q2: Em quais módulos concentram-se os defeitos mais caros de corrigir?]
    G --> Q3[Q3: Qual a eficiência atual da esteira de testes de regressão?]

    Q1 --> M1[M1: Horas de timesheet apontadas em manutenção corretiva]
    Q1 --> M2[M2: Custo total em R$ do esforço de correção de falhas]

    Q2 --> M3[M3: Densidade de defeitos por módulo em KLOC]

    Q3 --> M4[M4: Defect Removal Efficiency - DRE %]
```
