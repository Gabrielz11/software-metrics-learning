# Funções Transacionais (EE, SE e CE)

As **Funções Transacionais** representam a funcionalidade oferecida ao usuário para processamento de dados que entram ou saem da fronteira da aplicação.

---

## 1. EE — Entrada Externa (External Input - EI)

Processo elementar que processa dados ou informações de controle vindas de fora da fronteira da aplicação. Sua intenção primária é **manter um ou mais ALIs** e/ou alterar o comportamento do sistema.

### Exemplos no Sistema de Biblioteca
- `Cadastrar Livro`: insere registro no `ALI_Livro`.
- `Atualizar Usuário`: altera atributos no `ALI_Usuario`.
- `Registrar Devolução`: atualiza estado no `ALI_Emprestimo`.

---

## 2. SE — Saída Externa (External Output - EO)

Processo elementar que envia dados para fora da fronteira da aplicação. Sua intenção primária é apresentar informação ao usuário **através de lógica de processamento que contém cálculos, derivações ou criação de dados derivados**.

### Exemplos no Sistema de Biblioteca
- `Gerar Relatório de Empréstimos Atrasados com Gráfico e Estatísticas Derivadas`.

---

## 3. CE — Consulta Externa (External Inquiry - EQ)

Processo elementar que envia dados para fora da fronteira da aplicação. Sua intenção primária é a **recuperação simples de dados** de um ALI ou AIE, sem realizar cálculos ou alterar ALIs.

### Exemplos no Sistema de Biblioteca
- `Consultar Livro por Título`.
- `Listar Empréstimos Ativos do Usuário`.

---

## 4. Tabela Comparativa de Funções Transacionais

| Função Transacional | Intenção Primária | Altera ALIs? | Executa Cálculos/Derivações? |
| :--- | :--- | :---: | :---: |
| **Entrada Externa (EE)** | Manter dados (Incluir/Alterar/Excluir) | **Sim** | Opcional |
| **Saída Externa (SE)** | Apresentar dados calculados/derivados | Não | **Sim** |
| **Consulta Externa (CE)** | Recuperação e exibição simples de dados | Não | **Não** |

---

## 5. Você consegue responder?
1. Qual a diferença fundamental entre uma Saída Externa (SE) e uma Consulta Externa (CE)?
2. Qual a intenção primária de uma Entrada Externa (EE)?
3. Uma tela de pesquisa simples que traz dados direto da tabela sem efetuar cálculos é uma SE ou CE?
4. A funcionalidade "Cadastrar Aluno" altera algum ALI? Qual a sua classificação?
5. Qual a sigla em inglês para Entrada Externa e Saída Externa?

??? check "Mostrar Gabarito / Resposta"
    1. **SE vs. CE:** Ambas enviam dados para fora da fronteira, mas a SE (Saída Externa) contém lógica matemática/cálculos adicionais, dados derivados ou manutenção de um ALI. A CE (Consulta Externa) apenas recupera e apresenta dados sem efetuar cálculos ou derivados.
    2. **Intenção primária da EE:** Processar dados ou informações de controle que vêm de fora da fronteira da aplicação para manter um ou mais ALIs.
    3. **Pesquisa simples sem cálculos:** É uma **CE** (Consulta Externa).
    4. **Cadastrar Aluno:** Altera/mantém o `ALI Aluno`. Sua classificação é **EE** (Entrada Externa).
    5. **Siglas em inglês:** EI (*External Input*) para Entrada Externa e EO (*External Output*) para Saída Externa.

---

## 📚 Referências utilizadas
- **IFPUG**. *Function Point Counting Practices Manual*, Release 4.3.1.
