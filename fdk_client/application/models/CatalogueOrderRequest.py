"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .RewardsArticle import RewardsArticle


class CatalogueOrderRequest(BaseSchema):
    # Rewards swagger.json

    
    articles = fields.List(fields.Nested(RewardsArticle, required=False), required=False)
    

