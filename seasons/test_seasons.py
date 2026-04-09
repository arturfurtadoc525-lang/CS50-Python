import pytest
from seasons import Pessoa

def test_formatos_errados():
    with pytest.raises(SystemExit):
        Pessoa("January 1, 1999")
    with pytest.raises(SystemExit):
        Pessoa("1999/01/01")
    with pytest.raises(SystemExit):
        Pessoa("01-01-1999")
    with pytest.raises(SystemExit):
        Pessoa("1999-1-1")

def test_datas_impossiveis():
    with pytest.raises(SystemExit):
        Pessoa("1999-13-01")
    with pytest.raises(SystemExit):
        Pessoa("1999-01-32")
    with pytest.raises(SystemExit):
        Pessoa("1999-02-29")
    with pytest.raises(SystemExit):
        Pessoa("1999-00-10")

def test_textos_aleatorios():
    with pytest.raises(SystemExit):
        Pessoa("gato")
    with pytest.raises(SystemExit):
        Pessoa("")
