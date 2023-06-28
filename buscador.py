import csv

def buscar_pelicula(indice):
    resultados = []
    
    with open('data_title.principals.tsv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # Saltar la primera línea de encabezado
        
        for row in reader:
            tconst = row[0]
            nconst = row[2]
            category = row[3]
            
            if indice.lower() in tconst.lower() or indice.lower() in nconst.lower() or indice.lower() in category.lower():
                resultados.append(row)
    
    return resultados

def mostrar_resultados(resultados):
    if resultados:
        for row in resultados:
            tconst = row[0]
            ordering = row[1]
            nconst = row[2]
            category = row[3]
            job = row[4]
            characters = row[5]
            
            print("Tconst:", tconst)
            print("Ordering:", ordering)
            print("Nconst:", nconst)
            print("Category:", category)
            print("Job:", job)
            print("Characters:", characters)
            print("---------------------------------------")
    else:
        print("No se encontraron coincidencias.")

# Flujo principal del programa
indice_busqueda = input("Ingrese el índice de búsqueda: ")
resultados_busqueda = buscar_pelicula(indice_busqueda)
mostrar_resultados(resultados_busqueda)
