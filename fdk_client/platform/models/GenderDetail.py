"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .AttributeMaster import AttributeMaster

from .AttributeMasterMeta import AttributeMasterMeta







from .AttributeMasterDetails import AttributeMasterDetails







from .AttributeMasterFilter import AttributeMasterFilter


class GenderDetail(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    is_nested = fields.Boolean(required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
    meta = fields.Nested(AttributeMasterMeta, required=False)
    
    logo = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    description = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    

