import re
import pyinputplus as pyip
numeros = '1234567890'
caracteres = '!@#$%&*-_'

#Validador de e-mails
email_= re.compile(r'([a-zA-Z0-9_.]+)(@\w+)(\.\w+)')
#Validador de cpf
cpf_= re.compile(r'(\d{3})\.(\d{3})\.(\d{3})-(\d{2})')
#Validador de senhas:
#regras - 8 a 12 caracteres caracteres, letras maiúsculas e minúsculas, número e um caractere especial
senhas_= re.compile(r'[a-zA-Z0-9!@#$%&*-_]{8}')

#Eu não usei o pyip.inputEmail pois queria praticar com o módulo re
while True:
    email_usuario = input ('Digite seu e-mail: ')
    encontrarE = email_.findall (email_usuario)
    if encontrarE == []:
        print ('E-mail inválido!, tente novamente')
        continue
    else: 
        break
while True:
    cpf_usuario = input('Digite seu cpf: ')
    encontrarC = cpf_.findall (cpf_usuario) 
    if encontrarC == []:
        print ('Por favor digite seu cpf!')
        continue
    else: break
while True:
    senha_usuario = pyip.inputPassword('Digite sua senha: ')
    if len(senha_usuario) > 8:
        print ('Tem que ser 8 caracteres')
        continue
    elif len(senha_usuario) < 8:
        print ('Senha inválida, falta caracteres')
        continue
    encontrarS = senhas_.search(senha_usuario)
    achadoS = encontrarS.group()
    Ltext= list(filter (lambda x: x in r'[abcdefghijklmnopqrstuvwxyz]', list(achadoS)))
    Utext = list(filter(lambda x: x in r'[ABCDEFGHIJKLMNOPQRSTUVWXYZ]', list(achadoS)))
    Number = list(filter(lambda x: x in list(numeros), list(achadoS)))
    caracter =list(filter(lambda x: x in list(caracteres), list(achadoS)))
    if len(Ltext) == 0 or len(Utext) == 0 or len(Number) == 0 or len(caracter) == 0:
        print ('Falta alguma coisa ai!')
        continue
    else:
        break

print ('Sua senha é:', achadoS)
print ('Seu e-mail é:', str(encontrarE))
print ('E seu cpf é:', str(encontrarC))