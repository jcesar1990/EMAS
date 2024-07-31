import paths
import ERROR
import os
from datetime import date, datetime, timedelta
import pandas as pd

def save1(nombre,clave):
    file_in = paths.file+'weatherlink.csv'
    print('Trabajando el archivo:',file_in)
    try:
        #Se obtendra la fecha actual
        ahora = datetime.now()
        hoy = datetime.strftime(ahora,"%d%m%y")
        ayer = ahora-timedelta(days=1)
        print('Hoy:',hoy)
        print('Ayer:',ayer)
        if not os.path.exists(file_in)
        csv1=open(file_in)
        text0=csv1.read() 
        print(text)
        print('Se salvaran los datos de la estacion',nombre,'en un directorio llamado save')
    
    

    except Exception as e:
        error_message = str(e)
        print('ERROR:',e)
        ERROR.handle_error('SAVE','guardado',error_message)

test = save1('Agricola Oriental', 'AGOS')
