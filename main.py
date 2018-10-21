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






# options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=C:\\Users\\stakic\\AppData\\Local\\Google\\Chrome\\User%20Data") #Path to your chrome profile
# driver = webdriver.Chrome(chrome_options=options)
# keyboard.press(Key.f11)
# # keyboard.release(Key.f11)

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
    except FileNotFoundError or TypeError:
        print("NETACAN FOLDER")
        easygui.msgbox("NETACAN FOLDER, GASIM", "ERROR")
        sys.exit()

    global driver
    driver = webdriver.Chrome("D:\\GIT_PROJEKTI\\chromedriver.exe")

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
    vKategorija = excelSheet.cell(1,0).value
    kategorija = kategorije[vKategorija]
    kategorija.click()
    vKategorija = str(vKategorija)
    interval()
    print("kategorija : " + str(kategorija))
    interval()

    #DEFINISANJE GRUPA


    #IZBOR GRUPA
    vGrupa = str(excelSheet.cell(2,0).value)
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
    interval(8)



    # #IZABERI GRAD I TELEFON
    # telefon = "0616344878"
    # ime = "Nikola Radisic"

    # pGrad = driver.find_element_by_id("locationInsertSpot")
    # pGrad.click()
    # interval()
    # grad = driver.find_element_by_xpath("//div[@data-text='Beograd']")
    # driver.execute_script("arguments[0].click();", grad)
    # interval()
    #
    # pIme = driver.find_element_by_id("data[owner]")
    # pIme.clear()
    # pIme.send_keys(ime)
    #
    # interval()
    # pBroj = driver.find_element_by_id("phone_number")
    # pBroj.send_keys(telefon)
    # dugmeSledece()
    # interval(1)

    pVidljivost = driver.find_element_by_class_name("col-greedy")
    interval()
    driver.execute_script("arguments[0].click();", pVidljivost)
    print("yes")
    interval(1)


    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("//input[@action-name='adPromoNextButton']"))
    interval(1)

    # pVaseIme = driver.find_element_by_id("personEdit")
    # pVasePrezime = driver.find_element_by_id("personLastNameEdit")
    # pMesto = driver.find_element_by_name("data[d_person_location]")
    # pUliBroj = driver.find_element_by_name("data[d_person_address]")
    # pJMBG = driver.find_element_by_name("data[d_jmbg]")
    # pBrLK = driver.find_element_by_name("data[d_id_card_number]")
    # pIzdLK = driver.find_element_by_name("data[d_id_card_location]")
    #
    # pVaseIme.send_keys("Nikola")
    # pVasePrezime.send_keys("Radisic")
    # pMesto.send_keys("Beograd")
    # pUliBroj.send_keys("Stare Porte 1")
    # pJMBG.send_keys("123453221")
    # pBrLK.send_keys("1235533")
    # pIzdLK.send_keys("Kragujevac")
    # interval()

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

# dugmeSubmit = driver.find_element_by_xpath("//input[@value=' Sledeće ']")
# driver.execute_script("arguments[0].click();", dugmeSubmit)
# interval()

# time.sleep(5)
# driver.close()

