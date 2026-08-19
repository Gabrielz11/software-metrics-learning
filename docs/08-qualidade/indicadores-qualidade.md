# Indicadores de Qualidade Operacional

Este capítulo apresenta os principais indicadores operacionais utilizados para monitorar a confiabilidade e disponibilidade do software em produção.

---

## 1. MTBF — Mean Time Between Failures (Tempo Médio Entre Falhas)

Mede o tempo médio em que o sistema opera continuamente sem apresentar falhas.

$$\text{MTBF} = \frac{\text{Tempo Total de Operação}}{\text{Número de Falhas Ocorridas}}$$

---

## 2. MTTR — Mean Time to Repair (Tempo Médio de Reparo)

Mede o tempo médio necessário para identificar, corrigir e restabelecer o sistema após a ocorrência de uma falha.

$$\text{MTTR} = \frac{\text{Tempo Total de Indisponibilidade/Manutenção}}{\text{Número de Falhas Corrigidas}}$$

---

## 3. Disponibilidade (Availability - $A$)

Porcentagem do tempo total em que o sistema esteve totalmente operacional e disponível para os usuários.

$$A = \left( \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}} \right) \times 100\%$$

---

## 4. Você consegue responder?
1. O que representam as siglas MTBF e MTTR?
2. Se um sistema opera por 1.000 horas e apresenta 5 falhas com tempo total de reparo de 10 horas, quais são o MTBF e o MTTR?
3. Qual a fórmula da Disponibilidade percentual de um sistema?
4. Como a redução do MTTR afeta a disponibilidade geral de um software?
5. Qual a diferença entre MTTR e Lead Time de um bug?

??? check "Mostrar Gabarito / Resposta"
    1. **MTBF e MTTR:**
       - *MTBF:* Mean Time Between Failures (Tempo Médio Entre Falhas).
       - *MTTR:* Mean Time To Repair (Tempo Médio Para Reparo).
    2. **Cálculo de MTBF e MTTR (1.000h de operação, 5 falhas, 10h reparo):**
       $$\text{MTBF} = \frac{1.000}{5} = 200 \text{ horas/falha}$$
       $$\text{MTTR} = \frac{10}{5} = 2 \text{ horas/reparo}$$
    3. **Fórmula da Disponibilidade:**
       $$A = \left( \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}} \right) \times 100\%$$
    4. **Efeito da redução do MTTR:** Como o MTTR está no denominador da fração de indisponibilidade, recuperar o sistema mais rapidamente aumenta diretamente a porcentagem de disponibilidade total.
    5. **MTTR vs. Lead Time do Bug:** MTTR mede estritamente o tempo de indisponibilidade ativa do serviço do momento em que cai até voltar a funcionar; o Lead Time de um bug mede o tempo total desde que a issue foi aberta no repositório até sua correção final ir para produção.

---

## 📚 Referências utilizadas
- **Kan, S. H.** *Metrics and Models in Software Quality Engineering*, 2nd ed.
- **IEEE Computer Society**. *SWEBOK V4.0a*, Chapter 10.
