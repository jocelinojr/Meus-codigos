# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 15:31:41 2016

@author: jocelinoms
"""

import urllib as ur
import os 
from html.parser import HTMLParser
import re


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("achei uma tag:", tag)

    def handle_endtag(self, tag):
        print("achei uma end tag :", tag)

    def handle_data(self, data):
        print("achei data  :", data)


def usandourlopen():
    print('Buscando...novo2')
    url = 'http://www.sdh.gov.br/assuntos/pessoa-com-deficiencia/observatorio/acoes/acoes-municipio/TO/170190'
    meuhtml = ur.request.urlopen(url)
    texto = str(meuhtml.read(), encoding='utf8')
    print(texto)
    if texto.find('<spam>', 0) >= 0:
        print('Achou!')
    
    
    


def usandoretrieve():
    print('Buscando...novo')
    url = 'http://www.sdh.gov.br/assuntos/pessoa-com-deficiencia/observatorio/acoes/acoes-municipio/TO/170190'
    nomearquivo = os.path.join(os.getcwd(), 'Araguacema2.html')
    ur.request.urlretrieve(url, nomearquivo)
    # abre-o arquivo trazido
    arquivo = open(nomearquivo,'r', encoding = 'utf8',)
    texto = arquivo.read()
    textominusculo = texto.lower()
    sim = textominusculo.find(r'<span>sim</span>', 0)
    numero = re.search('(<td id="edu_sal_multifuncional" class="data">)(\s+)(<span>)(\d)(<\span>)', texto)
    if sim > 0:
        print('Achamos o Sim da Adesão!')
    if numero: 
        print('Achamos o numero!')
    
        
    
    """
    flag = False    
    for linha in texto:
      achouadesao = linha.find('rel_adesao') > 0
      if achouadesao:
          print(linha)
          flag = True
          continue
      # se estamos nos dados da adesão
      if linha.find('<span>') and flag:
          print(linha)
          flag = False
      """    
          
      
      
    
    
    """
    if texto.find('Aderiu ao Plano Viver sem Limite') > 0:
        print(texto)
    
    for linha in arquivo:
        print(linha)
        if linha.find('Aderiu ao Plano Viver sem Limite') > 0:
            print(linha)
        if linha.find('rel_adesao') > 0:
            print(linha)
            flag = True
            continue
        # se estamos na linha da resposta...    
        if flag:
            print(linha)
            # reseta a flag
            flag = False
     """       
        
            
            
    
    
    arquivo.close()
    
                
    



def main():
    usandoretrieve()
    # usandourlopen()
    # cria o objeto parser
    # parser = MyHTMLParser()
    # parser.feed(arquivohtml)

    
    
    
    
    
    
main()