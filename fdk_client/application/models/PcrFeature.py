"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class PcrFeature(BaseSchema):
    # Configuration swagger.json

    
    staff_selection = fields.Boolean(required=False)
    

