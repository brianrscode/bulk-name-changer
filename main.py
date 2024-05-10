import os


def validar_ruta(ruta):
    if not isinstance(ruta, str):
        raise TypeError("La ruta debe ser una cadena de caracteres.")
    if not os.path.exists(ruta) or not os.path.isdir(ruta):
        raise ValueError("La ruta no existe o no es un directorio.")


def renombrar_archivos(ruta, nuevo_nombre):
    i = 1
    for f in os.listdir(ruta):
        archivo_antiguo = os.path.join(ruta, f)

        if os.path.isfile(archivo_antiguo):
            extension = os.path.splitext(f)[1]
            nuevo_nombre_archivo = f"{nuevo_nombre}_{i}{extension}"
            nuevo_archivo = os.path.join(ruta, nuevo_nombre_archivo)

            if os.path.exists(nuevo_archivo):
                print(f"El archivo {nuevo_nombre_archivo} ya existe. No se ha renombrado.")
            else:
                os.rename(archivo_antiguo, nuevo_archivo)
                print(f"{f} -> {nuevo_nombre_archivo}")
                i += 1


def main():
    ruta = input("Ingrese la ruta del directorio con los archivos a renombrar: ")
    try:
        validar_ruta(ruta)
    except (TypeError, ValueError) as e:
        print(e)
        return

    if ruta == ".":
        ruta = os.getcwd()

    nuevo_nombre = input("Ingrese el nuevo nombre del archivo: ")

    renombrar_archivos(ruta, nuevo_nombre)


if __name__ == "__main__":
    main()
