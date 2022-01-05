"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Urls import Urls


class SignUrlResponse(BaseSchema):
    # FileStorage swagger.json

    
    urls = fields.List(fields.Nested(Urls, required=False), required=False)
    

