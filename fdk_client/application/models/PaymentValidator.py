"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class PaymentValidator:
    
    class getAggregatorsConfig(BaseSchema):
        
        x__api__token = fields.Str(required=False)
        
        refresh = fields.Boolean(required=False)
         
    
    class attachCardToCustomer(BaseSchema):
        
        pass 
    
    class getActiveCardAggregator(BaseSchema):
        
        refresh = fields.Boolean(required=False)
         
    
    class getActiveUserCards(BaseSchema):
        
        force_refresh = fields.Boolean(required=False)
         
    
    class deleteUserCard(BaseSchema):
        
        pass 
    
    class verifyCustomerForPayment(BaseSchema):
        
        pass 
    
    class verifyAndChargePayment(BaseSchema):
        
        pass 
    
    class initialisePayment(BaseSchema):
        
        pass 
    
    class checkAndUpdatePaymentStatus(BaseSchema):
        
        pass 
    
    class getPaymentModeRoutes(BaseSchema):
        
        amount = fields.Int(required=False)
        
        cart_id = fields.Str(required=False)
        
        pincode = fields.Str(required=False)
        
        checkout_mode = fields.Str(required=False)
        
        refresh = fields.Boolean(required=False)
        
        card_reference = fields.Str(required=False)
        
        user_details = fields.Str(required=False)
         
    
    class getPosPaymentModeRoutes(BaseSchema):
        
        amount = fields.Int(required=False)
        
        cart_id = fields.Str(required=False)
        
        pincode = fields.Str(required=False)
        
        checkout_mode = fields.Str(required=False)
        
        refresh = fields.Boolean(required=False)
        
        card_reference = fields.Str(required=False)
        
        order_type = fields.Str(required=False)
        
        user_details = fields.Str(required=False)
         
    
    class getRupifiBannerDetails(BaseSchema):
        
        pass 
    
    class getActiveRefundTransferModes(BaseSchema):
        
        pass 
    
    class enableOrDisableRefundTransferMode(BaseSchema):
        
        pass 
    
    class getUserBeneficiariesDetail(BaseSchema):
        
        order_id = fields.Str(required=False)
         
    
    class verifyIfscCode(BaseSchema):
        
        ifsc_code = fields.Str(required=False)
         
    
    class getOrderBeneficiariesDetail(BaseSchema):
        
        order_id = fields.Str(required=False)
         
    
    class verifyOtpAndAddBeneficiaryForBank(BaseSchema):
        
        pass 
    
    class addBeneficiaryDetails(BaseSchema):
        
        pass 
    
    class addRefundBankAccountUsingOTP(BaseSchema):
        
        pass 
    
    class verifyOtpAndAddBeneficiaryForWallet(BaseSchema):
        
        pass 
    
    class updateDefaultBeneficiary(BaseSchema):
        
        pass 
    