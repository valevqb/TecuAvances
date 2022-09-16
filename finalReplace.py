from fileinput import filename
import json
import os
import matplotlib.pyplot as plt
import numpy as np

#---------------------------------------------------------------------------------------------------------
# Verifica contenido y elimina el reemplazo en donde no hay letras
#---------------------------------------------------------------------------------------------------------
def isLetter(word):

    counter = 0;

    while(counter != len(word)):

        if(word[counter].isalpha() == False):
            return word[0:counter];

        counter += 1;

    return word;

#---------------------------------------------------------------------------------------------------------
# Aplica los cambios a los archivos
#---------------------------------------------------------------------------------------------------------
def runChanges (fileName):

    data       = {};
    dictionary = {}; #diccionario de contenidos

    with open('data.json',encoding="utf-8") as file: #abre el archivo json con tildes
        data = json.load(file);

        for neutral in data['datos']: #agrega los datos

            for abc in neutral:
                dictionary = dict (dictionary,**neutral[abc])

    #print("Write the file name:");
    #fileName = input();

    texts    = open (fileName, encoding="utf-8");
    contents = texts.read(); #contenido del texto
    contents = contents.lower();

    changedWords = [];
    replacesNum  = 0 ;

    for word in contents.split(' '): #recorrer texto por palabras

        word2 = isLetter(word);
        #print(word2)
        
        for key in dictionary: #recorrer diccionario
            
            if(word2[0:len(word2)-2] == key and word2[0:len(word2)-2] != ""): #si la palabra es igual a la llave
                changedWords.append(word2);
                lists        = dictionary[key];
                replacesNum += 1;
                contents     = contents.replace(word2,lists[0]);

    return(replacesNum)

    texts.close;

    name     = fileName.split('\\')
    name     = name[-1]

    texts    = open ('nuevos\\' + name[0:len(name)-4] + 'Cambio' + '.txt', 'w', encoding="utf-8");

    contents = contents + '\n\n' + 'File name: ' + fileName + '\nNumber of changes: ' + str(replacesNum) + '\n';
    contents = contents + "Palabras reemplazadas: " + ', '.join(changedWords);

    #print(contents);
    #print(contentsCopy);

    texts.write(contents);

    texts.close;

#Prueba 1
CARPETA = 'C:\\Users\\tania\\OneDrive\\Documentos\\GitHub\\TecuAvances\\txt';
#CARPETA = 'C:\\Users\\valev\\Documents\\GitHub\\TecuAvances\\txt';

listArc        = os.listdir(CARPETA); #lee todos los archivos en la carpeta
#print("los archivos en la carpeta: ")
#print(listArc)

listaDeCambios = [];


for list in listArc: #recorre uno a uno los archivos de la carpeta
    #runChanges('C:\\Users\\valev\\Documents\\GitHub\\TecuAvances\\txt\\'+list);
    listaDeCambios.append(runChanges('C:\\Users\\tania\\OneDrive\\Documentos\\GitHub\\TecuAvances\\txt\\'+list));
#listaDeCambios.sort()
#print(listaDeCambios)


#Se genera la gráfica
y                 = listaDeCambios; #Se cambia de lugar simplemente para más claridad a la hora de crear el gráfico
x                 = []; #Esta va a ser la lista de archivos modificados
promedioDeCambios = 0 ; #Este será el promedio de cambios realizados en los archivos

#print("Lista de cambios: "+ str(y) +'\n') #Muestra la lista de cambios que se han realizado por documento

for i in range (len(listaDeCambios)):
    x.append(i+1); #Básicamente es una especie de contador, es la cantidad de documentos procesados y en la gráfica se utiliza como la lista de documentos
    promedioDeCambios += listaDeCambios[i];  #Se suman todos lo cambios que se han efectuado en los documentos para luego sacar el promedio
 
promedioDeCambios = promedioDeCambios/len(listaDeCambios); #se obtiene el promedio de cambios realizado por documento

print("Promedio de cambios: "+ str(promedioDeCambios) +'\n')
#print(len(x)) 
#print(len(y))


plt.plot(x,y);

plt.show();
