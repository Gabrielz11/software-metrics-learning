# Vantagens e Limitações da APF

A Análise de Pontos de Função é amplamente aceita no mercado corporativo e governamental, mas possui trade-offs que devem ser compreendidos.

---

## 1. Vantagens da APF
- **Independência Tecnológica**: O mesmo projeto em Java, Python ou C# possuirá exatamente a mesma contagem de Pontos de Função se a especificação funcional for a mesma.
- **Medição Precoce**: Pode ser calculada logo na fase de especificação de requisitos, antes da escrita de qualquer linha de código.
- **Linguagem do Usuário**: Utiliza termos compreensíveis para stakeholders de negócio (tabelas, entradas, saídas, consultas).
- **Contratos e Editais**: Facilita a contratação de fábricas de software por preço fixo por PF.

---

## 2. Limitações da APF
- **Subjetividade Residual**: Contadores diferentes podem divergir ligeiramente na contagem de DETs ou FTRs se a documentação de requisitos for ambígua.
- **Dificuldade em Sistemas Não-Funcionais**: Não mede adequadamente o tamanho de drivers de dispositivo, algoritmos matemáticos complexos, jogos 3D ou compiladores (sistemas fortemente algorítmicos).
- **Curva de Aprendizado**: Exige treinamento e certificação formal (CFPS - *Certified Function Point Specialist*) para contadores profissionais.

---

## 3. Você consegue responder?
1. Cite duas grandes vantagens da APF para a gestão de contratos de software.
2. Em que tipo de sistema a APF apresenta limitações de medição?
3. Por que a APF exige requisitos funcionais razoavelmente especificados para ser precisa?
4. O que é a certificação CFPS do IFPUG?
5. Como a APF lida com aspectos de infraestrutura e desempenho?

??? check "Mostrar Gabarito / Resposta"
    1. **Duas grandes vantagens operacionais:** Permite estipular preços claros por unidade funcional (R$/PF) em licitações/contratos e possibilita estimar o tamanho antes da codificação iniciar.
    2. **Sistemas com limitações:** Sistemas fortemente algorítmicos ou científicos (compiladores, drivers de dispositivo, motores 3D de jogos, IA), onde a complexidade vem do processamento interno e não da gestão de dados/telas.
    3. **Exigência de requisitos:** Porque a contagem depende da identificação clara dos ALIs, AIEs, EEs, SEs e CEs, além dos seus respectivos DETs e FTRs/RETs.
    4. **Certificação CFPS:** *Certified Function Point Specialist*, concedida pelo IFPUG a profissionais que demonstram domínio prático e teórico do Manual de Práticas de Contagem (CPM).
    5. **Infraestrutura e desempenho:** A APF padrão (IFPUG 4.3.1) foca estritamente nos requisitos funcionais de negócio; requisitos não-funcionais (como tempo de resposta ou criptografia) não aumentam a contagem funcional direta.

---

## 📚 Referências utilizadas
- **IFPUG**. *Function Point Counting Practices Manual*, Release 4.3.1.
- **Fenton, N. E. & Bieman, J.** *Software Metrics*, 3rd ed.
