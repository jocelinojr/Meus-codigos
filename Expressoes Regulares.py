# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 17:31:07 2016

@author: jocelinoms
"""
import re

def pegando_preco():
    texto = 'Lista de Compras: Teclado R$ 125,23  Monitor R$ 1.250,32 Mouse R$ 12,23 Casa R$ 9.584.658,00'
    padrao = 'R\$\s[\d.,]+'
    padrao = '[\d.,]+'
    # extrai somente os preços da string    
    match = re.search(padrao, texto)
    if match :
        print('Achei -> ', match.group(0))        
    else:
        print('Nada feito')
        
    # pesquisa na string toda    
    precos = re.findall(padrao, texto)
    for preco in precos:
        print('Preço->  ', preco)
    
def main():
    pegando_preco()
    
    
if __name__ == '__main__':
   main()