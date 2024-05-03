import pandas as pd
#importacion de panda y se asigna como pd
import matplotlib.pyplot as plt
#importacion de matplotlib como plt
productos = [
{"nombre": "Camiseta", "precio": 20, "cantidad_disponible": 100},
    {"nombre": "Pantalón", "precio": 30, "cantidad_disponible": 80},
    {"nombre": "Zapatos", "precio": 50, "cantidad_disponible": 50},
    {"nombre": "Reloj", "precio": 100, "cantidad_disponible": 30},
    {"nombre": "Gorra", "precio": 15, "cantidad_disponible": 120},
    {"nombre": "Bufanda", "precio": 25, "cantidad_disponible": 60},
    {"nombre": "Sudadera", "precio": 40, "cantidad_disponible": 70},
    {"nombre": "Bolsa", "precio": 35, "cantidad_disponible": 90},
    {"nombre": "Chaqueta", "precio": 80, "cantidad_disponible": 40},
    {"nombre": "Gafas de sol", "precio": 45, "cantidad_disponible": 25},
    {"nombre": "Calcetines", "precio": 10, "cantidad_disponible": 150},
    {"nombre": "Sombrero", "precio": 20, "cantidad_disponible": 55},
    {"nombre": "Pulsera", "precio": 5, "cantidad_disponible": 200},
    {"nombre": "Pendientes", "precio": 15, "cantidad_disponible": 180},
    {"nombre": "Cinturón", "precio": 20, "cantidad_disponible": 100},
    {"nombre": "Vestido", "precio": 60, "cantidad_disponible": 35},
    {"nombre": "Corbata", "precio": 25, "cantidad_disponible": 75},
    {"nombre": "Bolso", "precio": 70, "cantidad_disponible": 45},
    {"nombre": "Paraguas", "precio": 30, "cantidad_disponible": 65},
    {"nombre": "Collar", "precio": 40, "cantidad_disponible": 85},
]

# punto 1  Calcular el valor total del inventario para cada producto
for producto in productos:
    producto['valor_inventario'] = producto['precio'] * producto['cantidad_disponible']

# punto 1 Mostrar el valor del inventario
valor_total_inventario = sum(p['valor_inventario'] for p in productos)
print(f"El valor total del inventario es ${valor_total_inventario}")

#punto 3 simulacion de ventas y actualicacion de produntos disponibles
ventas = {"Camiseta": 5, "Pantalón": 3, "zapatos":2}
for producto in productos:
    if producto['nombre'] in ventas:
        producto['cantidad_disponible'] -= ventas[producto['nombre']]

# punto 5Crear un DataFrame con los nombres de los productos y la cantidad disponible
df_productos = pd.DataFrame(productos)

#punto 4 mostrar la cnatidad  restante de cad aproducto despues de las ventas simuladas
print(df_productos[['nombre', 'cantidad_disponible']])

#punto 4
# Crear el gráfico de barras
plt.figure(figsize=(14, 7))  #tmaño de de la figura
plt.bar(df_productos['nombre'], df_productos['cantidad_disponible'], color='y') 
plt.xlabel('Nombre del Producto') 
plt.ylabel('Cantidad Disponible')  
plt.title('Cantidad Disponible de Productos')  
plt.xticks(rotation=90) #rotacion de 90 grados pra poder leer de manera entendible
plt.show()  
