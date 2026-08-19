# Comparação de Técnicas de Estimativa

Este capítulo fornece o quadro comparativo e a árvore de decisão para orientação do estudante quanto à escolha da técnica de estimativa mais adequada ao contexto.

---

## 1. Tabela Comparativa Obrigatória

| Técnica | Base de Cálculo | Independente de Linguagem | Antes do Código | Principal Uso | Requisito de Entrada |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **Analogia** | Dados históricos passados | Geralmente sim | Sim | Estimativa preliminar rápida | Projetos passados semelhantes catalogados |
| **LOC** | Contagem de linhas físicas/lógicas | Não | Parcialmente | Estimativa detalhada de tamanho físico | Histórico de produtividade LOC/h e arquitetura |
| **APF** | Funcionalidades de dados e transações | Sim | Sim | Estimativa de tamanho funcional e contrato | Requisitos funcionais especificados |
| **UCP** | Atores e fluxos de casos de uso | Sim | Sim | Estimativa baseada em Orientação a Objetos | Casos de uso estruturados e diagramados |

---

## 2. Árvore de Decisão Didática

```mermaid
flowchart TD
    A[Início: Preciso estimar um software] --> B{Tenho dados históricos semelhantes?}
    B -->|Sim| C[Considerar Estimativa por ANALOGIA]
    B -->|Não| D{Quais artefatos estão disponíveis?}
    D -->|Especificação de Requisitos Funcionais| E[Utilizar APF - Análise de Pontos de Função]
    D -->|Casos de Uso Detalhados| F[Utilizar UCP - Use Case Points]
    D -->|Código-fonte Existente / Refatoração| G[Utilizar LOC / SLOC]
```

---

## 3. Você consegue responder?
1. Qual técnica de estimativa é a mais recomendada quando se possui apenas os casos de uso do sistema?
2. Por que a APF é independente da linguagem de programação, enquanto a LOC não é?
3. Em que situação a Estimativa por Analogia supera as demais em velocidade?
4. Qual técnica deve ser evitada no início do projeto para estimar esforço de desenvolvimento do zero?
5. Como a maturidade dos requisitos condiciona a escolha da técnica de estimativa?

---

## 📚 Referências utilizadas
- **Fenton, N. E. & Bieman, J.** *Software Metrics*, 3rd ed.
- **McConnell, Steve**. *Software Estimation: Demystifying the Black Art*.
