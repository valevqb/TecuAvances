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
    ingeniero = 0;
    ingeniera = 0;
    ingenierAO = 0;
    artista = 0;
    artisto = 0;
    artistAO = 0;
    estudiante = 0;
    estudianta = 0;
    estudiantEA = 0;
    administrativo = 0;
    administrativa = 0;
    administrativOA = 0;
    abogado = 0;
    abogada = 0;
    abogadOA = 0;
    
    fileName = "C:\\Users\\valev\\Documents\\GitHub\\TecuAvances\\datosUnidos.txt"

    texts = open (fileName, encoding="utf-8");

    contents = texts.read(); #contenido del texto
    contents = contents.lower();
    listaPalabras = contents.split(' ');
    

    for index, item in enumerate (listaPalabras):

        if (item == "estudiantes" or item == "estudiante"):
                if (listaPalabras[index+1] == "en" or listaPalabras[index+1] == "de"):
                    if (listaPalabras[index+2] == "computación." or listaPalabras[index+2] == "computación"
                        or listaPalabras[index+2] == "computación:" or listaPalabras[index+2] == "computacion"
                        or listaPalabras[index+2] == "computacion." or listaPalabras[index+2] == "computacion:"):
                        estudiante = estudiante + 1;

        ####################################################################################################################
                        
        elif (item == "ingeniero" or item == "ingeniero." or item == "ingeniero:"):
            ingeniero = ingeniero + 1;

        ####################################################################################################################
                        
        elif (item == "ingeniera" or item == "ingeniera." or item == "ingeniera:"):
            ingeniera = ingeniera + 1;

        ####################################################################################################################

        elif(item == "la" or item == "la," or item == "la:"):
            if (listaPalabras[index+1] == "artista" or listaPalabras[index+1] == "artista." or listaPalabras[index+1] == "artista:"
                or listaPalabras[index+1] == "pintor" or listaPalabras[index+1] == "pintor." or listaPalabras[index+1] == "pintor:"):
                artista = artista + 1;

        ####################################################################################################################

        elif(item == "el" or item == "el," or item == "el:"):
            if (listaPalabras[index+1] == "artista" or listaPalabras[index+1] == "artista." or listaPalabras[index+1] == "artista:"
                or listaPalabras[index+1] == "pintor" or listaPalabras[index+1] == "pintor." or listaPalabras[index+1] == "pintor:"):
                artisto = artisto + 1;

        ####################################################################################################################

        elif (item == "abogado" or item == "abogado." or item == "abogado:"):
            abogado = abogado + 1;

        ####################################################################################################################

        elif (item == "abogada" or item == "abogada." or item == "abogada:"):
            abogada = abogada + 1;

        ####################################################################################################################

        elif (item == "administrativo" or item == "administrativo." or item == "administrativo:"
              or item == "administrador" or item == "administrador." or item == "administrador:"):
            administrativo = administrativo + 1;

        ####################################################################################################################

        elif (item == "administrativa" or item == "administrativa." or item == "administrativa:"):
            administrativa = administrativa + 1;

        ####################################################################################################################

        elif (item == "actriz" or item == "actriz." or item == "actriz:"):
            artista = artista + 1;

        ####################################################################################################################

        elif (item == "actor" or item == "actor." or item == "actor:"):
            artisto = artisto + 1;

        ####################################################################################################################

        elif (item == "administradora" or item == "administradora." or item == "administradora:"):
            administrativa = administrativa + 1;

        ########################################################################################################################
        
        elif (item == "los" or item == ".los" or item == ",los"):

            if (listaPalabras[index+1] == "estudiantes" or listaPalabras[index+1] == "estudiante"):
                if (listaPalabras[index+2] == "en" or listaPalabras[index+2] == "de"):
                    if (listaPalabras[index+3] == "computación." or listaPalabras[index+3] == "computación"
                        or listaPalabras[index+3] == "computación:" or listaPalabras[index+3] == "computacion"
                        or listaPalabras[index+3] == "computacion." or listaPalabras[index+3] == "computacion:"):
                        estudiante = estudiante + 1;

            ####################################################################################################################
            
            elif (listaPalabras[index-1] == "y"):
                if (listaPalabras[index-2] != "las" or listaPalabras[index-2] != "las." or listaPalabras[index-2] != "las,"):
                    continue;

            ####################################################################################################################
                        
            elif (listaPalabras[index+1] == "ingenieros" or listaPalabras[index+1] == "ingenieros." or listaPalabras[index+1] == "ingenieros:"):
                ingeniero = ingeniero + 1;

            ####################################################################################################################

            elif (listaPalabras[index+1] == "artistas" or listaPalabras[index+1] == "artistas." or listaPalabras[index+1] == "artistas:"
                     or listaPalabras[index+1] == "pintores" or listaPalabras[index+1] == "pintores." or listaPalabras[index+1] == "pintores:"
                     or listaPalabras[index+1] == "actores" or listaPalabras[index+1] == "actores." or listaPalabras[index+1] == "actores:"):
                artisto = artisto + 1;

            ####################################################################################################################

            elif (listaPalabras[index+1] == "abogados" or listaPalabras[index+1] == "abogados." or listaPalabras[index+1] == "abogados:"):
                abogado = abogado + 1;

            ####################################################################################################################

            elif (listaPalabras[index+1] == "administrativos" or listaPalabras[index+1] == "administrativos." or listaPalabras[index+1] == "administrativos:"):
                administrativo = administrativo + 1;

            ####################################################################################################################

            elif (listaPalabras[index+1] == "y"):
                if (listaPalabras[index+2] == "las" or listaPalabras[index+2] == ".las" or listaPalabras[index+2] == ",las"):
                    if (listaPalabras[index+3] == "ingeniero" or listaPalabras[index+3] == "ingenieros"
                        or listaPalabras[index+3] == "ingenieros." or listaPalabras[index+3] == "ingenieros:"
                        or listaPalabras[index+3] == "ingenieras" or listaPalabras[index+3] == "ingenieras"
                        or listaPalabras[index+3] == "ingenieras." or listaPalabras[index+3] == "ingenieras:"):
                        ingenierAO = ingenierAO + 1;

                    #############################################################################################################
                        
                    elif (listaPalabras[index+3] == "artistas" or listaPalabras[index+3] == "artistas:"
                             or listaPalabras[index+3] == "artistas." or listaPalabras[index+3] == "pintores"
                             or listaPalabras[index+3] == "pintores." or listaPalabras[index+3] == "pintores:"
                             or listaPalabras[index+3] == "pintoras" or listaPalabras[index+3] == "pintoras."
                             or listaPalabras[index+3] == "pintoras:" or listaPalabras[index+3] == "actrices"
                             or listaPalabras[index+3] == "actrices." or listaPalabras[index+3] == "actrices:"
                             or listaPalabras[index+3] == "actores" or listaPalabras[index+3] == "actores."
                             or listaPalabras[index+3] == "actores:"):
                        artistAO = artistAO + 1;

                    #############################################################################################################

                    elif (listaPalabras[index+3] == "administrativos" or listaPalabras[index+3] == "administrativos."
                             or listaPalabras[index+3] == "administrativos:" or listaPalabras[index+3] == "administrativas"
                             or listaPalabras[index+3] == "administrativas." or listaPalabras[index+3] == "administrativas:"):
                        administrativOA = administrativOA + 1;

                    #############################################################################################################

                    elif (listaPalabras[index+3] == "abogados" or listaPalabras[index+3] == "abogados."
                             or listaPalabras[index+3] == "abogados:" or listaPalabras[index+3] == "abogadas:"
                             or listaPalabras[index+3] == "abogadas" or listaPalabras[index+3] == "abogadas."):
                        abogadOA = abogadOA + 1;

                    #############################################################################################################

                    elif (listaPalabras[index+3] == "estudiantes"):
                        if (listaPalabras[index+4] == "en" or listaPalabras[index+4] == "de"):
                            if (listaPalabras[index+5] == "computación." or listaPalabras[index+5] == "computación"
                                or listaPalabras[index+5] == "computación:" or listaPalabras[index+5] == "computacion"
                                or listaPalabras[index+5] == "computacion." or listaPalabras[index+5] == "computacion:"):
                                estudiantEA = estudiantEA + 1;

        ########################################################################################################################

        elif (item == "las" or item == ".las" or item == ",las"):
            
            if (listaPalabras[index+1] == "estudiantes" or listaPalabras[index+1] == "estudiante"):
                if (listaPalabras[index+2] == "en" or listaPalabras[index+2] == "de"):
                    if (listaPalabras[index+3] == "computación." or listaPalabras[index+3] == "computación"
                        or listaPalabras[index+3] == "computación:" or listaPalabras[index+3] == "computacion"
                        or listaPalabras[index+3] == "computacion." or listaPalabras[index+3] == "computacion:"):
                        estudianta = estudianta + 1;

            ####################################################################################################################
                        
            elif (listaPalabras[index+1] == "ingenieras" or listaPalabras[index+1] == "ingenieras." or listaPalabras[index+1] == "ingenieras:"):
                ingeniera = ingeniera + 1;

            ####################################################################################################################

            elif (listaPalabras[index+1] == "artistas" or listaPalabras[index+1] == "artistas." or listaPalabras[index+1] == "artistas:"
                     or listaPalabras[index+1] == "pintoras" or listaPalabras[index+1] == "pintoras." or listaPalabras[index+1] == "pintoras:"
                     or listaPalabras[index+1] == "actrices" or listaPalabras[index+1] == "actrices." or listaPalabras[index+1] == "actrices:"):
                artista = artista + 1;

            ####################################################################################################################

            elif (listaPalabras[index+1] == "abogadas" or listaPalabras[index+1] == "abogadas." or listaPalabras[index+1] == "abogadas:"):
                abogada = abogada + 1;

            ####################################################################################################################

            elif (listaPalabras[index+1] == "administrativas" or listaPalabras[index+1] == "administrativas."
                     or listaPalabras[index+1] == "administrativas:"):
                administrativa = administrativa + 1;

            ####################################################################################################################
            
            elif (listaPalabras[index-1] == "y"):
                if (listaPalabras[index-2] != "los" or listaPalabras[index-2] != "los." or listaPalabras[index-2] != "los,"):
                    continue;

            ####################################################################################################################
                
            elif (listaPalabras[index+1] == "y"):
                if (listaPalabras[index+2] == "las" or listaPalabras[index+2] == ".las" or listaPalabras[index+2] == ",las"):
                    if (listaPalabras[index+3] == "ingeniero" or listaPalabras[index+3] == "ingenieros"
                        or listaPalabras[index+3] == "ingenieros." or listaPalabras[index+3] == "ingenieros:"
                        or listaPalabras[index+3] == "ingenieras" or listaPalabras[index+3] == "ingenieras"
                        or listaPalabras[index+3] == "ingenieras." or listaPalabras[index+3] == "ingenieras:"):
                        ingenierAO = ingenierAO + 1;

                    #############################################################################################################
                        
                    elif (listaPalabras[index+3] == "artistas" or listaPalabras[index+3] == "artistas:"
                             or listaPalabras[index+3] == "artistas." or listaPalabras[index+3] == "pintores"
                             or listaPalabras[index+3] == "pintores." or listaPalabras[index+3] == "pintores:"
                             or listaPalabras[index+3] == "pintoras" or listaPalabras[index+3] == "pintoras."
                             or listaPalabras[index+3] == "pintoras:" or listaPalabras[index+3] == "actrices"
                             or listaPalabras[index+3] == "actrices." or listaPalabras[index+3] == "actrices:"
                             or listaPalabras[index+3] == "actores" or listaPalabras[index+3] == "actores."
                             or listaPalabras[index+3] == "actores:"):
                        artistAO = artistAO + 1;

                    #############################################################################################################

                    elif (listaPalabras[index+3] == "administrativos" or listaPalabras[index+3] == "administrativos."
                             or listaPalabras[index+3] == "administrativos:" or listaPalabras[index+3] == "administrativas"
                             or listaPalabras[index+3] == "administrativas." or listaPalabras[index+3] == "administrativas:"):
                        administrativOA = administrativOA + 1;

                    #############################################################################################################

                    elif (listaPalabras[index+3] == "abogados" or listaPalabras[index+3] == "abogados."
                             or listaPalabras[index+3] == "abogados:" or listaPalabras[index+3] == "abogadas:"
                             or listaPalabras[index+3] == "abogadas" or listaPalabras[index+3] == "abogadas."):
                        abogadOA = abogadOA + 1;

                    #############################################################################################################

                    elif (listaPalabras[index+3] == "estudiantes"):
                        if (listaPalabras[index+4] == "en" or listaPalabras[index+4] == "de"):
                            if (listaPalabras[index+5] == "computación." or listaPalabras[index+5] == "computación"
                                or listaPalabras[index+5] == "computación:" or listaPalabras[index+5] == "computacion"
                                or listaPalabras[index+5] == "computacion." or listaPalabras[index+5] == "computacion:"):
                                estudiantEA = estudiantEA + 1;

    print("ingeniero" + ": " + str(ingeniero))
    print("ingeniera" + ": " + str(ingeniera))
    print("ingeniero(a)" + ": " + str(ingenierAO))
    print("la artista" + ": " + str(artista))
    print("el artista" + ": " + str(artisto))
    print("el artista(o)" + ": " + str(artistAO))
    print("el estudiante" + ": " + str(estudiante))
    print("la estudiante" + ": " + str(estudianta))
    print("el estudiante(a)" + ": " + str(estudiantEA))
    print("administrativo" + ": " + str(administrativo))
    print("administrativa" + ": " + str(administrativa))
    print("administrativo(a)" + ": " + str(administrativOA))
    print("abogado" + ": " + str(abogado))
    print("abogada" + ": " + str(abogada))
    print("abogado(a)" + ": " + str(abogadOA))

######################################################################################################################
    
runChanges2();
