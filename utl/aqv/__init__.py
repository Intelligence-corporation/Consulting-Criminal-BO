from typing import Literal
from utl.lay import colour as cl


def readint(msg):
    while True:

        try:
            x = int(input(msg))

        except Exception as error:
            print(f'{cl["r"]}{error.__class__}. Try again.{cl["limit"]}')
            continue

        else:
            return x


def titleFor(txt, num1=0):
    print(f'{cl["b"]}-' * num1)
    print(f'{txt.center(num1)}')
    print(f'-' * num1)
    print(f'{cl["limit"]}')


def onlyBool(txt):
    x = ''
    while True:
        try:
            x = str(input(txt)).title()[0]
        
        except Exception as error:
            print(f'{cl["r"]}{error.__class__}. Try again.{cl["limit"]}')
        
        else:
            return x


def boolTitle(txt):
    x = ''
    bool = ''
    while True:
        try:
            x = str(input(txt)).title().strip()
            bool = str(input(f'It is correct: {cl["p"]}"{x}"{cl["limit"]} \nYour answer [ {cl["b"]}Y{cl["limit"]} | {cl["r"]}N{cl["limit"]} ]: '))[0].title()

            if bool == 'N':
                continue

            elif bool not in 'NY':
                print(f'{cl["r"]}Please, type a valid command.{cl["limit"]}')

            else:
                return x
        
        except Exception as error:
            print(f'{cl["r"]}{error.__class__}. Try again.{cl["limit"]}')


def bool(txt):
    x = ''
    bool = ''
    while True:
        try:
            x = str(input(txt)).strip()
            bool = str(input(f'It is correct: {cl["p"]}"{x}"{cl["limit"]} \nYour answer [ {cl["b"]}Y{cl["limit"]} | {cl["r"]}N{cl["limit"]} ]: '))[0].title()

            if bool == 'N':
                continue

            elif bool not in 'NY':
                print(f'{cl["r"]}Please, type a valid command.{cl["limit"]}')

            else:
                return x
        except Exception as error:
            print(f'{cl["r"]}{error.__class__}. Try again.{cl["limit"]}')


def boolNumber(txt):
    while True:
        try:
            x = int(input(txt))
        except Exception as error:
            print(f'{cl["r"]}{error.__class__}. Try again.{cl["limit"]}')
            continue
        else:
            bool = ''
            bool = str(input(f'It is correct: {cl["p"]}"{x}"{cl["limit"]} \nYour answer [ {cl["b"]}Y{cl["limit"]} | {cl["r"]}N{cl["limit"]} ]: '))[0].title()

            if bool not in 'NY':
                print(f'{cl["r"]}Please, type a valid command.{cl["limit"]}')
            
            elif bool == 'N':
                continue
                
            else:
                return x


tiposAtendimentos = ['Apoio aos eventos municipais', 'Apoio as secretarias',
 'Mediação de conflitos', 
 'Averiguação de consumo de entorpecente em logradouros públicos',
'Abordagem por atitude suspeita', 'Intervenção para prevenção de ato infracional',
 'Intervenção/Orientação sócio-educativa',
'Apoio a sociedade civil organizada', 'Intervenção no ambito escolar',
 'Prestação de socorro', 'Transporte de diversos em VTR',
 'Apoio à ocorrência de trânsito',
'Intensificação de Ronda/Averiguação', 'Atendimento social a população de rua',
 'Atendimento ao idoso', 'Documentos e/ou objetos achados',
  'Atendimento a crianças e/ou adolescente em situação de risco',
'Outros atendimentos (Detalhar no histórico)']

def line(x):
    print('-' * x)