"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductDetailFeature import ProductDetailFeature

from .LandingPageFeature import LandingPageFeature

from .RegistrationPageFeature import RegistrationPageFeature

from .HomePageFeature import HomePageFeature

from .CommonFeature import CommonFeature

from .CartFeature import CartFeature

from .QrFeature import QrFeature

from .PcrFeature import PcrFeature

from .OrderFeature import OrderFeature












class AppFeature(BaseSchema):
    # Configuration swagger.json

    
    product_detail = fields.Nested(ProductDetailFeature, required=False)
    
    landing_page = fields.Nested(LandingPageFeature, required=False)
    
    registration_page = fields.Nested(RegistrationPageFeature, required=False)
    
    home_page = fields.Nested(HomePageFeature, required=False)
    
    common = fields.Nested(CommonFeature, required=False)
    
    cart = fields.Nested(CartFeature, required=False)
    
    qr = fields.Nested(QrFeature, required=False)
    
    pcr = fields.Nested(PcrFeature, required=False)
    
    order = fields.Nested(OrderFeature, required=False)
    
    _id = fields.Str(required=False)
    
    app = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    

