# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import generated.plagiarism_detection_pb2 as plagiarism__detection__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in plagiarism_detection_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class PingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
                '/plagiarism_detection.PingService/Ping',
                request_serializer=plagiarism__detection__pb2.PingRequest.SerializeToString,
                response_deserializer=plagiarism__detection__pb2.PingResponse.FromString,
                _registered_method=True)


class PingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=plagiarism__detection__pb2.PingRequest.FromString,
                    response_serializer=plagiarism__detection__pb2.PingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'plagiarism_detection.PingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('plagiarism_detection.PingService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/plagiarism_detection.PingService/Ping',
            plagiarism__detection__pb2.PingRequest.SerializeToString,
            plagiarism__detection__pb2.PingResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class AuthServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Login = channel.unary_unary(
                '/plagiarism_detection.AuthService/Login',
                request_serializer=plagiarism__detection__pb2.LoginRequest.SerializeToString,
                response_deserializer=plagiarism__detection__pb2.LoginResponse.FromString,
                _registered_method=True)
        self.Register = channel.unary_unary(
                '/plagiarism_detection.AuthService/Register',
                request_serializer=plagiarism__detection__pb2.RegisterRequest.SerializeToString,
                response_deserializer=plagiarism__detection__pb2.RegisterResponse.FromString,
                _registered_method=True)
        self.GetLoginHistory = channel.unary_unary(
                '/plagiarism_detection.AuthService/GetLoginHistory',
                request_serializer=plagiarism__detection__pb2.GetLoginHistoryRequest.SerializeToString,
                response_deserializer=plagiarism__detection__pb2.GetLoginHistoryResponse.FromString,
                _registered_method=True)


class AuthServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLoginHistory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=plagiarism__detection__pb2.LoginRequest.FromString,
                    response_serializer=plagiarism__detection__pb2.LoginResponse.SerializeToString,
            ),
            'Register': grpc.unary_unary_rpc_method_handler(
                    servicer.Register,
                    request_deserializer=plagiarism__detection__pb2.RegisterRequest.FromString,
                    response_serializer=plagiarism__detection__pb2.RegisterResponse.SerializeToString,
            ),
            'GetLoginHistory': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLoginHistory,
                    request_deserializer=plagiarism__detection__pb2.GetLoginHistoryRequest.FromString,
                    response_serializer=plagiarism__detection__pb2.GetLoginHistoryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'plagiarism_detection.AuthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('plagiarism_detection.AuthService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AuthService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/plagiarism_detection.AuthService/Login',
            plagiarism__detection__pb2.LoginRequest.SerializeToString,
            plagiarism__detection__pb2.LoginResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/plagiarism_detection.AuthService/Register',
            plagiarism__detection__pb2.RegisterRequest.SerializeToString,
            plagiarism__detection__pb2.RegisterResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetLoginHistory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/plagiarism_detection.AuthService/GetLoginHistory',
            plagiarism__detection__pb2.GetLoginHistoryRequest.SerializeToString,
            plagiarism__detection__pb2.GetLoginHistoryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class FileServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadFile = channel.stream_unary(
                '/plagiarism_detection.FileService/UploadFile',
                request_serializer=plagiarism__detection__pb2.UploadFileRequest.SerializeToString,
                response_deserializer=plagiarism__detection__pb2.UploadFileResponse.FromString,
                _registered_method=True)
        self.GetUploadedFileList = channel.unary_unary(
                '/plagiarism_detection.FileService/GetUploadedFileList',
                request_serializer=plagiarism__detection__pb2.GetUploadedFileListRequest.SerializeToString,
                response_deserializer=plagiarism__detection__pb2.GetUploadedFileListResponse.FromString,
                _registered_method=True)
        self.DownloadFile = channel.unary_stream(
                '/plagiarism_detection.FileService/DownloadFile',
                request_serializer=plagiarism__detection__pb2.DownloadFileRequest.SerializeToString,
                response_deserializer=plagiarism__detection__pb2.DownloadFileResponse.FromString,
                _registered_method=True)
        self.DownloadMultipleFiles = channel.unary_stream(
                '/plagiarism_detection.FileService/DownloadMultipleFiles',
                request_serializer=plagiarism__detection__pb2.DownloadMultipleFilesRequest.SerializeToString,
                response_deserializer=plagiarism__detection__pb2.DownloadMultipleFilesResponse.FromString,
                _registered_method=True)
        self.DeleteFile = channel.unary_unary(
                '/plagiarism_detection.FileService/DeleteFile',
                request_serializer=plagiarism__detection__pb2.DeleteFileRequest.SerializeToString,
                response_deserializer=plagiarism__detection__pb2.DeleteFileResponse.FromString,
                _registered_method=True)


class FileServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UploadFile(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUploadedFileList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadMultipleFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadFile': grpc.stream_unary_rpc_method_handler(
                    servicer.UploadFile,
                    request_deserializer=plagiarism__detection__pb2.UploadFileRequest.FromString,
                    response_serializer=plagiarism__detection__pb2.UploadFileResponse.SerializeToString,
            ),
            'GetUploadedFileList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUploadedFileList,
                    request_deserializer=plagiarism__detection__pb2.GetUploadedFileListRequest.FromString,
                    response_serializer=plagiarism__detection__pb2.GetUploadedFileListResponse.SerializeToString,
            ),
            'DownloadFile': grpc.unary_stream_rpc_method_handler(
                    servicer.DownloadFile,
                    request_deserializer=plagiarism__detection__pb2.DownloadFileRequest.FromString,
                    response_serializer=plagiarism__detection__pb2.DownloadFileResponse.SerializeToString,
            ),
            'DownloadMultipleFiles': grpc.unary_stream_rpc_method_handler(
                    servicer.DownloadMultipleFiles,
                    request_deserializer=plagiarism__detection__pb2.DownloadMultipleFilesRequest.FromString,
                    response_serializer=plagiarism__detection__pb2.DownloadMultipleFilesResponse.SerializeToString,
            ),
            'DeleteFile': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteFile,
                    request_deserializer=plagiarism__detection__pb2.DeleteFileRequest.FromString,
                    response_serializer=plagiarism__detection__pb2.DeleteFileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'plagiarism_detection.FileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('plagiarism_detection.FileService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FileService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UploadFile(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(
            request_iterator,
            target,
            '/plagiarism_detection.FileService/UploadFile',
            plagiarism__detection__pb2.UploadFileRequest.SerializeToString,
            plagiarism__detection__pb2.UploadFileResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetUploadedFileList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/plagiarism_detection.FileService/GetUploadedFileList',
            plagiarism__detection__pb2.GetUploadedFileListRequest.SerializeToString,
            plagiarism__detection__pb2.GetUploadedFileListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DownloadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/plagiarism_detection.FileService/DownloadFile',
            plagiarism__detection__pb2.DownloadFileRequest.SerializeToString,
            plagiarism__detection__pb2.DownloadFileResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DownloadMultipleFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/plagiarism_detection.FileService/DownloadMultipleFiles',
            plagiarism__detection__pb2.DownloadMultipleFilesRequest.SerializeToString,
            plagiarism__detection__pb2.DownloadMultipleFilesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/plagiarism_detection.FileService/DeleteFile',
            plagiarism__detection__pb2.DeleteFileRequest.SerializeToString,
            plagiarism__detection__pb2.DeleteFileResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class CheckServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OneToOneCheck = channel.unary_unary(
                '/plagiarism_detection.CheckService/OneToOneCheck',
                request_serializer=plagiarism__detection__pb2.OneToOneCheckRequest.SerializeToString,
                response_deserializer=plagiarism__detection__pb2.OneToOneCheckResponse.FromString,
                _registered_method=True)
        self.OneToManyCheck = channel.unary_stream(
                '/plagiarism_detection.CheckService/OneToManyCheck',
                request_serializer=plagiarism__detection__pb2.OneToManyCheckRequest.SerializeToString,
                response_deserializer=plagiarism__detection__pb2.OneToManyCheckResponse.FromString,
                _registered_method=True)
        self.ManyToManyCheck = channel.unary_stream(
                '/plagiarism_detection.CheckService/ManyToManyCheck',
                request_serializer=plagiarism__detection__pb2.ManyToManyCheckRequest.SerializeToString,
                response_deserializer=plagiarism__detection__pb2.ManyToManyCheckResponse.FromString,
                _registered_method=True)


class CheckServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def OneToOneCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OneToManyCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ManyToManyCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CheckServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'OneToOneCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.OneToOneCheck,
                    request_deserializer=plagiarism__detection__pb2.OneToOneCheckRequest.FromString,
                    response_serializer=plagiarism__detection__pb2.OneToOneCheckResponse.SerializeToString,
            ),
            'OneToManyCheck': grpc.unary_stream_rpc_method_handler(
                    servicer.OneToManyCheck,
                    request_deserializer=plagiarism__detection__pb2.OneToManyCheckRequest.FromString,
                    response_serializer=plagiarism__detection__pb2.OneToManyCheckResponse.SerializeToString,
            ),
            'ManyToManyCheck': grpc.unary_stream_rpc_method_handler(
                    servicer.ManyToManyCheck,
                    request_deserializer=plagiarism__detection__pb2.ManyToManyCheckRequest.FromString,
                    response_serializer=plagiarism__detection__pb2.ManyToManyCheckResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'plagiarism_detection.CheckService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('plagiarism_detection.CheckService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class CheckService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def OneToOneCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/plagiarism_detection.CheckService/OneToOneCheck',
            plagiarism__detection__pb2.OneToOneCheckRequest.SerializeToString,
            plagiarism__detection__pb2.OneToOneCheckResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def OneToManyCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/plagiarism_detection.CheckService/OneToManyCheck',
            plagiarism__detection__pb2.OneToManyCheckRequest.SerializeToString,
            plagiarism__detection__pb2.OneToManyCheckResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ManyToManyCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/plagiarism_detection.CheckService/ManyToManyCheck',
            plagiarism__detection__pb2.ManyToManyCheckRequest.SerializeToString,
            plagiarism__detection__pb2.ManyToManyCheckResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class ReportServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCheckList = channel.unary_unary(
                '/plagiarism_detection.ReportService/GetCheckList',
                request_serializer=plagiarism__detection__pb2.GetCheckListRequest.SerializeToString,
                response_deserializer=plagiarism__detection__pb2.GetCheckListResponse.FromString,
                _registered_method=True)
        self.GetCheck = channel.unary_unary(
                '/plagiarism_detection.ReportService/GetCheck',
                request_serializer=plagiarism__detection__pb2.GetCheckRequest.SerializeToString,
                response_deserializer=plagiarism__detection__pb2.GetCheckResponse.FromString,
                _registered_method=True)
        self.GetAllReportList = channel.unary_unary(
                '/plagiarism_detection.ReportService/GetAllReportList',
                request_serializer=plagiarism__detection__pb2.GetAllReportListRequest.SerializeToString,
                response_deserializer=plagiarism__detection__pb2.GetAllReportListResponse.FromString,
                _registered_method=True)
        self.GetReport = channel.unary_unary(
                '/plagiarism_detection.ReportService/GetReport',
                request_serializer=plagiarism__detection__pb2.GetReportRequest.SerializeToString,
                response_deserializer=plagiarism__detection__pb2.GetReportResponse.FromString,
                _registered_method=True)
        self.UpdateReport = channel.unary_unary(
                '/plagiarism_detection.ReportService/UpdateReport',
                request_serializer=plagiarism__detection__pb2.UpdateReportRequest.SerializeToString,
                response_deserializer=plagiarism__detection__pb2.UpdateReportResponse.FromString,
                _registered_method=True)


class ReportServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetCheckList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllReportList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetReport(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateReport(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReportServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCheckList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCheckList,
                    request_deserializer=plagiarism__detection__pb2.GetCheckListRequest.FromString,
                    response_serializer=plagiarism__detection__pb2.GetCheckListResponse.SerializeToString,
            ),
            'GetCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCheck,
                    request_deserializer=plagiarism__detection__pb2.GetCheckRequest.FromString,
                    response_serializer=plagiarism__detection__pb2.GetCheckResponse.SerializeToString,
            ),
            'GetAllReportList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllReportList,
                    request_deserializer=plagiarism__detection__pb2.GetAllReportListRequest.FromString,
                    response_serializer=plagiarism__detection__pb2.GetAllReportListResponse.SerializeToString,
            ),
            'GetReport': grpc.unary_unary_rpc_method_handler(
                    servicer.GetReport,
                    request_deserializer=plagiarism__detection__pb2.GetReportRequest.FromString,
                    response_serializer=plagiarism__detection__pb2.GetReportResponse.SerializeToString,
            ),
            'UpdateReport': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateReport,
                    request_deserializer=plagiarism__detection__pb2.UpdateReportRequest.FromString,
                    response_serializer=plagiarism__detection__pb2.UpdateReportResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'plagiarism_detection.ReportService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('plagiarism_detection.ReportService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ReportService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetCheckList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/plagiarism_detection.ReportService/GetCheckList',
            plagiarism__detection__pb2.GetCheckListRequest.SerializeToString,
            plagiarism__detection__pb2.GetCheckListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/plagiarism_detection.ReportService/GetCheck',
            plagiarism__detection__pb2.GetCheckRequest.SerializeToString,
            plagiarism__detection__pb2.GetCheckResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAllReportList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/plagiarism_detection.ReportService/GetAllReportList',
            plagiarism__detection__pb2.GetAllReportListRequest.SerializeToString,
            plagiarism__detection__pb2.GetAllReportListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetReport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/plagiarism_detection.ReportService/GetReport',
            plagiarism__detection__pb2.GetReportRequest.SerializeToString,
            plagiarism__detection__pb2.GetReportResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateReport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/plagiarism_detection.ReportService/UpdateReport',
            plagiarism__detection__pb2.UpdateReportRequest.SerializeToString,
            plagiarism__detection__pb2.UpdateReportResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
