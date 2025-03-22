import argparse

def cli_main():
    """
    Interface de linha de comando (CLI) para a assistente financeira.
    """
    parser = argparse.ArgumentParser(description="Assistente Financeira - CLI")
    parser.add_argument("--acao", help="Obter dados de uma ação")
    parser.add_argument("--indice", help="Obter dados de um índice")
    parser.add_argument("--futuro", help="Obter dados de um contrato futuro")
    args = parser.parse_args()

    if args.acao:
        print(f"Consultando dados da ação: {args.acao}")
    elif args.indice:
        print(f"Consultando dados do índice: {args.indice}")
    elif args.futuro:
        print(f"Consultando dados do contrato futuro: {args.futuro}")
    else:
        print("Por favor, especifique um ativo para análise.")

if __name__ == "__main__":
    cli_main()