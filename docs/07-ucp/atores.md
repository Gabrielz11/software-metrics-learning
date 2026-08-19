# Classificação de Atores em UCP (UAW)

O **UAW** (*Unadjusted Actor Weight*) calcula o peso dos atores que interagem com os casos de uso da aplicação.

---

## 1. Tabela de Classificação de Atores (Karner)

| Categoria | Descrição / Tipo de Interface | Peso |
| :--- | :--- | :---: |
| **Simples** | Sistema externo interagindo por meio de uma API estruturada ou protocolo bem definido (ex: REST JSON, SOAP). | **1** |
| **Médio** | Sistema externo interagindo via protocolo interativo (ex: TCP/IP) ou interface em linha de comando (CLI) / arquivos texto. | **2** |
| **Complexo** | Usuário humano interagindo por meio de uma Interface Gráfica (GUI, Web UI, App Mobile). | **3** |

---

## 2. Exemplo Prático no Sistema de Biblioteca

- **Ator `Leitor`**: Usuário humano interagindo via Web UI -> Complexo (Peso 3)
- **Ator `Bibliotecário`**: Usuário humano interagindo via Web UI -> Complexo (Peso 3)
- **Ator `ServiçoExternoCredito`**: Sistema parceiro via API REST -> Simples (Peso 1)

$$\text{UAW} = 3 + 3 + 1 = 7$$

---

## 3. Você consegue responder?
1. Quais são as três categorias de atores em UCP e seus respectivos pesos?
2. Por que um usuário humano através de interface web recebe peso 3 (complexo)?
3. Qual o peso atribuído a uma API externa REST de terceiros?
4. Calcule o UAW de um sistema que possui 2 usuários humanos e 1 sistema externo via API.
5. Qual a diferença de peso entre um ator via CLI e um via GUI?

---

## 📚 Referências utilizadas
- **Karner, Gustav**. *Resource Estimation Based on Use Cases*, 1993.
