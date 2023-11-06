class ArbolGenealogico:
    def __init__(self):
        self.arbol = {
            "Uziel": ["Jesús", "Graciela"],
            "Jesús": ["José", "Luis Miguel"],
            "José": ["Christina", "Xavier"],
            "Christina": ["Michael", "Michelle"],
            "Michael":[],
            "Michelle":[],
            "Xavier": ["Barak"],
            "Barak": ["George", "Kaleb"],
            "George": [],
            "Kaleb": [],
            "Luis Miguel": ["Lionel", "Cristiano R", "Diego"],
            "Lionel": ["Ronaldinho", "Dana"],
            "Ronaldinho": [],
            "Dana": ["Goku"],
            "Goku": ["Gohan", "Goten"],
            "Goten": [],
            "Gohan": ["Pan"],
            "Pan": ["Goku II"],
            "Goku II": [],
            "Cristiano R": ["Cristian N"],
            "Cristian N": ["Benito"],
            "Benito": ["Daniel", "Kevin"],
            "Daniel": [],
            "Kevin": [],
            
            "Graciela": ["Valentina", "Alfredo"],
            "Valentina":["Magi","Bart"],
            "Magi":["Brayan","Valentina II"],
            "Brayan":["Kimberly","Britani"],
            "Kimberly":["Ian"],
            "Ian":["Yandel","Alexander"],
            "Yandel":[],
            "Alexander":[],
            "Britani":[],
            
            "Valentina II":["Alex","Penelope"],
            "Alex":[],
            "Penelope":[],
            
            "Alfredo":["Joaquín","Juan"],
            "Joaquín":["Arturo"],
            "Arturo":["Ovidio"],
            "Ovidio":[],
            "Juan":["Melchor"],
            "Melchor":["Gaspar","Baltazar"],
            "Gaspar":["Eliel"],
            "Eliel":[],
            "Baltazar":["Omar"],
            "Omar":[],
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