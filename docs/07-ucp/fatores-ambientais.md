# Fatores Ambientais em UCP (ECF)

O **ECF** (*Environmental Complexity Factor*) avalia 8 fatores relacionados à equipe de desenvolvimento e maturidade do ambiente.

---

## 1. Tabela dos 8 Fatores Ambientais (E1 a E8)

| Código | Descrição do Fator Ambiental | Peso ($w_j$) |
| :---: | :--- | :---: |
| **E1** | Familiaridade com o processo de desenvolvimento | 1.5 |
| **E2** | Experiência com a aplicação / domínio de negócio | 0.5 |
| **E3** | Experiência em Orientação a Objetos | 1.0 |
| **E4** | Capacidade e liderança do Analista Principal | 0.5 |
| **E5** | Motivação da equipe | 1.0 |
| **E6** | Estabilidade dos requisitos | 2.0 |
| **E7** | Trabalhadores em tempo parcial (*Part-time*) | -1.0 |
| **E8** | Dificuldade da linguagem de programação | -1.0 |

---

## 2. Equação do ECF

Cada fator é avaliado de **0 (baixo/nulo)** a **5 (alto)**.

$$\text{ECF} = 1.4 + \left( -0.03 \times \sum_{j=1}^{8} (w_j \times \text{Nota}_j) \right)$$

---

## 3. Você consegue responder?
1. Quantos fatores ambientais compõem o ECF?
2. Por que os fatores E7 e E8 possuem pesos negativos na equação?
3. Qual fator ambiental tem o maior peso positivo (E6 = 2.0)?
4. O que acontece com a estimativa final em UCP quando a equipe possui alta maturidade e experiência?
5. Qual a faixa de avaliação de cada fator ambiental?

---

## 📚 Referências utilizadas
- **Karner, Gustav**. *Resource Estimation Based on Use Cases*, 1993.
