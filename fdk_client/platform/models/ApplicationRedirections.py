"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ApplicationRedirections(BaseSchema):
    # Common swagger.json

    
    redirect_from = fields.Str(required=False)
    
    redirect_to = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

