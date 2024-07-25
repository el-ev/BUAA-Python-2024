import time

from config import DB_NAME
from models.task_model import TaskModel
from models.report_model import ReportModel
from services.database_service import DatabaseService

class CheckService:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.db_service = DatabaseService(DB_NAME)
        return cls._instance
    
    def __del__(self):
        self.db_service.close()
        
    def create_task(self, type, owner_id, task_name, main_file_id=None, file_ids=[]) -> TaskModel:
        file_count = len(file_ids)
        if type == 0:
            if main_file_id is None or file_count == 0:
                return None
            query = "INSERT INTO tasks (type, owner_id, task_name, file_count) VALUES (?, ?, ?, ?)"
            args = (type, owner_id, task_name, file_count)
            self.db_service.query(query, args)
        elif type == 1:
            if file_count < 2:
                return None
            query = "INSERT INTO tasks (type, owner_id, task_name, main_file_id, file_count) VALUES (?, ?, ?, ?, ?)"
            args = (type, owner_id, task_name, main_file_id, file_count)
            self.db_service.query(query, args)
        query = "SELECT id FROM tasks WHERE owner_id = ? ORDER BY id DESC LIMIT 1"
        args = (owner_id,)
        result = self.db_service.query(query, args)
        return TaskModel(result[0][0], type, owner_id, main_file_id=main_file_id, file_ids=file_ids)
    
    
    def do_single_check(self, task, owner_id, file_id1, file_id2):
        if task is None:
            return
        # first check if (owner_id, file_id1, file_id2) already exists
        query = "SELECT id FROM reports WHERE owner_id = ? AND file_id1 = ? AND file_id2 = ?"
        args = (owner_id, file_id1, file_id2)
        result = self.db_service.query(query, args)
        if result:
            task.reportIds.append(result[0][0])
            with open(f'report/{result[0][0]}.json', 'r') as f:
                report = ReportModel.fromJson(f.read())
                return report.similarity
        # create a new report
        dist, dup = self.check_plagiarism(file_id1, file_id2)
        query = "INSERT INTO reports (owner_id, file_id1, file_id2, similarity) VALUES (?, ?, ?, ?)"
        args = (owner_id, file_id1, file_id2, dist)
        self.db_service.query(query, args)
        query = "SELECT id FROM reports WHERE owner_id = ? AND file_id1 = ? AND file_id2 = ?"
        result = self.db_service.query(query, args)
        report_id = result[0][0]
        task.reportIds.append(report_id)
        report = ReportModel(report_id, owner_id, file_id1, file_id2, dist, dup)
        with open(f'report/{report_id}.json', 'w') as f:
            f.write(report.to_json())
        return dist
        
    def finish_task(self, task, matrix=None):
        task_id = task.taskId
        if task.taskType == 1:
            if matrix is None:
                raise ValueError("clustering data is required for manyToMany task")
            
        with open(f'task/{task_id}.json', 'w') as f:
            f.write(task.to_json())
            
    def check_plagiarism(file_id1, file_id2):
        # TODO: implement this
        time.sleep(0.5)
        similarity = 0.5
        dup=[{
            "file1": (1 , 2),
            "file2": (1 , 2),
        }]
        return similarity, dup
            
    def clustering(self, matrix):
        # TODO: implement this
        return {0: [1, 2], 1: [3, 4]}