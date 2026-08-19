# Complexidade Ciclomática de McCabe

Desenvolvida por Thomas McCabe em 1976, a **Complexidade Ciclomática** $V(G)$ mede a quantidade de caminhos linearmente independentes no grafo de fluxo de controle de um programa.

---

## 1. Fórmulas de McCabe

### Fórmula Baseada em Grafos
$$V(G) = E - N + 2P$$

Onde:
- $E$ = Número de arestas (*edges*) no grafo de fluxo.
- $N$ = Número de nós (*nodes*) no grafo.
- $P$ = Número de componentes conectados (geralmente $P=1$ para um único método/função).

### Fórmula Simplificada por Predicados
$$V(G) = D + 1$$

Onde:
- $D$ = Número de nós de decisão (estruturas condicionais como `if`, `while`, `for`, `case`).

---

## 2. Exemplo em Código Python

```python
def conceder_desconto(valor, premium):
    if premium:              # Decisão 1 (+1)
        return valor * 0.80

    if valor > 1000:         # Decisão 2 (+1)
        return valor * 0.90

    return valor             # Base (+1)
```

$$\text{Complexidade Ciclomática } V(G) = 2\text{ (decisões)} + 1 = 3$$

---

## 3. Tabela de Riscos de McCabe

| Complexidade $V(G)$ | Nível de Risco | Avaliação do Código |
| :---: | :--- | :--- |
| **1 a 10** | Baixo Risco | Código simples, alta testabilidade. |
| **11 a 20** | Médio Risco | Código moderado, atenção na testabilidade. |
| **21 a 50** | Alto Risco | Código complexo, necessita refatoração imediata. |
| **> 50** | Múltiplo Risco / Incorrigível | Código não testável, altíssimo risco de manutenção. |

---

## 4. Você consegue responder?
1. Quem foi o criador da métrica de Complexidade Ciclomática?
2. Quais são as duas fórmulas de cálculo de $V(G)$ propostas por McCabe?
3. Calcule $V(G)$ para uma função que contém 3 instruções `if` e 1 laço `while`.
4. Qual o limite recomendado de complexidade ciclomática para uma única função antes de exigir refatoração?
5. Qual a relação entre a complexidade ciclomática e o número mínimo de casos de teste necessários para cobertura completa de caminhos?

---

## 📚 Referências utilizadas
- **McCabe, Thomas J.** *A Complexity Measure*, IEEE Transactions on Software Engineering, 1976.
- **Fenton, N. E. & Bieman, J.** *Software Metrics*, 3rd ed.
