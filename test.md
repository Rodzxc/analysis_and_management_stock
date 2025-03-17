# ${\color{orange}Análisis\ y\ Gestión\ de\ Stock}$

>  *"La gestión  del stock y de los productos tiene como objetivo principal asegurar la **disponibilidad de los productos adecuados en el momento adecuado** para satisfacer la demanda, minimizando costos y optimizando los recursos."*

En este proyecto *end-to-end* se implementa una solución integral para la gestión y análisis de productos utilizando la base de datos de AdventureWorks. Combina herramientas de Google Cloud Platform (GCP), SQL, Power BI y Python para desarrollar un flujo de trabajo robusto de ETL, análisis y pronóstico de demanda.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white) ![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black) ![GoogleCloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)

## ${\color{orange}Objetivo}$

Proporcionar una plataforma unificada que facilita la gestión de stock y optimiza el ciclo de vida de los productos mediante un enfoque basado en datos. 
La combinación de GCP, SQL, Power BI y Python permite una solución escalable y eficiente que soporta decisiones estratégicas en la gestión de stock.

## ${\color{orange}Resumen}$

| ROL                |Herramienta                          |Tarea |
|----------------|-------------------------------|-----------------------------|
|Data Engineer|GCP (CloudSQL, Data Stream, BigQuery y Python en BigQuery)           |ETL(*)          |
|Data Analyst|Power BI (y Python embebido en Power BI)           |Análisis y Dashboard(*)            |
|Data Scientist|Python (Pandas, Numpy, Prophet, ...)|Predicción de la demanda(**)|

<span>(*) Base de Datos "AdventureWorks 2014".<span>

<span>(**) Archivo "AdventureWorks Sales.xlsx".<span>


## ${\color{orange}Resultado}$

- Confección de un calendario para el control del stock: 
$\textsf{\color{grey}{Los productos más importantes se controlan 2 veces al mes y el resto 1 vez al mes.}}$
- Análisis de la demanda y los ingresos generados: 
$\textsf{\color{grey}{Expresado en valores y porcentajes; y Segmentados por producto, Región y País. }}$
- Impacto de los productos en el negocio:
$\textsf{\color{grey}{Calculado a traves de la demanda y los ingresos que genera cada producto.}}$
- Impacto de los proveedores en el negocio:
$\textsf{\color{grey}{Calculado a traves de la demanda y los ingresos que genera cada producto y la trazabilidad a cada proveedor.}}$
- Predicción de la demanda:
$\textsf{\color{grey}{Estimación de la demanda de cada producto en los próximos 3 meses.}}$

## ${\color{orange}Conclusión}$

Este proyecto proporciona un enfoque basado en datos para la toma de decisiones y puede continuar desarrollandose calculando el lote óptimo de compra, nivel de servicio, política de inventarios, la implementación de un sistema ERP, etc.




------------------------------------------------------------------------------------------------------------------------





# Gestión de Stock

## Descripción
La gestión de stock es una disciplina clave que se encarga de planificar, controlar y supervisar los productos y mercancías dentro de una empresa. Su principal objetivo es asegurar que el nivel de stock sea el adecuado para satisfacer la demanda de los clientes, minimizando al mismo tiempo los costos operativos.

Este proyecto se centra en la implementación de la gestión de stock utilizando la base de datos AdventureWorks de Microsoft.

Esta base de datos simula diversos escenarios empresariales, registrando compras, ventas, productos, clientes, empleados, proveedores y otros elementos relacionados a la actividad comercial de una empresa multinacional "ficticia" que fabrica y distribuye bicicletas, piezas y accesorios en mercados de Norteamérica, Europa y Asia.

##Objetivo
Obtener insight que ayuden a tomar acciones sobre los proveedores y las mercancías de una manera inteligente y estratégica.

##Resultados
- Clasificación de las mercancías y proveedores según su importancia en el negocio.
- Dashboard de ventas.
- Confección de tablas, dashboard y documentos para el control del stock.
- Predicción de la demanda.

##Estructura

##Repositorio


##Conclusión
Este trabajo puede adaptarse a otras empresas que necesiten gestionar un inventario para impulsar su negocio.
Es un punto de partida desde el cual se puede seguir ampliando, integrando inteligencia artificial, realizando un sistema de recomendación de productos ó segmentado clientes, entre otras opciones, con el fin de seguir nutriendo la Gestión del Stock.
