import operacoes
b = 0.0

def limpar(interface):
    interface.textEdit.clear()

def excluir_ultimo_item(interface):
    texto_atual = interface.textEdit.toPlainText()
    texto_atual = texto_atual.strip() 
    if texto_atual:  
        texto_atual = texto_atual[:-1]  
        texto_atual = texto_atual.strip()
        interface.textEdit.setText(texto_atual)


def igual(interface):
    texto_atual = interface.textEdit.toPlainText()

    if "%" in texto_atual:
      resultado = operacoes.porcentagem(texto_atual)
    else:
      if "+" in texto_atual:
        resultado = operacoes.soma(texto_atual)
      elif "-" in texto_atual:
        resultado = operacoes.subtracao(texto_atual)
      elif "x" in texto_atual:
        resultado = operacoes.multiplicacao(texto_atual)
      elif "÷" in texto_atual:
        resultado = operacoes.divisao(texto_atual)
      
    interface.textEdit.setText(str(resultado))
