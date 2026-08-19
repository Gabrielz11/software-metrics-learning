# Resultado Comparativo Final do Estudo de Caso

Este capítulo final do Estudo de Caso consolida a visão integrada das três métricas aplicadas ao *Sistema de Biblioteca*.

---

## 1. Visão Geral Consolidada

```text
Sistema de Biblioteca
│
├── SLOC → 10.000 Linhas Executáveis (Tamanho Físico)
│
├── APF  → 53 Pontos de Função (Tamanho Funcional IFPUG)
│
├── UCP  → 52.77 Use Case Points (Tamanho por Casos de Uso Karner)
│
├── Esforço Real → 500 Horas-Pessoa (3.125 Pessoas-Mês)
│
├── Defeitos Totais → 40 Defeitos (DRE = 87.5%)
│
└── Qualidade por PF → 0.75 Defeitos/PF | 4.0 Defeitos/KLOC
```

---

## 2. Por que os Números Não São Diretamente Intercambiáveis?

!!! important "Aviso Pedagógico Fundamental"
    - **1 PF NÃO é igual a N KLOC**: Converter Pontos de Função em LOC usando fatores fixos de "backfiring" é uma aproximação estatística sujeita a margens de erro elevadas.
    - **1 UCP NÃO é um PF**: Embora tenham convergido neste estudo de caso (~53 PF vs ~52.77 UCP), APF avalia arquivos de dados/transações e UCP avalia fluxos de casos de uso e atores.
    - Cada métrica atende a um propósito específico de medição.

---

## 3. Você consegue responder?
1. Apresente o resumo consolidado dos números obtidos no Sistema de Biblioteca.
2. Por que 1 Ponto de Função não deve ser convertido diretamente em uma quantidade fixa de LOC?
3. O que explica a convergência entre APF e UCP no estudo de caso?
4. Qual métrica você utilizaria para contratar a fábrica de software que construiu o sistema?
5. Qual métrica você utilizaria para planejar a refatoração do código-fonte Python?

??? check "Mostrar Gabarito / Resposta"
    1. **Resumo Consolidado:**
       - Tamanho Funcional: 53 PF / 52,77 UCP
       - Tamanho Físico: 10.000 SLOC
       - Esforço Real: 500 horas-pessoa
       - Produtividade: 9,43 h/PF (ou 20 SLOC/h)
       - Qualidade: 40 defeitos totais ($0,75\text{ def/PF}$, $4\text{ def/KLOC}$), DRE de $87,5\%$ e Cobertura de $92\%$.
    2. **Conversão direta de PF em LOC:** Porque a quantidade de LOC varia conforme a linguagem, estilo de codificação, nível de refatoração e uso de bibliotecas de terceiros; fazer "backfiring" gera altas margens de erro.
    3. **Convergência APF vs. UCP:** Ambos capturaram com precisão o mesmo escopo de negócio do estudo de caso sob perspectivas equivalentes.
    4. **Métrica para contratação de fábrica de software:** APF (Análise de Pontos de Função), por ser o padrão internacional neutro para precificação contratual (R$/PF).
    5. **Métrica para refatoração:** LOC/SLOC combinada com Complexidade Ciclomática $V(G)$ e Cobertura de Testes.

---

## 📚 Referências utilizadas
- **Fenton, N. E. & Bieman, J.** *Software Metrics*, 3rd ed.
- **IFPUG**. *Function Point Counting Practices Manual*, Release 4.3.1.
