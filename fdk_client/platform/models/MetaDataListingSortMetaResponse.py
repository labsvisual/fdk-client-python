"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class MetaDataListingSortMetaResponse(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    key = fields.Str(required=False)
    

