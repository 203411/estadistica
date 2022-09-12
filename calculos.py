import math

def ordenar(datos):
    datos.sort()
    return datos
    
def num_clases(datos):
    num_datos = len(datos)
    k = 1 + 3.322 * math.log10(num_datos)
    return round(k)

def rango(datos):
    r = (max(datos) - min(datos))
    return r

def amplitud(datos):
    a = rango(datos) / num_clases(datos)
    return a

def media(tabla, clases, n_datos):
    suma = 0
    for i in range(clases):
        suma += tabla[i][2] * tabla[i][5]
    media = suma / n_datos
    return round(media,3)

def mediana(tabla, clases, n_datos):
    suma=0
    for i in range(clases):
        suma += tabla[i][2]
    posicion_mediana = (suma + 1)/2
    for i in range(clases):
        if(i==0):
            if(posicion_mediana <= tabla[0][4] and posicion_mediana >= 1):
                lim_inf_exac = tabla[i][7]
                frec_acumulada = tabla[i-1][4]
                frec_absoluta = tabla[i][2]
                ancho_inter = tabla[i][8] - tabla[i][7]
        elif(posicion_mediana <= tabla[i][4] and posicion_mediana >= tabla[i-1][4]):
            lim_inf_exac = tabla[i][7]
            frec_acumulada = tabla[i-1][4]
            frec_absoluta = tabla[i][2]
            ancho_inter = tabla[i][8] - tabla[i][7]
    mediana = lim_inf_exac + (n_datos/2 - frec_acumulada) * ancho_inter / frec_absoluta
    return round(mediana,3)

def moda(tabla, clases):
    frec_absoluta = 0
    for i in range(clases):
        if(i<clases-1):
            if(tabla[i][2] > frec_absoluta):
                frec_absoluta = tabla[i][2]
                lim_inf_exact = tabla[i][7]
                frec_anterior = tabla[i-1][2]
                frec_siguiente = tabla[i+1][2]
                amplitud = tabla[i][8] - tabla[i][7]
    #print("Limite inferior: ",lim_inf_exact,"Frec Absoluta: ",frec_absoluta, "Frec Anterior: ",frec_anterior, "Frec Siguiente: ",frec_siguiente,"Amplitud: ", amplitud)
    moda = lim_inf_exact +((frec_absoluta - frec_anterior) / ((2*frec_absoluta) - frec_anterior - frec_siguiente))* amplitud
    return round(moda,3)

def nx(tabla,clases,dato,uv):
    frec_clase = 0
    for i in range(clases):
        if(tabla[i][0]<=dato and tabla[i][1]>=dato):
            frec_clase = tabla[i][2]
            lim_inf = tabla[i][0]
            lim_sup = tabla[i][1]
            frec_acumuladas = tabla[i][6]
    nx = (lim_sup - dato + uv) / (lim_sup - lim_inf + uv) * frec_clase
    total = frec_acumuladas + round(nx)
    return total

def ny(tabla,clases,dato,uv):
    frec_clase = 0
    lim_inf = 0
    lim_sup = 0
    frec_acumuladas = 0
    for i in range(clases):
        if(tabla[i][0]<=dato and tabla[i][1]>=dato):
            frec_clase = tabla[i][2]
            lim_inf = tabla[i][0]
            lim_sup = tabla[i][1]
            frec_acumuladas = tabla[i-1][4]
    #print("Limite inferior: ",lim_inf,"Limite superior: ",lim_sup,"Frecuencia acumulada: ",frec_acumuladas, "freclase: ",frec_clase)	
    ny = (dato - lim_inf + uv) / (lim_sup - lim_inf + uv) * frec_clase
    total = frec_acumuladas + round(ny)
    return total

def nxny(tabla, clases, dato, dato2, uv):
    frec_clase = 0
    for i in range(clases):
        if(tabla[i][0]<=dato and tabla[i][1]>=dato):
            frec_clase = tabla[i][2]
            lim_inf = tabla[i][0]
            lim_sup = tabla[i][1]
            punto1 = i
    nx = (lim_sup - dato + uv) / (lim_sup - lim_inf + uv) * frec_clase
    # print("Limite inferior: ",lim_inf,"Limite superior: ",lim_sup, "freclase: ",frec_clase)
    # print("NX: ",nx)
    frec_clase = 0
    lim_inf = 0
    lim_sup = 0
    frec_acumuladas = 0
    for i in range(clases):
        if(tabla[i][0]<=dato2 and tabla[i][1]>=dato2):
            frec_clase = tabla[i][2]
            lim_inf = tabla[i][0]
            lim_sup = tabla[i][1]
            punto2 = i
    i = punto1 + 1
    while i<punto2:
        frec_acumuladas += tabla[i][2]
        i += 1
    # print("Limite inferior: ",lim_inf,"Limite superior: ",lim_sup,"Frecuencia acumulada: ",frec_acumuladas, "freclase: ",frec_clase)	
    ny = (dato2 - lim_inf + uv) / (lim_sup - lim_inf + uv) * frec_clase
    # print("NY: ",ny)
    total = frec_acumuladas + round(nx) + round(ny)
    return total

#Datos no agrupados

def media_no_agrupados(datos):
    suma = 0
    for i in datos:
        suma += i
    media = suma/len(datos)
    return round(media,3)

def rango_no_agrupados(datos):
    rango = max(datos) - min(datos)
    return rango

def desviacion_media(datos, media):
    suma = 0
    for i in datos:
        suma += abs(i - media)
    desv_media = suma/len(datos)
    return round(desv_media,3)
    
def varianza_no_agrupados(datos,media,cantidad):
    suma = 0
    for i in datos:
        suma += (abs(i - media))**2
    varianza = suma/cantidad
    return round(varianza,3)

def desviacion_estandar(varianza):
    desv_estandar = varianza**(1/2)
    return round(desv_estandar,3)

#Datos agrupados

def rango_agrupados(tabla,clases):
    rango = tabla[clases-1][8] - tabla[0][7]
    return round(rango,3)

def varianza_agrupados(tabla, media, clases, n_datos):
    suma = 0
    for i in range(clases):
        suma += (((abs(tabla[i][5] - media))**2)*tabla[i][2])
    varianza = suma/n_datos
    return round(varianza,3)