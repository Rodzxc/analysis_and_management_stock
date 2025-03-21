# El código siguiente, que crea un dataframe y quita las filas duplicadas, siempre se ejecuta y actúa como un preámbulo del script: 

# dataset = pandas.DataFrame(Group, Name, Qty_Sales)
# dataset = dataset.drop_duplicates()

# Pegue o escriba aquí el código de script:
dataset = dataset.sort_values(by='Group')

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

fig, ax = plt.subplots(figsize=(14, 8), dpi=150)
ax.axis('equal')

# Tamaño
width = 0.25
radius = 1.3

# Valores para el anillo interno
group_sum = dataset.groupby('Group')['Qty_Sales'].sum()
sizes_inner = group_sum.values

# Valores para el anillo externo
sizes_outer = dataset['Qty_Sales'].tolist()

# Nombres
labels_inner = group_sum.index.tolist()
labels_outer =dataset['Name'].tolist()

# Fuente
plt.rcParams['font.family'] = 'Arial'

# Numeros formato #.###,dd
def format_number(num):
    # Formateo inicial con separador de miles como coma
    formatted = f'{num:,.2f}'
    # Reemplazo la coma de miles por punto y el punto decimal por coma
    formatted = formatted.replace(',', 'X').replace('.', ',').replace('X', '.')
    return formatted

# Colores de las regiones
color = {}
for label in labels_inner: 
    if label == "Europe":
        color[label] = "#FCB714"
    elif label == "North America":
        color[label] = "#3CB9CC"
    elif label == "Pacific":
        color[label] = "#2878BD"
    else:
        color[label] = "grey"

# Colores de los paises
color_list =[] 
for N,G  in zip(dataset['Name'],dataset['Group']):
	if  G == "Europe": color_list.append("#FDD472")
	elif   G == "North America": color_list.append("#83C6D0")
	elif   G == "Pacific": color_list.append("#7EAED7")	
	else: color_list.append("grey")


# Etiquetas
def func(sizes, labels, pct= False):
  # Circulo interior
    if pct:
      total = sum(sizes)
      absolute = pct / 100. * total
      idx = np.where(np.isclose(sizes, absolute))[0][0]
      return f"{labels[idx]}\n{format_number(sizes[idx])}\n{format_number(pct)}%"    
  # Circulo exterior      
    else: 
        tag = [f'{l}\n{format_number(s)}\n({format_number(s*100/sum(sizes_outer))}%)' for s, l in zip(sizes_outer, labels_outer)]
        return tag

# Crear el anillo interno 
wedges_inner, texts_inner, autotexts_inner = ax.pie(
    sizes_inner, radius= radius-width, shadow = True,
    textprops={'fontsize': 19,'color':'white', 
                'bbox':dict(boxstyle="square", fc = "0.1", ec='grey',lw=0.72, alpha= 0.5)
                } ,
    colors=[color[label] for label in labels_inner],
    wedgeprops=dict(width=width, edgecolor='white'),
    pctdistance=0.85,
    autopct= lambda pct: (func(sizes_inner, labels_inner, pct))
)


# Crear el anillo externo
wedges_outer, texts_outer = ax.pie(
    sizes_outer, radius= radius, shadow = True,
    colors = color_list,
    wedgeprops=dict(width=width, edgecolor='white'),
    
)

# Lineas y cajas grises, anillo externo
bbox_props = dict(boxstyle="square", fc = "0.1", ec='grey',lw=0.72, alpha= 0.3)
kw = dict(arrowprops=dict(arrowstyle="-", color= "grey"),
          bbox=bbox_props, zorder=0, va="center"
          )         

# Crea las etiquetas del anillo externo
for i, p in enumerate(wedges_outer):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = f"angle,angleA=0,angleB={ang-0.001}"
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    # Ajustar la posición del texto 0.8*(x+np.sign(x))
    offset = 1.35 if x > 0 else -1.35
    ax.annotate(list(func(sizes_outer, labels_outer))[i], xy=(x, y), xytext= (1*(x+np.sign(x)) , 1.4*y), 
                color="white", fontsize= 17,
                horizontalalignment='center', 
                **kw
                )

# Circulo del centro
circle = plt.Circle((0,0),radius - width - 0.5, facecolor = 'none')
ax.add_patch(circle)
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
im = ax.imshow(Z, interpolation='bilinear', cmap=cm.binary,
               origin='lower', extent=[-3, 3, -3, 3],
               clip_path=circle, clip_on=True)

# Texto del centro 
total = sum(dataset['Qty_Sales']) # Valor
text = f'Total\n{format_number(total)}'
ax.text(0., 0., text, horizontalalignment='center', verticalalignment='center', color='w', fontsize = 19)


# Ajustar el fondo y otras propiedades
ax.set_facecolor('none')  # Eliminar fondo del gráfico
fig.patch.set_facecolor('none')  # Eliminar fondo de la figura

# Ajustar el diseño para no solapar elementos
plt.tight_layout()

# Mostrar el gráfico
plt.show()
