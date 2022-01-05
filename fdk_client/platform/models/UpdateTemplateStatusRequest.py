"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class UpdateTemplateStatusRequest(BaseSchema):
    # Feedback swagger.json

    
    active = fields.Boolean(required=False)
    
    archive = fields.Boolean(required=False)
    

