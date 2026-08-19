# Sistema de Biblioteca: Medição em LOC

Análise dimensional de código físico do *Sistema de Biblioteca*.

---

## 1. Dados Coletados do Repositório

- **Linhas Físicas Totais**: 12.500 LOC
- **Linhas em Branco**: 1.500
- **Linhas de Comentários e Docstrings**: 1.000
- **Linhas de Código Executável (SLOC)**: 10.000 SLOC (10.0 KLOC)

---

## 2. Indicadores Derivados de LOC

- **Esforço total consumido**: 500 horas
- **Produtividade física**: $10.000 / 500 = 20\text{ SLOC/hora}$
- **Defeitos Totais Identificados**: 40 defeitos
- **Densidade por KLOC**: $40 / 10 = 4.0\text{ defeitos/KLOC}$

---

## 3. Você consegue responder?
1. Qual a contagem de linhas executáveis (SLOC) do Sistema de Biblioteca?
2. Qual a produtividade física obtida em SLOC/hora?
3. Qual a densidade de defeitos por KLOC registrada no projeto?
4. Quantas KLOC o sistema possui no total?
5. Como os comentários impactaram a diferença entre LOC total e SLOC?

??? check "Mostrar Gabarito / Resposta"
    1. **Contagem de SLOC:** 10.000 linhas executáveis de código-fonte em Python.
    2. **Produtividade física:**
       $$\text{Produtividade} = \frac{10.000\text{ SLOC}}{500\text{ horas}} = 20\text{ SLOC/hora}$$
    3. **Densidade de defeitos por KLOC:**
       $$D_{\text{KLOC}} = \frac{40\text{ defeitos}}{10\text{ KLOC}} = 4,0\text{ defeitos/KLOC}$$
    4. **Total de KLOC:** $10.000 / 1.000 = 10\text{ KLOC}$.
    5. **Impacto dos comentários:** O arquivo físico possui mais linhas totais (LOC), mas o analisador sintático ignorou linhas em branco e comentários para isolar exatamente os 10.000 SLOC executáveis.

---

## 📚 Referências utilizadas
- **Fenton, N. E. & Bieman, J.** *Software Metrics*, 3rd ed.
