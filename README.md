# Tarea-3

Datos (Descargar title.principals.tsv.gz y name.basics.tsv.gz)

```
https://datasets.imdbws.com/
```

Documentación
```
https://developer.imdb.com/non-commercial-datasets/
```

Primero se corre por terminal el codigo datos.py

```
python3 datos.py
```
Luego se usa este comando para el indice invertido

```python3 test2.py mapper < data_title.principals.tsv | sort | python3 test2.py reducer > inverted_index_output.txt
```
Y para el buscador se utiliza este comando

```
python3 buscador.py
```
Link del video


```

```
