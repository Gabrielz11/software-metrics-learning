# Throughput (Vazão de Entregas)

O **Throughput** mede a quantidade de entregáveis (Histórias, Tarefas, Bugs ou Pontos) concluídos por unidade de tempo (ex: por semana ou por sprint).

---

## 1. Lei de Little e Throughput

Na teoria das filas (Lean System), a **Lei de Little** relaciona o Throughput com o Trabalho em Progresso (*Work In Progress - WIP*) e o Cycle Time:

$$\text{WIP} = \text{Throughput} \times \text{Cycle Time}$$

$$\text{Throughput} = \frac{\text{WIP}}{\text{Cycle Time}}$$

---

## 2. Princípio do WIP Limite
Para aumentar o Throughput sem sobrecarregar a equipe, o caminho mais eficaz é **limitar o trabalho em progresso (WIP)**, reduzindo o Cycle Time.

---

## 3. Você consegue responder?
1. Como a Lei de Little relaciona WIP, Throughput e Cycle Time?
2. O que representa o Throughput semanal de uma equipe Kanban?
3. Por que limitar o Trabalho em Progresso (WIP) aumenta a vazão de entregas?
4. Escreva a equação matemática da Lei de Little.
5. Qual a diferença entre Throughput e Velocity?

??? check "Mostrar Gabarito / Resposta"
    1. **Relação da Lei de Little:** Estabelece que o tempo médio de permanência (Cycle Time) é igual ao Trabalho em Progresso (WIP) dividido pela taxa de saída (Throughput).
    2. **Throughput semanal:** A contagem absoluta de itens de trabalho concluídos (ex: Histórias, Bugs, Tasks) entregues em produção durante a semana.
    3. **Impacto da limitação do WIP:** Reduz a troca de contexto (*context switching*), diminui gargalos e faz os itens fluírem mais rapidamente do início ao fim.
    4. **Equação da Lei de Little:**
       $$\text{Cycle Time} = \frac{\text{WIP}}{\text{Throughput}} \quad \iff \quad \text{Throughput} = \frac{\text{WIP}}{\text{Cycle Time}}$$
    5. **Throughput vs. Velocity:** Throughput conta a quantidade bruta de *itens entregues* (ex: 12 tarefas/semana), enquanto Velocity soma os *pontos de estimativa* relativos entregues (ex: 30 Story Points/sprint).

---

## 📚 Referências utilizadas
- **Anderson, David J.** *Kanban*, 2010.
- **Little, J. D. C.** *A Proof for the Queuing Formula: L = W * W*, Operations Research, 1961.
