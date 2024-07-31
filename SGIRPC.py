import json
import ModuloSGIRPC

# Cargar las configuraciones desde el archivo JSON
with open('SGIRPC.json', 'r') as config_file:
    config_data = json.load(config_file)

# Procesar cada estación en las configuraciones
for station in config_data["stations"]:
    try:
        # Debugging print statement
        print(f'Debug: {station}')
        
        nombre = station["name"]
        print('nombre:',nombre)
        clave = station["id"]
        print('clave:',"id")
        url = station["url"]
        print('url:',url)
        
        try:
            web = ModuloSGIRPC.procesonew(nombre,clave, url)
            print(f'Éxito web para {nombre}')
        except Exception as e:
            print(f'ERROR en web para {nombre}:', e)
    
    except KeyError as ke:
        print(f'ERROR: {ke} no se encuentra en {nombre}')
