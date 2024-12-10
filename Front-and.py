import customtkinter as ctk

# Configuração inicial
ctk.set_appearance_mode("System")  # Tema: "Dark", "Light", ou "System"
ctk.set_default_color_theme("blue")  # Cores: "blue", "green", ou "dark-blue"

# Criação da Janela Principal
janela = ctk.CTk()
janela.title("Sistema de Login")
janela.geometry("400x300")


# Sub Janela
def abrir_nova_tela():
    nova_tela = ctk.CTkToplevel()
    nova_tela.title("Menu de Opções")
    nova_tela.geometry("400x300")

    titulo_menu = ctk.CTkLabel(nova_tela, text="Menu de Opções")
    titulo_menu.pack(pady=20)

    botao_opcao1 = ctk.CTkButton(nova_tela, text="Opção 1", command=lambda: print("Opção 1 selecionada"))
    botao_opcao1.pack(pady=10)

    botao_opcao2 = ctk.CTkButton(nova_tela, text="Opção 2", command=lambda: print("Opção 2 selecionada"))
    botao_opcao2.pack(pady=10)

    botao_opcao3 = ctk.CTkButton(nova_tela, text="Opção 3 ", command=lambda: print("Opção 3 selecionada"))
    botao_opcao3.pack(pady=10)

    botao_sair = ctk.CTkButton(nova_tela, text="Sair", command=nova_tela.destroy)
    botao_sair.pack(pady=20)


# Função de verificação do login
def verificar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario == "admin" and senha == "1234":
        janela.withdraw()
        abrir_nova_tela()
    else:
        mensagem["text"] = "Usuário ou senha incorretos."
        mensagem.configure(text_color="red")


# Elementos da interface
titulo = ctk.CTkLabel(janela, text="Login", font=("Arial", 24))
titulo.pack(pady=10)

entrada_usuario = ctk.CTkEntry(janela, placeholder_text="Usuário")
entrada_usuario.pack(pady=10)

entrada_senha = ctk.CTkEntry(janela, placeholder_text="Senha", show="*")
entrada_senha.pack(pady=10)

botao_login = ctk.CTkButton(janela, text="Entrar", command=verificar_login)
botao_login.pack(pady=20)

mensagem = ctk.CTkLabel(janela, text="", font=("Arial", 12))
mensagem.pack(pady=10)

# Iniciar o loop principal
janela.mainloop()