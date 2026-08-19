# Conceito de LOC, SLOC e KLOC

> 📚 **Conceito fundamentado em referência (Fenton & Bieman)**  
> LOC (*Lines of Code*) representa a quantidade de linhas contidas em arquivos de código-fonte.

---

## 1. Siglas e Definições

- **LOC (Lines of Code)**: Contagem genérica de linhas físicas.
- **SLOC (Source Lines of Code)**: Contagem restrita às linhas executáveis ou declarações de código, excluindo comentários e linhas em branco.
- **KLOC (Kilo Lines of Code)**: Unidade de milhar de linhas de código ($1\text{ KLOC} = 1.000\text{ LOC}$).

---

## 2. Fórmulas de Conversão

### Conceitual
$$\text{KLOC} = \frac{\text{Linhas de Código}}{1000}$$

### Matemática
$$\text{KLOC} = \frac{\text{LOC}}{1000}$$

### Exemplo
$$10.000\text{ LOC} = \frac{10.000}{1000} = 10\text{ KLOC}$$

---

## 3. Você consegue responder?
1. O que significam as siglas LOC, SLOC e KLOC?
2. Quantas linhas de código há em 4.5 KLOC?
3. O que diferencia LOC de SLOC?
4. Por que KLOC é utilizado em vez de LOC em projetos de grande porte?
5. Escreva a fórmula de conversão de LOC para KLOC.

??? check "Mostrar Gabarito / Resposta"
    1. **Significado das siglas:**
       - *LOC:* Lines of Code (Linhas de Código totais).
       - *SLOC:* Source Lines of Code (Linhas de Código Fonte declarativas/executáveis).
       - *KLOC:* Kilo Lines of Code (Milhares de Linhas de Código).
    2. **4.5 KLOC:** $4,5 \times 1.000 = 4.500$ linhas de código.
    3. **LOC vs. SLOC:** LOC refere-se à contagem bruta de linhas do arquivo (incluindo comentários e linhas em branco), enquanto SLOC contabiliza estritamente as linhas lógicas/executáveis de código.
    4. **Uso do KLOC:** Simplifica a leitura e manipulação de números grandes em sistemas corporativos de dezenas ou centenas de milhares de linhas.
    5. **Fórmula de conversão:**
       $$\text{KLOC} = \frac{\text{LOC}}{1000}$$

---

## 📚 Referências utilizadas
- **Fenton, N. E. & Bieman, J.** *Software Metrics*, 3rd ed.
