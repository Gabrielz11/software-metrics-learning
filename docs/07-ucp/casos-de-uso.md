# Classificação de Casos de Uso em UCP (UUCW)

O **UUCW** (*Unadjusted Use Case Weight*) calcula o peso dos casos de uso com base na quantidade de transações contidas em seus fluxos principal e alternativos.

---

## 1. Tabela de Classificação de Casos de Uso (Karner)

| Categoria | Complexidade / Número de Transações | Peso |
| :--- | :--- | :---: |
| **Simples** | 1 a 3 transações | **5** |
| **Médio** | 4 a 7 transações | **10** |
| **Complexo** | 8 ou mais transações | **15** |

---

## 2. Conceito de Transação em UCP
Uma transação é um ciclo completo de eventos entre o ator e o sistema (envio de dados pelo ator, processamento/validação pelo sistema e resposta de retorno).

---

## 3. Exemplo Prático no Sistema de Biblioteca

- `UC01_ManterUsuarios`: 4 transações -> Médio (Peso 10)
- `UC02_ManterAcervo`: 4 transações -> Médio (Peso 10)
- `UC03_RealizarEmprestimo`: 8 transações com regras -> Complexo (Peso 15)
- `UC04_RegistrarDevolucao`: 3 transações -> Simples (Peso 5)
- `UC05_PesquisarLivros`: 2 transações -> Simples (Peso 5)

$$\text{UUCW} = 10 + 10 + 15 + 5 + 5 = 45$$

---

## 4. Você consegue responder?
1. Como se determina a complexidade de um caso de uso na técnica UCP?
2. Quais são as três categorias de peso para casos de uso e seus respectivos valores numéricos (5, 10, 15)?
3. O que constitui uma transação em um cenário de caso de uso?
4. Calcule o UUCW de um sistema com 2 casos de uso simples e 1 caso de uso complexo.
5. Se um caso de uso possui 5 transações no fluxo principal e 4 nos alternativos (total 9), qual o seu peso?

??? check "Mostrar Gabarito / Resposta"
    1. **Determinação de complexidade:** Pelo número de transações (ou passos lógicos atômicos) contidas na descrição do caso de uso (somando fluxos principal, alternativos e de exceção).
    2. **Três categorias e pesos:**
       - *Simples:* 1 a 3 transações (Peso 5).
       - *Médio:* 4 a 7 transações (Peso 10).
       - *Complexo:* 8 ou mais transações (Peso 15).
    3. **O que é uma transação:** Uma sequência atômica de passos executados entre o ator e o sistema que é realizada completamente ou abortada (ex: envio de formulário e validação/resposta do sistema).
    4. **Cálculo de UUCW:** $2 \times 5 \text{ (simples)} + 1 \times 15 \text{ (complexo)} = 10 + 15 = 25$.
    5. **Caso de uso com 9 transações:** Classifica-se como **Complexo** ($\ge 8$ transações), recebendo **Peso 15**.

---

## 📚 Referências utilizadas
- **Karner, Gustav**. *Resource Estimation Based on Use Cases*, 1993.
