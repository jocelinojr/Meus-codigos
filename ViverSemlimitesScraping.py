# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 10:37:07 2016

@author: jocelino
"""



from bs4 import BeautifulSoup
import pandas as pd
import os
import urllib
import csv
import openpyxl
import xlrd
import UtilitariosTCU as tcu



def pega_codigo_municipios_3(url_tabela, uf):
    """
      retorna um dicionário com o código e nome
      do município do estado passado
    """
    municipios = tcu.pega_arquivo_municipios_ibge(url_tabela)
    estado =  municipios.loc[municipios['UF'] == uf, 'CODIGO':'NOME']
    result = dict(zip(estado.NOME, estado.CODIGO))
    return result
       

def pega_codigo_municipios_2(uf):
    """
      Versão 2 da função usando zip para empacotar diretamente do dataframe
    """
    municipios = pd.read_csv('municipios_cod_ibge.csv', sep = ';', encoding = 'ISO-8859-1')
    
    # seleciona só os do estado passado
    estado =  municipios.loc[municipios['UF'] == uf, 'CODIGO':'NOME']
    result = dict(zip(estado.NOME, estado.CODIGO))
    return result


def pega_codigo_municipios(uf):
    """
      Versão 1 da função que pega os municípios de um determinado estado do .csv   
      e retorna um dicionário
    """
    municipios = pd.read_csv('municipios_cod_ibge.csv', sep = ';', encoding = 'ISO-8859-1')
    result = {}
    # seleciona só os do estado passado
    estado =  municipios[municipios['UF'] == uf]
    # percorre o dataset
    i = 0
    while i < len(estado):
      # pega o codigo 
      codigo = estado.iloc[i, 1]
      codigostr = str(codigo)[0:6]
      # pega a cidade
      nome = estado.iloc[i, 2]            
      i =  i + 1
      # coloca no dicionário
      result[codigostr] = nome
     
    return result


def pega_valores_desejados(url, nomemunicipio):
   """
     varre a página passada em busca dos dois dados que queremos:
     1) Aderiu ao Plano Viver sem Limite??
     2) Escolas com Salas de Recursos Multifuncionais
     retorna uma tupla com os dados
   """
   aderiu = ''
   qde_salas = ''
   # diretório onde colocaremos os arquivos baixados
   dir_arquivos_baixar = os.path.join(os.getcwd(), 'arquivos')
   # se não existe o diretório onde colocaremos os arquivos, cria-o
   if not os.path.exists(dir_arquivos_baixar):
       os.mkdir(dir_arquivos_baixar)
   nome_arquivo = os.path.join(dir_arquivos_baixar, nomemunicipio + '.html') 
   # html = urllib.request.urlopen(url)
   # traz o arquivo e salva no disco
   urllib.request.urlretrieve(url, nome_arquivo)
   arquivo = open(nome_arquivo, 'r', encoding = 'utf-8')
   soup = BeautifulSoup(arquivo.read(), 'html.parser')
   tag_aderiu = soup.find("td", {"id": "rel_adesao"})
   # se achamos
   if tag_aderiu is None:
     print('Não Achou a tag de Adesão ')
   else:
     aderiu = tag_aderiu.get_text()
   
   tag_qde_salas = soup.find('td', {'id': 'edu_sal_multifuncional'})
   if tag_qde_salas is None:
     print('Não Achou a tag das Salas ')
     
   else:
     qde_salas = tag_qde_salas.get_text()
            
   return (aderiu, qde_salas)


def main():
   
   # pega os códigos e os nomes dos muncípios do site do IBGE   
   codigosnomes = pega_codigo_municipios_3('http://www.sidra.ibge.gov.br/bda/territorio/download/munic.xls', 'TO')    
   
   # percorre os municipios 
   # gera o csv na codificação ISO-8859-1
   csv_resp = csv.writer(open('resposta.csv', 'w', newline= '', encoding = 'ISO-8859-1'))
   print('Iniciando....')
   try:
       
       for nome_municipio, codigo in sorted(codigosnomes.items()):
         # imprime o atual...
         print('Município -> ', nome_municipio)
         # monta a url 
         url = ('http://www.sdh.gov.br/assuntos/pessoa-com-deficiencia/observatorio/acoes/acoes-municipio/TO/%s' % str(codigo)[0:6])
         # vai no servidor e pega os valores
         aderiu, qde = pega_valores_desejados(url, nome_municipio)
         # monta a tupla para ser escrita no arquivo csv de saída
         tupla = (nome_municipio.strip(), aderiu.strip(), qde.strip())
         # escreve no csv de saída
         csv_resp.writerow(tupla)
         
   except urllib.error.HTTPError as e:
       print('Ocorreu o seguinte erro ao conectar-se: ', e)
           

main()



