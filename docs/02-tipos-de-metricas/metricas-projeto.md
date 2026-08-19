# Métricas de Projeto

> 📚 **Conceito fundamentado em referência (SWEBOK / Sommerville)**  
> Métricas de projeto medem o operacional e o progresso da execução de um empreendimento de software, focando em esforço, custo, prazos e alocação de recursos.

---

## 1. O que são?
Métricas de projeto permitem ao gerente de projetos monitorar o andamento em relação ao planejamento inicial e prever variações de custo e prazo.

---

## 2. Principais Métricas de Projeto

1. **Esforço Realizado vs Planejado**:
   $$\text{Variação de Esforço (\%)} = \left( \frac{\text{Esforço Real} - \text{Esforço Planejado}}{\text{Esforço Planejado}} \right) \times 100\%$$
2. **Variação de Cronograma (Schedule Variance - SV)**:
   $$\text{SV} = \text{Valor Agregado (EV)} - \text{Valor Planejado (PV)}$$
3. **Custo por Unidade de Entregável**:
   $$\text{Custo por PF} = \frac{\text{Custo Total do Projeto}}{\text{Total de Pontos de Função Entregues}}$$

---

## 3. Exemplo Prático no Sistema de Biblioteca

!!! example "Análise de Variação de Esforço"
    O *Sistema de Biblioteca* foi estimado originalmente em 400 horas de desenvolvimento. Na conclusão, o registro de timesheet acusou 500 horas trabalhadas.
    $$\text{Variação de Esforço} = \left( \frac{500 - 400}{400} \right) \times 100 = 25\%$$
    Houve um estouro de esforço de 25% em relação à estimativa inicial.

---

## 4. Erros Comuns
- Confundir métricas de projeto (ex: horas gastas) com valor entregue ao cliente final.
- Atualizar o planejamento arbitrariamente para "forçar" as métricas de projeto a parecerem dentro da meta.

## 5. Você consegue responder?
1. Qual a diferença entre uma Métrica de Projeto e uma Métrica de Processo?
2. Como a Variação de Esforço auxilia na re-estimativa de projetos futuros?
3. O que mede a razão entre Custo Total e Pontos de Função Entregues?
4. Por que medir apenas o progresso de tarefas concluídas pode ser enganoso sem medir a qualidade dos entregáveis?
5. Como os dados históricos de métricas de projeto ajudam em novos orçamentos?

??? check "Mostrar Gabarito / Resposta"
    1. **Métrica de Projeto vs. Processo:** Métricas de projeto focam no acompanhamento operacional e gerencial de uma iniciativa específica com início e fim (custo, prazo, horas gastas), enquanto métricas de processo analisam a eficiência contínua da organização ao longo de múltiplos projetos.
    2. **Variação de Esforço:** Compara as horas estimadas com as horas reais trabalhadas. Ao identificar desvios constantes, a organização ajusta os fatores de produtividade para orçar projetos futuros com maior acurácia.
    3. **Custo Total / Pontos de Função:** Mede o custo unitário por Ponto de Função ($\text{Custo/PF}$), permitindo avaliar a eficiência financeira da entrega.
    4. **Progresso sem qualidade:** Uma equipe pode concluir 90% das tarefas no prazo, mas se os artefatos contiverem alta densidade de defeitos, o projeto sofrerá com atrasos massivos na fase de testes ou homologação.
    5. **Dados históricos e orçamentos:** Permitem estimar custos e prazos com base na produtividade real observada em projetos passados similares, reduzindo o risco de orçamentos irrealistas.

---

## 📚 Referências utilizadas
- **Sommerville, I.** *Software Engineering*, 10th ed., Pearson, 2015.
- **IEEE Computer Society**. *SWEBOK V4.0a*, Chapter 8.
