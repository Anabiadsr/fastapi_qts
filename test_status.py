from app.classificacao.status import calcular_status_pedido

def test_retorna_valido_quando_valor_zero():
    assert calcular_status_pedido(0 ,True)=="inválido"

def test_retorna_invalido_quando_valor_negativo():
    assert calcular_status_pedido(-10 ,True)=="inválido"

def test_retorna_valido_quando_nao_foi_pago():
    assert calcular_status_pedido(120 ,False)=="pendente"

def test_retorna_valido_quando_pago_e_valor_valido():
    assert calcular_status_pedido(120 ,True)=="confirmado"