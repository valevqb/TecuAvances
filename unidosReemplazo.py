from fileinput import filename
import json
import os

def isLetter(word):
    counter = 0;
    while(counter != len(word)):
        if(word[counter].isalpha() == False):
            return word[0:counter];
        counter += 1;
    return word;

def runChanges2 ():
    fileName = "C:\\Users\\valev\\Documents\\GitHub\\TecuAvances\\datosUnidos.txt"

    texts = open (fileName, encoding="utf-8");

    contents = texts.read(); #contenido del texto
    contents = contents.lower();
    listaPalabras = contents.split(' ');

    for index, item in enumerate (listaPalabras):
        #print("palabra");
        #print(item);
        newOne = isLetter(item)
        if(len(newOne) > 3):
            listaPalabras[index] = isLetter(item);
        else:
            del listaPalabras[index];
    
    repeticiones = dict(zip(listaPalabras,map(lambda x: listaPalabras.count(x),listaPalabras)))

    texts.close;

    name = fileName.split('\\')
    name = name[-1]

    texts = open ('UnidosAnalisis.txt', 'w', encoding="utf-8");

    datosFinales = "";

    for palabra in repeticiones:
        #print("Datos finales");
        datosFinales = datosFinales + palabra + ": " + str(repeticiones[palabra]) + "\n"
        

    texts.write(datosFinales);

    texts.close;

runChanges2();
