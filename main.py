from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlrd
import time
from pynput.keyboard import Key, Controller
import os
import easygui
import sys
import clipboard
import pickle

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
    x_path = easygui.diropenbox("Izaberi folder sa oglasom", "FOLDER", "D:\\GIT_PROJEKTI\\")

    keyboard = Controller()
    #
    try:
        ex_path = x_path + "\\main.xlsx"
        excel = xlrd.open_workbook(ex_path)
    except FileNotFoundError:
        print("NETACAN FOLDER")
        easygui.msgbox("NETACAN FOLDER, GASIM", "ERROR")
        sys.exit()
    global driver
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.google.com")
    for cookie in pickle.load(open("cookies.pkl", "rb")):
        driver.add_cookie(cookie)
    driver.get('https://www.kupujemprodajem.com')
    # driver.get('https://www.kupujemprodajem.com/user.php?action=login&data[remember]=0')
    # email = driver.find_element_by_name("data[email]")
    # password = driver.find_element_by_name("data[password]")
    # interval()
    # email.send_keys("nradisic84@gmail.com")
    # interval()
    # password.send_keys("nikola1984")
    # password.send_keys(Keys.ENTER)
    interval()
    driver.get('https://www.kupujemprodajem.com/oglasi.php?action=new')

    #ucitaj excel sheet
    excel_sheet = excel.sheet_by_index(0)

    predmet_oglasa = os.path.basename(x_path)
    p_predmet_oglasa = driver.find_element_by_id("data[group_suggest_text]")
    interval()
    p_predmet_oglasa.send_keys(predmet_oglasa)
    interval()

    p_stvar = driver.find_element_by_id('data[ad_kind]goods')
    p_stvar.click()
    interval()

    #DEFINISANJE KATEGORIJA


    #IZBOR KATEGORIJA
    v_kategorija = int(excel_sheet.cell(1,0).value)
    v_kategorija = str(v_kategorija)
    kategorija = driver.find_element_by_xpath("//div[@data-value='" + v_kategorija + "']")
    interval()
    print(kategorija)
    kategorija.click()
    interval()
    #DEFINISANJE GRUPA


    #IZBOR GRUPA
    v_grupa = int(excel_sheet.cell(2,0).value)
    print(v_grupa)
    v_grupa = str(v_grupa)
    grupa = driver.find_element_by_xpath("//div[@data-value='" + v_grupa + "']")
    grupa.click()
    # grupa = grupe[v_grupa]
    # grupa.click()
    print("grupa :  " + str(grupa))
    interval(1)

    #DEFINISANJE STANJA
    stanja = {"kaoNovo" : driver.find_element_by_id("data[condition]as-new"),
              "korisceno" : driver.find_element_by_id("data[condition]used"),
              "osteceno" : driver.find_element_by_id("data[condition]damaged"), }

    #IZBOR STANJA
    v_stanje = excel_sheet.cell(3,0).value
    stanje = stanja[v_stanje]
    interval()
    stanje.click()
    print("stanje :  " + str(stanje))
    interval()


    #
    # LOOP
    # ZA
    # CENU
    #



    #MENI ZA DOGOVOR, KONTAKT ETC.
    v_dog = excel_sheet.cell(4,0).value
    v_dog = str(v_dog)
    if v_dog == "/":
        #IZBOR CENE
        v_cena = excel_sheet.cell(5,0).value
        p_cena = driver.find_element_by_name("data[price]")
        p_cena.send_keys(int(v_cena))
        print("cena :  " + str(v_cena))
        interval()

        #DEFINISANJE VALUTE
        valute = {"evro" : driver.find_element_by_id("currency_eur"),
                  "din" : driver.find_element_by_id("currency_rsd"), }

        #IZBOR VALUTE
        v_valuta = excel_sheet.cell(6,0).value
        p_valuta = valute[v_valuta]
        p_valuta.click()

        #IZBOR FIKSNO/NE
        v_fiksno = excel_sheet.cell(7,0).value
        v_fiksno = str(v_fiksno)
        p_fiksno = driver.find_element_by_id("data[price_fixed]")
        if v_fiksno == "fiksno":
            p_fiksno.click()
    else:
        p_dog_meni = driver.find_element_by_xpath("//span[contains(text(),'Ili umesto cene')]")
        p_dog_meni.click()
        dogMeniIzbor = {"dogovor" : driver.find_element_by_xpath("//div[@data-value='Dogovor']"),
                        "kontakt" : driver.find_element_by_xpath("//div[@data-value='Kontakt']"),
                        "pozvati" : driver.find_element_by_xpath("//div[@data-value='Pozvati']"), }
        dog = dogMeniIzbor[v_dog]
        dog.click()
        print("dog :  " + str(dog))
        interval()

    #ZAMENA NE/DA
    v_zamena = excel_sheet.cell(8,0).value
    p_zamena = driver.find_element_by_id("exchange_yes")
    if v_zamena != "/":
        p_zamena.click()


    f_opis = open(x_path + "\\opis.txt", 'r+')
    v_opis = str(f_opis.read())
    print(v_opis)
    interval()
    clipboard.copy(v_opis)
    p_opis = driver.find_element_by_xpath("//iframe[@id='data[description]_ifr']")
    p_opis.click()
    interval()
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
    interval()

    #lista slika
    slike = []

    for root, dirs, files in os.walk(x_path):
        for filename in files:
            if filename.endswith(('.jpg', '.jpeg', '.gif', '.png')):
                slike.append(filename)

    interval()
    p_slika = driver.find_element_by_xpath("//input[@id='upload_file']")

    for slika in slike:
        slika = x_path + "\\" + slika
        p_slika.send_keys(slika)
    interval(10)

    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("//input[@action-name='adPromoNextButton']"))
    interval(2)

    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("//input[@action-name='adPromoNextButton']"))
    interval(2)

    p_dugme_garant = driver.find_element_by_id("swear_yes")
    p_dugme_prihvatam = driver.find_element_by_id("accept_yes")

    p_dugme_garant.click()
    p_dugme_prihvatam.click()

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

