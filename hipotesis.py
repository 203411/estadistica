from stadistics import NormalDist

def calcular_size_muestra(N,e,p,q): 
    # size = tamaÑo de muestra buscado,  N = tamaño de poblacion original, Z = depende del nivel de confianza, e = error de la muestra, p = probabilidad de exito, q = probabilidad de fracaso 
    # Si no se conoce p --> p = 50% y q = 50%
    if(p == 0 & q == 0):	# si no se conoce p y q
        p = 0.5
        q = 0.5
    Z = nivel_confianza(e)
    size = (N*(Z^2)*p*q)/((e^2)*(N-1)+(Z^2)*p*q)
    return round(size)
            

def nivel_confianza(e):
    dist = NormalDist.from_examples(e)
    z = NormalDist.inv_cdf((1+0.95)/2)
    h = dist.stddev * z / ((N - 1)**0.5)
    return dist.mean - h, dist.mean + h

