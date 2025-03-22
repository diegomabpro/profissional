import argparse
from interaction.cli_interface import cli_main
from interaction.gui_interface import gui_main

def main():
    """
    Função principal que decide se executa a CLI ou a GUI.
    """
    parser = argparse.ArgumentParser(description="Assistente Financeira")
    parser.add_argument("--cli", action="store_true", help="Executar a interface de linha de comando")
    parser.add_argument("--gui", action="store_true", help="Executar a interface gráfica")
    args = parser.parse_args()

    if args.cli:
        cli_main()
    elif args.gui:
        gui_main()
    else:
        print("Por favor, especifique --cli ou --gui para executar a assistente.")

if __name__ == "__main__":
    main()