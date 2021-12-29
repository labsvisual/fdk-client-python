"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class MediaState(BaseSchema):
    # Feedback swagger.json

    
    approve = fields.Boolean(required=False)
    
    archive = fields.Boolean(required=False)
    

