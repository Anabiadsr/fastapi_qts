import time
import pytest
from app.faturamento.cobranca import processar_cobranca

@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso,resultado_esperado",
    [
    
        (0.0, "BASICO", 0, -1.0),
        (100.0, " ", 0, -2.0),
        (100.0, "BASICO", 0, 100.0),
        (-50.0, "PREMIUM", 0, -1.0),
        (100.0, "EMPRESARIAL", -1, -1.0),
        (100.0, "INVALIDO", 0, -2.0),

        (200.0, "PREMIUM", 0, 180.0),
        (400.0, "EMPRESARIAL", 0, 320.0),
        (200.0, "  premium  ", 0, 180.0),

        (100.0, "BASICO", 10, 110.0),     
        (100.0, "PREMIUM", 10, 99.5),      
        (100.0, "BASICO", 45, 170.0),   
        (100.0, "EMPRESARIAL", 35, 133.0) 
    ]
)
def test_processar_cobranca_funcional(valor_base, plano, dias_atraso, resultado_esperado):
    assert processar_cobranca(valor_base, plano, dias_atraso) == resultado_esperado

def test_desempenho_processar_cobranca():
    inicio = time.perf_counter()
    processar_cobranca(100.0, "PREMIUM", 15)
    duracao = time.perf_counter() - inicio

    assert duracao < 0.1