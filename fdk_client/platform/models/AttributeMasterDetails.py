"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class AttributeMasterDetails(BaseSchema):
    # Catalog swagger.json

    
    display_type = fields.Str(required=False)
    

