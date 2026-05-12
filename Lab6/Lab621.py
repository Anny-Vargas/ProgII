# Uso de iterador en tupla
miTupla = ("asignacion", "laboratorio", "python")
myit = iter(miTupla)
print(next(myit))
print(next(myit))
print(next(myit))

# Uso en cadenas
mystr = "casa"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Recorrido con ciclo for
for x in mystr:
    print(x)