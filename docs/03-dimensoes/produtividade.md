# Dimensão 6: Produtividade em Engenharia de Software

A **Produtividade** expressa a relação entre o volume de trabalho entregue (tamanho funcional ou físico) e os recursos consumidos (esforço ou custo) para essa produção.

---

## 1. Fórmulas de Produtividade

### Fórmula Conceitual
$$\text{Produtividade} = \frac{\text{Tamanho do Software Entregue}}{\text{Esforço Investido}}$$

### Fórmula Matemática
$$P = \frac{S}{E}$$

### Exemplos em Unidades Diferentes

#### Em Linhas de Código (LOC/h)
$$P_{\text{LOC}} = \frac{10.000\text{ LOC}}{500\text{ horas}} = 20\text{ LOC/hora}$$

#### Em Pontos de Função (PF/h ou h/PF)
$$P_{\text{PF}} = \frac{50\text{ PF}}{500\text{ horas}} = 0.1\text{ PF/hora}$$
$$\text{Taxa de Esforço (h/PF)} = \frac{500\text{ horas}}{50\text{ PF}} = 10\text{ horas/PF}$$

---

## 2. As Armadilhas da Produtividade em Software

!!! warning "Cuidado com o Paradoxo da Produtividade"
    - Programadores que escrevem mais linhas de código (LOC) não são necessariamente mais produtivos; código mais prolixo pode conter mais bugs.
    - A produtividade deve ser avaliada **sempre** em conjunto com a **qualidade** (defeitos/KLOC ou defeitos/PF).

---

## 3. Você consegue responder?
1. Qual é a fórmula conceitual e matemática da produtividade?
2. Calcule a produtividade de uma equipe que entregou 120 Pontos de Função consumindo 600 horas de esforço.
3. O que significa uma taxa de esforço de 5 horas/PF?
4. Por que a medição de produtividade em LOC pode incentivar práticas ruins de codificação?
5. Qual a importância de analisar a produtividade paralelamente às métricas de qualidade?

---

## 📚 Referências utilizadas
- **Fenton, N. E. & Bieman, J.** *Software Metrics: A Rigorous and Practical Approach*, 3rd ed., 2014.
