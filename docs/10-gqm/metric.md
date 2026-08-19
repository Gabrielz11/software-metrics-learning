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

---

## 📚 Referências utilizadas
- **Basili, V. R., Caldiera, G., & Rombach, H. D.** *The Goal Question Metric Approach*, 1994.
