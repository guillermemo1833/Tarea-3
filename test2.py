import sys

# Cargar el diccionario de nombres de actores
def cargar_nombres_actores():
    nombres_actores = {}
    with open('data_name.tsv', 'r') as file:
        for line in file:
            line = line.strip()
            fields = line.split("\t")
            if len(fields) == 6:
                nconst = fields[0]
                primaryName = fields[1]
                nombres_actores[nconst] = primaryName
    return nombres_actores

# Mapper
def mapper():
    for line in sys.stdin:
        line = line.strip()
        fields = line.split("\t")
        
        # Verificar si la línea contiene la información requerida
        if len(fields) == 6:
            nconst = fields[2]
            tconst = fields[0]
            
            # Emitir el nconst del actor como clave y el ID de la película como valor
            print(f"{nconst}\t{tconst}")

# Reducer
def reducer():
    nombres_actores = cargar_nombres_actores()
    current_actor = None
    movies = []
    
    for line in sys.stdin:
        line = line.strip()
        nconst, tconst = line.split("\t")
        
        if current_actor is None:
            current_actor = nconst
            
        if nconst != current_actor:
            # Obtener el nombre del actor a partir del nconst
            actor_name = nombres_actores.get(current_actor, "Desconocido")
            
            # Emitir el resultado del índice invertido para el actor anterior
            print(f"{actor_name}\t{','.join(movies)}")
            movies = []
            current_actor = nconst
        
        movies.append(tconst)
    
    # Obtener el nombre del último actor
    actor_name = nombres_actores.get(current_actor, "Desconocido")
    
    # Emitir el resultado del índice invertido para el último actor
    if current_actor is not None:
        print(f"{actor_name}\t{','.join(movies)}")

# Flujo principal del programa
if __name__ == "__main__":
    if sys.argv[1] == "mapper":
        mapper()
    elif sys.argv[1] == "reducer":
        reducer()
