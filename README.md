# Métricas de Software — Medição, Estimativas e Qualidade

> Um repositório educacional para aprender métricas, medição, estimativas, qualidade e produtividade em Engenharia de Software.

[![CI Status](https://img.shields.io/badge/CI-passing-brightgreen)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.12%2B-blue)](pyproject.toml)
[![Documentation](https://img.shields.io/badge/Docs-MkDocs--Material-blueviolet)](#)

---

## 📌 Visão Geral

**Software Metrics Learning** é um repositório open-source criado para ensinar Métricas de Software de maneira progressiva, integrando teoria bem fundamentada, cálculos matemáticos explicados, biblioteca Python educacional e um **estudo de caso unificado** (Sistema de Biblioteca).

O projeto adota como filosofia central:
> **Não medir por medir. Medir para compreender, decidir e melhorar.**

```text
OBJETIVO → PERGUNTA → MEDIÇÃO → MÉTRICA → INDICADOR → INTERPRETAÇÃO → DECISÃO → MELHORIA
```

---

## 📚 Conteúdo Didático

O conteúdo está organizado em 14 módulos fundamentados em fontes primárias (SWEBOK v4.0a, IFPUG CPM 4.3.1, ISO/IEC 25010:2023, GQM):

1. **01 — Fundamentos**: Medição vs Medida vs Métrica vs Indicador, métricas diretas e indiretas.
2. **02 — Tipos de Métricas**: Métricas de Produto, Processo e Projeto.
3. **03 — Dimensões**: Tamanho, Esforço, Prazo, Custo, Qualidade e Produtividade.
4. **04 — Estimativas**: Processo contínuo de estimativa, Cone da Incerteza, Analogia.
5. **05 — LOC (Lines of Code)**: SLOC físicas e lógicas, convenções e limitações.
6. **06 — APF (Análise de Pontos de Função)**: ALI, AIE, EE, SE, CE, DET, RET, FTR e complexidade IFPUG.
7. **07 — UCP (Use Case Points)**: Karner method, Atores, Casos de Uso, TCF (T1-T13) e ECF (E1-E8).
8. **08 — Qualidade de Software**: Modelo ISO/IEC 25010:2023 (9 características), Densidade de Defeitos, Complexidade Ciclomática de McCabe, Cobertura.
9. **09 — Métricas Ágeis**: Velocity, Lead Time vs Cycle Time, Throughput, Burndown/Burnup.
10. **10 — GQM (Goal-Question-Metric)**: Derivação de métricas orientadas a objetivos de negócio.
11. **11 — Estudo de Caso Central**: Aplicação integrada do "Sistema de Biblioteca".
12. **12 — Exercícios Práticos**: Exercícios em três níveis (🟢 Básico, 🟡 Intermediário, 🔴 Desafio).
13. **13 — Respostas**: Resoluções detalhadas dos exercícios.
14. **14 — Glossário**: Termos e siglas técnicas alfabeticamente indexados.

---

## 💻 Biblioteca Python Educacional (`software_metrics`)

O repositório inclui uma biblioteca Python para simulação e aprendizado de cálculos de métricas.

### Instalação

```bash
pip install -r requirements.txt
pip install -e .
```

### Uso da CLI

```bash
# Calcular Produtividade
python -m software_metrics productivity --size 10000 --effort 500
# Produtividade: 20.00 unidades/hora

# Calcular Densidade de Defeitos
python -m software_metrics defects --defects 40 --size 10
# Densidade de defeitos: 4.00 defeitos/unidade

# Converter LOC para KLOC
python -m software_metrics kloc --loc 2500
# KLOC: 2.500
```

### Uso como Módulo Python

```python
from software_metrics import (
    FunctionPointCalculator,
    DataFunctionType,
    TransactionType,
    calculate_productivity,
)

# Cálculo de APF
calc = FunctionPointCalculator()
calc.add_data_function("Livro", DataFunctionType.ALI, ret=1, det=6)
calc.add_transactional_function("Cadastrar Livro", TransactionType.EE, ftr=1, det=3)
print(calc.summary())

# Cálculo de Produtividade
prod = calculate_productivity(size=10000, effort=500)
print(f"Produtividade: {prod} LOC/hora")
```

---

## 🧪 Testes Automatizados e Qualidade

Para rodar a suíte de testes unitários com Pytest:

```bash
pytest
```

Para verificar o linting do código Python:

```bash
ruff check src/ tests/
```

Para validar a documentação MkDocs sem erros de sintaxe ou links quebrados:

```bash
mkdocs build --strict
```

---

## 🌐 Visualização da Documentação Web (MkDocs)

Para visualizar o site da documentação interativa localmente:

```bash
mkdocs serve
```

Acesse `http://127.0.0.1:8000` no seu navegador.

---

## 📖 Referências Bibliográficas

- **IEEE Computer Society**. *Guide to the Software Engineering Body of Knowledge (SWEBOK Guide)*, Version 4.0, 2024.
- **ISO/IEC 25010:2023**. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.
- **IFPUG**. *Function Point Counting Practices Manual*, Release 4.3.1, 2010.
- **Fenton, N. E. & Bieman, J.** *Software Metrics: A Rigorous and Practical Approach*, 3rd ed., CRC Press, 2014.
- **Basili, V. R., Caldiera, G., & Rombach, H. D.** *The Goal Question Metric Approach*, 1994.

---

## 📄 Licença

Este projeto está licenciado sob a licença [MIT](LICENSE).
