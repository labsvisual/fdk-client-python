"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .ProductBrand import ProductBrand



from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute



from .ProductBrand import ProductBrand

























from .ProductListingAction import ProductListingAction



from .ProductListingPrice import ProductListingPrice



from .Media import Media




class ProductDetail(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    slug = fields.Str(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    attributes = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    rating_count = fields.Int(required=False)
    
    rating = fields.Float(required=False)
    
    image_nature = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    short_description = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    teaser_tag = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    uid = fields.Int(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    product_online_date = fields.Str(required=False)
    

