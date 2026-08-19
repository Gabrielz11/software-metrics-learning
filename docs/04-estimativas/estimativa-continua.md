# Estimativa Contínua e o Cone da Incerteza

Estimar não é um evento único que ocorre apenas no primeiro dia do projeto. É um **processo contínuo de refinamento**.

---

## 1. O Cone da Incerteza (Cone of Uncertainty)

No início do projeto (fase de concepção), a margem de variabilidade da estimativa pode oscilar entre **0.25x (25%)** e **4.0x (400%)** do valor real final. À medida que requisitos são detalhados e o código é escrito, a incerteza afunila.

```mermaid
graph LR
    A[Concepção<br/>0.25x a 4.0x] --> B[Requisitos<br/>0.5x a 2.0x]
    B --> C[Arquitetura<br/>0.75x a 1.25x]
    C --> D[Construção<br/>0.9x a 1.1x]
    D --> E[Entrega Final<br/>1.0x]
```

---

## 2. O Fluxo da Estimativa Contínua

```text
Ideia Inicial ──► Estimativa Conceitual (Faixa Larga)
     │
     ▼
Requisitos Detalhados ──► Estimativa Funcional (APF / UCP)
     │
     ▼
Desenvolvimento / Sprints ──► Re-estimativa por Dados Históricos / Velocity
```

---

## 3. Você consegue responder?
1. O que descreve o gráfico do Cone da Incerteza?
2. Por que a variabilidade no início do projeto pode chegar a 4x o valor real?
3. O que acontece com a margem de incerteza após a conclusão da fase de arquitetura?
4. Por que a estimativa deve ser atualizada em cada nova fase do projeto?
5. Qual é o erro de tentar travar o orçamento na fase de concepção sem prever faixas de incerteza?

??? check "Mostrar Gabarito / Resposta"
    1. **Cone da Incerteza:** Ilustra como o grau de incerteza e a variação potencial das estimativas diminuem à medida que o projeto avança e as decisões de requisitos, arquitetura e design são consolidadas.
    2. **Variabilidade inicial (4x / 0.25x):** No início (fase de concepção), os requisitos são vagos, o escopo não está detalhado e as escolhas tecnológicas ainda não foram validadas.
    3. **Após arquitetura:** A margem de erro se reduz drasticamente (ficando tipicamente entre $\pm 15\%$ a $\pm 20\%$), pois os componentes principais e riscos técnicos já foram mapeados.
    4. **Atualização contínua:** Conforme a incerteza diminui, novas informações reais surgem, permitindo refinar o planejamento e o orçamento com maior precisão.
    5. **Erro de travar orçamento cedo:** Tratar estimativas iniciais de alta incerteza como compromissos fixos leva a estouros inevitáveis de prazo/custo ou ao corte drástico da qualidade para cumprir contratos rígidos.

---

## 📚 Referências utilizadas
- **McConnell, Steve**. *Software Estimation: Demystifying the Black Art*.
