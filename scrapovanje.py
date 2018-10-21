import os
import sys
import xlsxwriter
import time
from bs4 import BeautifulSoup as BS

xPath = 'C:\\Users\\stakic\\Desktop\\SAV_HTML'

htmls = []


def extractKeys():
    global row
    global col
    row = 0
    col = 0
    for key in SVE.keys():
        worksheet.write(row, col, key)
        row += 1


def extractValues():
    row = 0
    col = 3

    for value in SVE.values():
        worksheet.write(row, col, value)
        row += 1


for root, dirs, files in os.walk(xPath):
    for filename in files:
        if filename.endswith('.html'):
            htmls.append(filename)

htmlPaths = []
for html in htmls:
    html = xPath + "\\" + html
    htmlPaths.append(html)

print(htmlPaths)
time.sleep(2)

savTekst = []
savValue = []

counter = 0
for path in htmlPaths:

    soup = BS(open(path, encoding='utf-8'),'html.parser')
    for div in soup.findAll('div', class_='uiMenuItem'):
        # print(str(div.get('data-text')) + "   " +str(div.get('data-value')))
        data_tekst = str(div.get('data-text'))
        savTekst.append(data_tekst)

        data_value = str(div.get('data-value'))
        savValue.append(data_value)
    SVE = dict(zip(savTekst, savValue))
    print(SVE)

    workbook = xlsxwriter.Workbook("C:\\Users\\stakic\\Desktop\\SAV_XLSX\\cigan2.xlsx")
    worksheet = workbook.add_worksheet()


    extractValues()
    extractKeys()
    workbook.close()



