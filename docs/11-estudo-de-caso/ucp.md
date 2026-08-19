# Sistema de Biblioteca: Medição em UCP

Consolidação do cálculo por Pontos de Caso de Uso (Karner) do *Sistema de Biblioteca*.

---

## 1. Resumo dos Componentes UCP

- **UAW (Atores)**: 7
- **UUCW (Casos de Uso)**: 45
- **UUCP (Unadjusted UCP)**: 52
- **TCF (Fator Técnico)**: 1.02
- **ECF (Fator Ambiental)**: 0.995

$$\text{Total UCP} = 52 \times 1.02 \times 0.995 = 52.77\text{ UCP}$$

---

## 2. Esforço Estimado pelo Método UCP

Usando o fator de produtividade padrão Karner de 20 horas por UCP:

$$\text{Esforço Estimado UCP} = 52.77 \times 20 = 1.055.4\text{ Horas}$$

---

## 3. Você consegue responder?
1. Quantos Pontos por Caso de Uso (UCP) foram calculados para o Sistema de Biblioteca?
2. Qual a estimativa de esforço em horas derivada diretamente pela fórmula padrão Karner (20h/UCP)?
3. Por que a estimativa em UCP deu 1.055 horas enquanto o projeto real consumiu 500 horas?
4. Como calibrar o fator de produtividade h/UCP para aderir ao histórico da empresa?
5. Qual a relação entre a contagem de 53 PF e a contagem de 52.77 UCP no mesmo projeto?

??? check "Mostrar Gabarito / Resposta"
    1. **UCP Calculados:** 52,77 UCP.
    2. **Estimativa padrão Karner:** $52,77 \times 20 = 1.055,4 \text{ horas-pessoa}$.
    3. **Diferença entre 1.055h e 500h:** O fator padrão original de Karner (20h/UCP) foi estabelecido em 1993 com ferramentas antigas; equipes modernas com alta produtividade/automação gastam menos horas por ponto (no caso real, a equipe operou a aproximadamente $9,47 \text{ h/UCP}$).
    4. **Calibração de h/UCP:** Registrar as horas reais dos últimos projetos da empresa e dividir pelo total de UCPs entregues, substituindo a constante 20 pela média própria da empresa (ex: 9.5 h/UCP).
    5. **Relação APF (53 PF) vs. UCP (52.77 UCP):** Demonstra que ambos os métodos chegaram a mensurações de tamanho funcional praticamente idênticas para a mesma especificação de negócio.

---

## 📚 Referências utilizadas
- **Karner, Gustav**. *Resource Estimation Based on Use Cases*, 1993.
