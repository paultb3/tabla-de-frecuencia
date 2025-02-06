import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Funciones existentes
def procesar_datos_excel(nombre_archivo, nombre_columna):
    try:
        df = pd.read_excel(nombre_archivo)
        if nombre_columna in df.columns:
            return df[nombre_columna].dropna()
        else:
            raise ValueError(f"La columna '{nombre_columna}' no existe en el archivo.")
    except FileNotFoundError:
        messagebox.showerror("Error", f"El archivo '{nombre_archivo}' no se encuentra.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

def crear_tabla_frecuencia(datos):
    frecuencias = Counter(datos)
    tabla_frecuencia = pd.DataFrame({
        'Clase': list(frecuencias.keys()),
        'Frecuencia Absoluta': list(frecuencias.values())
    })
    total_datos = len(datos)
    tabla_frecuencia['Frecuencia Absoluta Acumulada'] = tabla_frecuencia['Frecuencia Absoluta'].cumsum()
    tabla_frecuencia['Frecuencia Relativa'] = round(tabla_frecuencia['Frecuencia Absoluta'] / total_datos, 3)
    tabla_frecuencia['Frecuencia Relativa Acumulada'] = tabla_frecuencia['Frecuencia Relativa'].cumsum()
    tabla_frecuencia['Frecuencia Relativa %'] = round(tabla_frecuencia['Frecuencia Relativa'] * 100, 2)
    tabla_frecuencia['Frecuencia Relativa % Acumulada'] = tabla_frecuencia['Frecuencia Relativa %'].cumsum()
    return tabla_frecuencia

def graficar_frecuencia(tabla_frecuencia, tipo='barra', nombre_archivo='grafico.png'):
    plt.figure(figsize=(10, 6), dpi=300)
    if tipo == 'barra':
        barras = plt.bar(tabla_frecuencia['Clase'], tabla_frecuencia['Frecuencia Absoluta'], color='skyblue')
        plt.title('Frecuencia Absoluta por Clase')
        plt.xlabel('Clase')
        plt.ylabel('Frecuencia Absoluta')
        for barra in barras:
            altura = barra.get_height()
            plt.text(barra.get_x() + barra.get_width() / 2, altura, f'{int(altura)}', ha='center', va='bottom', fontsize=10)
    elif tipo == 'torta':
        plt.pie(tabla_frecuencia['Frecuencia Absoluta'], labels=tabla_frecuencia['Clase'], autopct='%1.1f%%', startangle=90)
        plt.title('Distribución de Frecuencias')
        plt.axis('equal')
    else:
        messagebox.showerror("Error", f"Tipo de gráfico '{tipo}' no reconocido. Usa 'barra' o 'torta'.")
        return
    plt.tight_layout()
    plt.savefig(nombre_archivo, dpi=3840//10)
    plt.show()

def exportar_tabla_excel(tabla_frecuencia, nombre_archivo='tabla_frecuencia.xlsx'):
    try:
        # Validar extensión del archivo
        if not nombre_archivo.lower().endswith('.xlsx'):
            nombre_archivo += '.xlsx'
        tabla_frecuencia.to_excel(nombre_archivo, index=False)
        messagebox.showinfo("Éxito", f"La tabla de frecuencia se ha exportado exitosamente a '{nombre_archivo}'.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al exportar la tabla: {e}")

# Interfaz Gráfica
class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Procesador de Datos")
        
        # Selección de archivo
        tk.Label(root, text="Archivo Excel:").grid(row=0, column=0, sticky="e")
        self.entry_archivo = tk.Entry(root, width=40)
        self.entry_archivo.grid(row=0, column=1)
        tk.Button(root, text="Examinar", command=self.seleccionar_archivo).grid(row=0, column=2)
        
        # Nombre de la columna
        tk.Label(root, text="Nombre de la Columna:").grid(row=1, column=0, sticky="e")
        self.entry_columna = tk.Entry(root, width=40)
        self.entry_columna.grid(row=1, column=1, columnspan=2)
        
        # Nombre del archivo de la tabla
        tk.Label(root, text="Nombre del Archivo de la Tabla:").grid(row=2, column=0, sticky="e")
        self.entry_tabla = tk.Entry(root, width=40)
        self.entry_tabla.grid(row=2, column=1, columnspan=2)
        
        # Nombre del archivo de la imagen
        tk.Label(root, text="Nombre del Archivo de la Imagen:").grid(row=3, column=0, sticky="e")
        self.entry_imagen = tk.Entry(root, width=40)
        self.entry_imagen.grid(row=3, column=1, columnspan=2)
        
        # Botón para procesar
        tk.Button(root, text="Procesar Datos", command=self.procesar).grid(row=4, column=0, columnspan=3, pady=10)
    
    def seleccionar_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx")])
        if archivo:
            self.entry_archivo.insert(0, archivo)
    
    def procesar(self):
        archivo = self.entry_archivo.get()
        columna = self.entry_columna.get()
        nombre_tabla = self.entry_tabla.get() or 'tabla_frecuencia.xlsx'
        nombre_imagen = self.entry_imagen.get() or 'grafico.png'

        # Validar extensión del archivo de la tabla
        if not nombre_tabla.lower().endswith('.xlsx'):
            nombre_tabla += '.xlsx'
        
        # Validar extensión del archivo de la imagen
        if not nombre_imagen.lower().endswith(('.png', '.jpg', '.jpeg')):
            nombre_imagen += '.png'

        if archivo and columna:
            datos = procesar_datos_excel(archivo, columna)
            if datos is not None:
                tabla_frecuencia = crear_tabla_frecuencia(datos)
                exportar_tabla_excel(tabla_frecuencia, nombre_tabla)
                graficar_frecuencia(tabla_frecuencia, tipo='barra', nombre_archivo=nombre_imagen)
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos requeridos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()