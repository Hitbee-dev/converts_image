from PIL import Image
import sys
from PyQt5.QtWidgets import *
import pillow_heif

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setAcceptDrops(True)
        grid = QGridLayout()
        self.setLayout(grid)

        label1 = QLabel("HEIC파일을 드래그하세요.")
        grid.addWidget(label1, 0, 0)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            print(f)
            heif_file = pillow_heif.read_heif(f)
            image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            )

            image.save(f"./{f.split('/')[-1].split('.')[0]}.png", format("png"))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        self.setWindowTitle('HEIC to PNG')
        self.resize(400, 200)
        self.center()
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   ex.show()
   sys.exit(app.exec_())