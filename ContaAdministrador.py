import os
import subprocess
import getpass
import ctypes
import time

def is_admin():
    """Verifica se o script está sendo executado como Administrador LOCAL"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def reativar_admin_local():
    os.system("cls")

    try:
        os.system("cls")
        nome_usuario = "Administrador"
        
        
        if not is_admin():
            print("\n ERRO: Você precisa executar como Administrador LOCAL!")
            print(" Solução: Clique com o botão direito no script e selecione")
            print(" 'Executar como Administrador'.")
            input("\n Pressione Enter para sair...")
            return False

        
        print("\n" + "="*50)
        print(f" DEFINIR SENHA PARA '{nome_usuario}'".center(50))
        print("="*50)
        
        while True:
            senha = getpass.getpass(f"\n Digite a nova senha para {nome_usuario} (Digite 'S' e presione Enter para retornar ao menu.): ")
    
            # Opção para voltar ao menu principal
            if senha.upper() == 'S':
                print("\n Retornando ao menu principal...")
                return True  
            
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
            print("\n Status: Sucesso!")
            print(" Ação: Apenas neste computador")
            return True
        except subprocess.CalledProcessError as e:
            print(f"\n FALHA: Não foi possível reativar a conta (Erro {e.returncode}).")
            print(" Motivos possíveis:")
            print(" - A conta foi renomeada ou excluída")
            print(" - Políticas de segurança bloqueiam a alteração")
            return False
    except Exception as e:
        print(f"\n ERRO CRÍTICO: {str(e)}")
        return False
    
    finally:
        print("\n Voltando ao menu principal em 5 segundos. (Presione Enter para continuar agora.)")
        start_time = time.time()
        while(time.time() - start_time) < 5:
            if msvcrt.kbhit():
                if msvcrt.getwch() == '\r':
                    print('\n')
                    return
                break
            time.sleep(0.1)
        print("\n")
        

def menu_principal():
    """Menu simples para execução"""
    while True:
        os.system('cls')
        print("="*50)
        print("REATIVADOR DE CONTA ADMINISTRADOR LOCAL === V1.2.0".center(50))
        print("="*50)
        print("\n Este script reativa a conta 'Administrador' APENAS")
        print("neste computador. Requer privilégios de Administrador.")
        print("\n 1. Reativar Administrador local")
        print(" 2. Sair")
        
        opcao = input("\n Selecione uma opção: ").strip()
        
        if opcao == '1':
            reativar_admin_local()
        elif opcao == '2':
            print("\n" + "="*50)
            print("Até logo".center(50))
            print("="*50)
            break
        else:
            print("\n Opção inválida! Digite 1 ou 2.")
            input(" Pressione Enter para continuar...")
        

if __name__ == "__main__":
    import msvcrt
    menu_principal()


""" Versão: 1.2.0
Criador: João Malfatti """