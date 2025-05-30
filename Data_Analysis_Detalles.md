# Detalles del proceso de Data Anaylisis

En este apartado se presentan algunas de las visualizaciones en Power BI.<br>
También se expone el código Python incorporado en Power BI por 2 motivos:

- Se ingestaron datos y una gráfica utilizando Python; y se quiere mostrar este proceso.
- Las gráficas creadas con Python no se puede ver a menos que se disponga de una licencia Pro.

Los resultados de este análisis de datos se encuentran en el archivo *Analisis_y_Gestion_del_stock.pbix*, puede descargarlo o puede verlo en la web haciendo click [aquí](https://app.powerbi.com/view?r=eyJrIjoiMWNiYjkxOWUtMzhlMS00ZjNkLWFlNjUtM2U2Y2U4YTJkOWY2IiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9&pageName=66945ba04729dd900102)

## Visualizaciones

### Análisis de Productos segmentados por región y país
<img src="https://github.com/user-attachments/assets/42a23502-947c-4b7c-a445-89802ae60cab" alt="Diagrama" width="800"/>

### Tabla de productos segmentados por ingresos y región
<img src="https://github.com/user-attachments/assets/11ebd3e4-fc16-48e7-9c87-df8f3c55a0b6" alt="Diagrama" width="800"/>

### Impacto y clasificación de los proveedores – Ingresos generados y Ventas
<img src="https://github.com/user-attachments/assets/ecb537a4-8f96-44fd-8829-367f2a5a10b3" alt="Diagrama" width="800"/>

## Código Python
### Ingesta de datos
![image](https://github.com/user-attachments/assets/c9ab2680-e1dc-4047-aba0-1a20e19ba049)
![image](https://github.com/user-attachments/assets/991d736e-b354-4eca-9b4a-e2cea09d811f)

### Gráfica
El script de la gráfica se encuentra en el archivo *[piechart.py](https://github.com/Rodzxc/analysis_and_management_stock/blob/main/piechart.py)*.<br>
El resultado es un doble gráfico de dona que se divide en regiones y países, y un círculo con el valor total en el centro:
![python_grafica](https://github.com/user-attachments/assets/91dc662a-0157-48f4-92ec-42efa4e97c29)

