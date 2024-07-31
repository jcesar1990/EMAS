
import json
import weatherlink_web_temps
import weatherlink_text

# Cargar las configuraciones desde el archivo JSON
with open('weatherlink.json', 'r') as config_file:
    config_data = json.load(config_file)

# Procesar cada estación en las configuraciones
for station in config_data["stations"]:
    try:
        # Debugging print statement
        print(f'Debug: {station}')
        
        nombre = station["name"]
        print('nombre:',nombre)
        url = station["url"]
        print('url:',url)
        
        try:
            web = weatherlink_web_temps.weatherlinkweb(nombre,url)
            print(f'Éxito web para {nombre}')
        except Exception as e:
            print(f'ERROR en web para {nombre}:', e)
        else:
            try:
                data = weatherlink_text.weatherlinktext(nombre)
                print(f'Éxito texto para {nombre}')
            except Exception as e:
                print(f'ERROR en texto para {nombre}:', e)
    except KeyError as ke:
        print(f'ERROR: {ke} no se encuentra en {nombre}')
