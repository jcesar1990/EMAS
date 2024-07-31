import ModuloSGIRPC

try:
    web = ModuloSGIRPC.procesoold("SGIRPC", "SGIRPC","http://189.254.33.151/stn/juarez/downld02.txt")
except Exception as e:
    print(f'ERROR para: SGIRPC')
