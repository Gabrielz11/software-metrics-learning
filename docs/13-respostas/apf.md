# Respostas: APF (Análise de Pontos de Função)

---

## 🟢 Soluções dos Exercícios Básicos

### Solução 01 🟢
- **Classificação**: ALI (mantido internamente pela aplicação).
- **Complexidade**: 1 RET e 12 DETs -> **Baixa** (Tabela ALI/AIE).
- **Pontos de Função**: **7 PF**.

### Solução 02 🟢
- **Classificação**: EE (Entrada Externa, altera ALI interno).
- **Complexidade**: 1 FTR e 4 DETs -> **Baixa** (Tabela EE).
- **Pontos de Função**: **3 PF**.

### Solução 03 🟢
- Segundo a tabela oficial IFPUG, um AIE de complexidade Média vale **7 PF**.

### Solução 04 🟢
- **Classificação**: CE (Consulta Externa, recuperação simples de dados sem cálculo).
- **Complexidade**: 1 FTR e 3 DETs -> **Baixa**.
- **Pontos de Função**: **3 PF**.

### Solução 05 🟢
- **Classificação**: SE (Saída Externa, realiza médias e cálculos estatísticos).
- **Complexidade**: 3 FTRs e 10 DETs -> **Média** (Tabela SE/CE).
- **Pontos de Função**: **5 PF**.

---

## 🟡 Soluções dos Exercícios Intermediários

### Solução 06 🟡
- 3 ALIs Baixos: $3 \times 7 = 21\text{ PF}$
- 1 AIE Baixo: $1 \times 5 = 5\text{ PF}$
- 4 EEs Baixas: $4 \times 3 = 12\text{ PF}$
- 2 CEs Baixas: $2 \times 3 = 6\text{ PF}$
- **PFNA Total** = $21 + 5 + 12 + 6 = \mathbf{44\text{ PF}}$

### Solução 07 🟡
$$\text{Custo Total} = 40\text{ PF} \times \text{R\$ } 800,00/\text{PF} = \mathbf{\text{R\$ } 32.000,00}$$

### Solução 08 🟡
$$\text{Esforço Estimado} = 65\text{ PF} \times 8\text{ horas/PF} = \mathbf{520\text{ Horas}}$$

### Solução 09 🟡
- **Classificação**: AIE (dados mantidos fora da fronteira por sistema externo).
- **Complexidade**: 3 RETs e 25 DETs -> **Média** (Tabela ALI/AIE).
- **Pontos de Função**: **7 PF**.

### Solução 10 🟡
Com 1 FTR e 3 DETs, a EE era Baixa (3 PF). Passando para 5 DETs com 1 FTR, ela permanece de complexidade Baixa na tabela de EE (limite de Baixa é até 15 DETs para 0-1 FTR). O peso se mantém em **3 PF**.

---

## 🔴 Soluções dos Exercícios Avançados / Desafio

### Solução 11 🔴
1. **Funções de Dados**:
   - `ALI Clientes` (1 RET, 8 DET) -> Baixa = 7 PF
   - `ALI Produtos` (1 RET, 10 DET) -> Baixa = 7 PF
   - `ALI Pedidos` (2 RET, 12 DET) -> Média = 10 PF
   - *Subtotal Dados* = 24 PF
2. **Funções Transacionais**:
   - `EE Cadastrar Cliente` (1 FTR, 5 DET) -> Baixa = 3 PF
   - `EE Efetuar Pedido` (3 FTR, 8 DET) -> Alta = 6 PF
   - `CE Consultar Produto` (1 FTR, 4 DET) -> Baixa = 3 PF
   - `SE Extrato Financeiro` (3 FTR, 15 DET) -> Média = 5 PF
   - *Subtotal Transações* = 17 PF
3. **PFNA Total** = $24 + 17 = \mathbf{41\text{ PF}}$.

### Solução 12 🔴
a)
- $\text{Produtividade (PF/h)} = 41 / 320 = \mathbf{0.128\text{ PF/hora}}$
- $\text{Taxa de Esforço (h/PF)} = 320 / 41 \approx \mathbf{7.80\text{ horas/PF}}$

b)
- $\text{Custo Total} = 320\text{ h} \times \text{R\$ } 100/\text{h} = \mathbf{\text{R\$ } 32.000,00}$
- $\text{Custo por PF} = 32.000 / 41 \approx \mathbf{\text{R\$ } 780,49/\text{PF}}$

### Solução 13 🔴
- **Fornecedor A**:
  - Custo direto do contrato: $100\text{ PF} \times \text{R\$ } 900/\text{PF} = \mathbf{\text{R\$ } 90.000,00}$
- **Fornecedor B**:
  - Esforço garantido: $100\text{ PF} \times 5\text{ h/PF} = 500\text{ horas}$.
  - Custo interno decorrente: $500\text{ h} \times \text{R\$ } 150/\text{h} = \mathbf{\text{R\$ } 75.000,00}$

**Conclusão**: O **Fornecedor B** apresenta o menor custo total para a organização (economia de R$ 15.000,00).
