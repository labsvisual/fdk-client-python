"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class SystemNotificationSettings(BaseSchema):
    # Communication swagger.json

    
    sound = fields.Boolean(required=False)
    
    priority = fields.Str(required=False)
    
    time_to_live = fields.Str(required=False)
    

