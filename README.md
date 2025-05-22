# Capital Gains Tax Calculator

## Decisões Técnicas e Arquiteturais

Este projeto implementa um calculador de impostos sobre ganho de capital para operações no mercado financeiro, seguindo uma arquitetura modular e orientada a objetos.

### Arquitetura

- **Padrão de Arquitetura**: Separação clara de responsabilidades usando princípios SOLID
- **Estrutura de Diretórios**:
  - `src/models/`: Modelos de dados (Operation, TaxResult)
  - `src/services/`: Lógica de negócio (TaxCalculator)
  - `src/utils/`: Funções utilitárias (processamento JSON)
  - `tests/`: Testes unitários e de integração

### Decisões Técnicas

1. **Uso de Decimal**: Para cálculos financeiros precisos, evitando problemas de arredondamento com float
2. **Imutabilidade**: Objetos de modelo são imutáveis para evitar efeitos colaterais
3. **Estado Isolado**: Estado mantido apenas no TaxCalculator, facilitando testes e manutenção
4. **Padrão Factory**: Método `from_dict` para criar objetos a partir de dados JSON

## Bibliotecas Utilizadas

O projeto utiliza apenas a biblioteca padrão do Python, sem dependências externas:
- `json`: Para processamento de entrada/saída em formato JSON
- `decimal`: Para cálculos financeiros precisos
- `unittest`: Para testes automatizados

## Requisitos

- Python 3.11.12 ou superior
- Não são necessárias bibliotecas externas, apenas a biblioteca padrão do Python
- Docker (opcional)

## Como Executar

### Formato de Entrada
```json
[{"operation":"buy", "unit-cost":10.00, "quantity": 100},{"operation":"sell", "unit-cost":15.00, "quantity": 50}]
```

### Formato de Saída
```json
[{"tax": 0.0}, {"tax": 0.0}]
```

### Execução Direta
```bash
# Executar a aplicação
python main.py
```

### Usando Makefile
```bash
# Executar a aplicação
make run
```

### Usando Docker
```bash
# Construir a imagem
docker build -t capital-gains-tax .

# Executar a aplicação em modo interativo
docker run -it capital-gains-tax
```

## Testes

O projeto inclui testes unitários e de integração abrangentes que cobrem todos os casos de uso especificados no enunciado.

### Executando Testes

```bash
# Diretamente
python -m unittest discover

# Via Makefile
make test

# Via Docker
docker run -it capital-gains-tax python -m unittest discover
```

### Cobertura de Testes

```bash
# Relatório de cobertura via Makefile
make coverage

# Relatório HTML de cobertura via Makefile
make coverage-html

# Relatório de cobertura via Docker
docker run -it capital-gains-tax bash -c "pip install coverage && python -m coverage run -m unittest discover && python -m coverage report -m"
```

## Notas Adicionais

- O código segue as convenções PEP 8 para estilo de código Python
- Todos os comentários e documentação estão em inglês para consistência
- A implementação lida corretamente com todos os casos de teste do enunciado
- O cálculo de impostos considera:
  - Preço médio ponderado das ações
  - Dedução de prejuízos acumulados
  - Isenção para operações ≤ R$ 20.000,00
  - Alíquota de 20% sobre o lucro
