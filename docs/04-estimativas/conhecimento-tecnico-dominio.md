# Conhecimento Técnico e Conhecimento do Domínio

A precisão de qualquer estimativa de software depende criticamente do nível de maturidade da equipe em duas dimensões independentes: **Conhecimento Técnico** e **Conhecimento do Domínio de Negócio**.

---

## 1. As Duas Dimensões da Incerteza

```text
                  ALTO CONHECIMENTO DO DOMÍNIO
                               ▲
                               │
      Cenário B:               │              Cenário A:
  Baixo risco funcional        │          Mínimo risco global
  Alto risco técnico           │          Estimativa precisa
                               │
BAIXO CONHECIMENTO ────────────┼────────────► ALTO CONHECIMENTO
TÉCNICO                        │              TÉCNICO
                               │
      Cenário D:               │              Cenário C:
  Máximo risco de projeto      │          Alto risco funcional
  Estimativa imprevisível      │          Baixo risco técnico
                               │
                  BAIXO CONHECIMENTO DO DOMÍNIO
```

---

## 2. Matriz de Impacto nas Estimativas

| Cenário | Conhecimento Técnico | Conhecimento do Domínio | Consequência na Estimativa |
| :--- | :--- | :--- | :--- |
| **A** | Alto | Alto | Baixa variabilidade, estimativas altamente confiáveis. |
| **B** | Baixo | Alto | Risco concentrado na curva de aprendizado de ferramentas/frameworks. |
| **C** | Alto | Baixo | Risco de construir a coisa errada com alta perfeição técnica. |
| **D** | Baixo | Baixo | Impossibilidade de estimar com segurança; exige prototipação e pesquisas (*Spikes*). |

---

## 3. Você consegue responder?
1. Quais são as duas dimensões de conhecimento que impactam a qualidade de uma estimativa?
2. O que acontece quando uma equipe tem alto conhecimento técnico mas baixo conhecimento do domínio?
3. O que é um *Spike* técnico ou funcional em projetos ágeis?
4. Em qual cenário da matriz a variabilidade da estimativa é mínima?
5. Como mitigar o risco de estimativa quando ambas as dimensões de conhecimento são baixas?

---

## 📚 Referências utilizadas
- **Pressman, R. S. & Maxim, B. R.** *Software Engineering*, 9th ed.
