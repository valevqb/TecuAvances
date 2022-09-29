from fileinput import filename
import json
import os
import matplotlib.pyplot as plt
import numpy as np
import operator
import time

tiempoInicio = time.perf_counter()



#---------------------------------------------------------------------------------------------------------
# Verifica contenido y elimina el reemplazo en donde no hay letras
#---------------------------------------------------------------------------------------------------------
def isLetter(word):
    counter = 0
    while(counter != len(word)):
        if(word[counter].isalpha() == False):
            return word[0:counter]
        counter += 1
    return word

#---------------------------------------------------------------------------------------------------------
# Aplica los cambios a los archivos
#---------------------------------------------------------------------------------------------------------
def runChanges (fileName):
    data = {}
    dictionary = {} #diccionario de contenidos

    with open('data.json',encoding="utf-8") as file: #abre el archivo json con tildes
        data = json.load(file)

        for neutral in data['datos']: #agrega los datos
            for abc in neutral:
                dictionary = dict (dictionary,**neutral[abc])

    #print("Write the file name:")
    #fileName = input()

    texts = open (fileName, encoding="utf-8")

    contents = texts.read() #contenido del texto
    contents = contents.lower()

    changedWords = []
    replacesNum = 0
    for word in contents.split(' '): #recorrer texto por palabras
        word2 = isLetter(word)
        #print(word2)
        for key in dictionary: #recorrer diccionario
            if(word2[0:len(word2)-2] == key and word2[0:len(word2)-2] != ""): #si la palabra es igual a la llave
                changedWords.append(word2)
                lists = dictionary[key]
                replacesNum += 1
                contents = contents.replace(word2,lists[0])

    texts.close

    name = fileName.split('\\')
    name = name[-1]

    texts = open ('nuevos\\' + name[0:len(name)-4] + 'Cambio' + '.txt', 'w', encoding="utf-8")

    contents = contents + '\n\n' + 'File name: ' + fileName + '\nNumber of changes: ' + str(replacesNum) + '\n'
    contents = contents + "Palabras reemplazadas: " + ', '.join(changedWords)

    print("Changed Words\n\n")
    print(changedWords)
    print("\n\n")
    #print(contentsCopy)

    texts.write(contents)

    texts.close
    return replacesNum

#---------------------------------------------------------------------------------------------------------
# Genera gráfico
#---------------------------------------------------------------------------------------------------------
def generarGráfico (listaDeCambios):
    #Se genera la gráfica
    y                 = listaDeCambios #Se cambia de lugar simplemente para más claridad a la hora de crear el gráfico
    x                 = [] #Esta va a ser la lista de archivos modificados

    #print("Lista de cambios: "+ str(y) +'\n') #Muestra la lista de cambios que se han realizado por documento

    for i in range (len(listaDeCambios)):
        x.append(i+1) #Básicamente es una especie de contador, es la cantidad de documentos procesados y en la gráfica se utiliza como la lista de documentos

    #print(len(x)) 
    #print(len(y))

    plt.plot(x, y)
    plt.title('Reporte de cambios en documentos')
    plt.ylabel('Lista de cambios por documento')
    plt.xlabel('Archivos modificados')
    plt.grid(True)
    plt.show()

#---------------------------------------------------------------------------------------------------------
# Obtiene el promedio de cambios
#---------------------------------------------------------------------------------------------------------
def obtenerPromedioDeCambios (listaDeCambios):
    
    promedioDeCambios = 0  #Este será el promedio de cambios realizados en los archivos

    for i in range (len(listaDeCambios)):
        promedioDeCambios += listaDeCambios[i]  #Se suman todos lo cambios que se han efectuado en los documentos para luego sacar el promedio
     
    promedioDeCambios = promedioDeCambios/len(listaDeCambios) #se obtiene el promedio de cambios realizado por documento


    return(promedioDeCambios)

#---------------------------------------------------------------------------------------------------------
# Top 10
#---------------------------------------------------------------------------------------------------------
def topDiez (listaDeArchivos, listaDeCambios):

    diccionarioDeDatos         = {listaDeArchivos:listaDeCambios for (listaDeArchivos,listaDeCambios) in zip(listaDeArchivos,listaDeCambios)} # Genera un diccionario a partir de las 2 listas de archivos y datos
    diccionarioDeDatosOrdenado = sorted(diccionarioDeDatos.items(),key=operator.itemgetter(1), reverse=True) # Genera una lista ordenada de mayor a menor basada en el diccionario anterior

    for i in range (10):
        print ("En "+str(i+1)+" lugar: "+ str(diccionarioDeDatosOrdenado[i][0])+" con: "+str (diccionarioDeDatosOrdenado[i][1])+ " cambios")

#---------------------------------------------------------------------------------------------------------
# Main o principal
#---------------------------------------------------------------------------------------------------------
#Prueba 1
CARPETA = 'Actas'

listArc = os.listdir(CARPETA) #lee todos los archivos en la carpeta

for list in listArc: #recorre uno a uno los archivos de la carpeta
    runChanges(CARPETA+'\\'+list)

#######################################

listaDeCambios = []
listTxt = os.listdir("txt") #lee todos los archivos en la carpeta
for file in listTxt: #recorre uno a uno los archivos de la carpeta
    
    listaDeCambios.append(runChanges('txt'+'\\'+file))

listaDeCambios.sort()
#print(listaDeCambios)


promedioDeCambios = obtenerPromedioDeCambios(listaDeCambios)
print("Promedio de cambios: "+ str(promedioDeCambios) +'\n')

topDiez (listArc, listaDeCambios)

tiempoFinal = time.perf_counter()
tiempoTranscurrido = tiempoFinal - tiempoInicio
print("\n\nEl programa tarda: \t" + str(tiempoTranscurrido))

generarGráfico (listaDeCambios)