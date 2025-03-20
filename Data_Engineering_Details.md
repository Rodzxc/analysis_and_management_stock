# Detalles del proceso de Data Engineering

![proceso](https://github.com/user-attachments/assets/01bbfc81-3b50-4ae2-b10e-2da6e8369a59)

En este apartado se explica las diferentes alternativas utilizadas para realizar el proceso de transformación de la base de datos AdventureWorks. 

Si bien todo este proceso se puede realizar siguiendo una sola alternativa, el propósito de tomar varias es para desarrollar el conocimiento en la materia.

## Stack Tecnológico
Cloud SQL: 
$\textsf{\color{grey}{Aloja la base de datos AdventureWorks.}}$
BigQuery: Selecciona las tablas necesarias para realizar este proyecto, tambien se desarrolla el proceso de transformación para el control de stock y se confecciona la base de datos final.
DataStream: Conecta Cloud SQL con BigQuery. Cualquier tranformación que se realice a AdventureWorks se refleja en BigQuery.
MySQL Workbench: crea tablas en AdventureWorks, estas tablas son necesarias para el control de stock y son enviadas a BigQuery para formar parte de la base de datos final.
Notebook Python: Dentro de BigQuery se puede utilizar el notebook de python, esta herramienta es utilizada para confeccionar un plan efectivo para el control del stock.
El resultado final es el archivo Control_de_Stock.ipynb.

## Diagrama

![image](https://github.com/user-attachments/assets/8dc2bf68-fd04-4c97-abb2-7cc2d66949a2)



## Conexiones
Para que se generen todas estas interacciones, es necesario crear conexiones, en este caso, Cloud SQL tiene varias conexiones para transformar AdventureWorks hasta llegar a la base de datos final:

- MySQL Workbench.
- DataStream.
- mysql.connector

Dentro del Notebook Python, la única librería que necesita una conexión es mysql.connector, esto se debe a que no realiza transformaciones a las tablas de BigQuery sino que transforma las tablas desde Cloud SQL y de allí se reflejan los cambios hasta BigQuery.
