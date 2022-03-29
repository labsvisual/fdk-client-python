"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .PayloadEmailStructure import PayloadEmailStructure

from .PayloadSmsStructure import PayloadSmsStructure




class PayloadStructure(BaseSchema):
    # Communication swagger.json

    
    data = fields.List(fields.Dict(required=False), required=False)
    
    email = fields.Nested(PayloadEmailStructure, required=False)
    
    sms = fields.Nested(PayloadSmsStructure, required=False)
    
    application = fields.Str(required=False)
    

