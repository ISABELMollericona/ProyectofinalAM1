from pymongo import MongoClient
import csv


# Conexión a MongoDB Atlas
MONGO_URI = "mongodb+srv://mollericonaisabel1:xS8UDopTzgVJOYXp@appmovilfarmaciav2.mlbpnmp.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client["appmovilfarmaciav2"]  # Cambia si tu base tiene otro nombre

# Nombre de la colección que quieres exportar

coleccion = "Farmacia_productos"


# Obtener documentos de MongoDB
docs = db[coleccion].find()

# Guardar en CSV
with open("farmacias_productos.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = None
    for doc in docs:
        data = dict(doc)
        data["id"] = str(data.get("_id", ""))  # incluir el ID del documento
        data.pop("_id", None)  # quitar el campo _id si no lo quieres duplicado
        if writer is None:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            writer.writeheader()
        writer.writerow(data)

print("✅ Exportación completada: farmacias.csv")
