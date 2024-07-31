import os
import time  
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import threading
import subprocess

def timer(timer_runs):
    while timer_runs.is_set():
        espacio='-------------'

        # Lista de nombres de los scripts que deseas ejecutar
        scripts_to_run = ['OH_dif24.py', 'SGIRPC.py', 'PEMBUUNAM.py', 'METAR.py','Cargar_datos.py','CONAGUA.py', 'killchrome.py']

        # Itera sobre la lista y ejecuta cada script
        for script in scripts_to_run:
            try:
                # Utiliza subprocess.run para ejecutar el script
                subprocess.run(['python', script], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar {script}: {e}")

        final=datetime.now()
        print(final)
        print('Se completo la descarga')
        time.sleep(550)   # 10 minutos=600.
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,))
t.start()