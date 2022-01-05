"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .LogisticResponseCategory import LogisticResponseCategory

from .LogisticPromise import LogisticPromise


class TatProductArticles(BaseSchema):
    # Logistic swagger.json

    
    error = fields.Dict(required=False)
    
    category = fields.Nested(LogisticResponseCategory, required=False)
    
    promise = fields.Nested(LogisticPromise, required=False)
    

