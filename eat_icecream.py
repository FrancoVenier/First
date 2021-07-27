tengo_ganas_de_helado_input = input("¿Queres un Helado? (Si / No): ")
tiene_dinero_input = input("¿Tienes dinero para un helado? (Si / No): ")
esta_abierto_el_local_input = input("¿Esta abierto el local? (Si / No): ")
esta_tu_hermana_para_pagar_input = input("¿Estas con tu hermana asi lo paga? (Si / No): ")

sale_helado = tengo_ganas_de_helado_input == "Si"
puede_pagarlo = tiene_dinero_input == "Si" or esta_tu_hermana_para_pagar_input == "Si"
esta_abierto_el_local = esta_abierto_el_local_input == "Si"

if sale_helado and puede_pagarlo and esta_abierto_el_local:
    print("Sale Helado perri :) ")
else:
    print("al lobby pt hoy no hay helado")
