import CONAGUA
import paths
import ERROR

intentos_numero = 5
for intento in range(1, intentos_numero + 1):

    try:
        temperatura = CONAGUA.conagua('temperatura')
    except Exception as e:
        error_message = str(e)
        print(error_message)
        ERROR.handle_error('CONAGUA', 'temperatura', error_message)
        if intento == intentos_numero:
            print('Se omite despues de 5 intentos')
            break
        else:
            print('Intentando obtener los datos nuevamente')
else:
    print('Datos de temperatura de CONAGUA obtenidos')


for intento in range(1, intentos_numero + 1):

    try:
        temperatura = CONAGUA.conagua('velocidad')
    except Exception as e:
        error_message = str(e)
        print(error_message)
        ERROR.handle_error('CONAGUA', 'velocidad', error_message)
        if intento == intentos_numero:
            print('Se omite despues de 5 intentos')
            
        else:
            print('Intentando obtener los datos nuevamente')
else:
    print('Datos de temperatura de CONAGUA obtenidos')


for intento in range(1, intentos_numero + 1):

    try:
        temperatura = CONAGUA.conagua('precipitacion')
    except Exception as e:
        error_message = str(e)
        print(error_message)
        ERROR.handle_error('CONAGUA', 'precipitacion', error_message)
        if intento == intentos_numero:
            print('Se omite despues de 5 intentos')
            
        else:
            print('Intentando obtener los datos nuevamente')
else:
    print('Datos de temperatura de CONAGUA obtenidos')

