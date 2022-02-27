from app.cesar import encripta


def test_encripta_felipe_retorna():
    assert encripta('Felipe') == 'sryvcr'


def test_encripta_deve_retornar_minusculas():
    assert encripta('F').islower()


def test_encripta_deve_presevar_espaços():
    resultado = encripta('e a')
    assert resultado[1] == ' '
