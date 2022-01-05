"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ArticleAssignmentRules import ArticleAssignmentRules




class ArticleAssignmentConfig(BaseSchema):
    # Configuration swagger.json

    
    rules = fields.Nested(ArticleAssignmentRules, required=False)
    
    post_order_reassignment = fields.Boolean(required=False)
    

