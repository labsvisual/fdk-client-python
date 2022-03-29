"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DataLoaderSchema import DataLoaderSchema


class DataLoadersSchema(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(DataLoaderSchema, required=False), required=False)
    

