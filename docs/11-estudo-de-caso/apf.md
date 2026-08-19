# Sistema de Biblioteca: Medição em APF

Consolidação da medição funcional do *Sistema de Biblioteca* via IFPUG.

---

## 1. Síntese da Contagem Funcional

- **Funções de Dados (ALIs + AIEs)**: 26 PF
  - `ALI_Usuario`: 7 PF
  - `ALI_Livro`: 7 PF
  - `ALI_Emprestimo`: 7 PF
  - `AIE_SerasaCredito`: 5 PF
- **Funções Transacionais (EE + SE + CE)**: 27 PF
  - `EE_CadastrarUsuario`: 3 PF
  - `EE_AtualizarUsuario`: 3 PF
  - `EE_CadastrarLivro`: 3 PF
  - `EE_RealizarEmprestimo`: 4 PF
  - `EE_RegistrarDevolucao`: 3 PF
  - `CE_ConsultarLivro`: 3 PF
  - `CE_ConsultarEmprestimos`: 3 PF
  - `SE_RelatorioAtrasos`: 5 PF

$$\text{Tamanho Funcional Total} = 53\text{ Pontos de Função (PF)}$$

---

## 2. Indicadores Derivados de APF

- **Produtividade Funcional**: $53\text{ PF} / 500\text{ h} = 0.106\text{ PF/hora}$
- **Taxa de Esforço**: $500\text{ h} / 53\text{ PF} = 9.43\text{ horas/PF}$
- **Densidade por PF**: $40\text{ defeitos} / 53\text{ PF} = 0.75\text{ defeitos/PF}$

---

## 3. Você consegue responder?
1. Qual o total de Pontos de Função obtido na contagem do Sistema de Biblioteca?
2. Quanto as funções de dados representam do tamanho total do sistema em porcentagem?
3. Qual a taxa de esforço em horas por Ponto de Função obtida?
4. Qual a densidade de defeitos por Ponto de Função do sistema?
5. Como os 53 PF obtidos nesta contagem se relacionam com a medição de 10 KLOC?

??? check "Mostrar Gabarito / Resposta"
    1. **Total de Pontos de Função:** 53 PF (26 PF em Funções de Dados + 27 PF em Funções Transacionais).
    2. **Porcentagem de Funções de Dados:**
       $$\%_{\text{Dados}} = \left( \frac{26}{53} \right) \times 100\% \approx 49,06\%$$
    3. **Taxa de Esforço:** $500 \text{ horas} / 53 \text{ PF} \approx 9,43 \text{ horas/PF}$.
    4. **Densidade de defeitos por PF:** $40 \text{ defeitos} / 53 \text{ PF} \approx 0,75 \text{ defeitos/PF}$.
    5. **Relação entre 53 PF e 10 KLOC:** Para a stack Python deste projeto, a relação obtida foi de aproximadamente $10.000 / 53 \approx 188,68 \text{ SLOC por Ponto de Função}$.

---

## 📚 Referências utilizadas
- **IFPUG**. *Function Point Counting Practices Manual*, Release 4.3.1.
