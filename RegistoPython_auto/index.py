
import pandas as pd
import pyautogui
import time

#importando a table
try:
    table = pd.read_csv("todo.csv", encoding='utf-8')
    print(table)
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
except Exception as e:
    print("Ocorreu um erro: ",e)

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")

# note é lento =/
time.sleep(3)
pyautogui.press("enter")
# acessando meu sistema
pyautogui.write("http://localhost:5173/")
pyautogui.press("enter")
time.sleep(4)

for linha in table.index:
    pyautogui.click(x=206, y=268)
    pyautogui.write(str(table.loc[linha,"title"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha,"description"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "category"]))
    pyautogui.press("tab")
    # pyautogui.scroll(-200)
    pyautogui.click(x=329,y=570)
    