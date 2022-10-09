""" This module contains all the functions that calculate the stock """

import pandas as pd

class Stock(pd.DataFrame):
    """ This class represents the stock of palhas italianas """

    def __init__(self, einstein, curie, newton, brigadeiro, pedro, isa):
        types = {
            'Albert Einstein': [einstein],
            'Marie Curie': [curie],
            'Isaac Newton': [newton],
            'Brigadeiro': [brigadeiro],
            '$ Pedro': [-pedro],
            '$ Isa': [-isa],
            }
        super().__init__(types)

    def _discount_palhas(self, sold):
        """ This function discounts from the stock the number of the type_ """

        for type_, number in sold.items():
            self[type_] -= number

    def _add_money(self, sold):
        """ This function adds money to each account according to the amount
        each spent """

        money = calculate_money(sold)
        pedro_debt = -self['$ Pedro'].values[0]
        isa_debt = -self['$ Isa'].values[0]
        debt = isa_debt + pedro_debt

        if money < debt and pedro_debt < isa_debt and money < isa_debt:
            self['$ Isa'] += money
        elif money < debt and pedro_debt < isa_debt and money > isa_debt:
            money += isa_debt
            self['$ Isa'] = 0
            self[['$ Isa', '$ Pedro']] += money/2
        elif money < debt and pedro_debt > isa_debt and money < pedro_debt:
            self['$ Pedro'] += money
        elif money < debt and pedro_debt > isa_debt and money > pedro_debt:
            money += pedro_debt
            self['$ Pedro'] = 0
            self[['$ Isa', '$ Pedro']] += money/2
        else:
            self[['$ Isa', '$ Pedro']] += money/2

    def sell(self, sold):
        """ Calculates changes in the stock given number of type_ sold """

        self._discount_palhas(sold)
        self._add_money(sold)
        self.to_csv('stock.csv')

class Receipt(pd.DataFrame):
    """ This class represents the receipt of the sellings """

    def __init__(self):
        data = {
            'Name': [],
            'Albert Einstein': [],
            'Isaac Newton': [],
            'Marie Curie': [],
            'Brigadeiro': [],
            'Price': [],
            }
        super().__init__(data)

    def add_receipt(self, name, sold):
        """ This function adds the person to the receipt """

        price = calculate_money(sold)
        row = [name, sold['Albert Einstein'], sold['Isaac Newton'],
               sold['Marie Curie'], sold['Brigadeiro'], price]
        breakpoint()
        self.loc[len(self.index)] = row
        self.to_excel('receipt.ods')

def calculate_money(sold):
    """ Given a dictionary of palhas that were sold, return amount
    of money """

    palha_types = ['Albert Einstein', 'Isaac Newton', 'Marie Curie']
    palhas = {palha_type: sold[palha_type] for palha_type in palha_types}
    number = sum(palhas.values())
    if number == 1:
        money = 5.5 
    elif number == 2:
        money = 10
    elif number == 3:
        money = 14.5
    elif number > 3:
        money = number*4.5

    brigadeiro = sold['Brigadeiro']
    money += brigadeiro*3

    return money
