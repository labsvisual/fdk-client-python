"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .UserInfo1 import UserInfo1







from .UserInfo1 import UserInfo1


class BulkResponse(BaseSchema):
    # Catalog swagger.json

    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo1, required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_on = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo1, required=False)
    

