"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GoogleMapCredentials import GoogleMapCredentials


class GoogleMap(BaseSchema):
    # Configuration swagger.json

    
    credentials = fields.Nested(GoogleMapCredentials, required=False)
    

