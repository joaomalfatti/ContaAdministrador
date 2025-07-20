import os
import subprocess
import getpass
import ctypes

def is_admin():
    """Verifica se o script está sendo executado como Administrador LOCAL"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def reativar_admin_local():
    os.system("cls")
    """Reativa a conta 'Administrador' apenas no computador local"""
    try:
        os.system("cls")
        nome_usuario = "Administrador"
        
        # Verifica privilégios
        if not is_admin():
            print("\nERRO: Você precisa executar como Administrador LOCAL!")
            print("Solução: Clique com o botão direito no script e selecione")
            print("'Executar como Administrador'.")
            input("\nPressione Enter para sair...")
            return False

        # Configuração da senha
        print("\n" + "="*50)
        print(f"DEFINIR SENHA PARA '{nome_usuario}'".center(50))
        print("="*50)
        
        while True:
            senha = getpass.getpass(f"\n Digite a nova senha para {nome_usuario}: ")
            if len(senha) < 8:
                print("\n AVISO: A senha deve ter pelo menos 8 caracteres!")
                continue
                
            confirmacao = getpass.getpass(" Confirme a senha: ")
            
            if senha == confirmacao:
                break
            print("\n ERRO: As senhas não coincidem. Tente novamente.")
        try:
            
            subprocess.run(f'net user Administrador /active:yes & net user Administrador "{senha}"', shell=True, check=True)
            
            print("\n" + "="*50)
            print("CONTA REATIVADA".center(50))
            print("="*50)
            print("\nStatus: Sucesso!")
            print("Ação: Apenas neste computador")
        except subprocess.CalledProcessError as e:
            print(f"\n FALHA: Não foi possível reativar a conta (Erro {e.returncode}).")
            print(" Motivos possíveis:")
            print(" - A conta foi renomeada ou excluída")
            print(" - Políticas de segurança bloqueiam a alteração")
    except Exception as e:
        print(f"\n ERRO CRÍTICO: {str(e)}")
    finally:
        input("\n Pressione Enter para voltar...")

def menu_principal():
    """Menu simples para execução"""
    while True:
        os.system('cls')
        print("="*50)
        print("REATIVADOR DE CONTA ADMINISTRADOR LOCAL === V1.1".center(50))
        print("="*50)
        print("\n Este script reativa a conta 'Administrador' APENAS")
        print("neste computador. Requer privilégios de Administrador.")
        print("\n 1. Reativar Administrador local")
        print(" 2. Sair")
        
        opcao = input("\n Selecione uma opção: ").strip()
        
        if opcao == '1':
            reativar_admin_local()
        elif opcao == '2':
            break
        else:
            print("\n Opção inválida! Digite 1 ou 2.")
            input(" Pressione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()


""" Versão: 1.0.0
Criador: João Malfatti """