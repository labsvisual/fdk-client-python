"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .FilerList import FilerList


class InventoryConfig(BaseSchema):
    # Catalog swagger.json

    
    multivalues = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(FilerList, required=False), required=False)
    

