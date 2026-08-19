# Cycle Time (Tempo de Ciclo de Desenvolvimento)

O **Cycle Time** é a métrica interna de vazão operacional do time de engenharia.

---

## 1. Decomposição do Cycle Time

```mermaid
flowchart LR
    A[Desenvolvimento] --> B[Code Review / PR]
    B --> C[Testes QA / CI]
    C --> D[Deploy Produção]
```

$$\text{Cycle Time Total} = T_{\text{Dev}} + T_{\text{Review}} + T_{\text{QA}} + T_{\text{Deploy}}$$

---

## 2. Gargalos Típicos Revelados pelo Cycle Time
- PRs (Pull Requests) paradas aguardando revisão por mais de 48 horas.
- Testes manuais lentos retendo itens na coluna de validação QA.

---

## 3. Você consegue responder?
1. Quais são os componentes do Cycle Time no fluxo de código?
2. Como a automação de testes em pipelines CI/CD reduz o Cycle Time?
3. O que indica um alto tempo de permanência na etapa de Code Review?
4. Qual a relação entre o tamanho das tarefas (fatiamento de histórias) e a redução do Cycle Time?
5. Escreva a equação de decomposição do Cycle Time.

---

## 📚 Referências utilizadas
- **Anderson, David J.** *Kanban*, 2010.
