# Velocity (Velocidade do Time)

A **Velocity** representa o volume médio de unidades de trabalho (Story Points, Itens ou Tarefas) concluídas por uma equipe durante uma iteração (Sprint).

---

## 1. O que é?
Mede o ritmo histórico de entregas da equipe para auxiliar no planejamento das próximas sprints.

$$\text{Velocity Médio} = \frac{\sum_{i=1}^{N} \text{Pontos Concluídos na Sprint}_i}{N}$$

---

## 2. Anti-Padrões no Uso do Velocity

!!! danger "Anti-Padrão: Comparar Velocity entre Equipes Diferentes"
    Story Points são estimativas relativas locais de uma equipe específica. Comparar o Velocity de duas equipes distintas é um erro grave de gestão, pois induz à inflação artificial dos pontos (*Point Inflation*).

---

## 3. Você consegue responder?
1. Como se calcula o Velocity médio de uma equipe Scrum?
2. Por que é proibido comparar a Velocity entre equipes diferentes?
3. O que é a inflação de pontos (*Point Inflation*)?
4. Qual a utilidade primária da Velocity no planejamento de capacidades futuras?
5. Uma equipe que concluiu 30, 25 e 35 pontos nas últimas três sprints possui qual Velocity médio?

??? check "Mostrar Gabarito / Resposta"
    1. **Cálculo do Velocity médio:** É a média aritmética da soma dos Story Points de itens totalmente concluídos (*Done*) nas últimas $N$ sprints (geralmente 3 a 5 sprints).
    2. **Comparação proibida entre equipes:** Porque a pontuação de Story Points é uma estimativa relativa local e subjetiva de uma equipe específica. Comparar equipes diferentes destrói a calibração interna e gera distorções.
    3. **Inflação de Pontos (*Point Inflation*):** Fenômeno em que a equipe passa a inflacionar a pontuação atribuída às histórias (ex: transformar tarefas de 3 pontos em 8 pontos) apenas para parecer mais "produtiva" quando cobrada por métricas absolutas de velocity.
    4. **Utilidade primária:** Prever a capacidade de entrega real da equipe para as próximas sprints e calcular previsões de término de releases no backlog.
    5. **Cálculo (30, 25 e 35 pontos):**
       $$\text{Velocity Médio} = \frac{30 + 25 + 35}{3} = 30 \text{ pontos/sprint}$$

---

## 📚 Referências utilizadas
- **Cohn, Mike**. *Agile Estimating and Planning*, Prentice Hall.
