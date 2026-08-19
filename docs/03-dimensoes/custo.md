# Dimensão 4: Custo de Software

O **Custo** é o valor financeiro acumulado necessário para produzir, testar, implantar e manter uma solução de software.

---

## 1. Composição do Custo de Software

```mermaid
pie title Composição Típica dos Custos de Software
    "Salários e Esforço Direto" : 70
    "Infraestrutura e Ferramentas" : 15
    "Treinamento e Gestão" : 10
    "Licenciamento e Terceiros" : 5
```

$$\text{Custo Total} = (\text{Esforço em Horas} \times \text{Custo Médio da Hora}) + \text{Custos Operacionais Indiretos}$$

---

## 2. Exemplo Prático no Sistema de Biblioteca

!!! example "Custo Total de Desenvolvimento"
    No *Sistema de Biblioteca*, foram consumidas 500 horas com um custo médio ponderado por hora de R\$ 100,00/hora.
    $$\text{Custo Direto de Esforço} = 500 \times 100 = \text{R\$ } 50.000,00$$
    Considerando R\$ 5.000,00 de licenças e infraestrutura, o custo total foi de R\$ 55.000,00.  
    $$\text{Custo por Ponto de Função} = \frac{55.000}{50\text{ PF}} = \text{R\$ } 1.100,00/\text{PF}$$

---

## 3. Você consegue responder?
1. Quais são as principais componentes do custo de desenvolvimento de software?
2. Como se calcula o custo por Ponto de Função (R$/PF)?
3. Qual é o peso do esforço humano na composição total do custo de software?
4. O que são custos indiretos ou de overhead em projetos de engenharia?
5. Por que subestimar o esforço afeta diretamente a margem de custo do projeto?

??? check "Mostrar Gabarito / Resposta"
    1. **Componentes do custo:** Esforço humano (salários e encargos), infraestrutura/ferramentas (hardware, licenças de software, serviços de nuvem), treinamento e custos de gestão/overhead.
    2. **Cálculo de R$/PF:**
       $$\text{Custo por PF} = \frac{\text{Custo Total do Projeto (R\$)}}{\text{Total de Pontos de Função Entregues}}$$
    3. **Peso do esforço humano:** Em engenharia de software, o esforço de pessoal responde tipicamente por 70% a 85% do custo total do projeto.
    4. **Custos indiretos / Overhead:** Gastos que não estão ligados diretamente à codificação de uma funcionalidade específica, como aluguel do escritório, utilidades, salários de liderança corporativa, RH e licenças organizacionais.
    5. **Impacto da subestimativa de esforço:** Como o custo é predominantemente derivado das horas de trabalho, subestimar as horas resulta diretamente em custo real maior do que o orçado, consumindo a margem financeira ou gerando prejuízo.

---

## 📚 Referências utilizadas
- **Pressman, R. S. & Maxim, B. R.** *Software Engineering: A Practitioner's Approach*, 9th ed., 2019.
