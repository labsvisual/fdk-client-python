"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SizeChartValues import SizeChartValues

from .ColumnHeaders import ColumnHeaders












class SizeChart(BaseSchema):
    # Catalog swagger.json

    
    sizes = fields.List(fields.Nested(SizeChartValues, required=False), required=False)
    
    headers = fields.Nested(ColumnHeaders, required=False)
    
    unit = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    image = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    size_tip = fields.Str(required=False)
    

