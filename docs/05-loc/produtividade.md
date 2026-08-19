# Produtividade e Defeitos em LOC

Neste capítulo são apresentados os cálculos numéricos tradicionais derivados de KLOC para avaliação de produtividade e densidade de defeitos.

---

## 1. Fórmulas de Produtividade em LOC

### Conceitual
$$\text{Produtividade} = \frac{\text{Linhas de Código Total}}{\text{Esforço Gasto em Horas}}$$

### Matemática
$$P = \frac{\text{LOC}}{E}$$

### Exemplo
Um módulo do Sistema de Biblioteca de 10.000 LOC consumiu 500 horas de desenvolvimento.
$$P = \frac{10.000}{500} = 20\text{ LOC/hora}$$

---

## 2. Fórmulas de Densidade de Defeitos por KLOC

### Conceitual
$$\text{Densidade de Defeitos} = \frac{\text{Quantidade Total de Defeitos}}{\text{Tamanho em KLOC}}$$

### Matemática
$$D_{\text{KLOC}} = \frac{N_{\text{def}}}{\text{KLOC}}$$

### Exemplo
Foram encontrados 40 defeitos no código de 10 KLOC do Sistema de Biblioteca.
$$D_{\text{KLOC}} = \frac{40}{10} = 4\text{ defeitos/KLOC}$$

---

## 3. Você consegue responder?
1. Qual a fórmula da produtividade em LOC/hora?
2. Calcule a produtividade de uma equipe que escreveu 6.000 LOC em 300 horas.
3. Se um software de 15 KLOC apresentou 30 defeitos, qual é sua densidade de defeitos por KLOC?
4. O que indica uma diminuição na densidade de defeitos/KLOC ao longo de três releases sucessivas?
5. Escreva a equação matemática da densidade de defeitos por KLOC.

---

## 📚 Referências utilizadas
- **Fenton, N. E. & Bieman, J.** *Software Metrics*, 3rd ed.
