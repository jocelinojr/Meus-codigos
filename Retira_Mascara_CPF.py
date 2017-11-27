# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 15:23:41 2016

@author: jocelinoms
"""

import sys
import os
import re


def retiraMascara(filename):
    arq_entrada = open(filename, 'r')
    arq_saida   = open('CPFSemMascara.txt', 'w')
    texto = arq_entrada.readlines()    
    for linha in texto:
      linha = re.sub('\W+', '', linha)
      arq_saida.write(linha + '\n')
    # fecha os arquivos  
    arq_entrada.close()
    arq_saida.close()
     

def main():
  filename = input('Nome do Arquivo -> ')
  try:
      retiraMascara(filename)
      print('Máscaras retiradas com Sucesso!')      
      
  except FileNotFoundError:

      print('Ocorreu um erro ->', 'Arquivo %s Inexistente' % filename)
    
    
    
    
    
    
    
    
    
    

main()