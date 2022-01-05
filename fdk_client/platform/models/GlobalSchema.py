"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GlobalSchemaProps import GlobalSchemaProps


class GlobalSchema(BaseSchema):
    # Theme swagger.json

    
    props = fields.List(fields.Nested(GlobalSchemaProps, required=False), required=False)
    

