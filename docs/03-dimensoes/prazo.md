# Dimensão 3: Prazo e Cronograma

O **Prazo** (ou duração do cronograma) representa o tempo de calendário transcorrido entre o início formal do desenvolvimento e a disponibilização da entrega final.

---

## 1. Prazo vs Esforço

```text
Esforço = 480 Horas-Pessoa
Equipe = 3 Desenvolvedores (160h/mês cada)
Prazo Teórico Mínimo = 480 / (3 * 160) = 1 Mês de Calendário
```

Em termos reais, contudo, interferências de comunicação, dependências externas e tempo de espera (queue time) impedem a divisão direta do esforço pelo número de pessoas.

---

## 2. Unidades de Medida de Prazo
- **Dias Úteis / Semanas / Meses de Calendário**: Unidades para planejamento operacional.
- **Lead Time**: Tempo decorrido desde a abertura da demanda até a entrega em produção.

---

## 3. Você consegue responder?
1. Por que o prazo de um projeto não é simples divisão do esforço pelo número de pessoas?
2. Qual a unidade principal de medida de prazo em gestão de cronogramas?
3. O que é o tempo de espera (queue time) e como ele impacta o prazo total?
4. Como a dependência entre tarefas estabelece o caminho crítico do prazo?
5. Qual é o perigo de comprimir o prazo de um projeto sem alterar o escopo?

??? check "Mostrar Gabarito / Resposta"
    1. **Divisão simples:** Porque tarefas possuem dependências sequenciais não-paralelizáveis e a adição de pessoas adiciona sobrecarga de comunicação ($N(N-1)/2$).
    2. **Unidade de medida:** Dias úteis, semanas ou meses de calendário (dias de cronograma decorrido).
    3. **Tempo de espera (Queue Time):** É o tempo em que o item fica parado aguardando aprovação, revisão de código ou disponibilidade de ambiente. Ele aumenta o Lead Time total sem agregar valor ou consumir esforço de desenvolvimento ativo.
    4. **Caminho crítico:** A sequência de tarefas encadeadas com folga zero que determina a duração mínima total do projeto; qualquer atraso nessas tarefas atrasará o prazo final.
    5. **Perigo de comprimir prazo:** Força a equipe a cortar cantos de qualidade (reduzir testes, criar dívida técnica) ou gera sobrecarga de horas extras e *burnout*, aumentando a incidência de defeitos.

---

## 📚 Referências utilizadas
- **Sommerville, I.** *Software Engineering*, 10th ed., Pearson, 2015.
