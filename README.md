# Modelo de IA rodando localmente com Ollama

Baixe a versão do Ollama correspondente ao seu sistema: https://ollama.com/download

### 1. Crie um ambiente virtual e o inicie:
``` 
    python venv <nome-do-projeto> 
    cd .\<nome-do-projeto>\
    .\Scripts\activate 
```

### 2. Instale o Ollama
``` 
    pip install ollama
```

### 3. Envie o seu prompt
```
    python llm_cli.py --prompt "Sua mensagem aqui"
```
