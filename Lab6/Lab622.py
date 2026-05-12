import datetime

# Fecha y hora actual
x = datetime.datetime.now()
print(x)

# Imprime año y día de la semana en inglés
print(x.year)
print(x.strftime("%A"))

# Crear fecha personalizada (Año, Mes, Día)
y = datetime.datetime(2010, 5, 11)
print(y)