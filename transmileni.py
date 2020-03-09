from xml.dom import minidom
import math

# Traer el documento 
xmldoc = minidom.parse('transmilenio.xml')

# Seleccionar la etiqueta troncal
itemlist = xmldoc.getElementsByTagName('troncal')


# tex = "Hay {}"
# print(tex.format( len(itemlist) ) )

troncal1 = []
troncal2 = []

def llenarPilas():
    # Contar Cuantas troncales hay y llenar pilas
    for s in itemlist:

        # print("....")
        # print(s.attributes['name'].value)
        # print("....")

        # Contar cunatas estaciones hay en cada Troncal
        for m in s.getElementsByTagName('estacion'):

            # Capturar la data de la etiqueta
            #print("hola?")

            # Tener los nodos de la estacion

            if s.attributes['name'].value == "Caracas Sur":
                troncal1.append(m)
            else:
                troncal2.append(m)
            #print(m)
         

            # for e in m.getElementsByTagName('nombre'):
            #     var = 0
            #     # print(e.firstChild.data)

            
def mostrardata(troncal, date):

    # Puedo mostrar nombre, latitud, longitud, tipo de cada estacion
    # Solo cambio el tagName por el que necesite :DDDD

    for z in troncal.getElementsByTagName(date):
        # print(z.firstChild.data)
        return z.firstChild.data

def mostrarListaEstaciones(troncol):
    var = 0
    for z in troncol:
        text = "{}  => "+ str( mostrardata(troncol[var], 'nombre') )
        print(text.format(var) )
        var = var +1

# MI APP
llenarPilas()
# mostrardata(troncal1[0], 'nombre')
# mostrardata(troncal1[0], 'longitud')
# mostrardata(troncal1[0], 'tipo')
# mostrardata(troncal1[0], 'latitud')

# nombre = "El nombre de la estacion es: "+ mostrardata(troncal1[0], 'nombre')
# print(nombre)


print("Troncal 1 \n")
print("num | Nombre Estacion \n" )
mostrarListaEstaciones(troncal1)
print("\n")
opctroncalinicio = input("Digite Numero de la estacion de Inicio : ")


print("Troncal 2 \n")
print("num | Nombre Estacion \n" )
mostrarListaEstaciones(troncal2)
print("\n")
opctroncalfinal = input("Digite Numero de la estacion de Destino : ")

x1 = float(mostrardata(troncal1[opctroncalinicio], 'longitud'))
y1 = float(mostrardata(troncal1[opctroncalinicio], 'latitud'))

x2 = float(mostrardata(troncal1[opctroncalfinal], 'longitud'))
y2 = float(mostrardata(troncal1[opctroncalfinal], 'latitud'))



msg = "De la estacion |{}| a la estacion |{}|  hay |{}|"
name1 = str(mostrardata(troncal1[opctroncalinicio], 'nombre'))
name2 = str(mostrardata(troncal2[opctroncalfinal], 'nombre'))


# Siguuiendo la formula de un Vector y restando x , y 

print(msg.format(name1, name2, math.sqrt((x2-x1)*2+(y2-y1)*2) )