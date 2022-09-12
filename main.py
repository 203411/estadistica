import calculos as cal
import pylightxl as xl
import plotly.graph_objects as plt
import matplotlib.pyplot as mat
import graficas as graf

def leer_no_agrupados():
    lista_datos = []
    archivo = xl.readxl(fn='datos.xlsx')
    for row in archivo.ws(ws='Hoja1').rows:
        lista_datos.append(row[0])
    print(lista_datos)
    return lista_datos

def leer_agrupados():
    lim_inferior = []
    lim_superior = []
    frecuencia = []
    archivo = xl.readxl(fn='datos.xlsx')
    clases = 0
    for row in archivo.ws(ws='Hoja2').rows:
        lim_inferior.append(row[0])
        lim_superior.append(row[1])
        frecuencia.append(row[2])
        clases += 1
    print(lim_inferior)
    print(lim_superior)
    print(frecuencia)
    return [clases,lim_inferior, lim_superior, frecuencia]

def rellenar_tabla(tabla, n_datos, uv, clases):
    frec_acumulada = 0
    for i in range(clases):
        tabla[i][3] = round(tabla[i][2] / n_datos,3) # frecuencia relativa
        frec_acumulada += tabla[i][2] #frecuencia acumulada
        tabla[i][4]= frec_acumulada
        tabla[i][5] = (tabla[i][0] + tabla[i][1]) / 2 # marca de clase
        tabla[i][6] = n_datos - tabla[i][4] # frecuencia complementaria     
        tabla[i][7] = tabla[i][0] - (uv/2) # limite inferior exacto
        tabla[i][8] = tabla[i][1] + (uv/2) # limite superior exacto
    return tabla

def dispersion_no_agrupados(datos):
    opcion = int(input("Los datos son: 1. Muestra 2. Poblacion \n"))
    print("Medidas de Dispersion")
    media = cal.media_no_agrupados(datos)
    print("Media: ",media)
    print("Rango: ",cal.rango_no_agrupados(datos))
    print("Desviacion media: ", cal.desviacion_media(datos, media))
    if(opcion == 1):
        varianza = cal.varianza_no_agrupados(datos, media, len(datos)-1)
    elif(opcion == 2):
        varianza = cal.varianza_no_agrupados(datos, media, len(datos))
    print("Varianza: ",varianza)
    print("Desviacion estandar: ", cal.desviacion_estandar(varianza))
    
def dispersion_agrupados(tabla, clases, n_datos):
    opcion = int(input("Los datos son: 1. Muestra 2. Poblacion \n"))
    print("Medidas de Dispersion")
    media = cal.media(tabla, clases,n_datos)
    print("Media: ",media)
    print("Rango: ",cal.rango_agrupados(tabla, clases))
    if(opcion == 1):
        varianza = cal.varianza_agrupados(tabla, media,clases, n_datos-1)
    elif(opcion == 2):
        varianza = cal.varianza_agrupados(tabla, media, clases, n_datos)
    print("Varianza: ",varianza)
    print("Desviacion estandar: ", cal.desviacion_estandar(varianza))

def medidas_tendencia_central(tabla, clases, n_datos,uv):
    print("Medidas de tendencia central")
    print("Media: ",cal.media(tabla, clases,n_datos))
    print("Mediana: ",cal.mediana(tabla, clases,n_datos))
    print("Moda: ",cal.moda(tabla, clases))
    # while True:
    #     opcion = int(input("Elija una opcion: \n1. Nx \n2. Ny \n3. NxNy \n4. Salir \n"))
    #     if opcion==1:
    #         buscar = float(input("Ingrese el valor 'al menos': "))
    #         nx = cal.nx(tabla, clases, buscar,uv)
    #         print("Valores por mayores a ", buscar,": ",nx)
    #     elif opcion==2:
    #         buscar = float(input("Ingrese el valor 'al menos': "))
    #         ny = cal.ny(tabla, clases, buscar,uv)
    #         print("Valores por menores a ", buscar,": ",ny)
    #     elif opcion==3:
    #         buscar = float(input("Ingrese el primer valor: "))
    #         buscar2 = float(input("Ingrese el otro valor: "))
    #         nxny = cal.nxny(tabla, clases, buscar, buscar2, uv)
    #         print("Valores entre ", buscar," y ",buscar2,": ",nxny)
    #     elif opcion==4:
    #         print("Saliendo...")
    #         break
    #     else:
    #         print("Opcion invalida")
    
def datos_agrupados(clases,lim_inferior,lim_superior,frec_absoluta):	
    tabla = [[j*0 for j in range(9)] for i in range(clases)]
    i= 0
    for dato in lim_inferior:
        if i < clases:
            # if (dato.isdigit() or len(dato)>0):
            tabla[i][0] = float(dato)
            i += 1
    i= 0
    for dato in lim_superior:
        if i < clases:
            # if (dato.isdigit() or len(dato)>0):
            tabla[i][1] = float(dato)
            i += 1
    i= 0
    n_datos = 0
    for dato in frec_absoluta:
        if i < clases:
            # if (dato.isdigit() or len(dato)>0):
            tabla[i][2] = float(dato)
            n_datos += float(dato)
            i += 1
    uv = tabla[1][0] - tabla[0][1]
    tabla = rellenar_tabla(tabla,n_datos, uv, clases)
    graf.mostrar_tabla(tabla, clases)
    medidas_tendencia_central(tabla, clases, n_datos,uv)
    return [tabla,n_datos]
    
def tabla_no_agrupados(numeros,clases,amplitud, uv):
    print("\nTabla de frecuencias")
    tabla = [[j*0 for j in range(9)] for i in range(clases)]
    lim_inferior = numeros[0]  #limite inferior
    for i in range(clases):
        tabla[i][0] = lim_inferior + (amplitud * i)
        if (i<clases and i>0):
            tabla[i-1][1] = lim_inferior + (amplitud * i) - uv
            tabla[clases-1][1] = lim_inferior + (amplitud * (i+1)) -uv   # posiblemente agregar la unidad de variacion
    frec_acumulada = 0
    for i in range(clases): #frecuencia absoluta
        for n in numeros:
            if(n >= tabla[i][0] and n <= tabla[i][1]): # si el numero esta dentro del rango
                tabla[i][2] += 1	        # se suma una frecuencia
    tabla = rellenar_tabla(tabla,len(numeros), uv, clases)
    graf.mostrar_tabla(tabla, clases)
    n_datos = len(numeros)
    medidas_tendencia_central(tabla, clases,n_datos ,uv)
    return tabla

def datos_no_agrupados(numeros):
    uv = float(input("Ingrese la unidad de variacion: "))
    numeros = cal.ordenar(numeros) # llamada a la funcion ordenar de calculos.py
    print("Ordenados: ",numeros)
    clases = cal.num_clases(numeros) # llamada a la funcion num_clases de calculos.py
    print("Numero de clases: ",clases)
    rango = round(cal.rango(numeros)) # llamada a la funcion rango de calculos.py
    amplitud = cal.amplitud(numeros) # llamada a la funcion amplitud de calculos.py
    print("Rango: ",rango)
    print("Amplitud: ",amplitud)
    amplitud = float(input("Confirme o modifique la amplitud: "))
    tabla = tabla_no_agrupados(numeros, clases, amplitud, uv)
    return [tabla,clases]

def main():
    tabla = [[]]
    clases = 0
    n_datos = 0
    while True:
        opcion = int(input("Seleccione una opcion: \n1. Datos No agrupados \n2. Datos Agrupados \n3. Salir \n"))
        if opcion == 1:
            datos = leer_no_agrupados()
            print("Datos No agrupados")
            calculos = datos_no_agrupados(datos)
            tabla = calculos[0]
            clases = calculos[1]
            dispersion_no_agrupados(datos)
            graf.mostrar_navegador(tabla, clases)
            graf.grafica(tabla, clases)
            graf.grafica_pasteles(tabla, clases)
        elif opcion == 2:
            print("Datos Agrupados")
            # clases = int(input("Ingrese el numero de clases: "))
            # lim_inferior = input("Ingrese los limites inferiores separados por comas: ").split(",")
            # lim_superior = input("Ingrese los limites superiores separados por comas: ").split(",")
            # frec_absoluta = input("Ingrese las frecuencias absolutas separadas por comas: ").split(",")
            # calculos = datos_agrupados(clases, lim_inferior, lim_superior, frec_absoluta)
            datos = leer_agrupados()
            calculos = datos_agrupados(datos[0],datos[1],datos[2],datos[3])
            tabla = calculos[0]
            clases = datos[0]
            n_datos = calculos[1]
            dispersion_agrupados(tabla, clases, n_datos)
            graf.mostrar_navegador(tabla, clases)
            graf.grafica(tabla, clases)
            graf.grafica_pasteles(tabla, clases)
        elif opcion == 3:
            print("Saliendo...")
            break
        else:
            print("Opcion no valida")

if __name__ == '__main__': 
    main()