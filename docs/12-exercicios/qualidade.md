# Exercícios: Qualidade e Defeitos

---

### Exemplo 01 🟢 (Básico - Densidade)
Um módulo de software de 5.0 KLOC apresentou 15 defeitos durante a fase de testes. Calcule a densidade de defeitos por KLOC.

---

### Exemplo 02 🟢 (Básico - DRE)
Durante os testes em homologação foram identificados e corrigidos 80 defeitos. Nos três primeiros meses de uso em produção, os usuários reportaram 20 defeitos. Calcule a Eficiência na Remoção de Defeitos (DRE %).

---

### Exemplo 03 🟡 (Intermediário - Complexidade Ciclomática)
Calcule a Complexidade Ciclomática $V(G)$ da função abaixo:

```python
def processar_pedido(pedido):
    if not pedido.valido:
        return "Invalido"

    if pedido.valor > 500:
        if pedido.cliente_vip:
            return "Desconto VIP"
        return "Desconto Padrao"

    return "Sem Desconto"
```

---

### Exemplo 04 🔴 (Desafio - MTBF e Disponibilidade)
Um servidor de aplicação funcionou por 720 horas em um mês. Durante esse período ocorreram 3 falhas não planejadas, com tempos de reparo de 2 horas, 1 hora e 3 horas.
Calcule o MTBF, o MTTR e a Disponibilidade percentual do sistema nesse mês.
