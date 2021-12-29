"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .HsnCodesObject import HsnCodesObject


class HsnCode(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(HsnCodesObject, required=False)
    

