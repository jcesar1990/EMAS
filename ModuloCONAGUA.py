#Importamos librerias
import glob
from os import remove
import urllib.request
import paths

def proceso(nombre,id):
    
    espacio="-------------"

    print(espacio)

    try:
        #Se obtienen los datos del portal de conagua
        url1 = 'https://smn.conagua.gob.mx/tools/GUI/sivea_v3/php/getReporteEstacion.php?tipo=1&nombre_estacion='+id
        print(url1)
        file1 = paths.tempo+nombre+'.xslx'
        print(file1)
        #Usaremos selenium        
        print("Datos de la estación",nombre,"obtenidos")
    except Exception as e:
        print("Ha ocurrido un error con la descarga del archivo")
        print(e)

#test = proceso('TACUBAYA', 'TACUBAYA')
