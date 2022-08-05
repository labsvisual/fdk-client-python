"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class SizeChartValues(BaseSchema):
    # Catalog swagger.json

    
    col_3 = fields.Str(required=False)
    
    col_1 = fields.Str(required=False)
    
    col_5 = fields.Str(required=False)
    
    col_6 = fields.Str(required=False)
    
    col_2 = fields.Str(required=False)
    
    col_4 = fields.Str(required=False)
    

