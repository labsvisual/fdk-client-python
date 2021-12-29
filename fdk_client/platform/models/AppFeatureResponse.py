"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AppFeature import AppFeature


class AppFeatureResponse(BaseSchema):
    # Configuration swagger.json

    
    feature = fields.Nested(AppFeature, required=False)
    

