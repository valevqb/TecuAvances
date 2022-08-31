from fileinput import filename
import json
import os
import matplotlib.pyplot as plt
import numpy as np

#verifica contenido y elimina el reemplazo en donde no hay letras
def isLetter(word):
    counter = 0;
    while(counter != len(word)):
        if(word[counter].isalpha() == False):
            return word[0:counter];
        counter += 1;
    return word;

def runChanges (fileName):
    data = {};
    dictionary = {}; #diccionario de contenidos

    with open('data.json',encoding="utf-8") as file: #abre el archivo json con tildes
        data = json.load(file);

        for neutral in data['datos']: #agrega los datos
            for abc in neutral:
                dictionary = dict (dictionary,**neutral[abc])

    #print("Write the file name:");
    #fileName = input();

    texts = open (fileName, encoding="utf-8");

    contents = texts.read(); #contenido del texto
    contents = contents.lower();

    changedWords = [];
    replacesNum = 0;
    for word in contents.split(' '): #recorrer texto por palabras
        word2 = isLetter(word);
        #print(word2)
        for key in dictionary: #recorrer diccionario
            if(word2[0:len(word2)-2] == key and word2[0:len(word2)-2] != ""): #si la palabra es igual a la llave
                changedWords.append(word2);
                lists = dictionary[key];
                replacesNum += 1;
                contents = contents.replace(word2,lists[0]);
    return(replacesNum)

    texts.close;

    name = fileName.split('\\')
    name = name[-1]

    texts = open ('nuevos\\' + name[0:len(name)-4] + 'Cambio' + '.txt', 'w', encoding="utf-8");

    contents = contents + '\n\n' + 'File name: ' + fileName + '\nNumber of changes: ' + str(replacesNum) + '\n';
    contents = contents + "Palabras reemplazadas: " + ', '.join(changedWords);

    #print(contents);
    #print(contentsCopy);

    texts.write(contents);

    texts.close;

#Prueba 1
CARPETA = 'C:\\Users\\tania\\OneDrive\\Documentos\\GitHub\\TecuAvances\\txt';
#CARPETA = 'C:\\Users\\valev\\Documents\\GitHub\\TecuAvances\\txt';

listArc = os.listdir(CARPETA); #lee todos los archivos en la carpeta
listaDeCambios = [];


for list in listArc: #recorre uno a uno los archivos de la carpeta
    #runChanges('C:\\Users\\valev\\Documents\\GitHub\\TecuAvances\\txt\\'+list);
    listaDeCambios.append(runChanges('C:\\Users\\tania\\OneDrive\\Documentos\\GitHub\\TecuAvances\\txt\\'+list));
#listaDeCambios.sort()
#print(listaDeCambios)


#Se genera la gráfica
y = listaDeCambios;
x = [];

for i in range (len(listaDeCambios)):
    x.append(i+1)
 

#print(len(x)) 
#print(len(y))


plt.plot(x,y);

plt.show();
