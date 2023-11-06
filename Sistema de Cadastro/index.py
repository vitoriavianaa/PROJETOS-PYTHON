import sqlite3
import os
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

numero_id = 0

def verificar_radiobuttons():
    if not (formulario.radioButton.isChecked() or formulario.radioButton_2.isChecked() or formulario.radioButton_3.isChecked() or formulario.radioButton_4.isChecked()):
        QtWidgets.QMessageBox.critical(None, "Erro", "Você deve marcar pelo menos uma categoria antes de salvar.")
        return False
    return True

def principal():
  primeiro_campo = formulario.lineEdit.text()
  segundo_campo = formulario.lineEdit_2.text() 
  terceiro_campo = formulario.lineEdit_3.text()  

  if not verificar_radiobuttons():
      return

  categoria = ""

  if formulario.radioButton.isChecked():
    categoria = "catraca"
  elif formulario.radioButton_2.isChecked():
    categoria = "coletor"
  elif formulario.radioButton_3.isChecked():
   categoria = "controladora"
  elif formulario.radioButton_4.isChecked():
    categoria = "peças"

  if not primeiro_campo or not segundo_campo:
      QtWidgets.QMessageBox.critical(None, "Erro", "Os campos 'Nome' e 'Código' não podem estar vazios.")
      return
  
  salvar_dados(primeiro_campo, segundo_campo, terceiro_campo, categoria)
  
  formulario.lineEdit.setText("")
  formulario.lineEdit_2.setText("")
  formulario.lineEdit_3.setText("")

  if formulario.radioButton.isChecked():
    formulario.radioButton.setAutoExclusive(False)
    formulario.radioButton.setChecked(False)
    formulario.radioButton.setAutoExclusive(True)
  elif formulario.radioButton_2.isChecked():
    formulario.radioButton_2.setAutoExclusive(False)
    formulario.radioButton_2.setChecked(False)
    formulario.radioButton_2.setAutoExclusive(True)
  elif formulario.radioButton_3.isChecked():
    formulario.radioButton_3.setAutoExclusive(False)
    formulario.radioButton_3.setChecked(False)
    formulario.radioButton_3.setAutoExclusive(True)
  elif formulario.radioButton_4.isChecked():
    formulario.radioButton_4.setAutoExclusive(False)
    formulario.radioButton_4.setChecked(False)
    formulario.radioButton_4.setAutoExclusive(True)


def salvar_dados(primeiro_campo, segundo_campo, terceiro_campo, categoria):
  conexao = sqlite3.connect(nome)
  cursor = conexao.cursor()
  comando = "INSERT INTO PRODUTOS (NOME, CODIGO, DESCRICAO, CATEGORIA) VALUES (?, ?, ?, ?)"
  dados = (str(primeiro_campo), str(segundo_campo), str(terceiro_campo), categoria)
  cursor.execute(comando, dados)
  conexao.commit()
  print("Dados adicionados com sucesso.")


def ler_dados():
  conexao = sqlite3.connect(nome)
  cursor = conexao.cursor()
  comando = "SELECT * FROM PRODUTOS"
  cursor.execute(comando)
  dados_lidos = cursor.fetchall()

  segunda_tela.tableWidget.setRowCount(len(dados_lidos))
  segunda_tela.tableWidget.setColumnCount(5)

  for linha in range(0, len(dados_lidos)):
    for coluna in range(0, 5):
      segunda_tela.tableWidget.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_lidos[linha][coluna])))

def buscar_dados():
  item = segunda_tela.lineEdit.text().lower()

  if item == '*':
    conexao = sqlite3.connect(nome)
    cursor = conexao.cursor()
    comando = "SELECT * FROM PRODUTOS"
    cursor.execute(comando)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)

    for linha in range(0, len(dados_lidos)):
      for coluna in range(0, 5):
        segunda_tela.tableWidget.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_lidos[linha][coluna])))
    segunda_tela.lineEdit.clear()  

  else:
    conexao = sqlite3.connect(nome)
    cursor = conexao.cursor()
    comando = "SELECT * FROM PRODUTOS WHERE CATEGORIA = ? OR NOME = ? OR CAST(CODIGO as varchar) = ?"
    dados = (str(item), str(item), str(item))
    cursor.execute(comando, dados)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)

    for linha in range(0, len(dados_lidos)):
      for coluna in range(0, 5):
        segunda_tela.tableWidget.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_lidos[linha][coluna])))
    segunda_tela.lineEdit.clear() 


def editar_item():
  global numero_id
  linha = segunda_tela.tableWidget.currentRow()
  
  conexao = sqlite3.connect(nome)
  cursor = conexao.cursor()
  cursor.execute("SELECT ID FROM PRODUTOS")
  dados_lidos = cursor.fetchall()
  valor_id = dados_lidos[linha][0]
  cursor.execute("SELECT * FROM PRODUTOS WHERE ID =" + str(valor_id))
  produto = cursor.fetchall() 
  """ irá trazer tudo que o cursor buscou anteriormente """
  
  numero_id = valor_id

  editar_tela.lineEdit.setText(str(produto[0][1]))
  editar_tela.lineEdit_2.setText(str(produto[0][2]))
  editar_tela.lineEdit_3.setText(str(produto[0][3]))
  editar_tela.lineEdit_4.setText(str(produto[0][4]))
  editar_tela.show()

def salvar_dados_editados():
  global numero_id

  nome = editar_tela.lineEdit.text()
  codigo = editar_tela.lineEdit_2.text()
  descricao = editar_tela.lineEdit_3.text()
  categoria = editar_tela.lineEdit_4.text()

  conexao = sqlite3.connect("SISTEMA_CADASTRO.db")
  cursor = conexao.cursor()
  cursor.execute(f"UPDATE PRODUTOS SET NOME = '{str(nome)}', CODIGO = '{str(codigo)}', DESCRICAO = '{str(descricao)}', CATEGORIA = '{str(categoria)}' WHERE ID = '{str(numero_id)}'")
  conexao.commit()
  print("Dados atualizados com sucesso.")

  editar_tela.close()
  ler_dados()


def excluir_item():
  linha = segunda_tela.tableWidget.currentRow()

  if linha < 0:
        return
    
  reply = QMessageBox.question(None, "Confirmação", "Deseja realmente excluir este item?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    
  if reply == QMessageBox.Yes:
        segunda_tela.tableWidget.removeRow(linha)

  conexao = sqlite3.connect(nome)
  cursor = conexao.cursor()
  cursor.execute("SELECT ID FROM PRODUTOS")
  dados_lidos = cursor.fetchall()
  valor_id = dados_lidos[linha][0]
  cursor.execute("DELETE FROM PRODUTOS WHERE ID =" + str(valor_id))
  conexao.commit()

def chama_tela_do_formulario():
  segunda_tela.close()
  formulario.show()


def chama_tela_de_listar():
  formulario.close()
  segunda_tela.show()
  ler_dados()

nome = "SISTEMA_CADASTRO.db"

if not os.path.exists(nome):
  conexao = sqlite3.connect(nome)
  print("Conexão bem sucedida")

  cursor = conexao.cursor()
  cursor.execute('''CREATE TABLE PRODUTOS (
                    ID INTEGER PRIMARY KEY,
                    NOME TEXT,
                    CODIGO TEXT,
                    DESCRICAO TEXT,
                    CATEGORIA TEXT
                )''')

  conexao.commit() 
   
   
app = QtWidgets.QApplication([])

formulario = uic.loadUi("formulario.ui")
segunda_tela = uic.loadUi("listar_dados.ui")
editar_tela = uic.loadUi("tela_edicao.ui")



formulario.pushButton.clicked.connect(principal)
formulario.pushButton_2.clicked.connect(chama_tela_de_listar)

segunda_tela.pushButton.clicked.connect(editar_item)
segunda_tela.pushButton_2.clicked.connect(excluir_item)
segunda_tela.pushButton_3.clicked.connect(chama_tela_do_formulario)
segunda_tela.pushButton_4.clicked.connect(buscar_dados)

editar_tela.pushButton.clicked.connect(salvar_dados_editados)

formulario.show()
app.exec()