import gzip

# Define el porcentaje de datos que deseas extraer
porcentaje = 0.1

# Función para generar una muestra reducida en orden
def generar_muestra_orden(nombre_archivo_entrada, nombre_archivo_salida):
    # Cuenta el número total de líneas
    total_lines = 0
    with gzip.open(nombre_archivo_entrada, 'rt') as file:
        for _ in file:
            total_lines += 1
    
    # Calcula el número de líneas a seleccionar
    lines_to_select = int(total_lines * porcentaje)
    
    # Crea una lista para almacenar las líneas seleccionadas
    selected_lines = []
    
    # Lee el archivo de entrada y selecciona las líneas en orden
    with gzip.open(nombre_archivo_entrada, 'rt') as file:
        for i, line in enumerate(file):
            if i < lines_to_select:
                selected_lines.append(line)
            else:
                break
    
    # Guarda las líneas seleccionadas en un nuevo archivo
    with open(nombre_archivo_salida, 'w') as file:
        file.writelines(selected_lines)

# Generar muestra reducida en orden para name.basics.tsv.gz
generar_muestra_orden('name.basics.tsv.gz', 'data_name.tsv')

# Generar muestra reducida en orden para title.principals.tsv.gz
generar_muestra_orden('title.principals.tsv.gz', 'data_title.principals.tsv')
