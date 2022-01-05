"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .LogEmail import LogEmail

from .LogPushnotification import LogPushnotification

from .LogMeta import LogMeta


















class Log(BaseSchema):
    # Communication swagger.json

    
    email = fields.Nested(LogEmail, required=False)
    
    pushnotification = fields.Nested(LogPushnotification, required=False)
    
    meta = fields.Nested(LogMeta, required=False)
    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    service = fields.Str(required=False)
    
    step = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    data = fields.Raw(required=False)
    
    expire_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    

