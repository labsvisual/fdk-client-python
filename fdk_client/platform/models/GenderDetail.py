"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .AttributeMasterDetails import AttributeMasterDetails









from .AttributeMasterFilter import AttributeMasterFilter



from .AttributeMaster import AttributeMaster

from .AttributeMasterMeta import AttributeMasterMeta


class GenderDetail(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    is_nested = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
    meta = fields.Nested(AttributeMasterMeta, required=False)
    

