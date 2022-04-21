"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class TeaserTag(BaseSchema):
    # Catalog swagger.json

    
    url = fields.Str(required=False)
    
    tag = fields.Str(required=False)
    

