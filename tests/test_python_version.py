import sys

def test_python_version():
    assert sys.version_info >= (3, 10), "Versão do Python é Menor que a 3.10!"
