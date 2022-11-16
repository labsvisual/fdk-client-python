"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .ColumnHeaders import ColumnHeaders



from .SizeChartValues import SizeChartValues


class SizeChart(BaseSchema):
    # Catalog swagger.json

    
    unit = fields.Str(required=False)
    
    size_tip = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    image = fields.Str(required=False)
    
    headers = fields.Nested(ColumnHeaders, required=False)
    
    title = fields.Str(required=False)
    
    sizes = fields.List(fields.Nested(SizeChartValues, required=False), required=False)
    

