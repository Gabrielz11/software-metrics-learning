# Gráfico Burnup

O **Gráfico Burnup** monitora a quantidade acumulada de trabalho concluído paralela à linha de **Escopo Total** do projeto ou release.

---

## 1. Estrutura do Gráfico Burnup

```text
Trabalho Acumulado (Points)
    │                  ┌─── Linha de Escopo Total (Escopo aumentou)
100 ┼──────────────────┘
    │              .---* (Trabalho Concluído)
 50 ┼────────.---'
    │   .---'
  0 └───┴───┴───┴───┴─── (Tempo / Iterações)
```

---

## 2. Vantagem em Relação ao Burndown
Enquanto o Burndown esconde se um atraso decorre de lentidão da equipe ou de **aumento do escopo**, o Burnup explicita a alteração da linha de escopo superior separadamente da linha de entregas efetuadas.

---

## 3. Você consegue responder?
1. Qual a grande vantagem do gráfico Burnup sobre o Burndown?
2. Como o Burnup visualiza o aumento de escopo (*Scope Creep*) durante uma release?
3. O que acontece quando a linha de trabalho concluído cruza a linha de escopo total?
4. Quais são as duas linhas principais plotadas em um gráfico Burnup?
5. Em que tipo de projeto o Burnup é preferível ao Burndown?

??? check "Mostrar Gabarito / Resposta"
    1. **Vantagem do Burnup:** Separa claramente o crescimento do escopo total da quantidade real de trabalho entregue acumulado.
    2. **Visualização do Scope Creep:** Exibida pelo desvio ascendente ou degraus na linha superior de escopo total (*Total Scope Line*).
    3. **Cruzamento das linhas:** Significa que 100% do escopo planejado para o projeto/release foi concluído.
    4. **Duas linhas principais:** A linha de **Escopo Total** (*Total Scope*) e a linha de **Trabalho Concluído Acumulado** (*Work Completed*).
    5. **Projeto preferível:** Projetos de longo prazo ou releases dinâmicas onde o escopo sofre constantes adições ou alterações por decisões de produto.

---

## 📚 Referências utilizadas
- **Cohn, Mike**. *Agile Estimating and Planning*.
