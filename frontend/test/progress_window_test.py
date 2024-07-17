import sys

sys.path.append("src")

import time
from PyQt5.QtWidgets import QApplication

from ui.progress import ProgressWindow, ProgressSignal

if __name__ == "__main__":
    app = QApplication(sys.argv)
    progress_window = ProgressWindow("Downloading files", 100)
    signal = ProgressSignal()
    signal.update.connect(progress_window.update_progress)
    progress_window.show()
    for i in range(100):
        signal.update.emit(i + 1)
        app.processEvents()
        time.sleep(0.1)
    progress_window.close()
    exit()