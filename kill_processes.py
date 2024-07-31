import psutil

def kill_processes():
    # Se establece un ciclo for para identificar el identificador del proceso deacuerdo al nombre del proceso o programa a buscar en "name"
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'chrome.exe':
            try:
                # Recorre los procesos del sistema y eliminara aquellos dentro de name
                proc.kill()
                print(f"Proceso{proc.info['pid']}-{proc.info['name']}terminado")
            except psutil.NoSuchProcess:
                print(f"Proceso {proc.info['pid']} ya no existe")
            except psutil.AccessDenied:
                print(f"No se puede terminar el proceso {proc.info['pid']}, acceso denegado")

# Ejecutar funcion
kill_processes()

