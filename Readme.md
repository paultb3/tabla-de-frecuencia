# ANALIZADOR DE TABLAS DE FRECUENCIA

V1.0

![Empresa encargada](./src/img/FORGE_FINL.png))

## Tecnologías Utilizadas

- **Lenguaje:**  Python 
- **Herramientas:** VSCode 

## Instalación

1. Cloná el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/nombre-del-repo.git

2. Crear un entorno virtual para instalar las librerias, abrir la terminal en la carpeta donde vas a trabajar
    ```bash
    python -m venv nombre_del_entorno
    python -m venv venv

3. Activar el entorno virtual
    ```bash
    .\venv\Scripts\activate
    source venv/bin/activate
    source venv/bin/activate
    
3. Instalar las librerias necesarias para ejecutar el codigo
    ```bash
    pip install pandas
    pip install collections
    pip install matplotlib

4. Finalmente ejecutamos el codigo con 
    ```bash
    python nombre_del_archivo.py 
    
## NOTA
    - Al ejecutar el archivo se generara un archivo con excel que almacenara la tabla de frecuencia generada 
    - Al mismo momento tambien se generara una imagen de la grafica
    - La primera version de este programa solo admite el tratamiento de variables de tipo cualitativo

## CONTRIBUCIONES
    - es necesario implemntar funciones y modulos para procesar variables cuantitativa continuas
