# Guia de Contribuição — Software Metrics Learning

Agradecemos o seu interesse em contribuir para o **Software Metrics Learning**! Este repositório é um projeto educacional voltado para a comunidade de Engenharia de Software.

## Como Contribuir

1. **Correções de Conteúdo Didático**: Caso encontre algum erro de digitação, imprecisão em tabelas ou equações, abra uma *Issue* ou envie um *Pull Request*.
2. **Novos Exercícios e Exemplos**: Aceitamos contribuições de exercícios didáticos e novos scripts de exemplo. Certifique-se de adicionar a resposta no diretório `docs/13-respostas/`.
3. **Melhorias na Biblioteca Python**:
   - Mantenha funções pequenas e com Type Hints.
   - Adicione testes unitários em `tests/` garantindo cobertura >= 90%.
   - Execute o linter `ruff check src/ tests/` antes de enviar o PR.

## Executando o Projeto Localmente

```bash
# Instalar dependências
pip install -r requirements.txt
pip install -e .

# Executar testes unitários
pytest

# Executar o servidor da documentação localmente
mkdocs serve
```

## Regra Acadêmica
Toda afirmação metodológica ou conceitual deve possuir fundamentação bibliográfica citada em `docs/referencias.md` e `references/references.bib`. NUNCA invente referências, edições, DOIs ou números de página.
