# Exercícios: APF (Análise de Pontos de Função)

---

## 🟢 Exercícios Básicos

### Exercício 01 🟢
Uma tabela de banco de dados é mantida internamente pela aplicação. Ela possui 1 subgrupo de dados (RET) e 12 campos (DET). Classifique essa função de dados (ALI ou AIE) e informe sua complexidade e pontos de função.

### Exercício 02 🟢
Uma tela de cadastro recebe dados digitados pelo usuário para incluir um novo registro no banco interno. Ela acessa 1 ALI e possui 4 DETs. Classifique a transação (EE, SE ou CE) e determine sua complexidade e pontos.

### Exercício 03 🟢
Qual o peso em Pontos de Função de um Arquivo de Interface Externa (AIE) de complexidade Média segundo a tabela do IFPUG?

### Exercício 04 🟢
Uma funcionalidade de consulta simples lê 1 ALI e exibe 3 campos na tela sem efetuar cálculos. Classifique a transação e informe seus Pontos de Função.

### Exercício 05 🟢
Um relatório estatístico calcula médias de vendas, acessa 3 ALIs e exibe 10 DETs. Classifique a transação (EE, SE ou CE), determine sua complexidade e calcule seus Pontos de Função.

---

## 🟡 Exercícios Intermediários

### Exercício 06 🟡
Um sistema possui 3 ALIs de complexidade Baixa, 1 AIE de complexidade Baixa, 4 EEs de complexidade Baixa e 2 CEs de complexidade Baixa. Calcule o total de Pontos de Função Não Ajustados (PFNA).

### Exercício 07 🟡
Uma fábrica de software cobra R$ 800,00 por Ponto de Função entregue. Se um módulo possui 40 PF, qual será o custo total contratual do módulo?

### Exercício 08 🟡
Se a taxa de esforço histórica de uma equipe é de 8 horas por Ponto de Função, quantas horas serão estimadas para desenvolver um sistema contado em 65 PF?

### Exercício 09 🟡
Classifique a função: Uma tela de importação de arquivo texto lê um arquivo mantido por um sistema legado externo (3 RETs e 25 DETs). A aplicação apenas lê esse arquivo sem alterá-lo. Classifique e determine os PF.

### Exercício 10 🟡
Uma alteração de manutenção inclui 2 novos campos (DETs) em uma Entrada Externa (EE) existente que mantinha 1 ALI (1 FTR), passando de 3 DETs para 5 DETs. O que acontece com a complexidade e com os Pontos de Função dessa EE?

---

## 🔴 Exercícios Avançados / Desafio

### Exercício 11 🔴
Estudo de Caso Mapeamento Completo: Um sistema de e-commerce possui as seguintes especificações:
- ALI Clientes (1 RET, 8 DET)
- ALI Produtos (1 RET, 10 DET)
- ALI Pedidos (2 RET, 12 DET)
- EE Cadastrar Cliente (1 FTR, 5 DET)
- EE Efetuar Pedido (3 FTR, 8 DET)
- CE Consultar Produto (1 FTR, 4 DET)
- SE Extrato Financeiro de Vendas (3 FTR, 15 DET)
Determine a complexidade de cada função e calcule o total de Pontos de Função Não Ajustados (PFNA).

### Exercício 12 🔴
Análise de Produtividade e Custo: O sistema do Exercício 11 foi desenvolvido em 320 horas por uma equipe de 2 desenvolvedores com custo de R$ 100/hora.
a) Calcule a produtividade em PF/hora e em horas/PF.  
b) Calcule o custo total do projeto e o custo unitário por Ponto de Função.

### Exercício 13 🔴
Tomada de Decisão Contratual: Um fornecedor A propõe entregar um sistema de 100 PF a um preço de R$ 900/PF com prazo de 3 meses. O fornecedor B propõe o mesmo sistema a R$ 1.200/PF com taxa de esforço garantida de 5h/PF. Sabendo que o custo interno da sua hora é de R$ 150/h, qual fornecedor apresenta o menor custo total para a organização?
