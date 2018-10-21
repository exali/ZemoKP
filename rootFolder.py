from bs4 import BeautifulSoup as BS
import xlsxwriter
import easygui

xPath = easygui.fileopenbox("Izaberi folder sa oglasom", "FOLDER", "C:\\Users\\stakic\\Desktop\\")
soup = BS(open(xPath, encoding='utf-8'), 'html.parser')
print(soup)

# print(match)
savTekst=[]
savValue=[]

for div in soup.findAll('div', class_='uiMenuItem'):
    # print(str(div.get('data-text')) + "   " +str(div.get('data-value')))
    data_tekst = str(div.get('data-text'))
    savTekst.append(data_tekst)

    data_value = str(div.get('data-value'))
    savValue.append(data_value)

print(savTekst)
print(savValue)

SVE = dict(zip(savTekst, savValue))
print(SVE)

excelPath = easygui.fileopenbox("Izaberi folder sa oglasom", "FOLDER", "C:\\Users\\stakic\\Desktop\\")

def extractKeys():
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

extractKeys()
extractValues()
workbook.close()


