import matplotlib.pyplot as plt

# incializamos variables para los KPIs
total_vehiculos = 0
sin_revision = 0
aprobado_2da = 0
aprobado_3ra = 0

conteo_livianos = 0
conteo_pesados = 0
conteo_motos = 0

# Salimos de la carpeta del MIS y entramos a la del TPS para buscar el archivo
ruta_archivo = "../TPS/data/vehiculos.txt"

print("Leyendo la base de datos de vehiculos línea por línea...")

with open(ruta_archivo, "r") as archivo:
    for linea in archivo:
        linea = linea.strip() # Limpia espacios y saltos de línea \n
        if not linea:
            continue # Si la línea está vacía, se la salta
            
        # Separar los datos por cada coma (crea una lista de textos)
        datos = linea.split(",")
        total_vehiculos += 1
        
        # Guardamos las variables que nos importan según su posición [cite: 1]
        tipo = datos[4]            # El tipo de vehículo está en la posición 4 [cite: 1]
        r1 = int(datos[6])         # r1 está en la posición 6 [cite: 1]
        r2 = int(datos[7])         # r2 está en la posición 7 [cite: 1]
        r3 = int(datos[8])         # r3 está en la posición 8 [cite: 1]
        
        # --- LÓGICA PARA EL KPI 1 Y KPI 2 (Revisiones) ---
        if r1 == 0 and r2 == 0 and r3 == 0:
            sin_revision += 1
        elif r2 == 1:
            aprobado_2da += 1
        elif r3 == 1:
            aprobado_3ra += 1
            
        # --- LÓGICA PARA EL KPI 3 (Tipos de vehículos) ---
        if tipo == "liviano":
            conteo_livianos += 1
        elif tipo == "pesado":
            conteo_pesados += 1
        elif tipo == "moto":
            conteo_motos += 1

# Calcular porcentajes básicos
matriculados_totales = aprobado_2da + aprobado_3ra
porcentaje_morosidad = (sin_revision / total_vehiculos) * 100

print("\n¡Procesamiento terminado con éxito!")
print(f"Total de vehículos leídos: {total_vehiculos}")


# KPI 1: GRÁFICO DE BARRAS (Matriculados vs Morosos)

plt.figure(figsize=(6, 4))
categorias_kpi1 = ['Matriculados', 'Morosos (Sin Revisión)']
valores_kpi1 = [matriculados_totales, sin_revision]
colores_kpi1 = ['green', 'red']

plt.bar(categorias_kpi1, valores_kpi1, color=colores_kpi1)
plt.title(f'KPI 1: Control de Matriculación Anual\n(Morosidad: {porcentaje_morosidad:.2f}%)')
plt.ylabel('Cantidad de Vehículos')

# Guardar el dibujo como imagen
plt.savefig('kpi1_morosidad.png')
plt.show() # Muestra el gráfico en pantalla


# KPI 2: GRÁFICO DE LÍNEAS (Eficiencia en qué cita aprueban)

plt.figure(figsize=(6, 4))
citas_kpi2 = ['1ra Cita', '2da Cita', '3ra Cita']
valores_kpi2 = [0, aprobado_2da, aprobado_3ra] # 0 en la primera porque lo pediste así [cite: 1]

plt.plot(citas_kpi2, valores_kpi2, marker='o', color='blue', linewidth=2)
plt.title('KPI 2: Curva de Eficiencia en Revisión Técnica')
plt.xlabel('Instancia de Aprobación')
plt.ylabel('Vehículos Aprobados')

plt.savefig('kpi2_eficiencia.png')
plt.show()


# KPI 3: GRÁFICO DE PASTEL (Distribución del Parque)

plt.figure(figsize=(5, 5))
etiquetas_kpi3 = ['Livianos', 'Pesados', 'Motos']
valores_kpi3 = [conteo_livianos, conteo_pesados, conteo_motos]
colores_kpi3 = ['lightblue', 'orange', 'yellow']

plt.pie(valores_kpi3, labels=etiquetas_kpi3, autopct='%1.1f%%', startangle=140, colors=colores_kpi3)
plt.title('KPI 3: Distribución del Parque Automotor')

plt.savefig('kpi3_distribucion.png')
plt.show()
