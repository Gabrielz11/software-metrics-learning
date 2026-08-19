# Funções de Dados (ALI e AIE)

As **Funções de Dados** representam os requisitos de armazenamento de dados mantidos ou referenciados pelo software.

---

## 1. ALI — Arquivo Lógico Interno (Internal Logical File - ILF)

Grupo de dados correlatos, identificável pelo usuário, mantido **dentro** da fronteira da aplicação por meio de um ou mais processos elementares da aplicação.

### Exemplos no Sistema de Biblioteca
- **ALI_Usuario**: Tabela/entidade de usuários mantida pelo cadastro interno.
- **ALI_Livro**: Entidade contendo as obras do acervo mantidas pela aplicação.
- **ALI_Emprestimo**: Registro de empréstimos e devoluções mantido internamente.

---

## 2. AIE — Arquivo de Interface Externa (External Interface File - EIF)

Grupo de dados correlatos, identificável pelo usuário, referenciado pela aplicação, mas mantido **fora** da fronteira de outra aplicação.

### Exemplos no Sistema de Biblioteca
- **AIE_SerasaCredito**: Cadastro de restrições de crédito mantido por um sistema externo bancário/órgão de proteção, consultado apenas para leitura pela biblioteca.

---

## 3. Regulamento IFPUG
- Arquivos de código temporários, tabelas de controle de sessão ou arquivos de log técnico NÃO são contados como ALI ou AIE.
- Um ALI de uma aplicação pode ser um AIE para outra aplicação que apenas lê seus dados.

---

## 4. Você consegue responder?
1. Qual a diferença fundamental entre um ALI e um AIE?
2. Por que arquivos temporários de banco de dados não são contados como ALIs?
3. Se o Sistema de Biblioteca consultar a tabela de CEPs dos Correios mantida externamente, essa tabela é um ALI ou AIE?
4. Qual a sigla em inglês para Arquivo Lógico Interno?
5. Dê dois exemplos de ALIs no contexto de um sistema acadêmico.

??? check "Mostrar Gabarito / Resposta"
    1. **ALI vs. AIE:** Um ALI (Arquivo Lógico Interno) é mantido (criado/atualizado) pela própria aplicação sendo contada. Um AIE (Arquivo de Interface Externa) é apenas lido/consultado pela aplicação, sendo mantido por outra aplicação externa.
    2. **Arquivos temporários:** Não são contados porque não atendem ao critério de serem um grupo logicamente relacionado de dados reconhecido pelo usuário final e de permanência/manutenção formal de negócio.
    3. **Tabela de CEPs dos Correios:** É um **AIE** (Arquivo de Interface Externa), pois é mantido por um sistema externo e apenas consultado pelo Sistema de Biblioteca.
    4. **Sigla em inglês para ALI:** ILF (*Internal Logic File*).
    5. **Exemplos de ALIs em sistema acadêmico:** `ALI Aluno` e `ALI Matrícula`.

---

## 📚 Referências utilizadas
- **IFPUG**. *Function Point Counting Practices Manual*, Release 4.3.1.
