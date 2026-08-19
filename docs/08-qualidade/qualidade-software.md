# Conceitos de Qualidade de Software

> 📚 **Conceito fundamentado em referência (SWEBOK / ISO/IEC 25010)**  
> Qualidade de Software é o grau em que um sistema satisfaz as necessidades declaradas e implícitas de seus diversos interessados (*stakeholders*).

---

## 1. O que é?
Qualidade não é um atributo único e binário ("tem qualidade" ou "não tem"). É um conjunto multifacetado de características quantificáveis.

## 2. Visão Histórica de Qualidade

```text
QUALIDADE DE SOFTWARE
       │
       ├── Adequação Funcional (O sistema faz o que deveria fazer?)
       ├── Confiabilidade (O sistema permanece operando sem falhar?)
       ├── Eficiência / Desempenho (O sistema responde rapidamente?)
       └── Manutenibilidade (É fácil alterar ou corrigir o código?)
```

---

## 3. Você consegue responder?
1. Como a norma ISO/IEC define a qualidade de software?
2. Por que a qualidade de software é considerada um conceito multifacetado?
3. O que diferencia a qualidade de processo da qualidade de produto?
4. Por que medir apenas o número de falhas em produção é insuficiente para avaliar a qualidade total?
5. Qual o papel das normas da família SQuaRE na Engenharia de Software?

??? check "Mostrar Gabarito / Resposta"
    1. **Definição ISO/IEC:** É o grau em que um conjunto de características inerentes de um produto de software atende às necessidades explícitas e implícitas dos seus usuários e partes interessadas.
    2. **Conceito multifacetado:** Porque envolve aspectos internos perceptíveis pelos desenvolvedores (legibilidade, manutenibilidade), aspectos externos perceptíveis pelo usuário (desempenho, usabilidade) e qualidade de uso no ambiente de negócio.
    3. **Qualidade de processo vs. produto:** Qualidade de processo foca em como o software é construído e mantido (práticas de engenharia, esteira CI/CD). Qualidade de produto foca nos atributos e no comportamento do artefato de software final gerado.
    4. **Insuficiência de falhas em produção:** Mede apenas a qualidade externa tardia; não revela o endividamento técnico, baixa testabilidade, má arquitetura ou risco de manutenibilidade futura.
    5. **Papel das normas SQuaRE (ISO/IEC 25000):** Padronizar internacionalmente a especificação e avaliação da qualidade do produto e requisitos de software.

---

## 📚 Referências utilizadas
- **ISO/IEC 25010:2023**. *Product quality model*.
- **IEEE Computer Society**. *SWEBOK V4.0a*, Chapter 10: Software Quality.
