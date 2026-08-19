# Requisitos do Sistema de Biblioteca

Especificação completa dos Requisitos Funcionais (RF) e Não-Funcionais (RNF) do estudo de caso.

---

## 1. Requisitos Funcionais (RF)

- **RF01 — Cadastrar usuário**: Permite incluir leitores com dados de identificação (nome, CPF, email).
- **RF02 — Atualizar usuário**: Permite alterar dados cadastrais do leitor.
- **RF03 — Cadastrar livro**: Permite registrar novas obras no acervo (título, autor, ISBN, categoria).
- **RF04 — Realizar empréstimo**: Permite vincular um exemplar a um leitor verificado e sem pendências.
- **RF05 — Registrar devolução**: Permite dar baixa em empréstimo ativo e liberar o exemplar.
- **RF06 — Consultar livro**: Permite buscar livros por palavra-chave ou autor.
- **RF07 — Consultar empréstimos**: Permite ao leitor ou bibliotecário verificar pendências ativas.
- **RF08 — Gerar relatório de empréstimos atrasados**: Apresenta listagem de atrasos e estatísticas de multas.

---

## 2. Requisitos Não-Funcionais (RNF)

- **RNF01 — Interface**: Interface Web amigável em HTML5/CSS3.
- **RNF02 — Segurança**: Integração de validação de CPF via serviço de consulta externo.
- **RNF03 — Desempenho**: Tempo de resposta inferior a 2 segundos para consultas.

---

## 3. Você consegue responder?
1. Quantos Requisitos Funcionais compõem a especificação do Sistema de Biblioteca?
2. Qual requisito funcional envolve a integração com serviço externo de consulta?
3. Quais são as entidades de dados mantidas no sistema?
4. Como a clareza dos requisitos afeta a contagem de Pontos de Função?
5. Qual a importância de manter a especificação de requisitos estável para o cálculo de UCP?

??? check "Mostrar Gabarito / Resposta"
    1. **Quantidade de Requisitos Funcionais:** 5 requisitos funcionais (RF01 a RF05: Manter Usuários, Manter Livros, Realizar Empréstimo, Registrar Devolução e Consultar Livro/Atrasos).
    2. **Integração externa:** O RF01 / RNF02, que realiza a consulta de validação de CPF junto a um serviço externo via API.
    3. **Entidades de dados mantidas:** `Livro` e `Empréstimo` (ALIs internos) e `Usuário` (mantido/consultado via AIE externo).
    4. **Clareza de requisitos na APF:** Requisitos claros e bem detalhados evitam ambiguidade na identificação de DETs, FTRs e tipos de funções, reduzindo a variabilidade entre contadores.
    5. **Estabilidade de requisitos no UCP:** Como o UCP se baseia no fatiamento de cenários de casos de uso e contagem de transações, qualquer alteração no fluxo altera o valor de UUCW e a estimativa final em horas.

---

## 📚 Referências utilizadas
- **Sommerville, I.** *Software Engineering*, 10th ed.
