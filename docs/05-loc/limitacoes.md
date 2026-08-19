# Limitações da Métrica de LOC

Apesar de sua simplicidade de coleta, a métrica de Linhas de Código (LOC) apresenta sérias deficiências teóricas e práticas quando utilizada como medida primária de tamanho ou produtividade.

---

## 1. Principais Limitações

### Dependência Crítica da Linguagem de Programação
Linguagens de baixo nível (como Assembly ou C) exigem muito mais linhas de código para realizar a mesma tarefa funcional do que linguagens de alto nível (como Python ou SQL).

| Linguagem | Linhas para Implementar a Mesma Funcionalidade (Exemplo Didático) |
| :--- | :--- |
| **Assembly** | 500 LOC |
| **C** | 100 LOC |
| **Python** | 15 LOC |

Se avaliarmos apenas por LOC/hora, o desenvolvedor Assembly pareceria "mais produtivo" do que o desenvolvedor Python, o que é um grande absurdo conceitual.

### Penalização do Reuso e da Refatoração
Um desenvolvedor experiente que refatora um método complexo reduzindo-o de 200 linhas para 30 linhas mais limpas e legíveis estaria gerando "produtividade negativa" se a métrica fosse LOC.

### Estímulo à Prolixidade
Se a meta individual for baseada em LOC, a equipe é incentivada a escrever código mais longo e verboso, aumentando a superfície para novos defeitos.

---

## 2. Erros Comuns
- Comparar a produtividade de equipes que trabalham em linguagens de programação diferentes utilizando LOC.
- Usar LOC antes da fase de escrita de código para estimar projetos do zero sem consultar estimativas funcionais.

## 3. Você consegue responder?
1. Por que a comparação de produtividade baseada em LOC entre linguagens distintas é conceitualmente inválida?
2. Como a refatoração afeta a contagem de LOC?
3. O que é o estímulo à prolixidade induzido por métricas de LOC?
4. Qual a diferença entre medir tamanho físico (LOC) e tamanho funcional (APF)?
5. Em que situações a métrica de LOC ainda possui utilidade prática legítima?

??? check "Mostrar Gabarito / Resposta"
    1. **Invalidez da comparação entre linguagens:** Linguagens expressivas de alto nível resolvem problemas complexos em poucas linhas, fazendo uma equipe em Python parecer "menos produtiva" em LOC do que uma equipe em C ou Assembly, mesmo entregando mais valor de negócio.
    2. **Efeito da refatoração:** A boa refatoração simplifica o código e reduz o número de linhas (LOC negativo), o que penalizaria um desenvolvedor sob uma medição simplista de linhas escritas.
    3. **Estímulo à prolixidade:** Fenômeno derivado da Lei de Goodhart: quando LOC vira meta de produtividade, os desenvolvedores passam a copiar código, evitar reuso de bibliotecas e escrever funções verbosas.
    4. **Tamanho Físico vs. Funcional:** LOC mede o tamanho da implementação/artefato técnico gerado. APF mede o tamanho das capacidades de negócio e dados fornecidas ao usuário final.
    5. **Utilidade legítima de LOC:** Estimativa do tamanho de manutenção de sistemas legados existentes, cálculo de densidade de defeitos interna na mesma stack e análise de evolução do volume de base de código ao longo do tempo.

---

## 📚 Referências utilizadas
- **Fenton, N. E. & Bieman, J.** *Software Metrics*, 3rd ed.
- **Pressman, R. S. & Maxim, B. R.** *Software Engineering*, 9th ed.
