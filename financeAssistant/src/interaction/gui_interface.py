import tkinter as tk
from tkinter import messagebox

def gui_main():
    """
    Interface gráfica (GUI) para a assistente financeira.
    """
    def analyze_asset():
        ticker = entry.get()
        if ticker:
            messagebox.showinfo("Análise", f"Analisando o ativo: {ticker}")
        else:
            messagebox.showwarning("Erro", "Por favor, insira um ticker válido.")

    # Configuração da janela
    root = tk.Tk()
    root.title("Assistente Financeira")
    root.geometry("300x150")

    # Widgets
    label = tk.Label(root, text="Insira o ticker do ativo:")
    label.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack(pady=10)

    button = tk.Button(root, text="Analisar", command=analyze_asset)
    button.pack(pady=10)

    # Inicia a interface
    root.mainloop()

if __name__ == "__main__":
    gui_main()