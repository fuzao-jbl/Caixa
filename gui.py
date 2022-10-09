""" This module contains the gui application """

import tkinter as tk
from tkinter import ttk
import pickle
from joblib import load, dump
import pandas as pd

import calculator as calc

class Selling(tk.Frame):
    """ This class represents the widgets to input the information about the
    selling """

    def __init__(self, parent, einstein, curie, newton, brigadeiro, 
                 pedro, isa, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Calculator related attributes
        self.stock = load('stock.pkl')
        self.receipt = load('receipt.pkl')

        # Defining the variables
        self.einstein = tk.IntVar()
        self.curie = tk.IntVar()
        self.newton = tk.IntVar()
        self.brigadeiro = tk.IntVar()
        self.status = tk.StringVar()
        self.name = tk.StringVar()
        self.status = tk.StringVar()
        self.pedro = tk.StringVar()
        self.isa = tk.StringVar()
        self.stock_einstein = tk.StringVar()
        self.stock_curie = tk.StringVar()
        self.stock_newton = tk.StringVar()
        self.stock_brigadeiro = tk.StringVar()
        self.error = tk.StringVar()
        self.price = tk.StringVar()

        # Initializing variables
        self.name.set('')
        self.error.set('')
        self.status.set('Not Saved')
        self.pedro.set(self.stock['$ Pedro'].values[0])
        self.isa.set(self.stock['$ Isa'].values[0])
        self.stock_einstein.set(self.stock['Albert Einstein'].values[0])
        self.stock_curie.set(self.stock['Marie Curie'].values[0])
        self.stock_newton.set(self.stock['Isaac Newton'].values[0])
        self.stock_brigadeiro.set(self.stock['Brigadeiro'].values[0])

        # Creating labels
        title_label = ttk.Label(self, text='Caixa', font=('TkDefaultFont', 16))
        name_label = ttk.Label(self, text='Nome')
        einstein_label = ttk.Label(self, text='Einstein')
        curie_label = ttk.Label(self, text='Curie')
        newton_label = ttk.Label(self, text='Newton')
        brigadeiro_label = ttk.Label(self, text='Brigadeiro')
        status_label = ttk.Label(self, textvariable=self.status)
        pedro_money_label = ttk.Label(self, textvariable=self.pedro)
        pedro_label = ttk.Label(self, text='Pedro R$')
        isa_money_label = ttk.Label(self, textvariable=self.isa)
        isa_label = ttk.Label(self, text='Isa R$')
        stock_einstein_quantity_label = ttk.Label(self,
                                            textvariable=self.stock_einstein)
        stock_einstein_label = ttk.Label(self, text='Estoque Einstein')
        stock_curie_quantity_label = ttk.Label(self, textvariable=self.stock_curie)
        stock_curie_label = ttk.Label(self, text='Estoque Curie')
        stock_newton_quantity_label = ttk.Label(self, textvariable=self.stock_newton)
        stock_newton_label = ttk.Label(self, text='Estoque Newton')
        stock_brigadeiro = ttk.Label(self, text='Estoque brigadeiro')
        stock_brigadeiro_quantity = ttk.Label(self, textvariable=self.stock_brigadeiro)
        error_label = ttk.Label(self, text='Erro:')
        error_type_label = ttk.Label(self, textvariable=self.error)
        price_label = ttk.Label(self, textvariable=self.price)

        # Creating the input windows
        name_entry = ttk.Entry(self, textvariable=self.name)
        einstein_spinbox = tk.Spinbox(self, from_=0, 
                                      to=float(self.stock['Albert Einstein']),
                                      increment=1, textvariable=self.einstein)
        curie_spinbox = tk.Spinbox(self, from_=0, 
                                   to=float(self.stock['Marie Curie']), 
                                   increment=1, textvariable=self.curie)
        newton_spinbox = tk.Spinbox(self, from_=0, 
                                    to=float(self.stock['Isaac Newton']),
                                    increment=1, textvariable=self.newton)
        brigadeiro_spinbox = tk.Spinbox(self, from_=0,
                                         to=float(self.stock['Brigadeiro']),
                                         increment=1, 
                                         textvariable=self.brigadeiro)
        enter_button = ttk.Button(self, text='Salvar', command=self.enter)
        calc_button = ttk.Button(self, text='Calcular', command=self.calcule)

        # Putting the pieces together
        title_label.grid(row=0, column=0, columnspan=5, sticky=tk.W)
        name_label.grid(row=1, column=0, sticky=tk.W)
        name_entry.grid(row=2, column=0, sticky=tk.W)
        einstein_label.grid(row=1, column=1, sticky=tk.W)
        einstein_spinbox.grid(row=2, column=1, sticky=tk.W)
        curie_label.grid(row=1, column=2, sticky=tk.W)
        curie_spinbox.grid(row=2, column=2, sticky=tk.W)
        newton_label.grid(row=1, column=3, sticky=tk.W)
        newton_spinbox.grid(row=2, column=3, sticky=tk.W)
        brigadeiro_label.grid(row=1, column=4, sticky=tk.W)
        brigadeiro_spinbox.grid(row=2, column=4, sticky=tk.W)
        pedro_label.grid(row=3, column=0, sticky=tk.W)
        pedro_money_label.grid(row=4, column=0, sticky=tk.W)
        isa_label.grid(row=3, column=1, sticky=tk.W)
        isa_money_label.grid(row=4, column=1, sticky=tk.W)
        stock_einstein_label.grid(row=3, column=2, sticky=tk.W)
        stock_einstein_quantity_label.grid(row=4, column=2, sticky=tk.W)
        stock_curie_label.grid(row=3, column=3, sticky=tk.W)
        stock_curie_quantity_label.grid(row=4, column=3, sticky=tk.W)
        stock_newton_label.grid(row=3, column=4, sticky=tk.W)
        stock_newton_quantity_label.grid(row=4, column=4, sticky=tk.W)
        stock_brigadeiro.grid(row=5, column=0, sticky=tk.W)
        stock_brigadeiro_quantity.grid(row=6, column=0, sticky=tk.W) 
        calc_button.grid(row=5, column=1, sticky=tk.W)
        price_label.grid(row=6, column=1, sticky=tk.W)
        enter_button.grid(row=5, column=2, sticky=tk.W)
        status_label.grid(row=6, column=2, sticky=tk.W)
        error_label.grid(row=5, column=3, sticky=tk.W)
        error_type_label.grid(row=6, column=3, sticky=tk.W)

    def _get_values(self):
        """ Inner function that retrives values """

        einstein = self.einstein.get()
        curie = self.curie.get()
        newton = self.newton.get()
        brigadeiro = self.brigadeiro.get()

        # Raise errors
        if not isinstance(einstein, int):
            self.error.set('EINSTEIN NAO E INT')
            return None
        elif not isinstance(curie, int):
            self.error.set('CURIE NAO E INT')
            return None
        elif not isinstance(newton, int):
            self.error.set('NEWTON NAO E INT')
            return None
        elif not isinstance(brigadeiro, int):
            self.error.set('BRIGADEIRO NAO E INT')
            return None
        # If no errors, prepare data and return it
        else:
            sold = {
                'Albert Einstein': einstein,
                'Marie Curie': curie,
                'Isaac Newton': newton,
                'Brigadeiro': brigadeiro,
                }
            return sold

    def enter(self):
        """ This function saves the sell and takes it to the stock """

        # Get values
        name = self.name.get()
        sold = self._get_values()
        if sold == None:
            return None
        elif not isinstance(name, str):
            self.error.set('NOME NAO E STRING')
            return None

        # Calculate from the stock and create receipt
        self.stock.sell(sold) 
        self.receipt.add_receipt(name, sold)

        # Set new values
        self.status.set(str(name) + ' salvo!')
        self.pedro.set(self.stock['$ Pedro'].values[0])
        self.isa.set(self.stock['$ Isa'].values[0])
        self.stock_einstein.set(self.stock['Albert Einstein'].values[0])
        self.stock_curie.set(self.stock['Marie Curie'].values[0])
        self.stock_newton.set(self.stock['Isaac Newton'].values[0])
        self.stock_brigadeiro.set(self.stock['Brigadeiro'].values[0])

    def calcule(self):
        """ This function calculates the price of the selling """

        sold = self._get_values()
        if sold == None:
            return None
        price = calc.calculate_money(sold)
        self.price.set('R$ ' + str(price))

class MainApplication(tk.Tk):
    """ Main window """

    def __init__(self, einstein, curie, newton, brigadeiro, pedro, isa, 
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Caixa Palha Italiana')
        self.geometry('800x600')
        Selling(self, einstein, curie, newton, brigadeiro, pedro, isa).grid(
                sticky=(tk.W+tk.E+tk.N+tk.S))
