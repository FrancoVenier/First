
confirmacion = False

while not confirmacion:
    user_name = input("¿Comó te llamas?: ")
    seguro_name = input("Has escrito {}, ¿Estas seguro/a? [Si/No]".format(user_name))
    if seguro_name == "Si":
        confirmacion = True

confirmacion_last_name = False

while not confirmacion_last_name:
    user_last_name = input("¿Comó te apellidas?: ")
    seguro_last_name = input("Has escrito {}, ¿Estas seguro/a? [Si/No]".format(user_last_name))
    if seguro_last_name == "Si":
        confirmacion_last_name = True

print("Has confirmado que te llamas {} {}".format(user_name, user_last_name))
