# Introdução à Análise de Pontos de Função (APF)

> 📚 **Conceito fundamentado em referência (IFPUG CPM 4.3.1 / Allan Albrecht 1979)**  
> A Análise de Pontos de Função (APF) mede o tamanho funcional do software sob a perspectiva das funcionalidades solicitadas e entregues aos usuários.

---

## 1. O que é?
Desenvolvida por Allan Albrecht na IBM em 1979 e posteriormente mantida e padronizada pelo **IFPUG** (*International Function Point Users Group*), a APF avalia o software com base na sua capacidade lógica de armazenar, recuperar e processar dados de negócio.

## 2. Por que existe?
Ela foi criada para resolver a principal limitação do LOC: permitir a medição do tamanho do software de forma consistente e comparável, independentemente das tecnologias, linguagens ou decisões de arquitetura adotadas no código.

---

## 3. Onde se Aplica a APF?

```mermaid
flowchart TD
    Req[Requisitos de Usuário] --> APF[Contagem de Pontos de Função]
    APF --> A[Estimativa de Esforço e Prazo]
    APF --> B[Medição de Produtividade h/PF]
    APF --> C[Gestão de Contratos de Software]
    APF --> D[Benchmarking de Mercado]
```

---

## 4. Você consegue responder?
1. Quem foi o criador da técnica de Análise de Pontos de Função?
2. Qual a organização internacional responsável por manter o padrão oficial da APF?
3. Por que a APF é considerada independente da linguagem de programação?
4. Qual a premissa de medição sob a visão do usuário?
5. Em quais momentos do desenvolvimento a APF pode ser realizada?

??? check "Mostrar Gabarito / Resposta"
    1. **Criador:** Allan J. Albrecht (na IBM, em 1979).
    2. **Organização internacional:** IFPUG (*International Function Point Users Group*).
    3. **Independência de linguagem:** Porque mede o tamanho das funcionalidades fornecidas ao usuário com base em seus requisitos de negócio, independentemente de se usar Java, Python, C# ou Cobol para implementar.
    4. **Visão do usuário:** Avalia o software sob a perspectiva externa daquilo que o usuário solicita e reconhece (entradas, saídas, consultas e arquivos mantidos), ignorando detalhes de implementação técnica.
    5. **Momentos de aplicação:** Desde a fase inicial de requisitos/orçamento (estimativa), passando pelo acompanhamento do projeto, até o produto final instalado (mensuração de aplicações legadas).

---

## 📚 Referências utilizadas
- **IFPUG**. *Function Point Counting Practices Manual (CPM)*, Release 4.3.1.
- **Albrecht, Allan J.** *Measuring Application Development Productivity*, IBM, 1979.
