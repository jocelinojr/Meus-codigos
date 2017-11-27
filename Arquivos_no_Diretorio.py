# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 17:47:59 2016

@author: jocelinoms
"""

import os, time, datetime
import glob

def main():
    # diretorio = input('Informe o Diretório->')
    
    nome_arqs = os.listdir(os.getcwd())   
    print(nome_arqs)
    
    
    for nome_arq in nome_arqs:
      datetime.date(time.ctime(os.path.getctime(os.path.abspath(nome_arq)))).year
      
        

main()
