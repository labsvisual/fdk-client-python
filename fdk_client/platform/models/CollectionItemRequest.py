"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ItemQueryForUserCollection import ItemQueryForUserCollection

from .CollectionQuery import CollectionQuery


class CollectionItemRequest(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    item = fields.List(fields.Nested(ItemQueryForUserCollection, required=False), required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    

