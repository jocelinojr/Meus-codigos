# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:15:55 2016

@author: jocelinoms
"""


import os
import pandas as pd
import urllib


def verifica_monta_dir_arq(nome_arquivo, diretorio):
    """
       Se o diretório passado não é o local, verifica se existe. Caso contrário, cria-o
       Após, monta o caminho completo com o nome do arquivo passdo
    """
    if diretorio.lower() == 'local':
        diretorio = os.getcwd() 
    else:
        # verifica se o diretório existe, senão, cria-o
        if not os.path.exists(diretorio):
           os.path.mkdir(diretorio)
    # monta o nome completo do arquivo    
    return os.path.join(diretorio, nome_arquivo) 
    

def baixa_arquivo_url(url, nome_arquivo, diretorio='local'):
    """
       Faz o download do arquivo relacionado ao url passado. 
       Por default, baixa na pasta local. Se for informada uma diferente, baixa nela
    """
    # monta o nome do arquivo completo, criando o diretório se preciso     
    nome_arquivo_completo = verifica_monta_dir_arq(nome_arquivo, diretorio)
    try:
       urllib.request.urlretrieve(url, nome_arquivo_completo)
    except urllib.error.HTTPError as e:
       print('Ocorreu o seguinte erro ao conectar-se: ', e)
    

def pega_arquivo_municipios_ibge(url_tabela):
    """
      vai na url passada do IBGE faz o download do arquivo xls com os 
      códigos dos municípios e retorna um dataframe com código e o nome
    """
    # nome local do arquivo - usa join para manter a portabilidade do código   
    nome_arquivo_xls = os.path.join(os.getcwd(), 'municipios_ibge.xls') 
    # baixa o arquivo, se ainda não o baixamos
    try:
        if not os.path.exists(nome_arquivo_xls):
          urllib.request.urlretrieve(url_tabela, nome_arquivo_xls)
    except urllib.error.HTTPError as e:
       print('Ocorreu o seguinte erro ao conectar-se: ', e)
    # abre o arquivo excel baixado com o Pandas
    xls = pd.ExcelFile(nome_arquivo_xls)
    municipios = xls.parse(xls.sheet_names[0], skiprows=1, index_col=None, na_values=['NA'])            
    # Renomeia as colunas para evitar o codigo com acento    
    municipios.columns = ['UF', 'CODIGO', 'NOME']    
    return municipios

