# Gráfico Burndown

O **Gráfico Burndown** mostra a evolução diária da quantidade de trabalho restante (em horas ou Story Points) ao longo de uma sprint ou release.

---

## 1. Estrutura do Gráfico Burndown

```text
Trabalho Restante (Points)
    │
 40 ┼───* (Início da Sprint)
    │   │ \
 30 ┼───│──*─── Linha Ideal
    │   │   \ \
 20 ┼───│────*─*─── Linha Real
    │   │       \
  0 └───┴───┴───┴───┴─── (Dias da Sprint: 1 a 10)
```

- **Linha Ideal**: Trajeto linear teórico que reduz a estimativa a zero no último dia.
- **Linha Real**: Acompanhamento diário das tarefas finalizadas pela equipe.

---

## 2. Padrões de Leitura
- **Linha Real acima da Linha Ideal**: Atraso na sprint (trabalho abaixo do esperado ou inclusão de escopo não planejado).
- **Linha Real abaixo da Linha Ideal**: Adiantamento na sprint.
- **Queda brusca no último dia (Gráfico Abismo)**: Falta de entregas parciais diárias ao longo da sprint.

---

## 3. Você consegue responder?
1. O que indica a linha ideal em um gráfico Burndown?
2. O que significa quando a linha real fica sistematicamente acima da linha ideal durante a sprint?
3. O que é o "efeito abismo" em um Burndown?
4. Quais são os dois eixos de um gráfico Burndown de sprint?
5. Qual a limitação do Burndown no acompanhamento de mudanças de escopo?

??? check "Mostrar Gabarito / Resposta"
    1. **Linha ideal:** Representa a taxa teórica linear de queima de trabalho restante por dia necessária para zerar todo o escopo no último dia da sprint.
    2. **Linha real acima da ideal:** Indica atraso na sprint — o trabalho restante está sendo concluído mais devagar do que o planejado ou histórias adicionais foram inseridas no meio da sprint.
    3. **Efeito Abismo:** Quando o gráfico permanece horizontal/alto durante quase toda a sprint e despenca de vez apenas no último dia, indicando falta de validações parciais diárias.
    4. **Eixos do gráfico:** Eixo X (Dias do Cronograma / Sprint) e Eixo Y (Trabalho Restante em Story Points ou Horas).
    5. **Limitação sobre escopo:** O Burndown mostra apenas o saldo líquido restante; se o escopo total aumentar durante a sprint, a linha sobe dando a impressão errônea de que a equipe não trabalhou naquele dia.

---

## 📚 Referências utilizadas
- **Cohn, Mike**. *Agile Estimating and Planning*.
