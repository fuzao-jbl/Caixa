import os
import cmd
import pickle
from joblib import dump

import pandas as pd
import calculator as calc

class Configuration(cmd.Cmd):
    """ This is the configuration CLI of the caixa """

    prompt = 'Digite seu comando $ '
    intro = '''Bem vindo ao caixa de palha italiana!\n
        Caso nao saiba me usar, digite "ajuda"\n'''

    def __init__(self):
        super(Configuration, self).__init__()
        self.einstein = None
        self.curie = None
        self.newton = None
        self.brigadeiro = None
        self.pedro = None
        self.isa = None
        self.save_files = [
                'stock.cav',
                'stock.pkl',
                'receipt.ods',
                'receipt.pkl',
                ]

    def do_ajuda(self, arg):
        """ Show how to use the configuration """
        
        print('''Os comandos sao:\n
            einstein\tinsere numero de palhas einstein\n
            curie\tinsere numero de palhas curie\n
            newton\tinsere numero de palhas newton\n
            brigadeiro\tinsere o numero de brigadeiros\n
            pedro\tinsere a divida de pedro\n
            isa\tinsere a divida de isa\n
            reset\treseta as configuracoes\n
            enter\tEntra no caixa\n''')

    def do_einstein(self, arg):
        """ Resets the einstein configuration """

        try:
            value = eval(arg)
        except:
            print('''ERRO: NUMERO DE PALHAS EINSTEIN NAO E INTEIRO\n
                TIPO EINSTEIN:''', type(arg))
            return None

        if isinstance(value, int):
            self.einstein = value 
            print('Einstein:', self.einstein)
        else:
            print('''ERRO: NUMERO DE PALHAS EINSTEIN NAO E INTEIRO\n
                TIPO EINSTEIN:''', type(value))
            return None

    def do_curie(self, arg):
        """ Resets the curie configuration """

        try:
            value = eval(arg)
        except:
            print('''ERRO: NUMERO DE PALHAS CURIE NAO E INTEIRO\n
                TIPO CURIE:''', type(value))
            return None

        if isinstance(value, int):
            self.curie = value
            print('Curie:', self.curie)
        else:
            print('''ERRO: NUMERO DE PALHAS CURIE NAO E INTEIRO\n
                TIPO CURIE:''', type(value))
            return None

    def do_newton(self, arg):
        """ Resets the newton configuration """

        try:
            value = eval(arg)
        except:
            print('''ERRO: NUMERO DE PALHAS NEWTON NAO E INTEIRO\n
                TIPO NEWTON:''', type(value))
            return None

        if isinstance(value, int):
            self.newton = value
            print('Newton:', self.newton)
        else:
            print('''ERRO: NUMERO DE PALHAS NEWTON NAO E INTEIRO\n
                TIPO NEWTON:''', type(value))
            return None

    def do_brigadeiro(self, arg):
        """ Resets the brigadeiro configuration """

        try:
            value = eval(arg)
        except:
            print('''ERRO: NUMERO DE BRIGADEIRO NAO E INTEIRO\n
                TIPO BRIGADEIRO:''', type(value))
            return None

        if isinstance(value, int):
            self.brigadeiro = value
            print('Brigadeiro:', self.brigadeiro)
        else:
            print('''ERRO: NUMERO DE BRIGADEIRO NAO E INTEIRO\n
                TIPO BRIGADEIRO:''', type(value))
            return None

    def do_pedro(self, arg):
        """ Reset the pedro configuration """

        try:
            value = eval(arg)
            self.pedro = value
            print('Pedro:', self.pedro)
        except:
            print('''ERRO: DIVIDA DE PEDRO NAO E NUMERO\n
                TIPO PEDRO:''', type(value))
            return None

    def do_isa(self, arg):
        """ Reset the pedro configuration """

        try:
            value = eval(arg)
            self.isa = value
            print('Isa:', self.isa)
        except:
            print('''ERRO: DIVIDA DE ISA NAO E NUMERO\n
                TIPO ISA:''', type(value))
            return None

    def do_reset(self, arg):
        """ Reset configuration """

        # Look for missing values
        if self.einstein is None:
            print('NAO HA CONFIGURACAO EINSTEIN')
            return None
        elif self.curie is None:
            print('NAO HA CONFIGURACAO CURIE')
            return None
        elif self.newton is None:
            print('NAO HA CONFIGURACAO NEWTON')
            return None
        elif self.brigadeiro is None:
            print('NAO HA CONFIGURACAO BRIGADEIRO')
            return None
        elif self.pedro is None:
            print('NAO HA CONFIGURACAO PEDRO')
            return None
        elif self.isa is None:
            print('NAO HA CONFIGURACAO ISA')
            return None

        # Reconfigure
        stock = calc.Stock(self.einstein, self.curie, self.newton, 
                           self.brigadeiro, self.pedro, self.isa)
        receipt = calc.Receipt()
        for file in os.listdir():
            if file in self.save_files:
                os.remove(file)
        dump(stock, 'stock.pkl')
        dump(receipt, 'receipt.pkl')
        # Tell the user the configuration was reseted
        print(f'''Configuracao pronta!\n
            Einstein:\t{self.einstein}
            Curie:\t{self.curie}
            Newton:\t{self.newton}
            Brigadeiro:\t{self.brigadeiro}
            Pedro:\t{self.pedro}
            Isa:\t{self.isa}\n
            Se qualquer um dos valores estiverem errados, voce pode resetar
            de novo!''')

    def do_enter(self, arg):
        """ Enter new value """
    
        files = os.listdir()
        if 'stock.csv' in files and 'receipt.ods' in files:
            stock = pd.read_csv('stock.csv')
            self.einstein = stock['Albert Einstein'].values[0]
            self.curie = stock['Marie Curie'].values[0]
            self.newton = stock['Isaac Newton'].values[0]
            self.brigadeiro = stock['Brigadeiro'].values[0]
            self.pedro = stock['$ Pedro'].values[0]
            self.isa = stock['$ Isa'].values[0]
            stock = calc.Stock(self.einstein, self.curie, self.newton,
                          self.brigadeiro, self.pedro, self.isa)
            dump(stock, 'stock.pkl')
            return True
        elif 'stock.pkl' in files and 'receipt.pkl' in files:
            return True
        else:
            print('NENHUMA CONFIGURACAO ENCONTRADA')
            return None
