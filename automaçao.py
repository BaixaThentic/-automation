#passo a passo do projeto:

#passo 1: entrar no sistema da empresa:
#https://dlp.hashtagtreinamentos.com/python/intensivao/tabela

import pyautogui #para instalar: pip install pyautogui
import time
#pyautogui.click -> clicar com o mouse
#pyautogui.write -> escrever um textp
#pyautogui.press -> apertaCodigo    Marca   r 1 tecla
#pyautogui.hotkey -> atalho (combinação de teclas)

#adiciomar uma pausa
pyautogui.PAUSE = 0.5

#abrir o seu navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#esperar o site carregar
time.sleep(3)

#passo 2: fazer login
pyautogui.click(x=686, y=499)
pyautogui.write("joao.lima205@gmail.com") #campo de email

pyautogui.press("tab")
pyautogui.write("Raposa0990") #campo de senha0

pyautogui.press("tab")
pyautogui.press("enter") #cliar em logar

time.sleep(3)

#passo 3: importar a base de dados do produto

import pandas #para instalar: pip install pandas numpy openpyxl

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index: #index são as linhas da tabela (0, 1, 2, 3...)
#passo 4: cadastrar 1 produto
    pyautogui.click(x=728, y=354)

    #preencher os campos
    pyautogui.write(str(tabela.loc [linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc [linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc [linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc [linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc [linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc [linha, "custo"]))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    #apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")
    #para voltar pro inicio
    pyautogui.scroll(99999)

#passo 5: repetir o cadastro para todos os produtos