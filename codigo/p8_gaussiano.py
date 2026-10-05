# Lopez Ricardo NC = 0085
import cv2

# Cargar la imagen
imagen = cv2.imread("iguana.jpg")

# Verificar que la imagen se haya cargado correctamente
if imagen is None:
    print("Error: No se pudo cargar la imagen 'iguana.jpg'.")
    print("Por favor, verifica que la imagen esté en la misma carpeta que este script.")
    exit()

# Aplicar filtro Gaussiano (suavizado)
# El tamaño del kernel debe ser impar (ej. 7x7)
imagen_suavizada = cv2.GaussianBlur(imagen, (7, 7), 0)

# Mostrar las imágenes en ventanas emergentes
cv2.imshow("Imagen original iguana 0085", imagen)
cv2.imshow("Imagen suavizada iguana 0085- Filtro Gaussiano", imagen_suavizada)

# Guardar el resultado en el disco
nombre_resultado = "resultados_iguana.jpg"
cv2.imwrite(nombre_resultado, imagen_suavizada)

print("¡Filtro Gaussiano aplicado correctamente!")
print(f"Resultado guardado como: {nombre_resultado}")
print("programa echo por Lopez Ricardo NC = 0085")
# Esperar a que presiones cualquier tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
