def calcular_status_pedido(valor_total:float, pago:bool) ->str:
    if valor_total<=0:
        return "inválido"
    if not pago:
        return "pendente"
    return"confirmado"



#invalido
#pendente
#confirmado