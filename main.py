from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import xlrd
import time
from pynput.keyboard import Key, Controller
import pyautogui
import os
import easygui
import sys
import clipboard

driver = webdriver.Chrome()

xPath = easygui.diropenbox("Izaberi folder sa oglasom", "FOLDER", "C:\\")
exPath = xPath + "\\main.xlsx"


keyboard = Controller()
#

# keyboard.press(Key.f11)
# keyboard.release(Key.f11)


#funkcija za interval
def interval(second=0.8):
    time.sleep(second)


driver.get('https://www.kupujemprodajem.com/user.php?action=login&return_url=MTM4MjExOTEx')
email = driver.find_element_by_name("data[email]")
password = driver.find_element_by_name("data[password]")
loginDugme = driver.find_element_by_name('submit[login]')
interval()
email.send_keys("matijas.stakic@gmail.com")
interval()
password.send_keys("matijacar123zy")
password.send_keys(Keys.ENTER)
interval()


try:
    excel = xlrd.open_workbook(exPath)
except FileNotFoundError:
    print("NETACAN FOLDER")
    driver.close()
    easygui.msgbox("NETACAN FOLDER, GASIM", "ERROR")
    sys.exit()

#ucitaj excel sheet
excelSheet = excel.sheet_by_index(0)

predmetOglasa = excelSheet.cell(0,0).value
pPredmetOglasa = driver.find_element_by_id("data[group_suggest_text]")
interval()
pPredmetOglasa.send_keys(predmetOglasa)
interval()

pStvar = driver.find_element_by_id('data[ad_kind]goods')
pStvar.click()
interval()

#DEFINISANJE KATEGORIJA
kategorije = {"kompjuterDesktop": driver.find_element_by_xpath("//div[@data-value='10']"),
              "kompjuterLaptop" : driver.find_element_by_xpath("//div[@data-value='1221']"),}


#IZBOR KATEGORIJA
vKategorija = excelSheet.cell(1,0).value
kategorija = kategorije[vKategorija]
kategorija.click()
print("kategorija : " + str(kategorija))
interval()

#DEFINISANJE GRUPA
grupe = {"mrezniUredjaji" : driver.find_element_by_xpath("//div[@data-value='105']"),
         "modemiRuteri": driver.find_element_by_xpath("//div[@data-value='95']"),
         "webKamere": driver.find_element_by_xpath("//div[@data-value='104']"),}

#IZBOR GRUPA
vGrupa = excelSheet.cell(2,0).value
grupa = grupe[vGrupa]
grupa.click()
print("grupa :  " + str(grupa))
time.sleep(1)

#DEFINISANJE STANJA
stanja = {"kaoNovo" : driver.find_element_by_id("data[condition]as-new"),
          "korisceno" : driver.find_element_by_id("data[condition]used"),
          "osteceno" : driver.find_element_by_id("data[condition]damaged"), }

#IZBOR STANJA
vStanje = excelSheet.cell(3,0).value
stanje = stanja[vStanje]
stanje.click()
print("stanje :  " + str(stanje))
interval()


#
# LOOP
# ZA
# CENU
#



#MENI ZA DOGOVOR, KONTAKT ETC.
vDog = excelSheet.cell(4,0).value
vDog = str(vDog)
if vDog == "/":
    #IZBOR CENE
    vCena = excelSheet.cell(5,0).value
    pCena = driver.find_element_by_name("data[price]")
    pCena.send_keys(int(vCena))
    print("cena :  " + str(vCena))
    interval()

    #DEFINISANJE VALUTE
    valute = {"evro" : driver.find_element_by_id("currency_eur"),
              "din" : driver.find_element_by_id("currency_rsd"), }

    #IZBOR VALUTE
    vValuta = excelSheet.cell(6,0).value
    pValuta = valute[vValuta]
    pValuta.click()

    #IZBOR FIKSNO/NE
    vFiksno = excelSheet.cell(7,0).value
    vFiksno = str(vFiksno)
    pFiksno = driver.find_element_by_id("data[price_fixed]")
    if vFiksno == "fiksno":
        pFiksno.click()
else:
    pDogMeni = driver.find_element_by_xpath("//span[contains(text(),'ili sledeći opis')]")
    pDogMeni.click()
    dogMeniIzbor = {"dogovor" : driver.find_element_by_xpath("//div[@data-value='Dogovor']"),
                    "kontakt" : driver.find_element_by_xpath("//div[@data-value='Kontakt']"),
                    "pozvati" : driver.find_element_by_xpath("//div[@data-value='Pozvati']"), }
    dog = dogMeniIzbor[vDog]
    dog.click()
    print("dog :  " + str(dog))
    interval()

#ZAMENA NE/DA
vZamena = excelSheet.cell(8,0).value
pZamena = driver.find_element_by_id("exchange_yes")
if vZamena != "/":
    pZamena.click()

#KOPIRAJ OPIS
# def paste_keys(self, pOpis, vOpis):
#     os.system("echo %s| clip" % vOpis.strip())
#     el = self.driver.find_element_by_xpath(pOpis)
#     el.send_keys(Keys.CONTROL, 'v')


fOpis = open(xPath + "\\opis.txt", 'r+')
vOpis = str(fOpis.read())
print(vOpis)
interval()
clipboard.copy(vOpis)
pOpis = driver.find_element_by_xpath("//iframe[@id='data[description]_ifr']")
pOpis.click()
with keyboard.pressed(Key.ctrl):
    keyboard.press('v')
interval()



#IZABERI GRAD I TELEFON
telefon = "0616344878"
ime = "Nikola Radisic"
# pGrad = driver.find_element_by_xpath(("//div[@action-name='choice-options-insert']"))
# pGrad = driver.find_element_by_class_name("uiMenuButtonInner")
# pGrad = driver.find_element_by_xpath("//span[contains(text(),'Izaberite')]")
pGrad = driver.find_element_by_id("locationInsertSpot")
driver.execute_script("arguments[0].click();", pGrad)
pGrad.click()
interval()
# grad = driver.find_element_by_xpath("//div[@data-value='1']")

# interval()
# pBroj = driver.find_element_by_id("phone_number")
# pBroj.send_keys(telefon)
# interval()
# pIme = driver.find_element_by_id("data[owner]")
# pIme.send_keys(ime)
# interval()
#
# pDugmeSledece = driver.find_element_by_xpath("//input[@action-name='adInfoNextButton']")
# driver.execute_script("arguments[0].click();", pDugmeSledece)



# time.sleep(5)
# driver.close()

