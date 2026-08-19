# Respostas: Fundamentos de Métricas

---

### Solução do Exemplo 01 🟢
1. **Medida**: Dado bruto absoluto sem relação com o tamanho.
2. **Métrica**: Dado relacionado/normalizado (defeitos por KLOC).
3. **Indicador**: Sinal contextualizado comparado a uma meta/teto que orienta uma decisão.

---

### Solução do Exemplo 02 🟢
- Horas de esforço: **Direta**
- Produtividade (LOC/h): **Indireta** (razão Tamanho/Esforço)
- Linhas de Código (LOC): **Direta**
- Densidade de Defeitos (Defeitos/PF): **Indireta** (razão Defeitos/PF)

---

### Solução do Exemplo 03 🟡
Aumentar LOC/dia ao trocar de linguagem não significa maior valor de negócio. Linguagens mais prolixas ou estilos de codificação menos compactos aumentam o LOC sem adicionar funcionalidades. Além disso, focar em LOC estimula código verboso e reduz a manutenibilidade.

---

### Solução do Exemplo 04 🔴
A conclusão do gerente foi precipitada. Devemos calcular a **Densidade de Defeitos** para normalizar os dados pelo tamanho:
- **Projeto A**: $80 / 40\text{ KLOC} = 2.0\text{ defeitos/KLOC}$
- **Projeto B**: $20 / 2\text{ KLOC} = 10.0\text{ defeitos/KLOC}$

O Projeto B possui uma densidade de defeitos 5 vezes maior do que o Projeto A. Portanto, a qualidade relativa do Projeto A é superior à do Projeto B.
