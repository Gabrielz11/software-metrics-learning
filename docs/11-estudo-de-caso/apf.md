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

---

## 📚 Referências utilizadas
- **IFPUG**. *Function Point Counting Practices Manual*, Release 4.3.1.
