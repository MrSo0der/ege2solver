import os, sys
from itertools import cycle

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

from solver import main_algorithm
from ui import Ui_MainWindow


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class App(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        MainWindow.setWindowIcon(QIcon(resource_path("laptop.ico")))
        self.btn_i_container.addButton(self.btn_i_1, 0)
        self.btn_i_container.addButton(self.btn_i_2, 1)
        self.btn_i_container.addButton(self.btn_i_3, 2)
        self.btn_i_container.addButton(self.btn_i_4, 3)
        self.btn_i_container.addButton(self.btn_i_5, 4)
        self.btn_i_container.addButton(self.btn_i_6, 5)
        self.btn_i_container.addButton(self.btn_i_7, 6)
        self.btn_i_container.addButton(self.btn_i_8, 7)
        self.btn_i_container.addButton(self.btn_i_9, 8)
        self.btn_i_container.addButton(self.btn_i_10, 9)
        self.btn_i_container.addButton(self.btn_i_11, 10)
        self.btn_i_container.addButton(self.btn_i_12, 11)
        self.btn_i_container.addButton(self.btn_i_13, 12)
        self.btn_i_container.addButton(self.btn_i_14, 13)
        self.btn_i_container.addButton(self.btn_i_15, 14)
        self.btn_i_container.addButton(self.btn_i_16, 15)
        self.btn_i_container.addButton(self.btn_i_17, 16)
        self.btn_i_container.addButton(self.btn_i_18, 17)
        self.btn_i_container.addButton(self.btn_i_19, 18)
        self.btn_i_container.addButton(self.btn_i_20, 19)
        self.btn_i_container.addButton(self.btn_i_21, 20)
        self.btn_i_container.addButton(self.btn_i_22, 21)
        self.btn_i_container.addButton(self.btn_i_23, 22)
        self.btn_i_container.addButton(self.btn_i_24, 23)
        self.btn_i_container.addButton(self.btn_i_25, 24)
        self.btn_i_container.addButton(self.btn_i_26, 25)
        self.btn_i_container.addButton(self.btn_i_27, 26)
        self.btn_i_container.addButton(self.btn_i_28, 27)
        self.btn_i_container.addButton(self.btn_i_29, 28)
        self.btn_i_container.addButton(self.btn_i_30, 29)
        self.btn_i_container.addButton(self.btn_i_31, 30)
        self.btn_i_container.addButton(self.btn_i_32, 31)
        self.click()
        self.cboxChanged()


    def click(self):
        self.btn_br_open.clicked.connect(lambda: self.output('('))
        self.btn_br_close.clicked.connect(lambda: self.output(')'))
        self.btn_accord.clicked.connect(lambda: self.output('≡'))
        self.btn_1.clicked.connect(lambda: self.output('1'))
        self.btn_0.clicked.connect(lambda: self.output('0'))
        self.btn_not.clicked.connect(lambda: self.output('¬'))
        self.btn_or.clicked.connect(lambda: self.output('∨'))
        self.btn_and.clicked.connect(lambda: self.output('∧'))
        self.btn_imp.clicked.connect(lambda: self.output('→'))
        self.btn_w.clicked.connect(lambda: self.output('w'))
        self.btn_x.clicked.connect(lambda: self.output('x'))
        self.btn_y.clicked.connect(lambda: self.output('y'))
        self.btn_z.clicked.connect(lambda: self.output('z'))

        self.btn_equal.clicked.connect(self.equalOutput)
        self.btn_back.clicked.connect(self.back)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_i_container.buttonClicked.connect(self.cycler)
        self.btn_cross.clicked.connect(self.destroyer)
        self.btn_check.clicked.connect(self.letUsRoll)

    def output(self, text):
        self.lbl_inst_text += text
        self.txtb_instance.setText(self.lbl_inst_text)

    def equalOutput(self):
        self.lbl_inst_text = '(' + self.lbl_inst_text + ')='
        self.txtb_instance.setText(self.lbl_inst_text)

    def clear(self):
        self.lbl_inst_text = ''
        self.txtb_instance.setText('Выражение (функция)')
        self.lbl_main.setText('Ожидание...')

    def back(self):
        if self.lbl_inst_text[-1] == '=':
            maximum, start, end = 3, 1, -2
        else:
            maximum, start, end = 1, 0, -1
        if len(self.lbl_inst_text) > maximum:
            self.lbl_inst_text = self.lbl_inst_text[start:end]
            self.txtb_instance.setText(self.lbl_inst_text)
        else:
            self.clear()

    def cycler(self, btn):
        btn_index = self.btn_i_container.id(btn)
        btn.setText(value := next(self.cycle_list[btn_index]))
        self.instance_list[btn_index // 4][btn_index % 4] = [int(value) if value != '*' else 2]

    def destroyer(self):
        self.clear()
        self.instance_list = [[[0] for _ in range(4)] for __ in range(8)]
        self.cycle_list = [cycle('1*0') for _ in range(32)]
        for i in range(32):
            self.btn_i_container.button(i).setText('0')


    def cboxChanged(self):
        self.cbox_str_value.currentIndexChanged.connect(self.btnController)

    def btnController(self, current_value):
        current_value += 1
        if current_value > self.str_value:
            for i in range(self.str_value * 4, current_value * 4):
                self.btn_i_container.button(i).setEnabled(True)
        else:
            for i in range(current_value * 4, self.str_value * 4):
                self.btn_i_container.button(i).setEnabled(False)
        self.str_value = current_value


    def letUsRoll(self):
        answer = main_algorithm(self.lbl_inst_text, self.instance_list, self.str_value)
        if type(answer) == str:
            color = 'red'
        else: #type(answer) == list
            answer = 'Ответ получен: ' + ''.join(answer)
            color = 'green'
        self.lbl_main.setText(f"<font color='{color}'>{answer}</font>")

    lbl_inst_text = ''
    str_value = 1
    instance_list = [[[0] for _ in range(4)] for __ in range(8)]
    cycle_list = [cycle('1*0') for _ in range(32)]
    btn_i_container = QtWidgets.QButtonGroup()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    App().setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
