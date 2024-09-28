

nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

# Clasificación de los nombres
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = []
for name in nombres:
    if name not in magos and name not in cientificos:
        otros.append(name)

#print(otros)

def hacer_grandioso():
    lista_magos_grandiosos = []
    for mago in magos:
        lista_magos_grandiosos.append(f'El gran {mago}')
    return lista_magos_grandiosos

magos_grandiosos = hacer_grandioso()

#print(magos_grandiosos)


def imprimir_nombres():
    for nombre in nombres:
        print(nombre)


print('Lista completa de nombres antes de ser modificados:')
imprimir_nombres()

print('\nNombres de los magos grandiosos:')
magos_grandiosos = '\n'.join(magos_grandiosos)
print(magos_grandiosos)

print('\nNombres de los cientificos:')
cientificos = '\n'.join(cientificos)
print(cientificos)
print('\nOtros:')
otros = '\n'.join(otros)
print(otros)