"""
Modelo de IA rodando localmente com Ollama e ArgParse
"""
from ollama import chat
from argparse import ArgumentParser

# Função ask vai receber e processar o nosso prompt
def ask(prompt: str):
    stream = chat(
        model="gemma3:1b",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    for chunk in stream:
        print(chunk["message"]["content"], end="", flush=True)


# a função cli_args envia o prompt para a IA
def cli_args():
    parser = ArgumentParser(description="Minha IA local")
    
    parser.add_argument(
        "--prompt",
        required=True,
        help="Prompt para enviar para a IA"
    )

    args = parser.parse_args()
    return args

# A função main é a junção do recebimento e envio da mensagem 
def main():
    args = cli_args()
    ask(args.prompt)

if __name__ == "__main__":
    main()