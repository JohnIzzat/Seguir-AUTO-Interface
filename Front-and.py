import customtkinter as ctk

# Configuração inicial
ctk.set_appearance_mode("System")  # Tema: "Dark", "Light", ou "System"
ctk.set_default_color_theme("blue")  # Cores: "blue", "green", ou "dark-blue"

# Criação da Janela Principal
janela = ctk.CTk()
janela.title("Sistema de Login")
janela.geometry("400x300")

# Função de verificação do login


def verificar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    # Credenciais para teste (pode ser substituído por um banco de dados no futuro)
    if usuario == "admin" and senha == "1234":
        mensagem["text"] = "Login bem-sucedido!"
        mensagem.configure(text_color="green")
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