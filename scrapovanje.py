import re
from bs4 import BeautifulSoup as bs
import urllib.request
import unicodecsv as csv

response = urllib.request.urlopen("https://nikolaradisic.kpizlog.rs/")
html = response.read()

soup = bs(html, 'html.parser')

def main(vrsta):
    print(type(soup))


    cigan = soup.find_all(href=re.compile(vrsta), text=True)

    lista = []
    for da in cigan:
        print(da.text)
        lista.append(da.text)

    print(lista)

    bosko = csv.list_dialects()
    print(bosko)

    with open("C:\\Users\\stakic\\Desktop\\SAV_HTML\\%s.txt" %(vrsta), "w+", encoding="utf-8") as file:
        for naziv in lista:
            file.write(naziv + "\n")

    file = open("C:\\Users\\stakic\\Desktop\\SAV_HTML\\%s.txt" %(vrsta), "r", encoding="utf-8")
    lines = file.read().splitlines()

    print(lines)

main("kategorija")
main("grupa")



