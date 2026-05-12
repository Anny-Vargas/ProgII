import string

def contar_palabras_unicas(texto):
    # Limpiar puntuación y pasar a minúsculas
    tabla = str.maketrans('', '', string.punctuation)
    texto_limpio = texto.translate(tabla).lower()
    palabras = texto_limpio.split()
    # Usar un set para obtener palabras diferentes
    return len(set(palabras))

def palabra_mas_larga(texto):
    tabla = str.maketrans('', '', string.punctuation)
    palabras = texto.translate(tabla).split()
    if not palabras:
        return ""
    return max(palabras, key=len)

def frecuencia_caracteres(texto):
    # Filtrar solo letras y pasar a minúsculas
    solo_letras = [c.lower() for c in texto if c.isalpha()]
    total_letras = len(solo_letras)
    
    frecuencias = {}
    for letra in solo_letras:
        frecuencias[letra] = frecuencias.get(letra, 0) + 1
        
    print("\n--- Frecuencia de Caracteres ---")
    for letra, cuenta in sorted(frecuencias.items()):
        porcentaje = (cuenta / total_letras) * 100
        print(f"Letra '{letra}': {cuenta} veces ({porcentaje:.2f}%)")

def main():
    print("--- Procesador de Texto ---")
    usuario_texto = input("Introduce una cadena de texto larga:\n")
    
    if not usuario_texto.strip():
        print("El texto está vacío.")
        return

    # Invocar funciones y desplegar reporte
    unicas = contar_palabras_unicas(usuario_texto)
    larga = palabra_mas_larga(usuario_texto)
    
    print("\n--- Reporte de Métricas ---")
    print(f"Cantidad de palabras únicas: {unicas}")
    print(f"Palabra más larga: {larga}")
    frecuencia_caracteres(usuario_texto)

if __name__ == "__main__":
    main()