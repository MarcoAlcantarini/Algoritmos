nombre = input("Proporcione su nombre: ", )
sexo = str("")
region = str("")
interes = str("")
if nombre[0].islower():
    print ("El nombre debe comenzar con mayuscula")
else: 
    sexo = (input("Proporcione su sexo: ", )).lower()
    if sexo == "hombre":
        print ("Podria decirnos cual de estas 3 regiones le interesa mas conocer?")
        region = (input("Japon, Alemania, Italia: ", )).lower()
        if region == "japon":
            print ("Que es lo que mas te interesa de Japon? Comida? Videojuegos? o el Anime?")
            interes = (input (" ")).lower()
            if interes == "comida":
                print ("Los sushis son uno de mis platos favoritos")
            elif interes == "videojuegos":
                print ("Sin duda alguna saben como evolucionar el genero")
            elif interes == "anime":
                print ("Mirate Steins Gate si es que no lo has hecho")
            else: 
                print ("Esa no era ninguna de las opciones", ) 
                exit()
        elif region == "alemania":
            print ("Que es lo que mas te interesa de Alemania? Idioma? Cultura? o la Infrestructura?")
            interes = (input (" ")).lower()
            if interes == "idioma":
                print ("Ich kann Deutsch sprechen")
            elif interes == "cultura":
                print ("Son un poco recluidos, pero cuando te les unes se vuelven amigos de por vida")
            elif interes == "infrestructura":
                print ("Son increibles excepto en el ambito de los trenes")
            else:
                print ("Esa no era ninguna de las opciones", ) 
                exit()
        elif region == "italia":
            print ("Que es lo que mas te interesa de Italia? Idioma? Cultura? o la Infrestructura?")
            interes = (input (" ")).lower()
            if interes == "idioma":
                print ("Si te dedicas lo puedes aprender rapidamente")
            elif interes == "cultura":
                print ("Cada región tiene sus propias tradiciones, dialectos, y, por supuesto, su gastronomía única")
            elif interes == "infrestructura":
                print ("Cuenta con una de las redes de trenes de alta velocidad más avanzadas de Europa")
            else:
                print ("Esa no era ninguna de las opciones", ) 
                exit()
        else:
            print ("Esa no era ninguna de las opciones", ) 
            exit()
    elif sexo == "mujer":
        print ("Podria decirnos cual de estas 3 regiones le interesa mas conocer?")
        region = (input("Japon, Alemania, Italia: ", )).lower()
        if region == "japon":
            print ("Que es lo que mas te interesa de Japon? Comida? Videojuegos? o el Anime?")
            interes = (input (" ")).lower()
            if interes == "comida":
                print ("Los sushis son uno de mis platos favoritos")
            elif interes == "videojuegos":
                print ("Sin duda alguna saben como evolucionar el genero")
            elif interes == "anime":
                print ("Mirate Steins Gate si es que no lo has hecho")
            else: 
                print ("Esa no era ninguna de las opciones", ) 
                exit()
        elif region == "alemania":
            print ("Que es lo que mas te interesa de Alemania? Idioma? Cultura? o la Infrestructura?")
            interes = (input (" ")).lower()
            if interes == "idioma":
                print ("Ich kann Deutsch sprechen")
            elif interes == "cultura":
                print ("Son un poco recluidos, pero cuando te les unes se vuelven amigos de por vida")
            elif interes == "infrestructura":
                print ("Son increibles excepto en el ambito de los trenes")
            else:
                print ("Esa no era ninguna de las opciones", ) 
                exit()
        elif region == "italia":
            print ("Que es lo que mas te interesa de Italia? Idioma? Cultura? o la Infrestructura?")
            interes = (input (" ")).lower()
            if interes == "idioma":
                print ("Si te dedicas lo puedes aprender rapidamente")
            elif interes == "cultura":
                print ("Cada región tiene sus propias tradiciones, dialectos, y, por supuesto, su gastronomía única")
            elif interes == "infrestructura":
                print ("Cuenta con una de las redes de trenes de alta velocidad más avanzadas de Europa")
            else:
                print ("Esa no era ninguna de las opciones", ) 
                exit()
        else:
            print ("Esa no era ninguna de las opciones", ) 
            exit()
    else:
        print ("Esa no era ninguna de las opciones", ) 
        exit()        




