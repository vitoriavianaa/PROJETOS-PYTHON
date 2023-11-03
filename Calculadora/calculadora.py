import acionamento_numeros
import acionamento_simbolos_operacoes
import acionamento_botoes_acao
from PyQt5 import uic, QtWidgets

app = QtWidgets.QApplication([])
interface = uic.loadUi("./interface.ui")

# Não permite que o usuário consiga editar o lineEdit, ou seja, fica inacessível como uma calculadora usual
interface.textEdit.setReadOnly(True)

# Aqui faço o acionamento dos botoões ligados com suas respectivas funções

# Acionamento de números e o ponto
interface.pushButton_17.clicked.connect(lambda: acionamento_numeros.adiciona_zero(interface))
interface.pushButton_13.clicked.connect(lambda: acionamento_numeros.adiciona_um(interface))
interface.pushButton_14.clicked.connect(lambda: acionamento_numeros.adiciona_dois(interface))
interface.pushButton_15.clicked.connect(lambda: acionamento_numeros.adiciona_tres(interface))
interface.pushButton_9.clicked.connect(lambda: acionamento_numeros.adiciona_quatro(interface))
interface.pushButton_10.clicked.connect(lambda: acionamento_numeros.adiciona_cinco(interface))
interface.pushButton_11.clicked.connect(lambda: acionamento_numeros.adiciona_seis(interface))
interface.pushButton_5.clicked.connect(lambda: acionamento_numeros.adiciona_sete(interface))
interface.pushButton_6.clicked.connect(lambda: acionamento_numeros.adiciona_oito(interface))
interface.pushButton_7.clicked.connect(lambda: acionamento_numeros.adiciona_nove(interface))
interface.pushButton_18.clicked.connect(lambda: acionamento_numeros.adiciona_ponto(interface))

# Acionamento dos caracteres de operação
interface.pushButton.clicked.connect(lambda: acionamento_simbolos_operacoes.aciona_porcentagem(interface))
interface.pushButton_16.clicked.connect(lambda: acionamento_simbolos_operacoes.aciona_soma(interface))
interface.pushButton_12.clicked.connect(lambda: acionamento_simbolos_operacoes.aciona_subtracao(interface))
interface.pushButton_8.clicked.connect(lambda: acionamento_simbolos_operacoes.aciona_divisao(interface))
interface.pushButton_4.clicked.connect(lambda: acionamento_simbolos_operacoes.aciona_multiplicacao(interface))

# Acionamento dos botões de ação
interface.pushButton_3.clicked.connect(lambda: acionamento_botoes_acao.excluir_ultimo_item(interface))
interface.pushButton_2.clicked.connect(lambda: acionamento_botoes_acao.limpar(interface))
interface.pushButton_19.clicked.connect(lambda: acionamento_botoes_acao.igual(interface))

interface.show()
app.exec()