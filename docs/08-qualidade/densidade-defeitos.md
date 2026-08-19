# Densidade de Defeitos

A **Densidade de Defeitos** é a métrica primária para avaliação de qualidade normalizada pelo tamanho do software.

---

## 1. Fórmulas de Densidade de Defeitos

### Densidade por KLOC
$$D_{\text{KLOC}} = \frac{\text{Quantidade Total de Defeitos}}{\text{Tamanho em KLOC}}$$

### Densidade por Ponto de Função (PF)
$$D_{\text{PF}} = \frac{\text{Quantidade Total de Defeitos}}{\text{Tamanho em Pontos de Função (PF)}}$$

---

## 2. Exemplo Numérico no Sistema de Biblioteca

!!! example "Densidade de Defeitos no Sistema de Biblioteca"
    O *Sistema de Biblioteca* (10 KLOC ou 50 PF) apresentou 40 defeitos no acumulado de suas fases de teste.
    $$D_{\text{KLOC}} = \frac{40}{10} = 4.0\text{ defeitos/KLOC}$$
    $$D_{\text{PF}} = \frac{40}{50} = 0.8\text{ defeitos/PF}$$

---

## 3. Você consegue responder?
1. Por que a Densidade de Defeitos é uma métrica mais justa do que a contagem absoluta de defeitos?
2. Calcule a densidade de defeitos de um sistema de 20 KLOC que apresentou 30 defeitos.
3. Se um sistema de 100 PF possui 20 defeitos, qual sua densidade por PF?
4. Como comparar a qualidade de dois módulos de tamanhos diferentes usando densidade?
5. Escreva as duas equações de densidade de defeitos.

---

## 📚 Referências utilizadas
- **Kan, S. H.** *Metrics and Models in Software Quality Engineering*, 2nd ed.
