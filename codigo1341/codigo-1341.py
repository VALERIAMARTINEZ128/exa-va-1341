# valeria yaretzi 1
# Valeria Yaretzi NC=1341
# Objeto: Congelador

import cv2
from pathlib import Path

# 1. Rutas del proyecto
proyecto = Path(__file__).resolve().parent.parent

ruta = proyecto / "img-original-1341" / "img-congelador-1341.jpg"
resultados = proyecto / "resultados-img-1341"
resultados.mkdir(parents=True, exist_ok=True)

# 2. Cargar la imagen original
img = cv2.imread(str(ruta))

if img is None:
    print("ERROR: No se pudo cargar la imagen.")
    print("Ruta que se intento abrir:", ruta)
    raise SystemExit

print("Imagen cargada correctamente")

# 3. Girar 90 grados
img90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# 4. Girar 45 grados
alto, ancho = img.shape[:2]
centro = (ancho // 2, alto // 2)
matriz = cv2.getRotationMatrix2D(centro, 45, 1.0)
img45 = cv2.warpAffine(img, matriz, (ancho, alto))

# 5. Cambiar tamaño a 600 x 500
img600 = cv2.resize(img, (600, 500))

# 6. Dibujar rectángulo rojo
img_rojo = img.copy()
cv2.rectangle(img_rojo, (50, 50), (150, 250), (0, 0, 255), 3)

# 7. Mostrar las cinco imágenes
cv2.imshow("1 - Congelador original", img)
cv2.imshow("2 - Congelador girado 90 grados", img90)
cv2.imshow("3 - Congelador girado 45 grados", img45)
cv2.imshow("4 - Congelador 600 x 500", img600)
cv2.imshow("5 - Congelador con rectangulo rojo", img_rojo)

# 8. Guardar las cuatro imágenes modificadas
cv2.imwrite(str(resultados / "congelador1-1341.jpg"), img90)
cv2.imwrite(str(resultados / "congelador2-1341.jpg"), img45)
cv2.imwrite(str(resultados / "congelador3-1341.jpg"), img600)
cv2.imwrite(str(resultados / "congelador4-1341.jpg"), img_rojo)

print("Se guardaron las cuatro imagenes procesadas.")
print("Presiona una tecla dentro de una ventana para cerrar.")

# 9. Mantener abiertas las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()


print("valeria 1341")