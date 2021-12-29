"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .LogisticTimestamp import LogisticTimestamp

from .Formatted import Formatted


class LogisticPromise(BaseSchema):
    # Logistic swagger.json

    
    timestamp = fields.Nested(LogisticTimestamp, required=False)
    
    formatted = fields.Nested(Formatted, required=False)
    

