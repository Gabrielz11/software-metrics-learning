# Dimensão 2: Esforço em Software

O **Esforço** representa o total de tempo de trabalho humano investido para produzir ou manter um artefato de software.

---

## 1. Unidades de Medida de Esforço

- **Horas-Pessoa (Person-Hours / Horas de Desenvolvimento)**: Unidade mais granular de registro direto de trabalho.
- **Pessoa-Mês (Person-Month - PM)**: Unidade padrão em modelos clássicos de estimativa (como COCOMO). Representa a quantidade de trabalho realizada por uma pessoa em tempo integral durante um mês (geralmente convencionado entre 152h e 160h).

$$\text{Pessoa-Mês (PM)} = \frac{\text{Total de Horas-Pessoa}}{160}$$

---

## 2. Relação entre Tamanho e Esforço

O esforço é uma função não linear do tamanho do software, devido aos custos de comunicação e complexidade da equipe à medida que o sistema cresce.

$$E = a \cdot (S)^b$$

Onde:
- $E$ = Esforço em Pessoa-Mês.
- $S$ = Tamanho (KLOC ou PF).
- $a, b$ = Constantes empíricas derivadas do histórico da organização.

---

## 3. Exemplo Prático no Sistema de Biblioteca

!!! example "Cálculo de Esforço no Sistema de Biblioteca"
    O desenvolvimento do *Sistema de Biblioteca* consumiu 500 horas-pessoa no total.
    $$\text{Esforço em Pessoa-Mês} = \frac{500}{160} = 3.125\text{ PM}$$

---

## 4. Erros Comuns
- Confundir **Esforço** (horas de trabalho total) com **Prazo** (tempo decorrido no calendário). Adicionar mais pessoas a um projeto atrasado pode aumentar o esforço total sem reduzir o prazo (Lei de Brooks).

## 5. Você consegue responder?
1. Qual a diferença entre Esforço e Prazo?
2. O que representa 1 Pessoa-Mês (PM)?
3. Por que a relação entre tamanho e esforço em software não é perfeitamente linear?
4. Se um projeto exige 480 horas-pessoa, a quantos Pessoas-Mês isso equivale?
5. Qual é a célebre Lei de Brooks sobre esforço e equipes em projetos atrasados?

---

## 📚 Referências utilizadas
- **Pressman, R. S. & Maxim, B. R.** *Software Engineering: A Practitioner's Approach*, 9th ed., 2019.
- **Brooks, Frederick P.** *The Mythical Man-Month*, Addison-Wesley.
