# Exemplo Prático de UCP: Sistema de Biblioteca

Aplicação completa do método Use Case Points no *Sistema de Biblioteca*.

---

## 1. Dados do Exemplo

### Atores (UAW)
- 2 Atores Complexos (Leitor, Bibliotecário) = $2 \times 3 = 6$
- 1 Ator Simples (ServiçoExternoCredito) = $1 \times 1 = 1$
- **UAW Total** = $6 + 1 = 7$

### Casos de Uso (UUCW)
- 2 UC Médios (`UC01_ManterUsuarios`, `UC02_ManterAcervo`) = $2 \times 10 = 20$
- 1 UC Complexo (`UC03_RealizarEmprestimo`) = $1 \times 15 = 15$
- 2 UC Simples (`UC04_RegistrarDevolucao`, `UC05_PesquisarLivros`) = $2 \times 5 = 10$
- **UUCW Total** = $20 + 15 + 10 = 45$

### UUCP
$$\text{UUCP} = 7 + 45 = 52$$

### Fatores de Ajuste (Ratings Padrão = 3)
- $\text{TCF} = 1.02$
- $\text{ECF} = 0.995$

---

## 2. Cálculo Final

$$\text{UCP} = 52 \times 1.02 \times 0.995 \approx 52.77\text{ UCP}$$

$$\text{Esforço Estimado} = 52.77 \times 20\text{ h/UCP} \approx 1.055.4\text{ Horas}$$

---

## 3. Você consegue responder?
1. Qual foi a pontuação UUCP obtida no exemplo do Sistema de Biblioteca?
2. Quantas horas de esforço foram estimadas para o sistema considerando o fator padrão Karner de 20h/UCP?
3. Qual o peso dos casos de uso no subtotal UUCW?
4. Como o TCF e ECF ajustaram o resultado do UUCP de 52 para 52.77?
5. Mostre como reproduzir este cálculo utilizando o módulo Python `software_metrics.use_case_points`.

??? check "Mostrar Gabarito / Resposta"
    1. **UUCP do exemplo:** 52 UUCP (UAW = 7, UUCW = 45).
    2. **Esforço total em horas:** 1.055,4 horas (calculado por $52,77 \times 20$).
    3. **Subtotal UUCW:** 45 pontos (2 Médios [20] + 1 Complexo [15] + 2 Simples [10]).
    4. **Ajuste por TCF e ECF:** $52 \times 1,02 \text{ (TCF)} \times 0,995 \text{ (ECF)} = 52,77 \text{ UCP}$, elevando levemente a contagem não ajustada em 1.48%.
    5. **Reprodução em Python:** Instanciar a classe de cálculo do módulo informando os atores, casos de uso e matrizes de notas de TCF e ECF para executar `calculate_ucp()`.

---

## 📚 Referências utilizadas
- **Karner, Gustav**. *Resource Estimation Based on Use Cases*, 1993.
