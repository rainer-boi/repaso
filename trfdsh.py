import os
os.system("cls")
# ________________________________________
# El programa debe solicitar:
DESCUENTO_NINO = 0.50      # menores de 12 años
DESCUENTO_ADULTO_MAYOR = 0.30  # 60 años o más
DESCUENTO_MARTES = 0.20
RECARGO_FIN_SEMANA = 0.15
IVA = 0.19
bandera_acceso_num=False
bandera_acceso_dia=False
try:
    nombre=input("Ingrese su nombre: ")
    edad=int(input("Ingrese su edad: "))
    entrada=int(input("Ingrese la cantidad de entradas que quiere comprar: "))
    precio_base=float(input("Ingrese precio: "))
    dia=input("¿Qué día vendrá?: ").lower()
    # Lunes, Martes, Viernes, Sábado, Domingo
    if edad>0 and entrada>0 and precio_base>0:
        bandera_acceso_num=True
    if dia!="miercoles" and dia!="jueves":
        bandera_acceso_dia=True
    if bandera_acceso_dia and bandera_acceso_num:
        subtotal = entrada*precio_base
        if edad<12:
            valor_dsc_edad=subtotal*DESCUENTO_NINO
            tipo_cliente="Niño(a)"
        elif edad>=60:
            valor_dsc_edad=subtotal*DESCUENTO_ADULTO_MAYOR
            tipo_cliente="Adulto mayor"
        else:
            valor_dsc_edad=0
            tipo_cliente="Adulto"
        valor_prov=subtotal-valor_dsc_edad
        if dia=="martes":
            valor_dsc_dia=valor_prov*DESCUENTO_MARTES
            valor_prov2=valor_prov-valor_dsc_dia
        elif dia=="sabado" or dia=="domingo":
            valor_recargo=valor_prov*RECARGO_FIN_SEMANA
            valor_prov2=valor_prov+valor_recargo
        else:
            valor_prov2=valor_prov
        valor_iva=valor_prov2*IVA
        valor_final=valor_prov2+valor_iva
        valor_final_redo=round(valor_final, 2)
        if valor_final_redo<=10000:
            clasificacion="Compra económica"
        elif valor_final_redo>10000 and valor_final_redo<=30000:
            clasificacion="Compra normal"
        else:
            clasificacion="Compra alta"
        print(f"Nombre: {nombre}")
        print(f"Edad: {edad} años")
        print(f"Tipo cliente: {tipo_cliente}")
        print(f"Total a pagar: ${valor_final_redo}")
        print(f"Clasificación: {clasificacion}")
    else:
        print("Error, un dato es incorrecto")
except:
    print(". . .")

# Salida esperada
# Mostrar:
# •	Nombre del cliente (puedes usar .upper()) 
# •	Edad 
# •	Tipo de cliente: 
# o	Niño / Adulto / Adulto Mayor 
# •	Total a pagar (con 2 decimales) 
# •	Clasificación de la compra 
# ________________________________________
# Requisitos obligatorios (según rúbrica)
# ✔ Uso correcto de variables (inicializar y actualizar)
# ✔ Entrada y salida de datos (input / print)
# ✔ Operaciones aritméticas correctas
# ✔ Uso de strings (comparaciones, formato, etc.)
# ✔ Uso de operadores lógicos (and, or)
# ✔ Uso correcto de if, elif, else
# ✔ Implementación de try-except

