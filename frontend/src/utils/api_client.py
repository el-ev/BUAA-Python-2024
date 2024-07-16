"""
Author: Iz0
Date: 2024-07-16
License: MIT License
Description: 
"""

import hashlib
import grpc

import utils.grpc.plagarism_detection_pb2 as plagarism_detection_pb2
import utils.grpc.plagarism_detection_pb2_grpc as plagarism_detection_pb2_grpc

from utils.error_codes import LoginStatus, RegisterStatus
from config import grpc_server_address


class ApiClient:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ApiClient, cls).__new__(cls)
            cls._instance._initiated = False
        return cls._instance
            
    def __init__(self):
        if self._initiated:
            return
        super().__init__()
        self._initiated = True
        
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = plagarism_detection_pb2_grpc.PlagarismDetectionStub(channel)
        self.token = None
    
    def login(self, username, password) -> LoginStatus:
        try:
            response = self.stub.Login(plagarism_detection_pb2.LoginRequest(username=username, password=hash_password(password)))
            if response.status == plagarism_detection_pb2.LoginResponse.LoginStatus.LOGIN_SUCCESS:
                self.token = response.token
                return LoginStatus.LOGIN_SUCCESS
            else:
                return LoginStatus(response.status)
        except grpc.RpcError as e:
            return LoginStatus.UNKOWN_ERROR
    
    def register(self, username, password) -> RegisterStatus:
        try:
            response = self.stub.Register(plagarism_detection_pb2.RegisterRequest(username=username, password=hash_password(password)))
            return RegisterStatus(response.status)
        except grpc.RpcError as e:
            return RegisterStatus.UNKOWN_ERROR
    
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()