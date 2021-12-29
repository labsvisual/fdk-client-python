"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class PaymentValidator:
    
    class getBrandPaymentGatewayConfig(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class saveBrandPaymentGatewayConfig(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updateBrandPaymentGatewayConfig(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getPaymentModeRoutes(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        refresh = fields.Boolean(required=False)
        
        request_type = fields.Str(required=False)
         
    
    class getAllPayouts(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        unique_external_id = fields.Str(required=False)
         
    
    class savePayout(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class updatePayout(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        unique_transfer_no = fields.Str(required=False)
         
    
    class activateAndDectivatePayout(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        unique_transfer_no = fields.Str(required=False)
         
    
    class deletePayout(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        unique_transfer_no = fields.Str(required=False)
         
    
    class getSubscriptionPaymentMethod(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        unique_external_id = fields.Str(required=False)
         
    
    class deleteSubscriptionPaymentMethod(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        unique_external_id = fields.Str(required=False)
        
        payment_method_id = fields.Str(required=False)
         
    
    class getSubscriptionConfig(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class saveSubscriptionSetupIntent(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class addBeneficiaryDetails(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class verifyIfscCode(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        ifsc_code = fields.Str(required=False)
         
    
    class getUserOrderBeneficiaries(BaseSchema):
        
        order_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getUserBeneficiaries(BaseSchema):
        
        order_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class confirmPayment(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    