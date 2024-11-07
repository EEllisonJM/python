from pdf2image import convert_from_path

# Ruta del archivo PDF
pdf_path = 'Temas Selectos de Física I Bloque 2 Sesion 2.pdf'

# Carpeta para guardar las imágenes
output_folder = 'a1'

# Convertir PDF a imágenes (una por cada página)
images = convert_from_path(pdf_path)

# Guardar cada imagen con un nombre basado en el número de página
for i, image in enumerate(images):
    image_path = f"{output_folder}/pagina_{i + 1}.png"
    image.save(image_path, 'PNG')
    print(f"Imagen guardada: {image_path}")
