##############################################################################
#
# A simple code automate the job search process.
#

import webbrowser
import pyautogui
import xlsxwriter
import time
import pyperclip
from utils.getxylogochrome import getxylogochrome
import pygetwindow as gw
import datetime

# 1- Abre la URL en el navegador Chrome en la URL de busqueda
#
url = 'https://www.linkedin.com/jobs/search-results/?'
employers= [
    'Pfizer',
    'JPMorgan',
    'Deloitte'
    ]

rol = [
    'IT Project Manager',
    'IT Program Manager',
    'Technical Project Manager'
    ]

position = []
position_list=[]
position=(['IT Project Manager','https://www.linkedin.com/jobs/view/4346190566/?alternateChannel=search&eBP=BUDGET_EXHAUSTED_JOB&refId=UsmUN6G2Le8F9kPsG%2FHg6Q%3D%3D&trackingId=DT3QElVS4JK5juprcYRWZQ%3D%3D&lipi=urn%3Ali%3Apage%3Ad_flagship3_nlsearch_srp_jobs%3BkkPN%2BegOT%2FOQEATawobAlg%3D%3D'])
position_list.append(position)


f_EA="f_EA=true&"
f_TPR="f_TPR=r86400&"
keywords = "keywords=" + rol[0].replace(" ","%20")+"&"  # Example "keywords=it%20project%20manager"
sortby = "sortBy=R"

url+=f_EA + f_TPR + keywords + sortby
# abre una nueva ventana
webbrowser.open_new(url)
time.sleep(5) # Pauses the program for 5 seconds


# 2- Ahora coloca en foco la Pagina recien abierta
# 
ventanas=gw.getAllTitles()
posicion=0
for indice, ventana in enumerate(ventanas):
    if "LinkedIn" in ventana:
        posicion=indice
LinkedinWindow = gw.getWindowsWithTitle(ventanas[posicion])[0]
LinkedinWindow.maximize()
LinkedinWindow.activate()

# 3- Hace Ajustes en la pagina
#
pyautogui.moveTo(837, 410, duration=0.5) 
pyautogui.dragTo(1400, 409, duration=1, button='left') # Arrastra por 1 segundo
pyautogui.hotkey('ctrl', 'c')
v_rol = pyperclip.paste()

# 4- Copia la URL de la posicion
LinkedinWindow.activate()
pyautogui.moveTo(837, 410, duration=0.5)
pyautogui.click()
pyautogui.moveTo(837+50, 410, duration=0.5) 
pyautogui.rightClick()
time.sleep(0.5) # 3. Pequeña espera para que aparezca el menú
# Presionar la tecla rápida para "Copiar dirección de enlace"
pyautogui.press('down', presses=6) # Baja 6 posiciones en el menú
pyautogui.press('enter')
v_url = pyperclip.paste()

# Adiciona rol, url, en la lista de roles
position_list.append([v_rol,v_url])

# 6- Store the data from list to excel file 

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook("results.xlsx")
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column("A:A", 20)
worksheet.set_column("D:D", 20)
worksheet.set_column("G:G", 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({"bold": True})

worksheet.write("A1", 'Rol', bold)
worksheet.write("B1", 'Url', bold)
worksheet.write("C1", 'Location', bold)
worksheet.write("D1", 'Contact', bold)
worksheet.write("E1", 'P Date', bold)
worksheet.write("F1", 'Apply Date', bold)
worksheet.write("G1", 'Remote', bold)
worksheet.write("H1", 'Salary', bold)
today_date = datetime.date.today()

for i,rol in enumerate(position_list):
    # Write the values from positions, with row/column notation.
    worksheet.write(i+1, 0, rol[0])
    worksheet.write(i+1, 1, rol[1])
    worksheet.write(i+1, 2, ' ')
    worksheet.write(i+1, 3, ' ')
    worksheet.write(i+1, 4, today_date)
    worksheet.write(i+1, 5, today_date)
    worksheet.write(i+1, 6, ' ')
    worksheet.write(i+1, 7, ' ')

# Insert an image.
#worksheet.insert_image("B5", "logo.png")

workbook.close()

pyautogui.alert('Termino la busqueda de empleo.') # Make an alert box appear and pause the program until OK is clicked.
