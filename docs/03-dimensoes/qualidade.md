# Dimensão 5: Qualidade de Software

A **Qualidade** reflete o grau em que o software satisfaz os requisitos explícitos e implícitos dos usuários e partes interessadas.

---

## 1. Métricas de Qualidade Externa vs Interna

- **Qualidade Externa**: Observada durante o uso (ex: taxa de falhas, confiabilidade, usabilidade, tempo de resposta).
- **Qualidade Interna**: Observada no código-fonte e arquitetura (ex: legibilidade, complexidade ciclomática, acoplamento, cobertura de testes).

---

## 2. Relação entre Qualidade e Produtividade

Tentar maximizar a produtividade bruta sem manter o controle de qualidade resulta em alto endividamento técnico (*Technical Debt*) e elevado retrabalho futuro, reduzindo a velocidade líquida da equipe.

---

## 3. Você consegue responder?
1. Qual a diferença entre qualidade interna e qualidade externa de software?
2. Por que o número absoluto de defeitos não avalia sozinho a qualidade?
3. O que é débito técnico (*technical debt*) e qual seu impacto na produtividade futura?
4. Cite duas métricas de qualidade interna e duas de qualidade externa.
5. Como a cobertura de testes impacta a confiabilidade do produto?

??? check "Mostrar Gabarito / Resposta"
    1. **Qualidade Interna vs. Externa:** Qualidade interna refere-se à estrutura e manutenibilidade dos artefatos (código limpo, baixa complexidade, acoplamento), percebida pelos desenvolvedores. Qualidade externa refere-se ao comportamento do software em execução (desempenho, usabilidade, ausência de falhas), percebida pelo usuário final.
    2. **Insuficiência do número absoluto:** Sem considerar a escala do sistema (LOC ou PF) e a severidade dos defeitos, não é possível saber se o produto tem alta ou baixa qualidade.
    3. **Débito Técnico:** É o custo acumulado de escolher soluções fáceis/rápidas em vez de abordagens bem estruturadas. Seu impacto é desacelerar o desenvolvimento futuro e aumentar a incidência de novos defeitos.
    4. **Duas métricas de cada:**
       - *Qualidade Interna:* Complexidade Ciclomática e Acoplamento entre Classes (CBO).
       - *Qualidade Externa:* Taxa de Falhas em Produção e Tempo de Resposta da Aplicação.
    5. **Cobertura de testes e confiabilidade:** Alta cobertura reduz o risco de regressões e garante que alterações no código não quebrem comportamentos existentes já validados.

---

## 📚 Referências utilizadas
- **ISO/IEC 25010:2023**. *Systems and software Quality Requirements and Evaluation*.
- **Kan, S. H.** *Metrics and Models in Software Quality Engineering*, 2nd ed.
