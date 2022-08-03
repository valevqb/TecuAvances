import json
import re

data = {};
dictionary = {}; #diccionario de contenidos

with open('data.json',encoding="utf-8") as file: #abre el archivo json con tildes
    data = json.load(file);

    for neutral in data['withS']: #agrega los datos
        dictionary[neutral['original']] = neutral['replacement'];

texts = open ('prueba.txt', 'r');

contents = texts.read(); #contenido del texto

for word in contents.split(): #recorrer texto por palabras
    for key in dictionary: #recorrer diccionario
        if(word[0:len(word)-2] == key): #si la palabra es igual a la llave
            contents = contents.replace(word,dictionary[key]);

texts.close;

texts = open ('texto.txt', 'w');

texts.write(contents);

print(contents);

texts.close;




