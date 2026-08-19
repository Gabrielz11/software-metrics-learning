# Métricas Diretas e Indiretas

Na Engenharia de Software, as propriedades medidas dividem-se formalmente em **métricas diretas** (atributos internos observáveis por medição simples) e **métricas indiretas** (atributos derivados obtidos por meio de cálculos ou modelos matemáticos).

---

## 1. Métricas Diretas

Métricas diretas são medições efetuadas sem a necessidade de combinar o atributo medido com outras variáveis.

### Exemplos de Métricas Diretas
- **Linhas de Código (LOC)**: Contagem física de linhas no arquivo.
- **Esforço**: Horas de trabalho registradas pelo desenvolvedor.
- **Tempo de Execução**: Milissegundos necessários para processar uma requisição.
- **Contagem de Defeitos**: Quantidade absoluta de erros reportados no sistema de bilhetagem.
- **Custo do Projeto**: Valor em moeda gasto durante a fase de desenvolvimento.

---

## 2. Métricas Indiretas

Métricas indiretas resultam da combinação matemática de duas ou mais medidas diretas ou indiretas. Elas geralmente medem atributos de qualidade, eficiência ou produtividade.

### Formas Conceituais e Matemáticas

#### Produtividade
- **Conceitual**: $\text{Produtividade} = \frac{\text{Tamanho do Software}}{\text{Esforço Gasto}}$
- **Matemática**: $P = \frac{S}{E}$
- **Exemplo**: $10.000\text{ LOC} / 500\text{ horas} = 20\text{ LOC/hora}$.

#### Densidade de Defeitos
- **Conceitual**: $\text{Densidade de Defeitos} = \frac{\text{Total de Defeitos}}{\text{Tamanho em KLOC}}$
- **Matemática**: $D = \frac{N_{\text{def}}}{\text{KLOC}}$
- **Exemplo**: $40\text{ defeitos} / 10\text{ KLOC} = 4\text{ defeitos/KLOC}$.

---

## 3. Tabela Comparativa

| Atributo Medido | Tipo de Métrica | Como é Obtida | Vantagem | Limitação |
| :--- | :--- | :--- | :--- | :--- |
| **Linhas de Código (LOC)** | Direta | Contagem automática via script | Fácil obtenção e objetividade | Depende da linguagem de programação |
| **Horas de Esforço** | Direta | Apontamento em ferramenta de timesheet | Medida precisa de custo | Sujeita a erros de apontamento humano |
| **Produtividade** | Indireta | Razão entre Tamanho e Esforço | Permite comparar eficiência entre projetos | Sensível a imprecisões no tamanho ou esforço |
| **Densidade de Defeitos** | Indireta | Razão entre Defeitos e KLOC | Permite avaliar qualidade independente da escala | Ignora a severidade individual dos defeitos |

---

## 4. Erros Comuns
- Tentar medir atributos complexos de qualidade (como legibilidade ou manutenibilidade) por meio de uma única medição direta simples.
- Tratar a densidade de defeitos de dois sistemas sem considerar a diferença entre a complexidade de seus domínios.

## 5. Você consegue responder?
1. Qual é a diferença entre uma métrica direta e uma métrica indireta?
2. Por que a produtividade é classificada como uma métrica indireta?
3. Apresente a fórmula conceitual e matemática da densidade de defeitos.
4. Por que atributos como "usabilidade" exigem métricas indiretas para sua avaliação?
5. Dê dois exemplos de medições diretas comumente realizadas em repositórios de código.

---

## 📚 Referências utilizadas
- **Fenton, N. E. & Bieman, J.** *Software Metrics: A Rigorous and Practical Approach*, 3rd ed., 2014.
- **IEEE Computer Society**. *SWEBOK V4.0a*, Chapter 8.
