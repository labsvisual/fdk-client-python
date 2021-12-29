"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .PropBeanConfig import PropBeanConfig



from .DefaultHeadersDTO import DefaultHeadersDTO


class DocMappingConfig(BaseSchema):
    # Inventory swagger.json

    
    properties = fields.Dict(required=False)
    
    junk_data_threshold_count = fields.Int(required=False)
    
    prop_bean_configs = fields.List(fields.Nested(PropBeanConfig, required=False), required=False)
    
    unwind_field = fields.Str(required=False)
    
    default_headers = fields.Nested(DefaultHeadersDTO, required=False)
    

