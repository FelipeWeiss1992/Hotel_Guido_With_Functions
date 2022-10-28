from datetime import datetime
from time import sleep

def saudacao():
    
    hora = datetime.today().strftime('\033[31m%H:%M\033[0;0m')
    saudacao = ''

    if hora > ('06:00') and hora < ('12:00'):
        saudacao = 'Bom dia!'
    elif hora > ('12:00') and hora < ('18:00'):
        saudacao = 'Boa tarde!'
    else: 
        saudacao = 'Boa noite!' 

    print(hora, '\n')
    print('\033[31m{} Seja bem vindo ao hotel Guidoloop!\033[0;0m\n'.format(saudacao))
  
def checkin(hospede):
    with open('listaHospedes.txt', 'a') as arquivo:
        arquivo.write(str(hospede)+'\n')
           
def listarHospedes():
    hospedes = []       
    with open('listaHospedes.txt', 'r') as arquivo:
        for hospede in arquivo:
            hospede = hospede.strip()   
            hospedes.append(hospede) 
        
    if len(hospedes) == 0:
            print('Não há hospedes cadastrados')
            sleep(1)

    return hospedes        

def procurarHospedes(pessoa):
    hospede = 0
    arquivo = open('listaHospedes.txt', 'r')
    for linha in arquivo:
        if pessoa == eval(linha)['Nome']:
            print(linha)
            hospede += 1
            sleep(1)
    if hospede == 0:
        print('Hóspede não cadastrado')   
        sleep(1)     
          
def checkout(pessoa):
    indice = 0
    hospede = 0
    arquivo = open('listaHospedes.txt', 'r')
    for linha in arquivo:
        indice += 1
        if pessoa == eval(linha)['Nome']:
            chave = indice
            hospede += 1
    arquivo.close()          
    if hospede == 0:
        print('Hóspede não cadastrado')
        sleep(1)
    else:    
        try:
            with open('listaHospedes.txt', 'r') as fr:

                linhas = fr.readlines()

                ptr = 1

                with open('listaHospedes.txt', 'w') as fw:
                    for linha in linhas:

                        if ptr != chave:
                            fw.write(linha)
                        ptr += 1

            print('Deletado\n') 
            sleep(1)
        except:
            print('Algo deu errado.\n') 
            sleep(1)                
    
   

    
    

