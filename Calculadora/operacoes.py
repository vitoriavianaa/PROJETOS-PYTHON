import re

def soma(texto_atual):
    partes = texto_atual.split("+")

    a = float(partes[0].strip())
    b = float(partes[1].strip())

    resultado = a + b

    if resultado.is_integer():
        resultado = int(resultado)

    return resultado

def subtracao(texto_atual):
    partes = texto_atual.split("-")
    a = float(partes[0].strip())
    b = float(partes[1].strip())

    resultado = a - b

    if resultado.is_integer():
        resultado = int(resultado)

    return resultado


def multiplicacao(texto_atual):
    partes = texto_atual.split("x")
    a = float(partes[0].strip())
    b = float(partes[1].strip())

    resultado = a * b

    if resultado.is_integer():
      resultado = int(resultado)

    return resultado


def divisao(texto_atual):
    partes = texto_atual.split("÷")
    a = float(partes[0].strip())
    b = float(partes[1].strip())

    resultado = a / b

    if resultado.is_integer():
        resultado = int(resultado)

    return resultado 


def porcentagem(texto_atual):
    partes = texto_atual.split("%")
    separado = partes[0]
    numeros = re.findall(r'\d+', separado)

    a = float(numeros[0])
    b = float(numeros[1])

    b = (b / 100) * a

    if "+" in texto_atual:
        resultado = a + b
    elif "-" in texto_atual:
        resultado = a - b
    elif "x" in texto_atual:
        resultado = a * b
    elif "÷" in texto_atual:
        resultado = a / b

    if resultado.is_integer():
        resultado = int(resultado)

    return resultado
    