# Detalles del proceso de Data Science

En este apartado se explica brevemente el proceso de predicción de la demanda. Todo el proceso esta detallado en el archivo [Prediccion_de_ventas.ipynb](https://github.com/Rodzxc/analysis_and_management_stock/blob/main/Prediccion_de_ventas.ipynb).

A diferencia del resto del proyecto, se utiliza el Dataset [AdventureWorks Sales.xlsx](https://github.com/microsoft/powerbi-desktop-samples/blob/main/AdventureWorks%20Sales%20Sample/AdventureWorks%20Sales.xlsx) el cual es un archivo excel con las ventas y también se encuentra en este repositorio.

Las predicciones se calculan utilizando la librería Prophet de Facebook, y los métodos Top-Down y Bottom-Up.

<img src="https://github.com/user-attachments/assets/4c25d09c-95ef-4b46-b728-62e2b99a21e5" alt="Diagrama" width="700"/>

 - Top-Down consiste en predecir las ventas globales y prorratear el resultado a los diferentes productos.
 - Bottom-Up consiste en predecir las ventas de cada producto, la suma de las predicciones es la predicción de ventas totales.

El manejo de errores determinará cual método tiene mejor desempeño.


