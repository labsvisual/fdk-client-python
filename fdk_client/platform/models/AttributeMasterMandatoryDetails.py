"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class AttributeMasterMandatoryDetails(BaseSchema):
    # Catalog swagger.json

    
    l3_keys = fields.List(fields.Str(required=False), required=False)
    

