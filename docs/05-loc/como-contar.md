# Como Contar Linhas de Código

A contagem de linhas exige a definição clara entre **Linhas Físicas** e **Linhas Lógicas**.

---

## 1. Linhas Físicas vs Linhas Lógicas

- **Linhas Físicas**: Quantidade total de linhas finalizadas pelo caractere de quebra de linha (`\n`), incluindo linhas de comentários e linhas vazias.
- **Linhas Lógicas**: Quantidade de instruções/instruções executáveis distintas no código.

---

## 2. Exemplo em Código Python

```python
# Módulo de Empréstimos (Comentário - Linha 1)
def validar_usuario(usuario):  # Instrução Lógica (Linha 2)
    if usuario.ativo and not usuario.bloqueado:  # Instrução Lógica (Linha 3)
        return True  # Instrução Lógica (Linha 4)

    return False  # Instrução Lógica (Linha 5)
```

- **Linhas Físicas Totais**: 7 linhas (incluindo linhas vazias)
- **Linhas de Comentários**: 1 linha
- **Linhas em Branco**: 2 linhas
- **Linhas Lógicas executáveis (SLOC)**: 4 linhas

---

## 3. Regras de Contagem Adotadas no Repositório

1. Comentários de linha única (`#` ou `//`) são contados como comentários.
2. Blocos de comentários multilinha (`/* ... */` ou `""" ... """`) são contados como linhas de comentário.
3. Linhas contendo apenas espaços ou tabulações são contadas como linhas em branco.
4. Qualquer linha contendo instrução executável ou declaração é contada como SLOC.

---

## 4. Você consegue responder?
1. Qual a diferença entre linhas físicas e linhas lógicas de código?
2. Como uma linha vazia é tratada na contagem de SLOC?
3. Se um desenvolvedor colocar duas instruções Python na mesma linha separadas por ponto e vírgula `;`, quantas linhas físicas e quantas lógicas teremos?
4. Por que convenções de codificação (como PEP 8) alteram a contagem de linhas físicas?
5. Qual a importância das ferramentas automáticas de análise na contagem de LOC?

---

## 📚 Referências utilizadas
- **Fenton, N. E. & Bieman, J.** *Software Metrics*, 3rd ed.
