"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ArticleAssignmentRule import ArticleAssignmentRule


class InventoryArticleAssignment(BaseSchema):
    # Configuration swagger.json

    
    post_order_reassignment = fields.Boolean(required=False)
    
    rules = fields.Nested(ArticleAssignmentRule, required=False)
    

