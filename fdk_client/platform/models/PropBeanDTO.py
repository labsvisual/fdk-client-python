"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








































class PropBeanDTO(BaseSchema):
    # Inventory swagger.json

    
    required = fields.Boolean(required=False)
    
    optional = fields.Boolean(required=False)
    
    include = fields.Boolean(required=False)
    
    source_field = fields.Str(required=False)
    
    source_fields = fields.List(fields.Str(required=False), required=False)
    
    destination_field = fields.Str(required=False)
    
    data_type = fields.Str(required=False)
    
    default_value = fields.Dict(required=False)
    
    const_value = fields.Dict(required=False)
    
    concat_str = fields.Str(required=False)
    
    function_name = fields.Str(required=False)
    
    transformer_name = fields.Str(required=False)
    
    all_param_function_name = fields.Str(required=False)
    
    sub_separator = fields.Str(required=False)
    
    index_field = fields.Str(required=False)
    
    ignore_if_not_exists = fields.Boolean(required=False)
    
    identifier_type = fields.Str(required=False)
    
    projection_query = fields.Dict(required=False)
    
    enrich_from_master = fields.Boolean(required=False)
    

