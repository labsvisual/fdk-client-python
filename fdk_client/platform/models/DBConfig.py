"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
























class DBConfig(BaseSchema):
    # Inventory swagger.json

    
    vendor = fields.Str(required=False)
    
    host = fields.Str(required=False)
    
    port = fields.Int(required=False)
    
    username = fields.Str(required=False)
    
    password = fields.Str(required=False)
    
    dbname = fields.Str(required=False)
    
    query = fields.Str(required=False)
    
    procedure = fields.Boolean(required=False)
    
    driver_class = fields.Str(required=False)
    
    jdbc_url = fields.Str(required=False)
    
    optional_properties = fields.Dict(required=False)
    

