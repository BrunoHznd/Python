import pyautogui
import time

#dando um tempo pro comando executar
pyautogui.PAUSE = 2

# "Apertando o botão do windows"
pyautogui.press("win")

#digitando "login.xlsl"
pyautogui.write("Login.xlsx")
pyautogui.press("backspace")
pyautogui.press("enter")



time.sleep(5)
pyautogui.click(x = 213,  y = 234)
pyautogui.write("Bruno")
pyautogui.click(x = 276, y = 282)
pyautogui.write("SenhaBruno")