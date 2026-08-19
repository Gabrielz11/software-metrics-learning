# Elementos de Contagem: DET, RET e FTR

A determinação da complexidade das Funções de Dados e Transacionais baseia-se na contagem exata dos seus elementos constitutivos.

---

## 1. DET — Data Element Type (Tipo de Dado Elementar)

Um DET é um campo único, não repetitivo, identificável pelo usuário.

### Exemplos
- No formulário de cadastro: `Nome`, `CPF`, `Data de Nascimento`, `Email` -> 4 DETs.
- Em um relatório: `Título do Livro`, `Data de Empréstimo`, `Valor da Multa` -> 3 DETs.

---

## 2. RET — Record Element Type (Tipo de Registro Elementar)

Um RET é um subgrupo de dados reconhecido pelo usuário dentro de um ALI ou AIE.

### Exemplos
- No `ALI_Usuario`: Subgrupo `Dados Pessoais` e subgrupo `Endereço` -> 2 RETs.
- Se o `ALI_Livro` não possuir subgrupos -> 1 RET.

---

## 3. FTR — File Type Referenced (Tipo de Arquivo Referenciado)

Um FTR é um ALI mantido ou lido por uma função transacional, ou um AIE lido por essa transação.

### Exemplos
- Na transação `Realizar Empréstimo`, que lê o `ALI_Usuario`, lê o `ALI_Livro` e altera o `ALI_Emprestimo` -> 3 FTRs.

---

## 4. Resumo de Atribuição de Elementos

```text
Funções de Dados (ALI / AIE)       ──────► DET + RET
Funções Transacionais (EE / SE / CE) ──────► DET + FTR
```

---

## 5. Você consegue responder?
1. O que é um DET e como ele é contado em uma tela?
2. Qual a diferença entre um RET e um FTR?
3. Quais elementos de contagem são usados para determinar a complexidade de um ALI?
4. Quais elementos de contagem são usados para determinar a complexidade de uma Entrada Externa (EE)?
5. Se uma transação lê 2 ALIs e 1 AIE, quantos FTRs ela possui?

---

## 📚 Referências utilizadas
- **IFPUG**. *Function Point Counting Practices Manual*, Release 4.3.1.
