from datetime import datetime
import os
import sys
from PyQt5.QtCore import Qt, QDateTime, QFileInfo, pyqtSignal, QRect, QSize, QPoint
from PyQt5.QtGui import QFont, QIcon, QCursor
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, \
    QFileDialog, QRadioButton, QTableWidget, QAbstractItemView, \
    QTableWidgetItem, QHeaderView, QStyleOptionButton, QStyle, QMenu, QMessageBox
from models.task_model import TaskModel
from ui.login_history import LoginHistoryWidget
from ui.many_to_many import ManyToManyPage
from ui.one_to_many import OneToManyPage
from ui.widgets.code_editor_widget import CodeEditor
from ui.widgets.progress_widget import start_progress_widget
from utils.error_codes import ErrorCode
from utils.api_client import ApiClient
from utils.info_container import InfoContainer
from ui.login import LoginWindow

class WelcomePage(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.setWindowTitle("Welcome")
        # self.resize(900, 600)
        # self.center()

        self.api_client = ApiClient()
        self.info_container = InfoContainer()
        self.code_editor = CodeEditor()
        self.code_editor.set_editable(False)
        self.code_editor.resize(800, 600)
        self.main_window = main_window

        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                font-family: Arial;
            }
            QLineEdit {
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
            QPushButton {
                padding: 10px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLabel#error_label {
                color: red;
                font-size: 12px;
            }
            QScrollBar:vertical, QScrollBar:horizontal {
                border: none;
                background: #e0e0e0;
                width: 8px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
                background: #a0a0a0;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                height: 0;
                width: 0;
                subcontrol-origin: margin;
            }
            QScrollBar::sub-page:vertical,
            QScrollBar::add-page:vertical {
                background: none;
                width: 0px;
                height: 0px;
            }
            QTableWidget {
               border-radius: 5px;
               font-size: 13px;
            }
        """)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.upload_widget = QWidget()
        layout.addWidget(self.upload_widget)

        title_label = QLabel('<p style="color: green">New Task</p>')
        title_label.setFont(QFont('Arial', 20, QFont.Bold))

        self.task_name_label = QLabel('Task Name')
        self.task_name_input = QLineEdit()
        self.task_name_input.setPlaceholderText('Please enter the task name (Default: Task_Date_Time)')
        # self.task_name_input.setText(self.get_default_name())
        task_name_layout = QHBoxLayout()
        task_name_layout.addWidget(self.task_name_label)
        task_name_layout.addWidget(self.task_name_input)

        self.file_label = QLabel('Upload/Delete Files')
        self.upload_file_button = QPushButton(' Upload Files')
        self.upload_file_button.setIcon(QIcon('assets/Upload.svg'))
        self.upload_file_button.clicked.connect(self.upload_file)
        delete_file_button = QPushButton(' Clear Selected Files')
        delete_file_button.setIcon(QIcon('assets/del.svg'))
        delete_file_button.clicked.connect(self.clear_selected_files)
        file_layout = QHBoxLayout()
        file_layout.addWidget(self.file_label)
        file_layout.addWidget(self.upload_file_button)
        file_layout.addWidget(delete_file_button)

        self.mode_select_label = QLabel('Checking Mode')
        self.check_mode = None
        one2many_button = QRadioButton('One-to-Many')
        group_button = QRadioButton('Many-to-Many (Max 20 files)')
        one2many_button.toggled.connect(self.switch_mode)
        group_button.toggled.connect(self.switch_mode)
        mode_layout = QHBoxLayout()
        mode_layout.addWidget(self.mode_select_label)
        mode_layout.addWidget(one2many_button)
        mode_layout.addWidget(group_button)

        self.target_layout = QHBoxLayout()
        self.target_file_label = QLabel('Target File (one-to-many mode only)')

        self.target_file_button = QPushButton('Click to select the target file')
        self.target_file_button.setStyleSheet("QPushButton::menu-indicator{image:none}")
        self.target_file_button.clicked.connect(self.select_target_file)
        self.target_layout.addWidget(self.target_file_label)
        self.target_layout.addWidget(self.target_file_button)

        self.file_table = QTableWidget()
        self.file_table.verticalHeader().setVisible(False)
        self.file_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.file_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.file_table.setHorizontalHeader(CheckBoxHeader())

        self.file_table.setColumnCount(6)
        self.file_table.setHorizontalHeaderLabels(('     Name ', 'Size', 'Uploaded at', 'Path', 'Op', 'ID'))
        self.file_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.file_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.file_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.file_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.file_table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.file_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.file_table.setFocusPolicy(Qt.NoFocus)
        self.file_table.setAlternatingRowColors(True)
        self.file_table.setColumnHidden(5, True)

        self.file_table.itemPressed.connect(self.toggle_current_checkbox)
        self.file_table.cellDoubleClicked.connect(self.open_file_click)
        self.file_table.cellClicked.connect(self.clear_target_file)

        start_layout = QHBoxLayout()
        login_history_button = QPushButton('Login History')
        self.login_history_widget = LoginHistoryWidget()
        login_history_button.clicked.connect(self.login_history_widget.show)
        start_layout.addWidget(login_history_button)
        
        self.error_label = QLabel()
        self.error_label.setObjectName("error_label")
        self.error_label.setStyleSheet("color: red")
        start_layout.addWidget(self.error_label)
        start_layout.addStretch(1)
        self.history_button = QPushButton('History Tasks')
        start_button = QPushButton('START')
        start_button.clicked.connect(self.start_check)
        start_layout.addWidget(self.history_button)
        start_layout.addWidget(start_button)

        upload_layout = QVBoxLayout()
        upload_layout.addWidget(title_label)
        upload_layout.addLayout(task_name_layout)
        upload_layout.addLayout(file_layout)
        upload_layout.addLayout(mode_layout)
        upload_layout.addWidget(self.file_table)
        upload_layout.addLayout(start_layout)
        self.upload_widget.setLayout(upload_layout)

    def clear_target_file(self, row, col):
        if col == 0:
            self.target_file_button.setText('Click to select the target file')
    
    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def get_default_name(self):
        datetime = QDateTime.currentDateTime()
        time = list(datetime.toString().split())[3]
        year = datetime.date().year()
        month = datetime.date().month()
        day = datetime.date().day()
        return 'Task_' + str(year) + '-' + str(month) + '-' + str(day) + '_' + time

    def get_current_time(self):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return current_time

    def toggle_current_checkbox(self):
        item = self.file_table.item(self.file_table.currentRow(), 0)
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)
        self.target_file_button.setText('Click to select the target file')


    def get_uploaded_files(self):
        self.info_container.clear_file_info()
        _, file_list = self.api_client.get_uploaded_file_list()
        if _ != ErrorCode.SUCCESS:
            QMessageBox.critical(self, 'Error', f'Failed to get uploaded files: {ErrorCode.get_error_message(_)}')
            return
        for file_info in file_list:
            # row = self.file_table.rowCount()
            self.info_container.add_file_info(file_info[0], os.path.basename(file_info[1]), file_info[2], file_info[1], file_info[3])
            if file_info[4] == 1:
                continue
            row = 0
            self.file_table.insertRow(row)

            checkbox = QTableWidgetItem(os.path.basename(file_info[1]))
            checkbox.setCheckState(Qt.Unchecked)
            self.file_table.setItem(row, 0, checkbox)
            size = file_info[2]
            if size < 1024:
                size_str = f"{size} B"
            elif size < 1024 * 1024:
                size_str = f"{size / 1024:.2f} KB"
            else:
                size_str = f"{size / 1024 / 1024:.2f} MB"
            size_item = QTableWidgetItem(size_str)
            size_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.file_table.setItem(row, 1, size_item)
            self.file_table.setItem(row, 2, QTableWidgetItem(file_info[3]))
            self.file_table.setItem(row, 3, QTableWidgetItem(file_info[1]))
            self.file_table.setItem(row, 5, QTableWidgetItem(str(file_info[0])))

            widget = QWidget()
            widget_layout = QHBoxLayout()

            open_button = QPushButton()
            open_button.setIcon(QIcon('assets/Open.svg'))
            open_button.setIconSize(QSize(10, 10))
            open_button.setStyleSheet("background-color: green;border-radius: 9px")
            open_button.setFixedSize(18, 18)
            open_button.clicked.connect(self.open_file_btn)

            delete_button = QPushButton()
            delete_button.setIcon(QIcon('assets/Delete.svg'))
            delete_button.setIconSize(QSize(10, 10))
            delete_button.setStyleSheet("background-color: red;border-radius: 9px")
            delete_button.setFixedSize(18, 18)
            delete_button.clicked.connect(self.delete_file)

            widget_layout.addWidget(open_button)
            widget_layout.addWidget(delete_button)
            widget.setLayout(widget_layout)
            widget_layout.setContentsMargins(5, 2, 5, 2)
            self.file_table.setCellWidget(row, 4, widget)
        # self.info_container.update_file_info()


    def upload_file(self):
        self.files, _ = QFileDialog.getOpenFileNames(self, "Upload Files", "./", "Python (*.py)")
        current_time = self.get_current_time()
        for file in self.files:
            info = QFileInfo(file)
            # row = self.file_table.rowCount()
            row = 0
            self.file_table.insertRow(row)

            checkbox = QTableWidgetItem(info.fileName())
            checkbox.setCheckState(Qt.Checked)
            self.file_table.setItem(row, 0, checkbox)
            size = info.size()
            if size < 1024:
                size_str = f"{size} B"
            elif size < 1024 * 1024:
                size_str = f"{size / 1024:.2f} KB"
            else:
                size_str = f"{size / 1024 / 1024:.2f} MB"
            size_item = QTableWidgetItem(size_str)
            size_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.file_table.setItem(row, 1, size_item)
            self.file_table.setItem(row, 2, QTableWidgetItem(current_time))
            self.file_table.setItem(row, 3, QTableWidgetItem(info.filePath()))

            widget = QWidget()
            widget_layout = QHBoxLayout()

            open_button = QPushButton()
            open_button.setIcon(QIcon('assets/Open.svg'))
            open_button.setIconSize(QSize(10, 10))
            open_button.setStyleSheet("background-color: green;border-radius: 9px")
            open_button.setFixedSize(18, 18)
            open_button.clicked.connect(self.open_file_btn)

            delete_button = QPushButton()
            delete_button.setIcon(QIcon('assets/Delete.svg'))
            delete_button.setIconSize(QSize(10, 10))
            delete_button.setStyleSheet("background-color: red;border-radius: 9px")
            delete_button.setFixedSize(18, 18)
            delete_button.clicked.connect(self.delete_file)

            widget_layout.addWidget(open_button)
            widget_layout.addWidget(delete_button)
            widget.setLayout(widget_layout)
            widget_layout.setContentsMargins(5, 2, 5, 2)
            self.file_table.setCellWidget(row, 4, widget)

            _, file_id = self.api_client.upload_file(file)
            if _ != ErrorCode.SUCCESS:
                QMessageBox.critical(self, 'Error', f'Failed to upload files: {ErrorCode.get_error_message(_)}')
                self.file_table.removeRow(row)
                return
            self.file_table.setItem(row, 5, QTableWidgetItem(str(file_id)))
            self.info_container.add_file_info(file_id, info.fileName(), size, info.filePath(), current_time)

        if self.file_table.rowCount() > 0:
            self.file_label.setStyleSheet("color: black")
            self.error_label.clear()

    def open_file_btn(self):
        x = self.sender().parentWidget().frameGeometry().x()
        y = self.sender().parentWidget().frameGeometry().y()
        row = self.file_table.indexAt(QPoint(x, y)).row()
        file_id = int(self.file_table.item(row, 5).text())
        file_name = self.file_table.item(row, 0).text()
        self.open_file(file_id, file_name)

    def open_file_click(self, row, col):
        file_id = int(self.file_table.item(row, 5).text())
        file_name = self.file_table.item(row, 0).text()
        self.open_file(file_id, file_name)
    
    def open_file(self, file_id, file_name):
        if not os.path.exists(f'cache/files/file_{file_id}.py'):
            _, file_content = self.api_client.download_file(file_id)
            if _ == ErrorCode.SUCCESS:
                with open(f'cache/files/file_{file_id}.py', 'wb') as f:
                    f.write(file_content)
            else:
                QMessageBox.critical(self, 'Error', f'Failed to get file: {ErrorCode.get_error_message(_)}')
        with open(f'cache/files/file_{file_id}.py', 'r', encoding='utf-8') as f:
            content = f.read()
        self.code_editor.set_text(content)
        self.code_editor.setWindowTitle(file_name)
        self.code_editor.show()

    def delete_file(self):
        x = self.sender().parentWidget().frameGeometry().x()
        y = self.sender().parentWidget().frameGeometry().y()
        row = self.file_table.indexAt(QPoint(x, y)).row()
        if self.file_table.item(row, 0).checkState() == Qt.Checked:
            self.target_file_button.setText('Click to select the target file')
        
        file_id = int(self.file_table.item(row, 5).text())
        self.delete_file_cache(file_id)
        self.file_table.removeRow(row)
    
    def clear_selected_files(self):
        for row in range(self.file_table.rowCount() - 1, -1, -1):
            if self.file_table.item(row, 0).checkState() == Qt.Checked:
                file_id = int(self.file_table.item(row, 5).text())
                self.delete_file_cache(file_id)
                self.file_table.removeRow(row)
        self.target_file_button.setText('Click to select the target file')

    def delete_file_cache(self, file_id):
        # if not os.path.exists(f'cache/files/file_{file_id}.py'):
        #     _, file_content = self.api_client.download_file(file_id)
        #     if _ == ErrorCode.SUCCESS:
        #         with open(f'cache/files/file_{file_id}.py', 'wb') as f:
        #             f.write(file_content)
        #     else:
        #         QMessageBox.critical(self, 'Error', f'Failed to delete file: {ErrorCode.get_error_message(_)}')
        _ = self.api_client.delete_file(file_id)
        if _ != ErrorCode.SUCCESS:
            QMessageBox.critical(self, 'Error', f'Failed to delete file: {ErrorCode.get_error_message(_)}')
    
    def switch_mode(self):
        sender = self.sender()
        self.mode_select_label.setStyleSheet("color: black")
        self.error_label.clear()
        if sender.text() == 'One-to-Many':
            if sender.isChecked():
                self.check_mode = 0
                self.upload_widget.layout().insertLayout(5, self.target_layout)
                self.target_file_button.show()
                self.target_file_label.show()
            else:
                self.target_file_button.hide()
                self.target_file_label.hide()
                self.upload_widget.layout().removeItem(self.target_layout)
        elif sender.text() == 'Many-to-Many (Max 20 files)':
            if sender.isChecked():
                self.check_mode = 1

    def select_target_file(self):
        menu = QMenu()
        flag = False
        cnt = 1
        self.target_files = []
        for row in range(self.file_table.rowCount()):
            if self.file_table.item(row, 0).checkState() == Qt.Checked:
                action = menu.addAction(str(cnt) + ': ' + self.file_table.item(row, 0).text())
                action.triggered.connect(self.set_target_file)
                flag = True
                cnt += 1
                self.target_files.append(self.file_table.item(row, 5).text())
        if flag:
            menu.exec_(QPoint(QCursor.pos().x(), QCursor.pos().y()))
        else:
            QMessageBox.warning(self, 'Prompt', 'Please check all the files to be checked first.')

    def set_target_file(self):
        self.target_file_button.setText(self.sender().text())
        self.target_file_label.setStyleSheet("color: black")

    def start_check(self):
        self.error_label.setStyleSheet("color: red")
        if not self.file_table.rowCount() > 0:
            self.file_label.setStyleSheet("color: red")
            self.error_label.setText('Please upload files to be checked')
            return
        elif self.check_mode is None:
            self.mode_select_label.setStyleSheet("color: red")
            self.error_label.setText('Please select the checking mode')
            return
        elif self.check_mode == 0 and self.target_file_button.text() == 'Click to select the target file':
            self.target_file_label.setStyleSheet("color: red")
            self.error_label.setText('Please select the target file')
            return

        file_ids = []
        cnt = 0
        for row in range(self.file_table.rowCount()):
            if self.file_table.item(row, 0).checkState() == Qt.Checked:
                file_ids.append(int(self.file_table.item(row, 5).text()))
                cnt += 1
        if cnt < 2:
            self.error_label.setStyleSheet("color: red")
            self.error_label.setText('Please select at least two files')
            return
        
        if cnt > 20 and self.check_mode == 1:
            self.error_label.setStyleSheet("color: red")
            self.error_label.setText('Many-to-Many mode can only select up to 20 files')
            return
        
        self.error_label.setStyleSheet("color: green")
        self.error_label.setText('Success!')

        if self.task_name_input.text() == '':
            task_name = self.get_default_name()
        else:
            task_name = self.task_name_input.text()
        
        self.main_window.hide()
        if self.check_mode == 0:       
            signal = start_progress_widget("Checking...", len(file_ids))
            main_file = self.target_file_button.text()
            main_file_id = int(self.target_files[int(main_file[:main_file.find(':')])-1])
            file_ids.remove(main_file_id)
            _, task_str = self.api_client.one_to_many_check(task_name, main_file_id, file_ids, signal)
            signal.emit(-1)
        else:
            signal = start_progress_widget("Checking...", len(file_ids) * (len(file_ids) - 1) // 2)
            _, task_str = self.api_client.many_to_many_check(task_name, file_ids, signal)
            signal.emit(-1)

        self.main_window.show_for_api()
        
        if _ != ErrorCode.SUCCESS:
            QMessageBox.critical(self, 'Error', f'Failed to start check: {ErrorCode.get_error_message(_)}')
            return
        
        task = TaskModel.fromJson(task_str)
        for file_id in task.fileIds:
            if not os.path.exists(f'cache/files/file_{file_id}.py'):
                _, file_content = self.api_client.download_file(file_id)
                if _ == ErrorCode.SUCCESS:
                    with open(f'cache/files/file_{file_id}.py', 'wb') as f:
                        f.write(file_content)
                else:
                    QMessageBox.critical(self, 'Error', f'Failed to get file: {ErrorCode.get_error_message(_)}')
        
        for report_id in task.reportIds:
            if not os.path.exists(f'cache/reports/report_{report_id}.json'):
                _, report_content = self.api_client.GetReport(report_id)
                if _ == ErrorCode.SUCCESS:
                    with open(f'cache/reports/report_{report_id}.json', 'w') as f:
                        f.write(report_content)
                else:
                    QMessageBox.critical(self, 'Error', f'Failed to get report: {ErrorCode.get_error_message(_)}')

        if task.taskType == 0:
            main_file_id = task.mainFileId
            if not os.path.exists(f'cache/files/file_{main_file_id}.py'):
                _, file_content = self.api_client.download_file(main_file_id)
                if _ == ErrorCode.SUCCESS:
                    with open(f'cache/files/file_{main_file_id}.py', 'wb') as f:
                        f.write(file_content)
                else:
                    QMessageBox.critical(self, 'Error', f'Failed to get file: {ErrorCode.get_error_message(_)}')
        
        if self.check_mode == 0:
            self.check_page = OneToManyPage()
        else:
            self.check_page = ManyToManyPage()
        self.check_page.init_task(task_name, task)
        self.check_page.show()            


class CheckBoxHeader(QHeaderView):
    select_all_clicked = pyqtSignal(bool)

    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(CheckBoxHeader, self).__init__(orientation, parent)
        self.isOn = False
        self.select_all_clicked.connect(self.toggle_all_checkboxes)

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        super(CheckBoxHeader, self).paintSection(painter, rect, logicalIndex)
        painter.restore()

        if logicalIndex == 0:
            option = QStyleOptionButton()
            option.rect = QRect(3, 6, 10, 10)
            option.state = QStyle.State_Enabled | QStyle.State_Active
            if self.isOn:
                option.state |= QStyle.State_On
            else:
                option.state |= QStyle.State_Off
            self.style().drawControl(QStyle.CE_CheckBox, option, painter)

    def mousePressEvent(self, event):
        index = self.logicalIndexAt(event.pos())
        if 0 == index:
            if self.isOn:
                self.isOn = False
            else:
                self.isOn = True
            self.select_all_clicked.emit(self.isOn)
            self.updateSection(0)
        super(CheckBoxHeader, self).mousePressEvent(event)

    def toggle_all_checkboxes(self, check):
        table = self.parent()
        for row in range(table.rowCount()):
            item = table.item(row, 0)
            if check:
                item.setCheckState(Qt.Checked)
            else:
                item.setCheckState(Qt.Unchecked)


if __name__ == "__main__":
    PyQt5.QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    app = QApplication(sys.argv)

    welcome_page = WelcomePage()
    welcome_page.show()
    exit(app.exec_())
