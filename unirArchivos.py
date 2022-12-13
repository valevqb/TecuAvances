from fileinput import filename
import json
import os

def runChanges (fileName):
    texts = open (fileName, encoding="utf-8");

    contents = texts.read(); #contenido del texto
    contents = contents.lower();

    #print(contents);

    return contents;

def isLetter(word):
    counter = 0;
    while(counter != len(word)):
        if(word[counter].isalpha() == False):
            return word[0:counter];
        counter += 1;
    return word;

#####Inicio Main#####
#####Inicio Main#####
#####Inicio Main#####

final = "";

CARPETA = ['C:\\Users\\valev\\Documents\\GitHub\\TecuAvances\\hoyeneltec\\2022',
           'C:\\Users\\valev\\Documents\\GitHub\\TecuAvances\\hoyeneltec\\2021',
           'C:\\Users\\valev\\Documents\\GitHub\\TecuAvances\\hoyeneltec\\2020',
           'C:\\Users\\valev\\Documents\\GitHub\\TecuAvances\\hoyeneltec\\2019',
           'C:\\Users\\valev\\Documents\\GitHub\\TecuAvances\\hoyeneltec\\2018',
           'C:\\Users\\valev\\Documents\\GitHub\\TecuAvances\\hoyeneltec\\2016',
           'C:\\Users\\valev\\Documents\\GitHub\\TecuAvances\\hoyeneltec\\2015',
           'C:\\Users\\valev\\Documents\\GitHub\\TecuAvances\\hoyeneltec\\2014'];

for e in CARPETA:
    print("avanza");
    listArc = os.listdir(e); #lee todos los archivos en la carpeta
    for list in listArc: #recorre uno a uno los archivos de la carpeta
        final = final + runChanges(e + '\\' + list);
    
texts = open("datosUnidos.txt", "w", encoding="utf-8");
texts.write(final);
texts.close;

