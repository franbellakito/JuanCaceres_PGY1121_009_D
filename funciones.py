import os
import time
import numpy
escenario = numpy.zeros((10,10),int)
listas_rut = []
listas_columnas = []
listas_filas = []
listas_asistentes = []
cantidad_entradas = 0
listas_cant_entradas = []
listas_tipo_entrada = ["PLATINUM","GOLD","SILVER"]
platinum = 120.000 
gold = 80.000
silver = 50.000

def mostrar_menu():
    print(""" CREATIVOS.CL
    1. comprar entradas
    2. mostrar ubicaciones disponibles
    3. ver listados asistentes
    4. mostrar ganancias totales
    5. salir
    """)
def validar_opc():
    while True:
        try:
            opc =int(input("ingrese una opcion 1-5: "))
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("error opcion ingresada no valida")    
        except:
            print("error debe ingresar un numero entero")
def validar_rut():
    while True:
        try:
            rut= int(input("ingrese su rut sin digito verficador,puntos ni guion:  "))
            if len(str(rut)) >= 7 and len(str(rut)) <= 8:
                return rut 
        except:
            print("ERROR! DEBE INGESAR UN NUMERO ENTERO") 
def ver_escenario():
    print("       A B C D E F G H I J")
    for x in range(10):
        print("piso",str(x+1), end =" ") 
        for y in range(10):
            print (escenario [x][y], end=" ")
        print()
            
           



def salir ():
    print("""juan francisco caceres pinto\n
             06-07-2023\n     
    """)

def  validar_fila():
    while True:
        try:
            fila= int(input("ingrese la fila en la cual se desea quedar: "))
            if fila in (1,2,3,4,5,6,7,8,9,10):
                return fila
            else:
                print("ERROR LA FILA NO EXISTE")
        except:
            print("ERROR DEBE INGRESAR UN NUMERO ENTERO")   

listas_letras =["A","B","C","D","E","F","G","H","I","J"]
def validar_columna():
    letra= input("ingrese la columna (A-J): ")
    if letra.upper in listas_letras:
        listas_letras.index(letra.upper())
        return letra
    else:
        print("ERROR LETRA INGRESADA NO VALIDA O NO EXISTE")

def validar_cant_entradas():
    while True:
        try:
            entradas= int(input("ingrese la cantidad de entradas que desea comprar (MAX 3!): "))
            if entradas >= 1 and entradas <= 3:
                return entradas
            else:
                print("ERROR DEBE COMPRAR AL MENOS UNA ENTRADA Y MENOS DE 3!")    
        except:
            print("ERROR DEBE INGRESAR UN NUMERO ENTERO") 
def tipo_entrada():
 
    while True:
        tipo_entr =input("ingrese que tipo de entrada prefiere: ")
        if tipo_entr.upper() in listas_tipo_entrada:
            print("ENTRADA SELECCIONADA CON EXITO")
            return tipo_entr
        else:
            print("ERROR LA ENTRADA SELECCIONADA NO ES VALIDA") 

def mostrar_menu_entradas():
       print(""" tipo entradas
    platinum
    gold
    silver""")               


listas_asientos1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
listas_asientos2 = [21,22,23,24,25,26,27,28,29,30,31,32,33,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
listas_asientos3 = [51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
def comprar_entradas(p_total: int):
    if 0 in escenario:
        rut= validar_rut()
        mostrar_menu_entradas()
        tip_entrada = tipo_entrada() 
        cant_entradas= validar_cant_entradas()
        columna= validar_columna()
        filaa = validar_fila()
        
        
        print("UBICACIONES DISPONIBLES")
        ver_escenario()
    
        if escenario [filaa-1][columna-1]==0:
            escenario [filaa-1][columna-1]= 1
            if filaa in listas_asientos1:
                print("su total a pagar es :",cant_entradas*platinum)
                p_total+= platinum
            elif filaa in listas_asientos2:
                print("su total a pagar es: ", cant_entradas*gold)
                p_total+= gold
            else:
                print("su total a pagar es: ", cant_entradas*silver)
                p_total+= silver
            listas_rut.append(rut)
            listas_columnas.append(columna+1)
            listas_filas.append(filaa+1)
            listas_cant_entradas.append(cant_entradas)
            listas_tipo_entrada.append(tip_entrada)
            print("LA OPERACCION SE AH REALIZADO CORRECTAMENTE")
            return p_total
        else:
            print("ERROR ASIENTO OCUPADO!")
    else:
            print("ERROR ESCENARIO COMPLETAMENTE LLENO!, VUELVA PRONTO")    

def ver_asistentes():
    print(listas_rut.sort)


    
          






