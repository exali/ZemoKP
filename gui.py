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

repeat = 0


def main():
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
    global path_oglas_folder
    if repeat == 0:
        path_oglas_folder = gui.diropenbox("Izaberi folder sa oglasom", "FOLDER", "C:\\Users\\stakic\\Desktop\\SAV_XLSX\\")

    predmet_oglasa = os.path.basename(path_oglas_folder)
    kat_choice = gui.choicebox(msg="Izaberi kategoriju", title=predmet_oglasa, choices=kat_imena)
    kat_choice_value = kat_dict[kat_choice]
    print(kat_choice)
    print(kat_choice_value)

    #DODAJ INPUT ZA XLSX FAJL (0,0)

    grupa_choice = gui.choicebox(msg="Izaberi grupu", choices=grupe_imena)
    grupa_choice_value = grupe_dict[grupa_choice]

    print(grupa_choice)
    print(grupa_choice_value)

    #DODAJ INPUT ZA XLSX FAJL (1,0)

    stanje_choice = gui.choicebox(msg="Izaberi stanje", choices=stanja)

    print(stanje_choice)

    #DODAJ INPUT ZA XLSX FAJL (2,0)\

    opis_tekst = gui.enterbox(msg="Nalepi opis:")


    dog_choice = gui.choicebox(msg="Dogovor/kontakt/pozvati", choices=dog_izbori)

    print(dog_choice)
    #DODAJ INPUT ZA XLSX FAJL (3,0)



    if dog_choice == "/":
        cena_choice = gui.enterbox(msg="Cena:")
        valuta_choice = gui.choicebox(msg="Valuta:", choices=valute_izbori)
        fiksno_choice = gui.buttonbox(msg="Fiksno?", choices=fiksno_izbori)
        zamena_choice = gui.buttonbox(msg="Zamena?", choices=zamena_izbori)
        print(cena_choice)
        print(valuta_choice)
        print(fiksno_choice)
        poslednja_provera = [kat_choice, grupa_choice, stanje_choice, opis_tekst, cena_choice, valuta_choice, fiksno_choice, zamena_choice]
    else:
        zamena_choice = gui.buttonbox(msg="Zamena?", choices=zamena_izbori)
        poslednja_provera = [kat_choice, grupa_choice, stanje_choice, opis_tekst, dog_choice, zamena_choice]


    print(zamena_choice)
    poslednja_provera = '\n'.join(poslednja_provera)
    poslednji_box = gui.textbox(msg="proveri podatke:", text=(poslednja_provera))
main()

potrebni_podaci = []
if dog_choice == "/":
    potrebni_podaci = [kat_choice_value, grupa_choice_value, stanje_choice, "/", cena_choice, valuta_choice, fiksno_choice, zamena_choice]
    print(potrebni_podaci)

elif dog_choice != "/":
    potrebni_podaci = [kat_choice_value, grupa_choice_value, stanje_choice, dog_choice, "", "", "", zamena_choice]
    print(potrebni_podaci)

odluka_box = gui.buttonbox(msg="Potvrdi:", choices=["Ponovi oglas", "Nastavi drugi oglas"])
if odluka_box == "Nastavi drugi oglas":
    #write to excel

    workbook = xlsxwriter.Workbook(path_oglas_folder + '\\main.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    for vrednost in potrebni_podaci:
        worksheet.write(row, 0, vrednost)
        row += 1
    workbook.close()
    repeat = 0

    main()
elif odluka_box == "Ponovi oglas":
    repeat = 1
    main()








