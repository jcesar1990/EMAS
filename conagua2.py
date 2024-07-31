import ModuloCONAGUA

try:
    ModuloCONAGUA.proceso('TACUBAYA', 'TACUBAYA')
except Exception as e:
    print('ERROR:'+e)

try:
    ModuloCONAGUA.proceso('MOLINODELREY', 'MOLINO%20DEL%20REY')
except Exception as e:
    print('ERROR:'+e)

try:
    ModuloCONAGUA.proceso('TEZONTLE', 'TEZONTLE')
except Exception as e:
    print('ERROR:'+e)
