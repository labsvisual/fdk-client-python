"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BigqueryHeadersResHeaders import BigqueryHeadersResHeaders


class BigqueryHeadersRes(BaseSchema):
    # Communication swagger.json

    
    headers = fields.List(fields.Nested(BigqueryHeadersResHeaders, required=False), required=False)
    

