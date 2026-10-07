from app.descontos.descontos import calcular_desconto

def test_valor_zero():
    resultado = calcular_desconto(-10, True)
    assert resultado == 0


def test_valor_zero_retorna_zero():
    resultado = calcular_desconto(0, False)
    assert resultado == 0


def test_cliente_vip_com_valor_valido():
    resultado = calcular_desconto(100, True)
    assert resultado == 80


def test_cliente_nao_vip_com_valor_valido():
    resultado = calcular_desconto(100, False)
    assert resultado == 90


def test_valor_positivo_muito_pequeno():
    resultado = calcular_desconto(0.01, False)
    assert round(resultado, 3) == 0.009


def test_valor_maior_cliente_vip():
    resultado = calcular_desconto(200, True)
    assert resultado == 160


def test_valor_maior_cliente_nao_vip():
    resultado = calcular_desconto(200, False)
    assert resultado == 180