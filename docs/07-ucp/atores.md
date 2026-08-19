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

??? check "Mostrar Gabarito / Resposta"
    1. **Categorias e pesos de atores:**
       - *Simples:* API / Interface de sistema definida (Peso 1).
       - *Médio:* Protocolo de comunicação / CLI / Linha de comando (Peso 2).
       - *Complexo:* Usuário humano via Interface Gráfica / Web GUI (Peso 3).
    2. **Peso 3 para usuário via GUI:** Porque interfaces gráficas envolvem entradas imprevisíveis do usuário, validações de tela, navegação complexa e tratamento de erros visuais.
    3. **Peso de API REST externa:** Ator Simples, com Peso 1.
    4. **Cálculo de UAW:** $2 \text{ humanos (complexos)} \times 3 + 1 \text{ API (simples)} \times 1 = 6 + 1 = 7$.
    5. **Diferença de peso CLI vs. GUI:** Ator via CLI tem peso 2 (Médio) e via GUI tem peso 3 (Complexo), uma diferença de 1 ponto.

---

## 📚 Referências utilizadas
- **Karner, Gustav**. *Resource Estimation Based on Use Cases*, 1993.
