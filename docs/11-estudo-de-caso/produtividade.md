# Sistema de Biblioteca: Análise de Produtividade

Análise integrada da produtividade registrada no desenvolvimento do *Sistema de Biblioteca*.

---

## 1. Tabela Integrada de Produtividade e Taxas de Esforço

| Métrica | Base de Tamanho | Esforço Total | Produtividade Calculada | Taxa de Esforço Unitário |
| :--- | :--- | :---: | :---: | :---: |
| **Linhas de Código (SLOC)** | 10.000 SLOC | 500 horas | **20.0 SLOC / hora** | 0.05 horas / SLOC |
| **Pontos de Função (APF)** | 53 PF | 500 horas | **0.106 PF / hora** | **9.43 horas / PF** |
| **Use Case Points (UCP)** | 52.77 UCP | 500 horas | **0.105 UCP / hora** | **9.47 horas / UCP** |

---

## 2. Análise da Convergência APF vs UCP

Note a notável convergência entre os resultados de tamanho e produtividade de **APF (53 PF)** e **UCP (52.77 UCP)** para este sistema. Ambas as abordagens capturaram a complexidade funcional de maneira equivalente sob a visão do usuário.

---

## 3. Você consegue responder?
1. Qual foi a taxa de esforço em horas por Ponto de Função obtida no projeto real?
2. Por que os resultados numéricos de APF (53 PF) e UCP (52.77 UCP) foram tão convergentes neste estudo de caso?
3. Qual a produtividade em SLOC/hora obtida?
4. Como utilizar o dado de 9.43 h/PF obtido neste projeto para orçar um novo sistema de 100 PF?
5. Qual a importância de registrar o esforço real por meio de ferramentas de timesheet?

??? check "Mostrar Gabarito / Resposta"
    1. **Taxa de esforço real:** $9,43 \text{ horas por Ponto de Função}$ ($500 \text{ horas} / 53 \text{ PF}$).
    2. **Convergência APF vs. UCP:** Porque a especificação de casos de uso manteve equivalência direta com o escopo de dados e transações do IFPUG, sem distorções de complexidade ambiental desproporcionais.
    3. **Produtividade em SLOC/hora:** $20 \text{ SLOC/hora}$ ($10.000 \text{ SLOC} / 500 \text{ horas}$).
    4. **Orçamento de novo sistema (100 PF):**
       $$\text{Esforço Estimado} = 100\text{ PF} \times 9,43\text{ h/PF} = 943\text{ horas-pessoa}$$
    5. **Importância do timesheet:** Fornece o histórico empírico real de horas consumidas, permitindo calcular taxas de produtividade reais da organização para calibrar orçamentos futuros.

---

## 📚 Referências utilizadas
- **Fenton, N. E. & Bieman, J.** *Software Metrics*, 3rd ed.
