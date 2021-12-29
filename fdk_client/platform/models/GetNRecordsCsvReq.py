"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class GetNRecordsCsvReq(BaseSchema):
    # Communication swagger.json

    
    url = fields.Str(required=False)
    
    header = fields.Boolean(required=False)
    
    count = fields.Int(required=False)
    

