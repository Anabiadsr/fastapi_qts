import pytest
from app.credito.credito import classificar_credito

@pytest.mark.parametrize(
    "renda_mensal, score_credito, restricao_cadastral, retorno_esperado",
    [
        (0, 1000, True, "renda invalida"),
        (0, -300, True, "renda invalida"),
        (1500, -1000, False, "score invalido"),
        (1500, 3000, False, "score invalido"),
        (300, 500, True, "reprovado"),
        (200, 399,False, "reprovado"),
        (1000, 599,False, "aprovado padrao"),
        (1500, 1000,False, "aprovado premium")
    ],

)
def test_classificar_credito_caixa_preta(
    renda_mensal, score_credito,restricao_cadastral, retorno_esperado
):
    assert classificar_credito(renda_mensal, score_credito, restricao_cadastral) == retorno_esperado

@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito, retorno_esperado",
    [
        (0, 0, True, "renda invalida"),
        (0.01, 0, False, "reprovado"),

        (0.01, -1, False, "score invalido"),
        (0.01, 0, False, "reprovado"),

        (0.01, 399, False, "reprovado"),
        (0.01, 400, False, "aprovado padrao"),
        
        (0.01, 699, False, "aprovado padrao"),
        (0.01, 700, False, "aprovado premium"),

        (0.01, 1000, False, "aprovado premium"),
        (0.01, 1001, False, "score invalido")
    ],
)
def test_calcular_credito_limites_criticos(
    renda_mensal, score_credito, restrito, retorno_esperado
):
    assert classificar_credito(renda_mensal, score_credito, restrito) == retorno_esperado