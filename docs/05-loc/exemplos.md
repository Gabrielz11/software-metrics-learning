# Exemplos Práticos de Contagem de LOC

Este capítulo demonstra a contagem aplicada de linhas de código em trechos funcionais do *Sistema de Biblioteca*.

---

## 1. Trecho 1: Função de Desconto

```python
def calcular_desconto(valor: float, cliente_frequente: bool) -> float:
    # Aplica 15% de desconto para clientes frequentes
    if cliente_frequente:
        return valor * 0.85

    if valor > 500.0:
        return valor * 0.90

    return valor
```

### Análise de Linhas
- **Linhas Físicas Totais**: 9
- **Linhas de Comentários**: 1
- **Linhas em Branco**: 2
- **SLOC (Linhas de Código Executável)**: 6

---

## 2. Execução via Biblioteca Python do Projeto

Você pode reproduzir esta contagem utilizando o módulo `software_metrics.loc`:

```python
from software_metrics.loc import count_code_lines

code = """
def calcular_desconto(valor, cliente_frequente):
    # Comentário
    if cliente_frequente:
        return valor * 0.85
    return valor
"""

stats = count_code_lines(code)
print(stats)
# Saída: {'total_lines': 7, 'blank_lines': 1, 'comment_lines': 1, 'code_lines': 5}
```

---

## 3. Você consegue responder?
1. Qual a utilidade do módulo `software_metrics.loc` na automação da contagem de linhas?
2. Em um projeto com 500 arquivos Python, como automatizar a extração de KLOC?
3. Por que a contagem manual de LOC torna-se inviável em projetos médios e grandes?
4. Mostre como identificar as linhas em branco em uma função.
5. Qual a contagem SLOC de um arquivo composto apenas por docstrings e comentários?

---

## 📚 Referências utilizadas
- **Fenton, N. E. & Bieman, J.** *Software Metrics*, 3rd ed.
