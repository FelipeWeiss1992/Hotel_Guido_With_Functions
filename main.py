from time import sleep
from controller import saudacao, checkin, listarHospedes,procurarHospedes,checkout

def menu():

    saudacao()

    while True:
        try:
            print('\033[32m1 - Fazer Check-In\n2 - Listar Hóspedes\n3 - Procurar Hóspedes\n4 - Fazer Check-Out\n5 - Sair\033[0;0m\n')
            opcaoMenu = int(input('\033[33mDigite uma das Opções: \033[0;0m'))

            if opcaoMenu == 1:
                while True:
                    nomehospede = str(input('Qual seu nome completo? '))
                    cpfhospede = int(input('Qual seu cpf? '))
                    idadehospede = int(input('Qual sua idade? '))
                    hospede = {'Nome': nomehospede, 'CPF': cpfhospede, 'Idade': idadehospede}
                    checkin(hospede)
                    while True:
                        resp = str(input('Deseja cadastrar outro hóspede? [S/N} ')).upper()
                        if resp in 'SN':
                            break
                        print('ERRO! Responda apensa S ou N')    
                    if resp in 'N':
                        break
            
            elif opcaoMenu == 2:
                while True:
                    print(listarHospedes())
                    sleep(1)
                    print()
                    break
                    

            elif opcaoMenu == 3:
                while True:
                    pessoa = str(input('Digite o Nome do hóspede:'))
                    procurarHospedes(pessoa)
                    while True:
                        resp = str(input('Deseja procurar outro hóspede? [S/N} ')).upper()
                        if resp in 'SN':
                            break
                        print('ERRO! Responda apensa S ou N')    
                    if resp in 'N':
                        break

            elif opcaoMenu == 4:
                while True:
                    pessoa = str(input('Digite o Nome do hóspede:')) 
                    checkout(pessoa)
                    while True:
                        resp = str(input('Deseja fazer o checkout de outro hóspede? [S/N} ')).upper()
                        if resp in 'SN':
                            break
                        print('ERRO! Responda apensa S ou N')    
                    if resp in 'N':
                        break

            elif opcaoMenu == 5:
                print('Programa Finalizado.')
                break

            else:
                print('Não existe a opção digitada.\n')
                sleep(1)

        except(ValueError):
            print('Opção Inválida\n')
            sleep(1)

menu()




                
                