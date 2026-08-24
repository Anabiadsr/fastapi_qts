import time 

def processar_pagamento(valor:float) -> bool:
    if valor <=0:
        return False


    #simula latência de rede ou comunicação com API externa
    time.sleep(0.60)
    return True