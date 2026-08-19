# Cálculo Completo de UCP e Esforço

Neste capítulo é demonstrada a consolidação matemática do método Use Case Points.

---

## 1. Passo a Passo do Cálculo

1. **Somar UAW**:
   $$\text{UAW} = \sum (\text{Atores Simples} \times 1) + (\text{Atores Médios} \times 2) + (\text{Atores Complexos} \times 3)$$
2. **Somar UUCW**:
   $$\text{UUCW} = \sum (\text{UC Simples} \times 5) + (\text{UC Médios} \times 10) + (\text{UC Complexos} \times 15)$$
3. **Calcular UUCP**:
   $$\text{UUCP} = \text{UAW} + \text{UUCW}$$
4. **Calcular TCF e ECF**:
   $$\text{TCF} = 0.6 + (0.01 \times \text{TFactor})$$
   $$\text{ECF} = 1.4 + (-0.03 \times \text{EFactor})$$
5. **Calcular UCP Final**:
   $$\text{UCP} = \text{UUCP} \times \text{TCF} \times \text{ECF}$$
6. **Estimativa de Esforço em Horas**:
   $$\text{Esforço (Horas)} = \text{UCP} \times \text{Fator de Produtividade (PF)}$$
   *(Padrão Karner: PF = 20 horas por UCP).*

---

## 2. Você consegue responder?
1. Qual a sequência de fórmulas para obter a estimativa de esforço em UCP?
2. Se o UUCP é 50, o TCF é 1.0 e o ECF é 1.0, quantos Pontos de Caso de Uso teremos?
3. Qual a estimativa em horas para 50 UCP utilizando o fator Karner padrão de 20h/UCP?
4. Como alterar o fator de produtividade (ex: 15h/UCP ou 28h/UCP) altera a estimativa de esforço?
5. Escreva a equação completa de UCP.

??? check "Mostrar Gabarito / Resposta"
    1. **Sequência de fórmulas:**
       $$\text{UUCP} = \text{UAW} + \text{UUCW}$$
       $$\text{UCP} = \text{UUCP} \times \text{TCF} \times \text{ECF}$$
       $$\text{Esforço (Horas)} = \text{UCP} \times \text{Fator de Produtividade}$$
    2. **Cálculo de UCP:** $50 \times 1.0 \times 1.0 = 50 \text{ UCP}$.
    3. **Estimativa em horas:** $50 \text{ UCP} \times 20 \text{ h/UCP} = 1.000 \text{ horas-pessoa}$.
    4. **Alteração do fator de produtividade:** Reflete diretamente a eficiência da equipe; com 15h/UCP o projeto consumirá 750h, enquanto com 28h/UCP consumirá 1.400h.
    5. **Equação completa de UCP:**
       $$\text{UCP} = (\text{UAW} + \text{UUCW}) \times \left(0.6 + 0.01 \sum w_i t_i\right) \times \left(1.4 - 0.03 \sum w_j e_j\right)$$

---

## 📚 Referências utilizadas
- **Karner, Gustav**. *Resource Estimation Based on Use Cases*, 1993.
