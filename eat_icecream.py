tengo_ganas_de_helado_input = input("¿Queres un Helado? (Si / No): ") .upper()

if tengo_ganas_de_helado_input == "SI":
    sale_helado = True
elif tengo_ganas_de_helado_input == "NO":
    sale_helado = False
else:
    print("Te he dicho que me digas si o no, no se que has dicho pero cuento como que no")
    sale_helado = False

tiene_dinero_input = input("¿Tienes dinero para un helado? (Si / No): ") .upper()
esta_abierto_el_local_input = input("¿Esta abierto el local? (Si / No): ") .upper()
esta_tu_hermana_para_pagar_input = input("¿Estas con tu hermana asi lo paga? (Si / No): ") .upper()

puede_pagarlo = tiene_dinero_input == "SI" or esta_tu_hermana_para_pagar_input == "SI"
esta_abierto_el_local = esta_abierto_el_local_input == "SI"

if sale_helado and puede_pagarlo and esta_abierto_el_local:
    print("Sale Helado perri :) ")
else:
    print("al lobby pt hoy no hay helado")
