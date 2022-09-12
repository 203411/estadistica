import pylightxl as xl
import plotly.graph_objects as plt
import matplotlib.pyplot as mat

def mostrar_tabla(tabla, clases):
    print("{:<6} {:<15} {:<10} {:<10} {:<7} {:<7} {:<10} {:<7} {:<10} {:<10} ".format( "Clase","L Dinferior","Lsuperior","F Absoluta","F Relativa","F Acumulada","Marca de clase","F Complementaria","L I exacto","L S exacto"))
    for i in range(clases):
        print("{:^6} {:^12,.2f} {:^12,.2f} {:^7} {:^15,.3f} {:^7} {:^15,.3f} {:^7} {:^15,.3f} {:^15,.3f} ".format(chr(65+i),tabla[i][0],tabla[i][1],tabla[i][2],tabla[i][3],tabla[i][4],tabla[i][5],tabla[i][6],tabla[i][7],tabla[i][8]))

def grafica(tabla,clases):
    fig, ax = mat.subplots()
    for i in range(clases):
        ax.bar(chr(65+i),tabla[i][2],color='blue')
    ax.set_title('Grafica de Barras')
    mat.show()

def grafica_pasteles(tabla, clases):
    totales = []
    nombres = []
    for i in range(clases):
        totales.append(tabla[i][2])
        nombres.append(chr(65+i))
    mat.pie(totales, labels=nombres, autopct="%0.1f%%")
    mat.suptitle('Grafica de Pasteles')
    mat.show()
    
def mostrar_navegador(tabla,num_clases):
    clases = []
    lim_inf = []
    lim_sup = []
    frec_abs = []
    frec_rel = []
    frec_acum = []
    marca_clase = []
    frec_comp = []
    lim_inf_ex = []
    lim_sup_ex = []
    for i in range(num_clases):
        clases.append(chr(65+i))
        lim_inf.append(tabla[i][0])
        lim_sup.append(tabla[i][1])
        frec_abs.append(tabla[i][2])
        frec_rel.append(tabla[i][3])
        frec_acum.append(tabla[i][4])
        marca_clase.append(tabla[i][5])
        frec_comp.append(tabla[i][6])
        lim_inf_ex.append(tabla[i][7])
        lim_sup_ex.append(tabla[i][8])
    fig = plt.Figure(data=[plt.Table(header=dict(values =['Clase','Limite Inferior','Limite Superior','Frecuencia Absoluta','Frecuencia Relativa','Frecuencia Acumulada', 'Marca de Clase', 'Frecuencia Complementaria','Limite Inferior Exacto', 'Limite Superior Exacto']),
                     cells = dict(values=[clases,lim_inf,lim_sup,frec_abs,frec_rel,frec_acum,marca_clase,frec_comp,lim_inf_ex,lim_sup_ex]))
    ])
    fig.show()