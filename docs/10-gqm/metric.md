# Métricas Derivadas (Metric) em GQM

O nível **Metric** identifica quais dados quantitativos ou qualitativos devem ser coletados para responder concretamente a cada pergunta elaborada no nível anterior.

---

## 1. Mapeamento Pergunta -> Métricas

```text
PERGUNTA: "Quão eficaz é nossa etapa de testes antes do deploy?"
    │
    ├── Métrica 1: Eficiência na Remoção de Defeitos (DRE %)
    ├── Métrica 2: Cobertura de Testes de Código (% Line Coverage)
    └── Métrica 3: Densidade de Defeitos Pós-Release (Defeitos/KLOC)
```

---

## 2. Coleta de Dados Empíricos
No GQM, a coleta de dados é **orientada por hipóteses**. Os dados coletados alimentam a análise das perguntas, que por sua vez concluem o atingimento ou não do Objetivo de negócio.

---

## 3. Você consegue responder?
1. Como as métricas são associadas às perguntas no GQM?
2. Uma mesma métrica pode responder a mais de uma pergunta em uma árvore GQM?
3. O que acontece com métricas que não possuem ligação com nenhuma pergunta da árvore GQM?
4. Qual a diferença entre coletar dados por rotina e coletar dados orientados pelo GQM?
5. Dê dois exemplos de métricas derivadas para responder sobre a velocidade de correção de bugs.

??? check "Mostrar Gabarito / Resposta"
    1. **Associação de métricas:** Cada pergunta é mapeada para uma ou mais métricas quantitativas (diretas ou indiretas) que fornecem os dados numéricos necessários para responder àquela indagação.
    2. **Reuso de métricas:** Sim, uma única métrica (ex: contagem de KLOC ou tempo de teste) pode alimentar o cálculo de respostas para diferentes perguntas da mesma árvore.
    3. **Métricas sem ligação:** São consideradas "métricas órfãs" ou desperdício de esforço de medição e devem ser descartadas do programa de métricas.
    4. **Coleta por rotina vs. GQM:** A coleta por rotina acumula dados aleatórios sem propósito claro. A coleta orientada pelo GQM é guiada por hipóteses e focada estritamente no suporte à tomada de decisão.
    5. **Duas métricas para velocidade de bugs:** MTTR (Mean Time to Repair em horas) e Tempo Médio no Estado "In Progress" para os cards do tipo Bug.

---

## 📚 Referências utilizadas
- **Basili, V. R., Caldiera, G., & Rombach, H. D.** *The Goal Question Metric Approach*, 1994.
