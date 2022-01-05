"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class Notification(BaseSchema):
    # Communication swagger.json

    
    title = fields.Str(required=False)
    
    body = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    icon = fields.Str(required=False)
    
    deeplink = fields.Str(required=False)
    
    click_action = fields.Str(required=False)
    

