class ArbolGenealogico:
    def __init__(self):
        """ self.arbol = {
            "Uziel": ["Jesús", "Graciela"],
            "Jesús": ["José", "Luis Miguel"],
            "José": ["Christina", "Xavier"], #Pos de 2 veda
            "Christina": ["Michael"], #Cuando tiene 1 solo hijo
            "Michael":[], #Cuando no tiene Hijos
            "Michelle":[],
        } """ #Ps de ejemplo :D

        #Elias: Apolo
        #Axel: Hermes
        #Ambrosio: Callisto

        self.arbol = {
            "Zeus": ["Apolo","Artemisa"],

            "Apolo": ["Asclepio","Orfeo"],
            #Sub Arbol Asclepio:
            "Asclepio": ["Podalirio","Machaon"],
            #Sub Arbol Podalirio:
            "Podalirio": ["Polidoro"],
            "Polidoro": ["Peonio","Polifonte"],
            "Peonio": ["Anficlea","Icario"],
            "Anficlea": ["Milo","Bato"],

            "Icario": ["Ersinoe","Ritmo"],
            "Ersinoe" : ["Butes","Crenaeus"],
            "Ritmo": ["Tirreno","Carme"],

            "Polifonte": ["Bacis","Cometes"],
            "Bacis": ["Cleoboea", "Ismaro"],
            "Cleoboea" : ["Clytie", "Leucothea"],
            "Ismaro" : ["Marpessa","Hypsipyle"],
            "Cometes": ["Lelanto","Titono"],
            "Lelanto":["Pegasides","Nereides"],
            "Titono": ["Eos","Hemera"],
            #Sub Arbol Machaon:
            "Machaon": ["Nireo","Nicomedes"],
            #Sub Arbol Nireo:
            "Nireo": ["Iofante","Pandaro"],
            "Iofante": ["Sicino","Ceafix"],
            "Sicino" :["Etolo", "Sibaris"],
            "Etolo": ["Leucippe","Thestius"],
            "Sibaris":["Hesperia", "Lapyx"],
            "Ceafix":["Toloso", "Cecrope"],
            "Toloso":["Gelone","Batis"],
            "Cecrope":["Europa","Cadmus"],
            "Pandaro":["Atymnius","Equeclea"],
            "Atymnius":["Aglao","Androgea"],
            "Aglao":["Lilaea","Podargos"],
            "Androgea":["Ceneo", "Glanis"],
            "Equeclea":["Ergino","Periboea"],
            "Ergino":["Corinna","Hipaso"],
            "Periboea":["Oeneus","Agrius"],
            #Sub Arbol Nicomedes
            "Nicomedes":["Linanto","Medonte"],
            #Linanto
            "Linanto":["Aleimon","Acestor"],
            "Aleimon":["Pilos","Argeo"],
            "Acestor":["Poeas","Piritoo"],
            "Poeas":["Philammon","Sarpedon"],
            "Piritoo":["Cleopatra"],
            #Medonte
            "Medonte":["Lago","Capaneo"],
            "Lago":["Clitio","Perieres"],
            "Capaneo":["Licofonte","Ilares"],
            #Fin Sub Arbol Asclepio
            #Sub Arbol Orfeo
            "Orfeo":["Linus","Eurydice"],
            "Eurydice":["Gargareia","Argonautas"],
            #Sub Arbol Gargareia
            "Gargareia":["Licaon","Cecropia"],
            "Licaon":["Nicomaco","Misipe"],
            "Nicomaco":["Alcmeon","Erato"],
            "Misipe":["Anaxibia","Astioquia"],
            "Cecropia":["Erecteo","Atenea"],
            "Erecteo":["Aglauro","Herse"],
            "Aglauro":["Cecrops","Eryshicthon"],
            "Atenea":["Erictonio","Pandion"],
            "Pandion":["Egeo","Pallas"],
            #Sub Arbol Argonautas
            "Argonautas":["Canace","Estinfalo"],
            "Canace":["Linceo","Abante"],
            "Linceo":["Euricione"],
            "Abante":["Pero","Laodice"],
            "Estinfalo":["Atys","Milon"],
            "Atys":["Aglaura","Aglie"],
            "Milon":["Deifobo","Prodico"],
            #Fin Sub Arbol Orfeo
        #Fin Sub Arbol Apolo
        #Todos los sin hijo:
            "Milo": [],
            "Bato": [],
            "Butes": [],
            "Crenaeus": [],
            "Tirreno": [],
            "Carme": [],
            "Clytie": [],
            "Leucothea": [],
            "Marpessa": [],
            "Hypsipyle": [],
            "Pegasides": [],
            "Nereides": [],
            "Eos": [],
            "Hemera": [],
            "Leucippe": [],
            "Thestius": [],
            "Hesperia": [],
            "Lapyx": [],
            "Gelone": [],
            "Batis": [],
            "Europa": [],
            "Cadmus": [],
            "Lilaea": [],
            "Podargos": [],
            "Ceneo": [],
            "Glanis": [],
            "Corinna": [],
            "Hipaso": [],
            "Oeneus": [],
            "Agrius": [],
            "Pilos": [],
            "Argeo": [],
            "Philammon": [],
            "Sarpedon": [],
            
            "Cleopatra": [],
            "Clitio": [],
            "Perieres": [],
            "Licofonte": [],
            "Ilares": [],
            "Linus": [],
            "Alcmeon": [],
            "Erato": [],
            "Anaxibia": [],
            "Astioquia": [],
            "Cecrops": [],
            "Eryshicthon": [],
            "Erictonio":[],
            "Egeo":[],
            "Pallas":[],
            "Euricione":[],
            "Pero":[],
            "Laodice":[],
            "Aglaura":[],
            "Aglie":[],
            "Deifobo":[],
            "Prodico":[],
            

            
            "Artemisa": ["Hermes","Callisto"],

            "Hermes": ["Pan","Dionisio"],
            "Pan": ["Silenos","Eufeme"],
            "Silenos": ["Fauno","Marone"],
            "Fauno": ["Latinus","Tarquino"],
            "Latinus": ["Silvius","Aventino"],
            "Silvius": [],
            "Aventino": [],
            "Tarquino": ["Aruntio","Tanaquil"],
            "Aruntio": [],
            "Tanaquil": [],
            "Marone": ["Sileno","Milo"],
            "Sileno": ["Filira","Pegaso"],
            "Pegaso": ["Melanipe"],
            "Melanipe": [],
            "Filira": [],
            "Milo": ["Astidamas","Tiagro"],
            "Astidamas": [],
            "Tiagro": [],
            "Eufeme": ["Batus","Erinome"],
            "Batus": ["Elatiades","Epeio"],
            "Elatiades": ["Ameinias","Molon"],
            "Ameinias": [],
            "Molon": [],
            "Epeio": ["Endeo", "Toxeo"],
            "Endeo": [],
            "Toxeo": [],
            "Erinome": ["Lacedemon","Gala"],
            "Lacedemon": ["Dorio","Eurice"],
            "Dorio": [],
            "Eurice": [],
            "Gala": ["Alexiada","Polydora"],
            "Alexiada": [],
            "Polydora": [],
            "Dionisio": ["Priapo", "Ampelo"],
            "Priapo": ["Adono", "Cefiro"],
            "Adono": ["Ninias","Agdistis"],
            "Ninias": ["Cuidir","Polyxeño"],
            "Cuidir": [],
            "Polyxeño": [],
            "Agdistis": ["Circe","Acis"],
            "Circe": [],
            "Acis": [],
            "Cefiro": ["Balio", "Xanto"],
            "Balio": ["Jacasta", "Harmonia"],
            "Jacasta": [],
            "Harmonia": [],
            "Xanto": ["Antigona", "Ismene"],
            "Antigona": [],
            "Ismene": [],
            "Ampelo": ["Bromio", "Oinopion"],
            "Bromio": ["Liriope","Naso"],
            "Liriope": ["Narciso","Melo"],
            "Narciso": [],
            "Melo": [],
            "Naso": [],
            "Oinopion": ["Tiro"],
            "Tiro": ["Neleo","Pelias"],
            "Neleo":[],
            "Pelias": [],

            #Padre de lado derecho
            "Callisto": ["Arcas","Iasion"],
            #Izquierda
            "Arcas": ["Elato","Azeo"],
            "Elato": ["Apolis","Toxeo"],
            "Apolis": [],
            "Toxeo": [],
            
            "Azeo": ["Carpo","Eufrosine"],
            "Carpo": ["Ascaio", "Corinto"],
            "Ascaio": ["Ateneo","Atuctona"],
            "Ateneo": [],
            "Autoctona": [],
            "Corinto": ["Eutonos","Bellerofonte"],
            "Eutonos": [],
            "Bellerofonte": [],
            
            "Eufrosine": ["Cleta","Euforion"],
            "Cleta": ["Doris","Melite"],
            "Doris": [],
            "Melite": [],
            "Euforion": ["Deifone","Danae"],
            "Deifone": [],
            "Danae": [],
            #Derecha
            "Iasion": ["Demofonte","Pluto"],
            "Demofonte": ["Amintor","Cale"],
            "Amintor": ["Emetes","Etesicoro"],
            "Emetes": ["Psamathe","Echinades"],
            "Psamathe": [],
            "Echinades":[],
            "Etesicoro": ["Arete","Nicias"],
            "Arete": [],
            "Nicias": [],
            "Cale": ["Micceon","Lutro"],
            "Micceon": ["Hipseo","Sceus"],
            "Hipseo": [],
            "Sceus": [],
            "Lutro": ["Himera", "Eryx"],
            "Himera": [],
            "Eryx": [],
            
            "Pluto": ["Zagreo","Iaco"],
            "Zagreo": ["Agave","Pantino"],
            "Agave": ["Penteo","Pirante"],
            "Penteo": [],
            "Pirante": [],
            "Pantino": ["Menesicle","Leocoridas"],
            "Menesicle": [],
            "Leocoridas": [],
            
            "Iaco": ["Acasto","Pelias"],
            "Acasto": [],
            "Pelias": []


        }

    def encontrar_lca(self, personas):
        if not all(persona in self.arbol for persona in personas):
            return "Al menos una de las personas no se encuentra en el árbol."

        ancestros_personas = [self.obtener_ancestros(persona) for persona in personas]

        # Encontrar los ancestros comunes de todas las personas
        ancestros_comunes = set(ancestros_personas[0]).intersection(*ancestros_personas)

        if not ancestros_comunes:
            return "No se encontró un ancestro común."

        # Encontrar el ancestro anterior a los ancestros comunes
        ancestro_anterior = self.obtener_ancestro_anterior(ancestros_comunes)

        return ancestro_anterior

    def obtener_ancestros(self, persona):
        ancestros = []
        for padre, hijos in self.arbol.items():
            if persona in hijos:
                ancestros.append(padre)
                ancestros.extend(self.obtener_ancestros(padre))
        return ancestros

    def obtener_ancestro_anterior(self, ancestros):
        ancestro_anterior = ancestros.pop()
        while ancestros:
            persona = ancestros.pop()
            if all(ancestro in self.obtener_ancestros(persona) for ancestro in [ancestro_anterior]):
                ancestro_anterior = persona
        return ancestro_anterior


# Función para preguntar por personas y buscar el ancestro común
def buscar_ancestro_comun(arbol):
    personas = input("Ingresa los nombres de las personas (separados por comas): ").split(',')
    ancestro_anterior = arbol.encontrar_lca(personas)

    if ancestro_anterior != "No se encontró un ancestro común." and ancestro_anterior != "Al menos una de las personas no se encuentra en el árbol.":
        print(f"El ancestro anterior al ancestro común de {', '.join(personas)} es: {ancestro_anterior}")
    else:
        print(ancestro_anterior)


# Ejemplo de uso
arbol = ArbolGenealogico()

while True:
    buscar_ancestro_comun(arbol)
    continuar = input("¿Deseas buscar otro ancestro anterior? (Sí/No): ")
    if continuar.lower() != "sí":
        break



    
   #  "Graciela": ["Valentina", "Alfredo"],
    #        "Valentina": ["Magi","Bart"],
     #       "Magi":["Brayan","Valentina II"],
      #      "Brayan":["Kimberly","Britani"],
       #     "Kimberly":["Ian"],
        #    "Alfredo": ["Joaquín","Juan"],
         #   "Hijo3": ["Nieto1"],
          #  "Hijo4": ["Nieto2"],
           # "Nieto1": [],
            #"Nieto2": [] """
            # Puedes agregar más nombres y relaciones según tus necesidades """