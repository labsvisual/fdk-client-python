"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema















from .PropBeanConfig import PropBeanConfig















from .DefaultHeadersDTO import DefaultHeadersDTO


class FileConfig(BaseSchema):
    # Inventory swagger.json

    
    delimiter = fields.Str(required=False)
    
    charset = fields.Str(required=False)
    
    properties = fields.Dict(required=False)
    
    file_has_header = fields.Boolean(required=False)
    
    header_index = fields.Int(required=False)
    
    header_array = fields.List(fields.Str(required=False), required=False)
    
    data_start_index = fields.Int(required=False)
    
    prop_bean_configs = fields.List(fields.Nested(PropBeanConfig, required=False), required=False)
    
    junk_data_threshold_count = fields.Int(required=False)
    
    file_type = fields.Str(required=False)
    
    line_validity_check = fields.Boolean(required=False)
    
    sheet_names = fields.List(fields.Str(required=False), required=False)
    
    read_all_sheets = fields.Boolean(required=False)
    
    quote_char = fields.Str(required=False)
    
    escape_char = fields.Str(required=False)
    
    default_headers = fields.Nested(DefaultHeadersDTO, required=False)
    

