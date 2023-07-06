from funciones import *
p_total = 0
total= 0

while True:
    mostrar_menu()
    opcion = validar_opc()
    if opcion ==1:
        comprar_entradas(p_total)
    elif opcion== 2:
        ver_escenario()
    elif opcion == 3:
        ver_asistentes()
    elif opcion== 4:
        pass
    else:
        salir()
        break