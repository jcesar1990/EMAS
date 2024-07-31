import ModuloSGIRPC

try:
    web = ModuloSGIRPC.procesoold("SGIRPC", "SGIRPC","http://189.254.33.151/pron/2023/STFS/download.txt")
except Exception as e:
    print(f'ERROR para: SGIRPC')
