# Detalles del proceso de Data Engineering

<img src="https://github.com/user-attachments/assets/01bbfc81-3b50-4ae2-b10e-2da6e8369a59" alt="Proceso" width="700"/>

En este apartado se explica las diferentes alternativas utilizadas para realizar el proceso de transformación de la base de datos AdventureWorks. 

Si bien todo este proceso se puede realizar siguiendo una sola alternativa, el propósito de tomar varias es para desarrollar el conocimiento en la materia.

## Stack Tecnológico
Cloud SQL<br />
$\textsf{\color{grey}{Aloja la base de datos AdventureWorks.}}$

BigQuery<br />
$\textsf{\color{grey}{Selecciona las tablas necesarias para realizar este proyecto, tambien se desarrolla el proceso de transformación para el control de stock y se}}$<br />
$\textsf{\color{grey}{confecciona la base de datos final.}}$

DataStream<br />
$\text{\color{grey}{Conecta Cloud SQL con BigQuery. Cualquier tranformación que se realice a AdventureWorks se refleja en BigQuery.}}$

MySQL Workbench<br />
$\text{\color{grey}{Crea tablas en AdventureWorks necesarias para el control de stock y son enviadas a BigQuery para formar parte de la base de datos final.}}$
$\text{\color{grey}{A diferencia del resto, las consultas parten del entorno local.}}$

<img src="https://github.com/user-attachments/assets/6d8691b0-f5a4-4455-9dfb-23d1318627bd" alt="Local->nube" width="600"/><br />

Notebook Python<br />
$\text{\color{grey}{Dentro de BigQuery se puede utilizar el notebook de python, esta herramienta es utilizada para confeccionar un plan efectivo para el}}<br /> 
$\text{\color{grey}{control del stock.}}$<br />
$\text{\color{grey}{El resultado final es el archivo}}$ <code style="color : red">Control_de_Stock.ipynb</code>.


## Diagrama

<img src="https://github.com/user-attachments/assets/e1c3bd4f-ccac-437b-818a-0a0865525612" alt="Diagrama" width="700"/>

## Conexiones
Para que se generen todas estas interacciones, es necesario crear conexiones, en este caso, Cloud SQL tiene varias conexiones para transformar AdventureWorks en la base de datos final:

- MySQL Workbench.
- DataStream.
- mysql.connector

Dentro del Notebook Python, la única librería que necesita una conexión es *mysql.connector*, esto se debe a que *no* realiza transformaciones a las tablas de BigQuery sino que transforma las tablas desde Cloud SQL y de allí se reflejan los cambios hasta BigQuery.
