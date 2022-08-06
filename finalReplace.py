import json
import re

data = {};
dictionary = {}; #diccionario de contenidos

with open('data.json',encoding="utf-8") as file: #abre el archivo json con tildes
    data = json.load(file);

    for neutral in data['datos']: #agrega los datos
        for abc in neutral:
            dictionary = dict (dictionary,**neutral[abc])

texts = open ('prueba.txt', 'r');

contents = texts.read(); #contenido del texto

#verifica contenido y elimina el reemplazo en donde no hay letras
def isLetter(word):
    counter = 0;
    while(counter != len(word)):
        if(word[counter].isalpha() == False):
            return word[0:counter];
        counter += 1;
    return word;


for word in contents.split(' '): #recorrer texto por palabras
    print(word);
    word2 = isLetter(word);
    print(word2)
    for key in dictionary: #recorrer diccionario
        if(word2[0:len(word2)-2] == key and word2[0:len(word2)-2] != ""): #si la palabra es igual a la llave
            lists = dictionary[key]
            contents = contents.replace(word2,lists[0]);

texts.close;

texts = open ('texto.txt', 'w');

texts.write(contents);

print(contents);

texts.close;




