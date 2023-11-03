def aciona_soma(interface):
  texto_atual = interface.textEdit.toPlainText()

  if not any(operador in texto_atual for operador in "+-x÷"):
    if "+" not in texto_atual:
        texto_atual += " + "
        interface.textEdit.setText(texto_atual)

def aciona_divisao(interface):
  texto_atual = interface.textEdit.toPlainText()
  
  if not any(operador in texto_atual for operador in "+-x÷"):
    texto_atual = interface.textEdit.toPlainText()
    if "÷" not in texto_atual:
        texto_atual += " ÷ "
        interface.textEdit.setText(texto_atual)

def aciona_multiplicacao(interface):
  texto_atual = interface.textEdit.toPlainText()
  
  if not any(operador in texto_atual for operador in "+-x÷"):
    texto_atual = interface.textEdit.toPlainText()
    if "x" not in texto_atual:
        texto_atual += " x "
        interface.textEdit.setText(texto_atual)

def aciona_subtracao(interface):
  texto_atual = interface.textEdit.toPlainText()
  
  if not any(operador in texto_atual for operador in "+-x÷"):
    texto_atual = interface.textEdit.toPlainText()
    if "-" not in texto_atual:
        texto_atual += " - "
        interface.textEdit.setText(texto_atual)

def aciona_porcentagem(interface):
 texto_atual = interface.textEdit.toPlainText()
 ult_caracter = texto_atual[-1] if texto_atual else None  

 if ult_caracter not in "-x÷+%":
  texto_atual += "%"  
  interface.textEdit.setText(texto_atual)