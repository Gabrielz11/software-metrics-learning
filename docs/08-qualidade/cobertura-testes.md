# Cobertura de Testes de Código

A **Cobertura de Testes** (*Test Coverage*) quantifica a proporção da estrutura do código-fonte que é efetivamente executada durante a rodada de suítes de testes automatizados.

---

## 1. Tipos de Cobertura de Código

1. **Cobertura de Linhas (Line Coverage / Statement Coverage)**:
   $$\text{Line Coverage (\%)} = \left( \frac{\text{Linhas Executadas pelos Testes}}{\text{Total de Linhas de Código Executáveis}} \right) \times 100\%$$
2. **Cobertura de Ramos (Branch Coverage)**:
   $$\text{Branch Coverage (\%)} = \left( \frac{\text{Ramos de Decisão Executados}}{\text{Total de Ramos de Decisão (If/Else/Switch)}} \right) \times 100\%$$

---

## 2. A Ilusão da Cobertura de 100%

!!! warning "Cuidado"
    Atingir 100% de *Line Coverage* não garante que o software esteja livre de bugs de regra de negócio. Ela garante apenas que todas as linhas foram tocadas ao menos uma vez pelos testes.

---

## 3. Você consegue responder?
1. O que mede a cobertura de linhas de código?
2. Qual a diferença entre *Statement Coverage* e *Branch Coverage*?
3. Por que 100% de cobertura de código não garante ausência de defeitos funcionais?
4. Escreva a equação de cálculo de cobertura de linhas.
5. Qual a ferramenta padrão em Python para medir cobertura em testes com pytest?

??? check "Mostrar Gabarito / Resposta"
    1. **Cobertura de linhas:** Mede a porcentagem de linhas de código executáveis (SLOC) que foram exercitadas pelo menos uma vez durante a execução da suíte de testes automatizados.
    2. **Statement Coverage vs. Branch Coverage:** *Statement Coverage* verifica se cada linha/instrução foi executada. *Branch Coverage* verifica se cada ramificação condicional (cada caminho verdadeiro e falso de um `if`/`switch`) foi percorrida.
    3. **100% de cobertura vs. Ausência de defeitos:** Porque a cobertura valida apenas o código que foi escrito, não testando requisitos esquecidos, regras de negócio incorretas, dados nulos inesperados ou problemas de concorrência.
    4. **Equação de cobertura de linhas:**
       $$\text{Cobertura (\%)} = \left( \frac{\text{Linhas Executadas pelos Testes}}{\text{Total de Linhas Executáveis}} \right) \times 100\%$$
    5. **Ferramenta em Python:** `pytest-cov` (baseada na biblioteca `coverage.py`).

---

## 📚 Referências utilizadas
- **Kan, S. H.** *Metrics and Models in Software Quality Engineering*, 2nd ed.
