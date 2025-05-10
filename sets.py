#EN LOS SETS NO IMPORTA EL ORDEN
sets1={1,2,3,4,5}
print(type(sets1))

print(sets1)#A LOS SETS SE LE PUEDEN AGREGAR ELEMENTOS Y BORRAR

sets1.add(6)
print(sets1)

sets1.remove(3)
print(sets1)

sets1.discard(9)
print(sets1)

sets2={2,3,4,5,6}
sets2.clear()
print(sets2)

#sets1.pop()#ELIMINA EL ELEMENTO DE LA POSICION 0 normalmente aleatoriamente
#sets1.pop()
#sets1.pop()
print(sets2)

print(2 in sets1)
print(7 in sets2)