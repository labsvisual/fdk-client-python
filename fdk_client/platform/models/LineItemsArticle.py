"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Quantities import Quantities





from .Manufacturer import Manufacturer

from .ArticlePrice import ArticlePrice



from .Company import Company



from .FailOrderDateMeta import FailOrderDateMeta



from .MarketplaceIdentifiers import MarketplaceIdentifiers





from .Dimension import Dimension

from .Weight import Weight

from .Store import Store

from .ArticleMeta import ArticleMeta



from .ArticleBrand import ArticleBrand







from .LineItemsArticleIdentifier import LineItemsArticleIdentifier








class LineItemsArticle(BaseSchema):
    # Order swagger.json

    
    quantities = fields.Nested(Quantities, required=False)
    
    old_article_uid = fields.Str(required=False)
    
    total_quantity = fields.Int(required=False)
    
    manufacturer = fields.Nested(Manufacturer, required=False)
    
    price = fields.Nested(ArticlePrice, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    company = fields.Nested(Company, required=False)
    
    is_active = fields.Boolean(required=False)
    
    date_meta = fields.Nested(FailOrderDateMeta, required=False)
    
    fragile = fields.Boolean(required=False)
    
    marketplace_identifiers = fields.Nested(MarketplaceIdentifiers, required=False)
    
    size = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    dimension = fields.Nested(Dimension, required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    store = fields.Nested(Store, required=False)
    
    meta = fields.Nested(ArticleMeta, required=False)
    
    uid = fields.Str(required=False)
    
    brand = fields.Nested(ArticleBrand, required=False)
    
    item_id = fields.Int(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    identifier = fields.Nested(LineItemsArticleIdentifier, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    

