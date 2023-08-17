import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PIL import Image, ImageTk
from gnr_model import generate_cluster_image

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'GNR 602 Project'
        self.left = 100
        self.top = 100
        self.width = 700
        self.height = 500
        self.image_width = 300
        self.image_height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create labels and input fields
        self.param_label = QLabel('Parameter k :', self)
        self.param_label.move(20, 20)
        self.param_input = QLineEdit(self)
        self.param_input.move(100, 20)

        self.path_label = QLabel('Input Image :', self)
        self.path_label.move(20, 50)
        self.path_input = QLineEdit(self)
        self.path_input.move(100, 50)

        # Create a file dialog button to select a file
        self.browse_btn = QPushButton('Browse', self)
        self.browse_btn.move(250, 50)
        self.browse_btn.clicked.connect(self.browse_file)

        self.folder_label = QLabel('Output Folder:', self)
        self.folder_label.move(20, 80)
        self.folder_input = QLineEdit(self)
        self.folder_input.move(100, 80)

        # Create a file dialog button to select a file
        self.browse_file_btn = QPushButton('Browse', self)
        self.browse_file_btn.move(250, 80)
        self.browse_file_btn.clicked.connect(self.browse_folder)

        # Create a submit button
        self.submit_btn = QPushButton('Submit', self)
        self.submit_btn.move(120, 120)
        self.submit_btn.clicked.connect(self.submit_form)

        self.folder_label = QLabel('Takes around 30 sec after Submit..', self)
        self.folder_label.move(250, 125)


        self.label = QLabel(self)
        self.label.move(10,150)

        self.label_out = QLabel(self)
        self.label_out.move(320,150)
        self.show()

    def browse_file(self):
        # Open a file dialog to select a file
        filename, _ = QFileDialog.getOpenFileName(self, 'Open file', '.', 'image files (*.jpg *.png)')
        if filename:
            self.path_input.setText(filename)

    def browse_folder(self):
        # Open a folder dialog to select a folder
        foldername = QFileDialog.getExistingDirectory(self, 'Open folder', '.')
        if foldername:
            self.folder_input.setText(foldername)

    def submit_form(self):
        # Get the input parameters and file path and perform the ML operation
        parameter = self.param_input.text()
        input_path = self.path_input.text()
        output_path = self.folder_input.text()
        print(parameter, input_path, output_path)
        # When waiting for generate_cluster_image to finish, show a loading screen
        print("Loading...")
        generate_cluster_image(int(parameter), input_path, output_path)


        pixmap = QPixmap(input_path)
        pixmap = pixmap.scaled(self.image_width, self.image_height, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.label.adjustSize() 

        out_pixmap = QPixmap(output_path + '/out_cluster_texture.jpg')
        out_pixmap = out_pixmap.scaled(self.image_width, self.image_height, QtCore.Qt.KeepAspectRatio)
        self.label_out.setPixmap(out_pixmap)
        self.label_out.adjustSize()
        

        # Call your ML function with the parameter and file path


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    print(ex.param_input.text())
    sys.exit(app.exec_())
