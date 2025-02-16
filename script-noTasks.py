import os

def verificar_archivo_vacio(nombre_archivo):
    """Verifica si un archivo está vacío y muestra un mensaje."""
    if os.path.exists(nombre_archivo):
        if os.path.getsize(nombre_archivo) == 0:
            print(f"El archivo '{nombre_archivo}' está vacío. Error")
        else:
            print(f"El archivo '{nombre_archivo}' tiene contenido.")
    else:
        print(f"El archivo '{nombre_archivo}' no existe.")


archivo_a_verificar = "archivo-Tasks.txt"
verificar_archivo_vacio(archivo_a_verificar)
