"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Url(BaseSchema):
    # Feedback swagger.json

    
    main = fields.Str(required=False)
    
    thumbnail = fields.Str(required=False)
    

