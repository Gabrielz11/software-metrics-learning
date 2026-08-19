# Sistema de Biblioteca: Avaliação de Qualidade

Resumo consolidado dos dados operacionais de qualidade do *Sistema de Biblioteca*.

---

## 1. Dados de Defeitos Coletados

- **Defeitos Encontrados em Testes (Pré-Release)**: 35
- **Defeitos Reportados pelos Clientes (Pós-Release)**: 5
- **Defeitos Totais Identificados**: 40

---

## 2. Indicadores de Qualidade Calculados

- **Densidade por KLOC**: $40 / 10 = 4.0\text{ defeitos/KLOC}$
- **Densidade por PF**: $40 / 53 = 0.75\text{ defeitos/PF}$
- **Eficiência na Remoção de Defeitos (DRE)**:
  $$\text{DRE} = \left( \frac{35}{35 + 5} \right) \times 100 = 87.5\%$$
- **Cobertura de Testes de Código (pytest-cov)**: 92%

---

## 3. Você consegue responder?
1. Qual foi a Eficiência na Remoção de Defeitos (DRE) atingida no Sistema de Biblioteca?
2. Quantos defeitos escaparam para o ambiente de produção?
3. Qual a densidade de defeitos por Ponto de Função obtida?
4. Qual o percentual de cobertura de testes automatizados atingido?
5. Qual ação de melhoria de processo deve ser tomada para reduzir os 5 defeitos escapados?

---

## 📚 Referências utilizadas
- **Kan, S. H.** *Metrics and Models in Software Quality Engineering*, 2nd ed.
