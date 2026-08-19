# Respostas: Qualidade e Defeitos

---

### Solução do Exemplo 01 🟢
$$D_{\text{KLOC}} = \frac{15\text{ defeitos}}{5.0\text{ KLOC}} = \mathbf{3.0\text{ defeitos/KLOC}}$$

---

### Solução do Exemplo 02 🟢
$$\text{DRE} = \left( \frac{80}{80 + 20} \right) \times 100 = \left( \frac{80}{100} \right) \times 100 = \mathbf{80.0\%}$$

---

### Solução do Exemplo 03 🟡
Contagem de nós de decisão ($D$):
1. `if not pedido.valido:` (+1)
2. `if pedido.valor > 500:` (+1)
3. `if pedido.cliente_vip:` (+1)

Total de predicados $D = 3$.  
$$V(G) = D + 1 = 3 + 1 = \mathbf{4}$$

A complexidade ciclomática é 4 (Baixo Risco).

---

### Solução do Exemplo 04 🔴
- Total de falhas = 3
- Tempo total de reparo = $2 + 1 + 3 = 6\text{ horas}$
- Tempo operacional sem falhas = $720 - 6 = 714\text{ horas}$

1. $\text{MTBF} = 714 / 3 = \mathbf{238\text{ horas}}$
2. $\text{MTTR} = 6 / 3 = \mathbf{2.0\text{ horas}}$
3. $\text{Disponibilidade } A = \left( \frac{238}{238 + 2} \right) \times 100 = \left( \frac{238}{240} \right) \times 100 \approx \mathbf{99.17\%}$
