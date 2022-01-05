"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PaymentModeConfig import PaymentModeConfig

from .PaymentModeConfig import PaymentModeConfig

from .PaymentModeConfig import PaymentModeConfig

from .PaymentModeConfig import PaymentModeConfig

from .PaymentModeConfig import PaymentModeConfig

from .PaymentModeConfig import PaymentModeConfig

from .PaymentModeConfig import PaymentModeConfig

from .PaymentModeConfig import PaymentModeConfig

from .PaymentModeConfig import PaymentModeConfig

from .PaymentModeConfig import PaymentModeConfig

from .PaymentModeConfig import PaymentModeConfig

from .PaymentModeConfig import PaymentModeConfig

from .PaymentModeConfig import PaymentModeConfig

from .PaymentModeConfig import PaymentModeConfig

from .PaymentModeConfig import PaymentModeConfig

from .PaymentModeConfig import PaymentModeConfig

from .PaymentModeConfig import PaymentModeConfig

from .PaymentModeConfig import PaymentModeConfig

from .PaymentModeConfig import PaymentModeConfig


class Methods(BaseSchema):
    # Configuration swagger.json

    
    pl = fields.Nested(PaymentModeConfig, required=False)
    
    card = fields.Nested(PaymentModeConfig, required=False)
    
    nb = fields.Nested(PaymentModeConfig, required=False)
    
    wl = fields.Nested(PaymentModeConfig, required=False)
    
    ps = fields.Nested(PaymentModeConfig, required=False)
    
    upi = fields.Nested(PaymentModeConfig, required=False)
    
    qr = fields.Nested(PaymentModeConfig, required=False)
    
    cod = fields.Nested(PaymentModeConfig, required=False)
    
    pp = fields.Nested(PaymentModeConfig, required=False)
    
    jp = fields.Nested(PaymentModeConfig, required=False)
    
    pac = fields.Nested(PaymentModeConfig, required=False)
    
    fc = fields.Nested(PaymentModeConfig, required=False)
    
    jiopp = fields.Nested(PaymentModeConfig, required=False)
    
    stripepg = fields.Nested(PaymentModeConfig, required=False)
    
    juspaypg = fields.Nested(PaymentModeConfig, required=False)
    
    payubizpg = fields.Nested(PaymentModeConfig, required=False)
    
    payumoneypg = fields.Nested(PaymentModeConfig, required=False)
    
    rupifipg = fields.Nested(PaymentModeConfig, required=False)
    
    simpl = fields.Nested(PaymentModeConfig, required=False)
    

