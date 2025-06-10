# ${\color{orange}Análisis\ y\ Gestión\ de\ Stock}$
# 🟧 Análisis y Gestión de Stock
>  *"La gestión  del stock tiene como objetivo principal **asegurar la disponibilidad de los productos adecuados en el momento adecuado** para satisfacer la demanda, minimizando costos y optimizando los recursos."*

En este proyecto *end-to-end* se implementa una solución integral para la gestión y análisis de productos utilizando la base de datos de AdventureWorks. Combina herramientas de Google Cloud Platform (GCP), SQL, Power BI y Python para desarrollar un flujo de trabajo robusto de ELT, análisis y pronóstico de demanda.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white) ![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black) ![GoogleCloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)

AdventureWorks es una base de datos que simula diversos escenarios empresariales, registrando compras, ventas, productos, clientes, empleados, proveedores y otros elementos relacionados a la actividad comercial de una empresa multinacional que fabrica y distribuye bicicletas, piezas y accesorios en mercados de Norteamérica, Europa y el Pacífico.

## ${\color{orange}Objetivo}$

Proporcionar una plataforma unificada que facilita la gestión de stock y optimiza el ciclo de vida de los productos mediante un enfoque basado en datos. 
La combinación de GCP, SQL, Power BI y Python permite una solución escalable y eficiente que soporta decisiones estratégicas en la gestión de stock.

## ${\color{orange}Resumen}$

| ROL                |Herramienta                          |Tarea |
|----------------|-------------------------------|-----------------------------|
|Data Engineer|GCP (CloudSQL, Data Stream, BigQuery y Python en BigQuery)           |ELT(*)          |
|Data Analyst|Power BI (y Python embebido en Power BI)           |Análisis y Dashboard(*)            |
|Data Scientist|Python (Pandas, Numpy, Prophet, ...)|Predicción de la demanda(**)|

<span>(*) Base de Datos "AdventureWorks 2014".<span>

<span>(**) Archivo "AdventureWorks Sales.xlsx".<span>


## ${\color{orange}Resultado}$

- Confección de un calendario para el control del stock: 
$\textsf{\color{grey}{Los productos más importantes se controlan 2 veces al mes y el resto 1 vez al mes.}}$
- Análisis de la demanda y los ingresos generados: 
$\textsf{\color{grey}{Expresado en valores y porcentajes; y segmentados por producto, región y país. }}$
- Impacto de los productos en el negocio:
$\textsf{\color{grey}{Calculado a través de la demanda y los ingresos que genera cada producto.}}$
- Impacto de los proveedores en el negocio:
$\textsf{\color{grey}{Calculado a través de la demanda y los ingresos que genera cada producto y la trazabilidad a cada proveedor.}}$
- Predicción de la demanda:
$\textsf{\color{grey}{Estimación de la demanda de cada producto en los próximos 3 meses.}}$

## ${\color{orange}Estructura}$
<img src="https://github.com/user-attachments/assets/fc318e48-41ef-4431-948a-f4e9e82ab80d" alt="Estructura" width="700"/>

Para más detalles ver los archivos:
  - [Data_Engineering_Detalles.md](https://github.com/Rodzxc/analysis_and_management_stock/blob/main/Data_Engineering_Detalles.md)
  - [Data_Analysis_Detalles.md](https://github.com/Rodzxc/analysis_and_management_stock/blob/main/Data_Analysis_Detalles.md)
  - [Data_Science_Detalles.md](https://github.com/Rodzxc/analysis_and_management_stock/blob/main/Data_Science_Detalles.md)

## ${\color{orange}Repositorio}$
AdventureWorks Sales.xlsx<br/>
$\textsf{\color{grey}{Lista de precios, utilizado en la predicción de la demanda.}}$

Analisis_y_Gestion_del_stock.pbix<br/>
$\textsf{\color{grey}{Dashboard confeccionado en el proceso de Data Analysis.}}$

Control_de_Stock.ipynb<br/>
$\textsf{\color{grey}{Planificación y confección del control del stock.}}$

Data_Analysis_Detalles.md<br/>
$\textsf{\color{grey}{Muestra visualizaciones y código implementado en el dashboard.}}$

Data_Engineering_Detalles.md<br/>
$\textsf{\color{grey}{Describe las tareas realizadas y las interacciones dentro del ecosistema de GCP.}}$

Data_Science_Detalles.md<br/>
$\textsf{\color{grey}{Describe el desarrollo del algoritmo de predicción.}}$

Prediccion_de_ventas.ipynb<br/>
$\textsf{\color{grey}{Confección de las predicciones de ventas mensuales.}}$

piechart.py<br/>
$\textsf{\color{grey}{Script en python del gráfico de dona utilizado en el dashboard.}}$

## ${\color{orange}Conclusión}$

Este proyecto puede adaptarse a otras empresas que necesiten gestionar un inventario para impulsar su negocio.
Es un punto de partida desde el cual se puede seguir ampliando, integrando inteligencia artificial, realizando un sistema de recomendación de productos ó segmentado clientes, entre otras opciones, con el fín de seguir nutriendo la Gestión del Stock.
