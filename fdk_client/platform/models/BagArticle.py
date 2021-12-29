"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ArticleIdentifiers import ArticleIdentifiers









from .Set import Set



from .BagArticleReturnConfig import BagArticleReturnConfig








class BagArticle(BaseSchema):
    # Order swagger.json

    
    identifiers = fields.Nested(ArticleIdentifiers, required=False)
    
    esp_modified = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    size = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    set = fields.Nested(Set, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    return_config = fields.Nested(BagArticleReturnConfig, required=False)
    
    _id = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    child_details = fields.Dict(required=False)
    

