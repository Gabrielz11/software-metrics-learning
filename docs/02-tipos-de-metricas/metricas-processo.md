# Métricas de Processo

> 📚 **Conceito fundamentado em referência (SWEBOK / Pressman)**  
> Métricas de processo quantificam os atributos do ambiente de desenvolvimento, eficácia das atividades de verificação e eficiência da metodologia de trabalho.

---

## 1. O que são?
Métricas de processo avaliam *como* o software é produzido, incluindo o tempo gasto em etapas, a eficiência na detecção de defeitos e o nível de retrabalho da equipe.

---

## 2. Principais Métricas de Processo

1. **Eficiência na Remoção de Defeitos (DRE - Defect Removal Efficiency)**:
   $$\text{DRE} = \left( \frac{\text{Defeitos Pré-Release}}{\text{Defeitos Pré-Release} + \text{Defeitos Pós-Release}} \right) \times 100\%$$
2. **Tempo Médio de Reparo (MTTR - Mean Time to Repair)**:
   $$\text{MTTR} = \frac{\text{Tempo Total Gasto em Correções}}{\text{Número de Defeitos Corrigidos}}$$
3. **Taxa de Retrabalho (Rework Ratio)**:
   $$\text{Retrabalho (\%)} = \left( \frac{\text{Horas Gastas em Correção de Bugs}}{\text{Horas Totais do Projeto}} \right) \times 100\%$$
4. **Lead Time e Cycle Time**: Métricas de fluxo de entrega em processos ágeis e Kanban.

---

## 3. Exemplo Realista no Sistema de Biblioteca

!!! example "Cálculo de DRE e Retrabalho"
    Durante a fase de testes do *Sistema de Biblioteca*, a equipe encontrou 35 defeitos. Após a entrega em produção, os usuários finais reportaram mais 5 defeitos.
    $$\text{DRE} = \left( \frac{35}{35 + 5} \right) \times 100 = 87.5\%$$
    A equipe dedicou 60 horas de um total de 500 horas de projeto para corrigir falhas.
    $$\text{Retrabalho} = \left( \frac{60}{500} \right) \times 100 = 12\%$$

---

## 4. Erros Comuns
- Tentar melhorar processos punindo individualmente desenvolvedores que reportam ou corrigem bugs.
- Ignorar o tempo de espera (queue time) ao medir o ciclo de vida do processo.

## 5. Você consegue responder?
1. Qual o objetivo principal das Métricas de Processo?
2. Como se calcula a Eficiência de Remoção de Defeitos (DRE)?
3. Qual é a importância da métrica de retrabalho para a gestão de engenharia?
4. O que a métrica MTTR avalia dentro de um processo de manutenção?
5. Qual a diferença de foco entre métricas de produto e métricas de processo?

---

## 📚 Referências utilizadas
- **Pressman, R. S. & Maxim, B. R.** *Software Engineering: A Practitioner's Approach*, 9th ed., 2019.
- **IEEE Computer Society**. *SWEBOK V4.0a*, Chapter 8.
