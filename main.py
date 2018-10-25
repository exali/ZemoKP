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
import keyboard

# keyboard.press(Key.f11)
# keyboard.release(Key.f11)

#funkcija za interval
def interval(second=0.8):
    time.sleep(second)

def dugmeSledece():
    pDugmeSledece = driver.find_element_by_xpath("//input[@action-name='adInfoNextButton']")
    driver.execute_script("arguments[0].select();", pDugmeSledece)
    driver.execute_script("arguments[0].click();", pDugmeSledece)


def glavni():
    xPath = easygui.diropenbox("Izaberi folder sa oglasom", "FOLDER", "D:\\GIT_PROJEKTI\\")

    keyboard = Controller()
    #
    try:
        exPath = xPath + "\\main.xlsx"
        excel = xlrd.open_workbook(exPath)
    except FileNotFoundError:
        print("NETACAN FOLDER")
        easygui.msgbox("NETACAN FOLDER, GASIM", "ERROR")
        sys.exit()

    global driver
    driver = webdriver.Chrome("chromedriver.exe")

    driver.get('https://www.kupujemprodajem.com/user.php?action=login&return_url=MTM4MjExOTEx')
    email = driver.find_element_by_name("data[email]")
    password = driver.find_element_by_name("data[password]")
    interval()
    email.send_keys("nradisic84@gmail.com")
    interval()
    password.send_keys("nikola1984")
    password.send_keys(Keys.ENTER)
    interval()


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


    #IZBOR KATEGORIJA
    vKategorija = int(excelSheet.cell(1,0).value)
    vKategorija = str(vKategorija)
    kategorija = driver.find_element_by_xpath("//div[@data-value='" + vKategorija + "']")
    interval()
    print(kategorija)
    kategorija.click()
    interval()
    #DEFINISANJE GRUPA


    #IZBOR GRUPA
    vGrupa = int(excelSheet.cell(2,0).value)
    # print(vGrupa)
    # if vKategorija == "kompjuterDesktop":
    #     grupe = {"mrezniUredjaji": driver.find_element_by_xpath("//div[@data-value='105']"),
    #                "modemiRuteri": driver.find_element_by_xpath("//div[@data-value='95']"),
    #                "webKamere": driver.find_element_by_xpath("//div[@data-value='104']"),
    #              }
    # elif vKategorija == "kompjuterLaptop":
    #     grupe = {"laptAdapt": driver.find_element_by_xpath("//div[@data-value='2285']"),
    #              "laptDOprema": driver.find_element_by_xpath("//div[@data-value='1235']"),
    #              }
    # else:
    #     easygui.msgbox("PRAZNO/NETACNO POLJE SA KATEGORIJAMA")
    #     sys.exit()
    vGrupa = str(vGrupa)
    grupa = driver.find_element_by_xpath("//div[@data-value='" + vGrupa + "']")
    grupa.click()
    # grupa = grupe[vGrupa]
    # grupa.click()
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
        pDogMeni = driver.find_element_by_xpath("//span[contains(text(),'Ili umesto cene')]")
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


    fOpis = open(xPath + "\\opis.txt", 'r+')
    vOpis = str(fOpis.read())
    print(vOpis)
    interval()
    clipboard.copy(vOpis)
    pOpis = driver.find_element_by_xpath("//iframe[@id='data[description]_ifr']")
    pOpis.click()
    interval()
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
    interval()

    #lista slika
    slike = []

    for root, dirs, files in os.walk(xPath):
        for filename in files:
            if filename.endswith(('.jpg', '.jpeg', '.gif', '.png')):
                slike.append(filename)

    interval()
    pSlika = driver.find_element_by_xpath("//input[@id='upload_file']")

    for slika in slike:
        slika = xPath + "\\" + slika
        pSlika.send_keys(slika)
    interval(10)

    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("//input[@action-name='adPromoNextButton']"))
    interval(2)

    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("//input[@action-name='adPromoNextButton']"))
    interval(2)

    pDugmeGarant = driver.find_element_by_id("swear_yes")
    pDugmePrihvatam = driver.find_element_by_id("accept_yes")

    pDugmeGarant.click()
    pDugmePrihvatam.click()

glavni()
izbor = easygui.indexbox(msg='Nastaviti?', title=' ', choices=('Yes', 'No'), image=None, default_choice='Yes', cancel_choice='No')
print(izbor)
if izbor == 1:
    driver.close()
    sys.exit(0)
elif izbor == 0:
    driver.close()
    glavni()



# pPostaviOglas = driver.find_element_by_name("submit[post]")
# pPostaviOglas.click()

# time.sleep(5)
# driver.close()

