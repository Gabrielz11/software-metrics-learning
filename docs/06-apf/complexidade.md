# Matrizes de Complexidade Funcional IFPUG

O IFPUG estabelece matrizes normativas para classificar a complexidade de cada função em **Baixa**, **Média** ou **Alta**.

---

## 1. Matriz de Complexidade para Funções de Dados (ALI / AIE)

Com base na quantidade de **RETs** e **DETs**:

| RET / DET | 1 a 19 DETs | 20 a 50 DETs | 51+ DETs |
| :--- | :---: | :---: | :---: |
| **1 RET** | Baixa | Baixa | Média |
| **2 a 5 RETs** | Baixa | Média | Alta |
| **6+ RETs** | Média | Alta | Alta |

---

## 2. Matriz de Complexidade para Entradas Externas (EE)

Com base na quantidade de **FTRs** e **DETs**:

| FTR / DET | 1 a 4 DETs | 5 a 15 DETs | 16+ DETs |
| :--- | :---: | :---: | :---: |
| **0 a 1 FTR** | Baixa | Baixa | Média |
| **2 FTRs** | Baixa | Média | Alta |
| **3+ FTRs** | Média | Alta | Alta |

---

## 3. Matriz de Complexidade para Saídas Externas (SE) e Consultas Externas (CE)

Com base na quantidade de **FTRs** e **DETs**:

| FTR / DET | 1 a 5 DETs | 6 a 19 DETs | 20+ DETs |
| :--- | :---: | :---: | :---: |
| **0 a 1 FTR** | Baixa | Baixa | Média |
| **2 a 3 FTRs** | Baixa | Média | Alta |
| **4+ FTRs** | Média | Alta | Alta |

---

## 4. Você consegue responder?
1. Qual a complexidade de um ALI com 1 RET e 30 DETs?
2. Qual a complexidade de uma EE com 3 FTRs e 10 DETs?
3. Qual a complexidade de uma CE com 1 FTR e 8 DETs?
4. Por que a matriz de EE é mais rigorosa nos limites de DET do que a matriz de SE/CE?
5. Qual a complexidade de um AIE que possui 7 RETs e 60 DETs?

??? check "Mostrar Gabarito / Resposta"
    1. **ALI (1 RET, 30 DETs):** Média complexidade (faixa de 20 a 50 DETs com 1 RET).
    2. **EE (3 FTRs, 10 DETs):** Média complexidade (faixa de 5 a 15 DETs com 2 a 3 FTRs).
    3. **CE (1 FTR, 8 DETs):** Baixa complexidade (1 FTR com 6 a 19 DETs).
    4. **Matriz de EE mais rigorosa:** Porque entradas externas realizam escrita e validações de dados diretas no banco de dados, acumulando riscos de integridade funcional com menos campos.
    5. **AIE (7 RETs, 60 DETs):** Alta complexidade (mais de 5 RETs e mais de 50 DETs).

---

## 📚 Referências utilizadas
- **IFPUG**. *Function Point Counting Practices Manual*, Release 4.3.1.
