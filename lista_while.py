
mi_lista = []
input_usuario = ""

while input_usuario != "FIN":
    input_usuario = input("¿Qué necesitas comprar? (FIN para cerrar sesion): ")
    if input_usuario != "FIN":
        mi_lista.append((input_usuario))

for item in mi_lista:
    print("tengo que comprar {}".format(item))

print("Esta es la lista de la compra")
