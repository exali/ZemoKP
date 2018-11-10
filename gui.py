import easygui as gui
import csv
import os
import xlsxwriter

path_kat = "C:\\Users\\stakic\\Desktop\\SAV_XLSX\\PODACI_SVI_KATEGORIJE.csv"
path_grupe = "C:\\Users\\stakic\\Desktop\\SAV_XLSX\\PODACI_SVI_GRUPE.csv"
file_kat = open(path_kat, newline='', encoding="utf8")
file_grupe = open(path_grupe, newline='', encoding="utf8")
reader_grupe = csv.reader(file_grupe)
reader_kat = csv.reader(file_kat)


zamena_izbori = ["zamena", "ne"]
fiksno_izbori = ["fiksno", "ne"]
valute_izbori = ["evro", "din"]
dog_izbori = ["/", "dogovor", "kontakt", "pozvati"]
stanja = ["kaoNovo", "korisceno", "osteceno"]

kat_imena = []
kat_values = []

grupe_imena = []
grupe_values = []

for row in reader_kat:
    ime = row[0]
    value = row[1]
    kat_imena.append(ime)
    kat_values.append(value)

kat_dict = dict(zip(kat_imena, kat_values))

print(kat_dict)

for row in reader_grupe:
    ime = row[0]
    value = row[1]
    grupe_imena.append(ime)
    grupe_values.append(value)

grupe_dict = dict(zip(grupe_imena, grupe_values))

print(grupe_dict)
print(grupe_imena)
print(grupe_values)


def ispisi():
    potrebni_podaci = []
    if dog_choice == "/":
        potrebni_podaci = [kat_choice_value, grupa_choice_value, stanje_choice, "/", cena_choice, valuta_choice,
                           fiksno_choice, zamena_choice]
        print(potrebni_podaci)

    elif dog_choice != "/":
        potrebni_podaci = [kat_choice_value, grupa_choice_value, stanje_choice, dog_choice, "", "", "", zamena_choice]
        print(potrebni_podaci)
    file = open(path_oglasa + "\\opis.txt", "w+")
    file.write(opis_tekst)
    file.close()

    odluka_box = gui.buttonbox(msg="Potvrdi:", choices=["Ponovi oglas", "Nastavi drugi oglas"])
    if odluka_box == 1:
        # write to excel

        workbook = xlsxwriter.Workbook(path_oglasa + '\\main.xlsx')
        worksheet = workbook.add_worksheet()
        row = 0
        for vrednost in potrebni_podaci:
            worksheet.write(row, 0, vrednost)
            row += 1
        workbook.close()
        ponoviOglas(False)
    elif odluka_box == 0:
        ponoviOglas(True)

def kreiraj(path_oglasa):
    global file
    global kat_choice_value
    global grupa_choice_value
    global stanje_choice
    global opis_tekst
    global dog_choice
    global cena_choice
    global valuta_choice
    global fiksno_choice
    global zamena_choice
    global poslednja_provera
    global poslednji_box
    global opis_tekst
    predmet_oglasa = os.path.basename(path_oglasa)
    kat_choice = gui.choicebox(msg="Izaberi kategoriju", title=predmet_oglasa, choices=kat_imena)
    kat_choice_value = kat_dict[kat_choice]
    print(kat_choice)
    print(kat_choice_value)

    # DODAJ INPUT ZA XLSX FAJL (0,0)

    grupa_choice = gui.choicebox(msg="Izaberi grupu", choices=grupe_imena, title=predmet_oglasa)
    grupa_choice_value = grupe_dict[grupa_choice]

    print(grupa_choice)
    print(grupa_choice_value)

    # DODAJ INPUT ZA XLSX FAJL (1,0)

    stanje_choice = gui.choicebox(msg="Izaberi stanje", choices=stanja, title=predmet_oglasa)

    print(stanje_choice)

    # DODAJ INPUT ZA XLSX FAJL (2,0)\
    file = open(path_oglasi_folder + "\\opis.txt", "w+")
    opis_tekst = gui.enterbox(msg="Nalepi opis:")
    file.write(opis_tekst)
    file.close()

    dog_choice = gui.choicebox(msg="Dogovor/kontakt/pozvati", choices=dog_izbori, title=predmet_oglasa)

    print(dog_choice)
    # DODAJ INPUT ZA XLSX FAJL (3,0)

    if dog_choice == "/":
        cena_choice = gui.enterbox(msg="Cena:")
        valuta_choice = gui.choicebox(msg="Valuta:", choices=valute_izbori, title=predmet_oglasa)
        fiksno_choice = gui.buttonbox(msg="Fiksno?", choices=fiksno_izbori, title=predmet_oglasa)
        zamena_choice = gui.buttonbox(msg="Zamena?", choices=zamena_izbori, title=predmet_oglasa)
        print(cena_choice)
        print(valuta_choice)
        print(fiksno_choice)
        poslednja_provera = [kat_choice, grupa_choice, stanje_choice, opis_tekst, cena_choice, valuta_choice,
                             fiksno_choice, zamena_choice]
    else:
        zamena_choice = gui.buttonbox(msg="Zamena?", choices=zamena_izbori, title=predmet_oglasa)
        poslednja_provera = [kat_choice, grupa_choice, stanje_choice, opis_tekst, dog_choice, zamena_choice]

    print(zamena_choice)
    poslednja_provera = '\n'.join(poslednja_provera)
    poslednji_box = gui.textbox(msg="proveri podatke:", text=poslednja_provera, title=predmet_oglasa)

def main(repeat):

    global path_oglasi_folder
    global oglasi
    global izabrani_oglasi
    global svi_oglasi
    global path_oglasa
    global trenutni_index
    global svi_oglasi
    path_oglasi_folder = gui.diropenbox("Izaberi folder sa oglasima", "FOLDER", "C:\\Users\\stakic\\Desktop\\SAV_XLSX\\")
    svi_oglasi = os.listdir(path_oglasi_folder)
    izabrani_oglasi = gui.multchoicebox(msg="Izaberi sve oglase koje zelis da kreiras:", choices=svi_oglasi)
    pisi_oglase = '\n'.join(izabrani_oglasi)
    print(izabrani_oglasi)
    gui.textbox(msg="Proveri izabrane oglase:", text=pisi_oglase)
    nastavi_box = gui.ccbox(msg="Nastavi?", choices=["Da", "Ne"])
    while nastavi_box == False:
        main(True)
    if repeat == False:
        ponoviOglas(False)


def ponoviOglas(repeat):
    global path_oglasa
    for oglas in izabrani_oglasi:
        path_oglasa = path_oglasi_folder + "\\" + oglas
        if repeat == False:
            kreiraj(path_oglasa)
            ispisi()
        if repeat == True:
            while repeat == True:
                kreiraj(path_oglasa)
                ispisi()


main(False)










