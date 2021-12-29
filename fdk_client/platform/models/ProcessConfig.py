"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DBConfig import DBConfig

from .DBParamConfig import DBParamConfig

from .SFTPConfig import SFTPConfig

from .AWSS3config import AWSS3config

from .MongoDocConfig import MongoDocConfig

from .FTPConfig import FTPConfig

from .EmailConfig import EmailConfig

from .FileConfig import FileConfig

from .JsonDocConfig import JsonDocConfig

from .DocMappingConfig import DocMappingConfig

from .TaskStepConfig import TaskStepConfig

from .HttpConfig import HttpConfig

from .LocalFileConfig import LocalFileConfig

from .OAuthConfig import OAuthConfig

from .GoogleSpreadSheetConfig import GoogleSpreadSheetConfig


class ProcessConfig(BaseSchema):
    # Inventory swagger.json

    
    db_config = fields.Nested(DBConfig, required=False)
    
    db_param_config = fields.Nested(DBParamConfig, required=False)
    
    sftp_config = fields.Nested(SFTPConfig, required=False)
    
    aws_s3_config = fields.Nested(AWSS3config, required=False)
    
    mongo_doc_config = fields.Nested(MongoDocConfig, required=False)
    
    ftp_config = fields.Nested(FTPConfig, required=False)
    
    email_config = fields.Nested(EmailConfig, required=False)
    
    file_config = fields.Nested(FileConfig, required=False)
    
    json_doc_config = fields.Nested(JsonDocConfig, required=False)
    
    doc_mapping_config = fields.Nested(DocMappingConfig, required=False)
    
    task_step_config = fields.Nested(TaskStepConfig, required=False)
    
    http_config = fields.Nested(HttpConfig, required=False)
    
    local_file_config = fields.Nested(LocalFileConfig, required=False)
    
    oauth_config = fields.Nested(OAuthConfig, required=False)
    
    google_spreadsheet_config = fields.Nested(GoogleSpreadSheetConfig, required=False)
    

