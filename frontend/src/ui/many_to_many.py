import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import itertools
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QTableWidget, QAbstractItemView, QTableWidgetItem, QTabWidget, QPushButton, QMessageBox, QFileDialog, QSizePolicy
    
from models.report_model import ReportModel
from models.task_model import TaskModel
from ui.comparison_page import ComparisonPage
from ui.widgets.graph_widget import GraphWidget, EdgeSelectedSignal, CLUSTER_COLORS
from ui.widgets.filter_widget import FilterWidget, ThresholdChangedSignal
from ui.widgets.dynamic_checkbox_widget import DynamicCheckboxWidget, CheckboxChangedSignal
from ui.widgets.color_hint_text_widget import ColorHintTextWidget

from utils.api_client import ApiClient
from utils.error_codes import ErrorCode
from utils.info_container import InfoContainer

class ManyToManyPage(QWidget):
    def __init__(self):
        super().__init__()
        self.info_container = InfoContainer()
        self.api_client = ApiClient()
        self.active_comparison_pages = []

        self.setWindowTitle("Many to Many Task")
        
        layout = QVBoxLayout()
        tab_widget = QTabWidget()
        tab_widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        
        self.graph_tab = QWidget()
        self._init_graph_tab()
        self.table_widget = QTableWidget()
        self._init_table_tab()
        
        tab_widget.setContentsMargins(0, 0, 0, 0)
        tab_widget.addTab(self.graph_tab, "Graph")
        tab_widget.addTab(self.table_widget, "Table")
        
        cluster_selection_changed_signal = CheckboxChangedSignal()
        self.cluster_select_area = DynamicCheckboxWidget(checkboxChangedSignal=cluster_selection_changed_signal)
        self.cluster_select_area.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        cluster_selection_changed_signal.connect(self._on_cluster_selection_changed)
        
        layout.addWidget(tab_widget)
        layout.addWidget(self.cluster_select_area)
        
        self.setLayout(layout)
        
    def _init_graph_tab(self):
        edge_selected_signal = EdgeSelectedSignal()
        threshold_changed_signal = ThresholdChangedSignal()
        
        layout = QVBoxLayout()
        bottom_layout = QHBoxLayout()
        bottom_layout.setContentsMargins(10, 0, 0, 0)

        self.graph_widget = GraphWidget(edgeSelectedSignal=edge_selected_signal)
        self.graph_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        
        self.filter_widget = FilterWidget(thresholdChangedSignal=threshold_changed_signal)
        self.filter_widget.setFixedHeight(100)
        self.filter_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.graph_label = QLabel()
        self.graph_label.setAlignment(Qt.AlignVCenter)
        self.graph_label.setText(f"Selected Edge count: {1000}")
        label_width = self.graph_label.fontMetrics().boundingRect(self.graph_label.text()).width()
        self.graph_label.setFixedWidth(label_width)
        
        self.export_button = QPushButton()
        self.export_button.setFixedSize(100, 50)
        self.export_button.setText("Export")
        self.export_button.setStyleSheet("""
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
        """)
        
        layout.addWidget(self.graph_widget, 1)
        layout.addLayout(bottom_layout)
        bottom_layout.setAlignment(Qt.AlignBottom)

        bottom_layout.addWidget(self.filter_widget, 1)
        bottom_layout.setAlignment(self.filter_widget, Qt.AlignVCenter)
        bottom_layout.addWidget(self.graph_label, 0)
        bottom_layout.addWidget(self.export_button, 0)
        bottom_layout.setAlignment(self.export_button, Qt.AlignVCenter)
        bottom_layout.setStretch(0, 1)
        
        self.graph_tab.setLayout(layout)

        self.export_button.clicked.connect(self._on_export_button_clicked)
        edge_selected_signal.connect(self._on_edge_selected)
        threshold_changed_signal.connect(self._on_threshold_changed)
        
    def _init_table_tab(self):
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(['One', 'The other', 'Distance'])
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_widget.setAlternatingRowColors(True)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_widget.cellDoubleClicked.connect(self._on_table_row_selected)
        self.table_widget.setStyleSheet("selection-background-color: #A3DFF5")
        
    
    def init_task(self, task_name, task: TaskModel):
        self.setWindowTitle(f"Many to Many Task - {task_name}")
        assert task.taskType == 1
        self.ids = task.fileIds
        self.labels = ["" for _ in range(len(self.ids))]
        self.id_to_index = {label: i for i, label in enumerate(self.ids)}
        for id in self.ids:
            self.labels[self.id_to_index[id]] = self.info_container.get_file_name(id)
        self.clustering = [0 for _ in range(len(self.ids))]
        self.distance_matrix = [[0 for _ in range(len(self.ids))] for _ in range(len(self.ids))]
        self.file_pair_to_report = {}
        for k, v in task.clusters.items():
            for i in v:
                self.clustering[self.id_to_index[i]] = int(k) - 1
        for report_id in task.reportIds:
            report_content = self.info_container.get_report(report_id)
            report = ReportModel.fromJson(report_content)
            file1_id = report.file1Id
            file2_id = report.file2Id
            distance = report.distance
            self.file_pair_to_report[(file1_id, file2_id)] = report_id
            self.distance_matrix[self.id_to_index[file1_id]][self.id_to_index[file2_id]] = distance
            self.distance_matrix[self.id_to_index[file2_id]][self.id_to_index[file1_id]] = distance

        self.graph_widget.setup(self.distance_matrix, 0.25, self.clustering, self.labels)
        self.filter_widget.setup([(i, j, self.distance_matrix[i][j]) for i, j in itertools.combinations(range(len(self.distance_matrix)), 2)])
        self.threshold = 0.25
        self.enabled_clusters = set(self.clustering)
        
        index = 0
        for i in range(len(self.distance_matrix)):
            for j in range(i + 1, len(self.distance_matrix)):
                self.table_widget.insertRow(index)
                self.table_widget.setCellWidget(index, 0, ColorHintTextWidget(f"{self.labels[i]}", CLUSTER_COLORS[self.clustering[i]]))
                self.table_widget.setCellWidget(index, 1, ColorHintTextWidget(f"{self.labels[j]}", CLUSTER_COLORS[self.clustering[j]]))
                self.table_widget.setItem(index, 2, QTableWidgetItem(f"{self.distance_matrix[i][j]:.2f}"))
                index += 1
        self.table_widget.resizeColumnsToContents()
        self.table_widget.sortItems(2)
        
        clusters = {}
        for i, c in enumerate(self.clustering):
            if c not in clusters:
                clusters[c] = []
            clusters[c].append(i)
        self.cluster_select_area.setup(len(clusters), CLUSTER_COLORS)
        
    def _on_edge_selected(self, edge):
        id1 = self.ids[edge[0]]
        id2 = self.ids[edge[1]]
        if id1 > id2:
            id1, id2 = id2, id1
        report_id = self.file_pair_to_report[(id1, id2)]
        comparison_page = ComparisonPage()
        comparison_page.setup(report_id)
        self.active_comparison_pages.append(comparison_page)
        comparison_page.show()
    
    def _on_threshold_changed(self, threshold, count):
        self.threshold = threshold
        self.graph_widget.update_filter(threshold=threshold)
        self.graph_label.setText(f"Threshold: {threshold: .2f}\n\nSelected Edge count: {count}")
        
    def _on_table_row_selected(self, row, column):
        label1 = self.table_widget.cellWidget(row, 0).label.text()
        label2 = self.table_widget.cellWidget(row, 1).label.text()
        id1 = self.ids[self.labels.index(label1)]
        id2 = self.ids[self.labels.index(label2)]
        if id1 > id2:
            id1, id2 = id2, id1
        report_id = self.file_pair_to_report[(id1, id2)]
        comparison_page = ComparisonPage()
        comparison_page.setup(report_id)
        self.active_comparison_pages.append(comparison_page)
        comparison_page.show()        
        
    def _on_cluster_selection_changed(self, checked):
        self.enabled_clusters = set(checked)
        self.graph_widget.update_filter(used_clusters=checked)
        selected_lines = []
        for i, c in enumerate(self.clustering):
            if c in checked:
                selected_lines.append(i)
        data = []
        for i in selected_lines:
            for j in selected_lines:
                if i < j:
                    data.append((i, j, self.distance_matrix[i][j]))
        self.filter_widget.update_data(data)
        
        # Update table
        for i in range(self.table_widget.rowCount()):
            label1 = self.table_widget.cellWidget(i, 0).label.text()
            label2 = self.table_widget.cellWidget(i, 1).label.text()
            if self.clustering[self.labels.index(label1)] not in self.enabled_clusters or self.clustering[self.labels.index(label2)] not in self.enabled_clusters:
                self.table_widget.setRowHidden(i, True)
            else:
                self.table_widget.setRowHidden(i, False)
                
    def _on_export_button_clicked(self):
        file_ids = set()
        for i in range(len(self.ids)):
            if self.clustering[i] not in self.enabled_clusters:
                continue
            for j in range(i + 1, len(self.ids)):
                if self.clustering[j] not in self.enabled_clusters:
                    continue
                if self.distance_matrix[i][j] <= self.threshold:
                    file_ids.add(self.ids[i])
                    file_ids.add(self.ids[j])
        # print(file_ids)
        if not file_ids:
            QMessageBox.warning(self, 'Warning', 'No files to export.', QMessageBox.Ok)
            return
        file_name = f"{time.time()}.zip"
        packpath, _ = QFileDialog.getSaveFileName(self, "代码导出", f"./{file_name}", "Zip (*.zip)")
        if not packpath:
            return
        _, pack_content = self.api_client.download_multiple_files(file_ids)
        if _ != ErrorCode.SUCCESS:
            QMessageBox.critical(self, 'Error', f'{ErrorCode.get_error_message(_)}')
        with open(packpath, 'wb') as f:
            f.write(pack_content)