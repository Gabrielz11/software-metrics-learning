# Lead Time e Cycle Time

A diferenciação clara entre **Lead Time** e **Cycle Time** é a chave para a análise de eficiência de fluxo de valor (Lean / Kanban).

---

## 1. Diagrama Comparativo de Fluxo

```text
Solicitação do Cliente (Backlog)
       │
       ├─────────────────────────────────────────┐
       │                                         │
       ▼                                         │
Trabalho Iniciado (In Progress)                  │ Lead Time
       │                                         │
       ├───────────────────────┐                 │
       │                       │ Cycle Time      │
       ▼                       │                 │
Trabalho Concluído (Done) ─────┴─────────────────┴
```

- **Lead Time**: Tempo decorrido desde a solicitação do cliente (criação do card/item no backlog) até a entrega final em produção.
- **Cycle Time**: Tempo decorrido desde o início ativo do desenvolvimento do item até a sua conclusão.

---

## 2. Exemplo Prático no Sistema de Biblioteca

!!! example "Lead Time vs Cycle Time"
    - **Segunda-feira 08:00**: Usuário abre a solicitação de um novo relatório de atrasos no backlog (Início do Lead Time).
    - **Quarta-feira 14:00**: Desenvolvedor puxa a tarefa para "Em Desenvolvimento" (Início do Cycle Time).
    - **Sexta-feira 17:00**: O código é testado e feito o deploy em produção (Fim do Lead Time e Cycle Time).
    - **Cycle Time** = 2 dias e 3 horas.
    - **Lead Time** = 4 dias e 9 horas.

---

## 3. Você consegue responder?
1. Qual a diferença fundamental entre Lead Time e Cycle Time?
2. Por que o Lead Time inclui o tempo em que o item ficou parado no backlog?
3. Como a redução do tempo de espera (*Queue Time*) impacta o Lead Time?
4. Qual das duas métricas reflete melhor a experiência direta do cliente final?
5. Qual das duas métricas reflete a eficiência técnica direta do time de desenvolvimento?

---

## 📚 Referências utilizadas
- **Anderson, David J.** *Kanban: Successful Evolutionary Change for Your Technology Business*, Blue Hole Press.
