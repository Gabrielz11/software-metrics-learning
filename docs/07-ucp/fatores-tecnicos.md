# Fatores Técnicos em UCP (TCF)

O **TCF** (*Technical Complexity Factor*) avalia 13 requisitos não-funcionais e características técnicas da arquitetura do projeto.

---

## 1. Tabela dos 13 Fatores Técnicos (T1 a T13)

| Código | Descrição do Fator Técnico | Peso ($w_i$) |
| :---: | :--- | :---: |
| **T1** | Sistema Distribuído | 2.0 |
| **T2** | Desempenho / Tempo de Resposta | 1.0 |
| **T3** | Eficiência do Usuário Final | 1.0 |
| **T4** | Processamento Interno Complexo | 1.0 |
| **T5** | Reutilização de Código | 1.0 |
| **T6** | Facilidade de Instalação | 0.5 |
| **T7** | Facilidade de Uso | 0.5 |
| **T8** | Portabilidade | 2.0 |
| **T9** | Facilidade de Mudança / Manutenibilidade | 1.0 |
| **T10** | Concorrência | 1.0 |
| **T11** | Recursos de Segurança Especiais | 1.0 |
| **T12** | Acesso Direto a Terceiros | 1.0 |
| **T13** | Treinamento Especial do Usuário | 1.0 |

---

## 2. Escala de Avaliação e Equação

Cada fator recebe uma nota de **0 (irrelevante)** a **5 (essencial)**.

$$\text{TCF} = 0.6 + \left( 0.01 \times \sum_{i=1}^{13} (w_i \times \text{Nota}_i) \right)$$

---

## 3. Você consegue responder?
1. Quantos fatores técnicos compõem o cálculo do TCF?
2. Quais fatores técnicos possuem o maior peso individual (2.0)?
3. Qual é a faixa de notas atribuída a cada fator (0 a 5)?
4. Se todas as notas forem 0, qual será o valor mínimo do TCF?
5. Qual a finalidade do TCF no ajuste do tamanho em UCP?

??? check "Mostrar Gabarito / Resposta"
    1. **Quantidade de fatores técnicos:** 13 fatores (T1 a T13).
    2. **Fatores de maior peso (2.0):** T1 (Sistema Distribuído) e T2 (Performance / Tempo de Resposta).
    3. **Faixa de notas:** De 0 (sem impacto / irrelevante) a 5 (impacto essencial / crítico).
    4. **TCF Mínimo (todas as notas = 0):**
       $$\text{TCF} = 0,6 + (0,01 \times 0) = 0,60$$
    5. **Finalidade do TCF:** Ajustar a contagem não-ajustada de casos de uso (UUCP) incorporando os requisitos técnicos e não-funcionais da arquitetura do sistema.

---

## 📚 Referências utilizadas
- **Karner, Gustav**. *Resource Estimation Based on Use Cases*, 1993.
