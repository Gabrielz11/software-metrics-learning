# Cálculo e Tabela de Pesos IFPUG

Após classificar a complexidade de cada função de dados e transação (Baixa, Média ou Alta), aplicam-se os **pesos oficiais do IFPUG** para obter a contagem de Pontos de Função Não Ajustados (PFNA).

---

## 1. Tabela Oficial de Pesos IFPUG

| Tipo de Função | Complexidade Baixa | Complexidade Média | Complexidade Alta |
| :--- | :---: | :---: | :---: |
| **ALI (Arquivo Lógico Interno)** | 7 PF | 10 PF | 15 PF |
| **AIE (Arquivo de Interface Externa)** | 5 PF | 7 PF | 10 PF |
| **EE (Entrada Externa)** | 3 PF | 4 PF | 6 PF |
| **SE (Saída Externa)** | 4 PF | 5 PF | 7 PF |
| **CE (Consulta Externa)** | 3 PF | 4 PF | 6 PF |

---

## 2. Equação do Somatório de PFNA

$$\text{PFNA} = \sum (\text{Qtd ALI}_i \times \text{Peso}) + \sum (\text{Qtd AIE}_i \times \text{Peso}) + \sum (\text{Qtd EE}_i \times \text{Peso}) + \sum (\text{Qtd SE}_i \times \text{Peso}) + \sum (\text{Qtd CE}_i \times \text{Peso})$$

---

## 3. Exemplo Didático

- 2 ALIs de Complexidade Baixa: $2 \times 7 = 14\text{ PF}$
- 1 EE de Complexidade Média: $1 \times 4 = 4\text{ PF}$
- 1 CE de Complexidade Baixa: $1 \times 3 = 3\text{ PF}$
- **Total PFNA** = $14 + 4 + 3 = 21\text{ PF}$

---

## 4. Você consegue responder?
1. Qual o peso de um ALI de alta complexidade?
2. Qual o peso de uma Entrada Externa (EE) de baixa complexidade?
3. Qual o peso de uma Saída Externa (SE) de média complexidade?
4. Como é calculado o total de Pontos de Função Não Ajustados (PFNA)?
5. Qual a diferença de peso entre um ALI baixo (7) e um AIE baixo (5)?

---

## 📚 Referências utilizadas
- **IFPUG**. *Function Point Counting Practices Manual*, Release 4.3.1.
