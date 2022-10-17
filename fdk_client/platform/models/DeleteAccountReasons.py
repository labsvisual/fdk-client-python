"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class DeleteAccountReasons(BaseSchema):
    # User swagger.json

    
    reason_text = fields.Str(required=False)
    
    reason_id = fields.Str(required=False)
    
    show_text_area = fields.Boolean(required=False)
    

