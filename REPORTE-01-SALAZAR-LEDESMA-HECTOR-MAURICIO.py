from lifestore_file import lifestore_sales,lifestore_searches,lifestore_products


# mas_vendidos = [id_product, cantidad, name] 
mas_vendidos = []
# mas_buscados = [id_product, cantidad, name]
mas_buscados = []
# Número total de ventas
numero_ventas = len(lifestore_sales)
#Número total de productos
numero_productos = len(lifestore_products)
#Número total de búsquedas
numero_busquedas = len(lifestore_searches)
#por_categoria = [id_product, cantidad por categoria, name]
por_categoria = []

"""
Menú
#Creamos una lista con los reportes deseados
#Imprimimos los tipos que existen para que posteriormente el usuario ingrese
#el tipo de reporte deseado

"""
reportes = ["Productos mas vendidos", "Productos mas buscados", "Menos vendidos por categoria",
            "Menos buscados por categoria", "Productos con mejores reseñas", "Productos con peores reseñas",
            "Total de ingresos mensuales", "Total de ingresos anuales", "Ventas promedio por mes", "Meses con mas ventas"]

print("Seleccione el tipo de reporte que desea: ")
print("Estos pueden ser los que se muestran a continuación: ")
for reporte in reportes:
    print(reporte)
    
#Varibale que decide si seguimos imprimiendo reportes o no
#"continuar" para continuar imprimiendo los reportes deseados y cualquier
#otro valor para no continuar
    
x = "continuar"

#Definimos un numero de intentos como 3 para que el usuario tenga la oportunidad
#de corregir si se ha equivocado

while x == "continuar":
     
    for i in range(3):
        reporte = input("Ingrese a continuación el reporte que desea: ")
        if reporte in reportes:
            print("Usted ha seleccionado: ", reporte)
            break
        else :
            print("Por favor ingrese un valor válido")
            print("Intentos restantes: ", 2-i)
            if 2 - i == 0:
                print("Número de intentos permitidos superado, adiós")

#Si el valor seleccionado fue "Productos mas vendidos" entonces 
#buscamos en lifestore_sales hasta encontrar todos los productos iguales 
#y vamos contabilizando con la variable c cuantas veces de vendió este producto
#por último los agregamos a la lista llamada mas_vendidos

    if reporte == "Productos mas vendidos":
        for j in range(numero_productos):
            c = 0
            for i in range(numero_ventas):
                if lifestore_sales[i][1] == j:
                    c += 1
            mas_vendidos.append([j,c,lifestore_products[j-1][1]]) 
            
#Ordenamos la lista de manera descendente 
   
        lista_ordenada = sorted(mas_vendidos, key = lambda x: x[1], reverse = True) 
        print("Estos son los 15 productos más vendidos y la cantidad de veces que se vendieron")
        
#Imprimimos los 15 mas vendidos

        for i in range(15):
            print(i + 1, ".-", lista_ordenada[i][2])
            print("Se vendió ",lista_ordenada[i][1], "veces"  )
            print("\n")

#Si el valor seleccionado fue "Productos mas buscados" ocurre un procesos similar al proceso anterior,
#solo que en vez de buscar en lifestore_sales
#buscamos en lifestore_searches

    if reporte == "Productos mas buscados":
        for j in range(numero_productos):
            c = 0
            for i in range(numero_busquedas):
                if lifestore_searches[i][1] == j:
                    c += 1
            mas_buscados.append([j,c,lifestore_products[j-1][1]]) 
            
#Ordenamos la lista de manera descendente
        
        lista_ordenada = sorted(mas_buscados, key = lambda x: x[1], reverse = True)

#Imprimimos los 20 productos mas buscados
    
        print("Estos son los 20 productos más buscados y la cantidad de veces que se buscaron \n")
        print("\n")
        for i in range(20):
            print(i + 1, ".-", lista_ordenada[i][2])
            print("Cantidad de veces que se buscó este producto: " , lista_ordenada[i][1]) 
            print("\n")

#Definimos una lista para separar las categroias existentes
#en nuestra lista de productos

    categorias = []

#Si el valor seleccionado fue "Menos vendidos por categoria"
#imprimimos las categorias disponibles y con base en ese valor
#buscamos los menos vendidos
    if reporte == "Menos vendidos por categoria":
        print("\n")
        print("Elija una categoria a buscar")
        print("\n")
        for i in range(numero_productos):
            if lifestore_products[i][3] == lifestore_products[i-1][3]:
                continue
            print(lifestore_products[i][3])
            categorias.append(lifestore_products[i][3])
            
#Definimos un numero de intentos igual a 3 para seleccionar una categoria completa
   
        for i in range(3):
            categoria = input("Ingrese a continuación la categoria que desea: ")
            if categoria in categorias:
                print("Usted ha seleccionado: ", categoria)
                print("\n")
                break
        else :
            print("Por favor ingrese un valor válido")
            print("Intentos restantes: ", 2-i)
            if 2 - i == 0:
                print("Número de intentos permitidos superado, adiós")
                
#El proceso es igual que los dos anteriore
                
        for j in range(numero_productos):
            if categoria == lifestore_products[j-1][3]:
                c = 0
                for i in range(numero_ventas):
                    if lifestore_sales[i][1] == j:
                        c += 1
                por_categoria.append([j,c,lifestore_products[j-1][1]])
                
#Ordenamos la lista de manera ascendente

        lista_ordenada = sorted(por_categoria, key = lambda x: x[1])
        
#Imprimimos los 5 productos menos vendidos por categorias    
        print("\n")  
        print("Estos son los 5 productos menos vendidos por la categoria: ","\"",categoria,"\""," y la cantidad de veces que se vendieron \n")
        print("\n")
        for i in range(5):
            print(i + 1, ".-", lista_ordenada[i][2])
            print("Cantidad de veces que se vendió este producto: " , lista_ordenada[i][1]) 
            print("\n")

#Si el valor es "Menos buscados por categoria" hacemos exactamente lo mismo 
#que el proceso anterior 
    if reporte == "Menos buscados por categoria":
        print("\n")
        print("Elige una categoria a buscar: ")

        for i in range(numero_productos):
            if lifestore_products[i][3] == lifestore_products[i-1][3]:
                continue
            print(lifestore_products[i][3])
            categorias.append(lifestore_products[i][3])
#Definimos un numero de intentos permitidos igual a 3        
        for i in range(3):
            categoria = input("Ingrese a continuación la categoria que desea: ")
            
            if categoria in categorias:
                print("Usted ha seleccionado: ", categoria)
                break
            else :
                print("Por favor ingrese un valor válido")
                print("Intentos restantes: ", 2-i)
                if 2 - i == 0:
                    print("Número de intentos permitidos superado, adiós")
    
        for j in range(numero_productos):
            if categoria == lifestore_products[j-1][3]:
                c = 0
                for i in range(numero_busquedas):
                    if lifestore_searches[i][1] == j:
                        c += 1
                por_categoria.append([j,c,lifestore_products[j-1][1]])
                
#Ordenamos la lista de manera ascendente    
   
        lista_ordenada = sorted(por_categoria, key = lambda x: x[1])
        print("\n")    
        print("Estos son los 20 productos menos buscados por la categoria: ", "\"", categoria,"\""," y la cantidad de veces que se buscaron \n")
        
        for i in range(20):
            print(i + 1 , ".-", lista_ordenada[i][2])
            print("Cantidad de veces que se buscó este producto: " , lista_ordenada[i][1]) 
            print("\n")

#Creamos una lista donde llamada calificaciones donde vamos guardando 
#las calificaciones promedio para cada producto su identificador, su nombre 
#y las veces que fueron devueltas
    calificaciones = []
#Lista ordenada de manera descendente con respecto a las calificaciones
    calificaciones_ordenadas = []

    for j in range(1,numero_productos + 1):
        c = 0
        suma = 0
        dev = 0
        for i in range(numero_ventas):
            if lifestore_sales[i][1] == j:
                c += 1
                suma += lifestore_sales[i][2]
                dev += lifestore_sales[i][4]
                
        if c ==0:
            continue
        else:
            calificaciones.append([j,suma / c,lifestore_products[j-1][1],dev]) 
#Ordenamos las calificaciones con respecto a las calificaciones obtenidas de manera 
#descendente        
    calificaciones_ordenadas = sorted(calificaciones, key = lambda x: x[1], reverse = True) 

#Si se selecciona el valor de "Productos con mejores reseñas" imprimimos
#los productos con mejores reseñas
    if reporte == "Productos con mejores reseñas":
    
        print("Estos son los 10 productos mejor calificados y su calificación promedio")
        print("\n")
        
        for i in range(10):
            print(i + 1,".-",calificaciones_ordenadas[i][2])
            print("Calificación promedio: ",calificaciones_ordenadas[i][1] )
            print("Cantidad de devoluciones: ",calificaciones_ordenadas[i][3])
            print("\n")

# Si se selecciona el valor de "Productos con peores reseñas
#Ordenamos de manera ascendente e imprimimos los productos con peores reseñas

    if reporte == "Productos con peores reseñas":

        peor_calificados = sorted(calificaciones, key = lambda x: x[1])

        print("Estos son los 10 productos peor calificados y la cantidad de veces que se devolvieron ")
        print("\n")
        
        for i in range(10):
            print(i + 1, ".-", peor_calificados[i][2])
            print("Calificación promedio: ", peor_calificados[i][1] )
            print("Cantidad de devoluciones: ", peor_calificados[i][3])
            print("\n")


#Lista que contiene los meses del año, su numero en el calendario y sus días

    meses = [["Enero","01",31],["Febrero","02",29],["Marzo","03",31]
             ,["Abril","04",30],["Mayo","05",31],["Junio","06",30]
             ,["Julio","07",31],["Agosto","08",31],["Septiembre","09",30]
             ,["Octubre","10",31],["Noviembre","11",30],["Diciembre","12",31]]

#Lista que contiene la cantidad de ventas para cada mes
         
    cantidad_meses = []


    for j in range(len(meses)):
        c = 0
        for i in range(len(lifestore_sales)):
            fecha = lifestore_sales[i][3]
            mes = fecha[3:5]
            if mes == meses[j][1]:
                c += 1
        cantidad_meses.append([meses[j][0],c, c / meses[j][2]])

# Si se selecciona el valor de "Meses con mas ventas" ordenamos
# de manera descendente e imprimimos los meses con mas ventas y la cantidad 
# de ventas que se obtuvieron

    if reporte == "Meses con mas ventas":
        lista_ordenada = sorted(cantidad_meses, key = lambda x: x[1], reverse = True)
        
        for i in range(len(lista_ordenada)):
            print(lista_ordenada[i][0], "con un total de ventas de ", lista_ordenada[i][1])
            
# Si el valor obtenido fue "Ventas promedio por mes, 
# imprimimos el mes y su promedio de ventas por mes

    if reporte == "Ventas promedio por mes":
        for i in range(len(cantidad_meses)):
            print(cantidad_meses[i][0], "con un promedio de: ", cantidad_meses[i][2], "ventas por dia.")

#Lista que contabiliza los ingresos por cada mes obtenido

    ingresos_por_mes = []
    
    for m in range(len(meses)):
        suma = 0
        for j in range(numero_productos):
            c = 0
            for i in range(numero_ventas):
                fecha = lifestore_sales[i][3]
                num = fecha[3:5]        
                if meses[m][1] == num:
                    if lifestore_sales[i][1] == j and lifestore_sales[i][4] == 0:
                        c += 1
                        suma += c * lifestore_products[j - 1][2]
        
        ingresos_por_mes.append(suma)
    
#Si se selecciona el valor de "Total de ingresos mensuales" imprimimos
#los ingresos mensuales obtenidos

    if reporte == "Total de ingresos mensuales":
        for m in range(12):
            print("El total de ingresos para el mes de ", meses[m][0], "es de ",ingresos_por_mes[m])
    
#Si se selecciona el valor de #Total de ingresos anuales 
#imprimimos los ingresos anuales

    if reporte == "Total de ingresos anuales":
        suma = 0
        for i in range(len(ingresos_por_mes)):
            suma += ingresos_por_mes[0]
            
        print("Los ingresos para el año 2020 fueron de", suma)
        
    print("Para continuar, escriba: continuar, para salir pulse cualquier tecla")
    x = input()    