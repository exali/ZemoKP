import easygui as gui
import csv

path_kat = "C:\\Users\\stakic\\Desktop\\SAV_XLSX\\PODACI_SVI_KATEGORIJE.csv"
path_grupe = "C:\\Users\\stakic\\Desktop\\SAV_XLSX\\PODACI_SVI_GRUPE.csv"
file_kat = open(path_kat, newline='', encoding="utf8")
file_grupe = open(path_grupe, newline='', encoding="utf8")
reader_grupe = csv.reader(file_grupe)
reader_kat = csv.reader(file_kat)

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


path_oglas_folder = gui.diropenbox("Izaberi folder sa oglasom", "FOLDER", "C:\\Users\\stakic\\Desktop\\SAV_XLSX\\")
kat_choice = gui.choicebox(msg="Izaberi kategoriju", choices=kat_imena)

kat_choice_value = kat_dict[kat_choice]
print(kat_choice)
print(kat_choice_value)

grupa_choice = gui.choicebox(msg="Izaberi grupu", choices=grupe_imena)
grupa_choice_value = grupe_dict[grupa_choice]

print(grupa_choice)
print(grupa_choice_value)



