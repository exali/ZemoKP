import xlrd
import xlsxwriter
import easygui


excel = xlrd.open_workbook("C:\\Users\\stakic\\Desktop\\SAV_XLSX\\SVE.xlsx")
excelSheet = excel.sheet_by_index(0)

counter = 0
col = 3
row = 0
grupe = []
for grupa in excelSheet.col(3):
        grupe.append(grupa.value)

savLink = []

for grupa in grupe:
    link = "//div[@data-value='" + grupa + "']"
    ceoData = "driver.find_element_by_xpath(" + '"' + link + '"'")"
    savLink.append(ceoData)

print(savLink)

workbook = xlsxwriter.Workbook("C:\\Users\\stakic\\Desktop\\SAV_XLSX\\SVE_DATA.xlsx")
worksheet = workbook.add_worksheet()

row = 0
for link in savLink:
    col = 3
    worksheet.write(row, col, link)
    row += 1

row = 0
for grupa in grupe:
    col = 0
    worksheet.write(row, col, grupa)
    row += 1

workbook.close()




