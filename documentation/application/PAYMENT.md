



##### [Back to Application docs](./README.md)

## Payment Methods
Collect payment through many payment gateway i.e Stripe, Razorpay, Juspay etc.into Fynd or Self account
* [getAggregatorsConfig](#getaggregatorsconfig)
* [attachCardToCustomer](#attachcardtocustomer)
* [getActiveCardAggregator](#getactivecardaggregator)
* [getActiveUserCards](#getactiveusercards)
* [deleteUserCard](#deleteusercard)
* [verifyCustomerForPayment](#verifycustomerforpayment)
* [verifyAndChargePayment](#verifyandchargepayment)
* [initialisePayment](#initialisepayment)
* [checkAndUpdatePaymentStatus](#checkandupdatepaymentstatus)
* [getPaymentModeRoutes](#getpaymentmoderoutes)
* [getPosPaymentModeRoutes](#getpospaymentmoderoutes)
* [getRupifiBannerDetails](#getrupifibannerdetails)
* [getEpaylaterBannerDetails](#getepaylaterbannerdetails)
* [resendOrCancelPayment](#resendorcancelpayment)
* [getActiveRefundTransferModes](#getactiverefundtransfermodes)
* [enableOrDisableRefundTransferMode](#enableordisablerefundtransfermode)
* [getUserBeneficiariesDetail](#getuserbeneficiariesdetail)
* [verifyIfscCode](#verifyifsccode)
* [getOrderBeneficiariesDetail](#getorderbeneficiariesdetail)
* [verifyOtpAndAddBeneficiaryForBank](#verifyotpandaddbeneficiaryforbank)
* [addBeneficiaryDetails](#addbeneficiarydetails)
* [addRefundBankAccountUsingOTP](#addrefundbankaccountusingotp)
* [verifyOtpAndAddBeneficiaryForWallet](#verifyotpandaddbeneficiaryforwallet)
* [updateDefaultBeneficiary](#updatedefaultbeneficiary)
* [getPaymentLink](#getpaymentlink)
* [createPaymentLink](#createpaymentlink)
* [resendPaymentLink](#resendpaymentlink)
* [cancelPaymentLink](#cancelpaymentlink)
* [getPaymentModeRoutesPaymentLink](#getpaymentmoderoutespaymentlink)
* [pollingPaymentLink](#pollingpaymentlink)
* [createOrderHandlerPaymentLink](#createorderhandlerpaymentlink)
* [initialisePaymentPaymentLink](#initialisepaymentpaymentlink)
* [checkAndUpdatePaymentStatusPaymentLink](#checkandupdatepaymentstatuspaymentlink)
* [customerCreditSummary](#customercreditsummary)
* [redirectToAggregator](#redirecttoaggregator)
* [checkCredit](#checkcredit)
* [customerOnboard](#customeronboard)



## Methods with example and description


### getAggregatorsConfig
Get payment gateway keys




```python
try:
    result = await client.payment.getAggregatorsConfig(xApiToken=xApiToken, refresh=refresh)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| xApiToken | String? | no | Used for basic authentication. |   
| refresh | Boolean? | no | This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one. |  



Use this API to retrieve the payment gateway key, secrets, merchant, SDK/API details to complete a payment at front-end.

*Returned Response:*




[AggregatorsConfigDetailResponse](#AggregatorsConfigDetailResponse)

Success. Returns the keys of all payment gateways. Check the example shown below or refer `AggregatorsConfigDetailResponse` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "simpl": {
    "key": "bf9d0ff65ffe6e54223a871e733bbd1c",
    "secret": "XXXX-XXXX-XXXX-XXXX",
    "config_type": "fynd",
    "sdk": true
  },
  "juspay": {
    "key": "XXXX-XXXX-XXXX-XXXX",
    "secret": "XXXX-XXXX-XXXX-XXXX",
    "config_type": "fynd",
    "merchant_key": "XXXX-XXXX-XXXX-XXXX",
    "sdk": false,
    "api": "https://api.juspay.in"
  },
  "mswipe": {
    "key": "XXXX-XXXX-XXXX-XXXX",
    "secret": "XXXX-XXXX-XXXX-XXXX",
    "config_type": "fynd",
    "merchant_id": "XXXX-XXXX-XXXX-XXXX",
    "user_id": "XXXX-XXXX-XXXX-XXXX",
    "pin": "XXXX-XXXX-XXXX-XXXX",
    "sdk": true,
    "verify_api": "https://www.mswipetech.com/verificationapi/api/VerificationApi/MswipeCardSaleVerificationApi"
  },
  "razorpay": {
    "key": "XXXX-XXXX-XXXX-XXXX",
    "secret": "XXXX-XXXX-XXXX-XXXX",
    "config_type": "fynd",
    "webhook_secret": "XXXX-XXXX-XXXX-XXXX",
    "sdk": true,
    "api": "https://api.razorpay.com/v1/",
    "vpa": "XXXX-XXXX-XXXX-XXXX"
  },
  "success": true,
  "env": "live"
}
```
</details>









---


### attachCardToCustomer
Attach a saved card to customer.




```python
try:
    result = await client.payment.attachCardToCustomer(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [AttachCardRequest](#AttachCardRequest) | yes | Request body |


Use this API to attach a customer's saved card at the payment gateway, such as Stripe, Juspay.

*Returned Response:*




[AttachCardsResponse](#AttachCardsResponse)

Success. Check the example shown below or refer `AttachCardsResponse` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "message": "",
  "data": {
    "id": "pm_1IGQlvHY5NCLOJpYNTBP6WpY",
    "brand": "visa",
    "checks": {
      "address_line1_check": null,
      "address_postal_code_check": null,
      "cvc_check": "pass"
    },
    "country": "US",
    "exp_month": 11,
    "exp_year": 2025,
    "fingerprint": "poKWfSweJ0I5CvEA",
    "funding": "credit",
    "generated_from": null,
    "last4": "1111",
    "networks": {
      "available": [
        "visa"
      ],
      "preferred": null
    },
    "three_d_secure_usage": {
      "supported": true
    },
    "wallet": null
  }
}
```
</details>









---


### getActiveCardAggregator
Fetch active payment gateway for card payments




```python
try:
    result = await client.payment.getActiveCardAggregator(refresh=refresh)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| refresh | Boolean? | no |  |  



Use this API to retrieve an active payment aggregator along with the Customer ID. This is applicable for cards payments only.

*Returned Response:*




[ActiveCardPaymentGatewayResponse](#ActiveCardPaymentGatewayResponse)

Success. Returns an active payment gateway. Check the example shown below or refer `ActiveCardPaymentGatewayResponse` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "message": "",
  "cards": {
    "aggregator": "Stripe",
    "api": "https://www.example.com/cards/",
    "customer_id": "lorem_12345"
  }
}
```
</details>









---


### getActiveUserCards
Fetch the list of cards saved by the user




```python
try:
    result = await client.payment.getActiveUserCards(forceRefresh=forceRefresh)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| forceRefresh | Boolean? | no |  |  



Use this API to retrieve a list of cards stored by user from an active payment gateway.

*Returned Response:*




[ListCardsResponse](#ListCardsResponse)

Success. Returns a list of cards saved by the user. Check the example shown below or refer `ListCardsResponse` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "message": "Success",
  "data": [
    {
      "aggregator_name": "Razorpay",
      "card_id": "token_lorem_ipsum_001",
      "card_token": "card_token_lorem_ipsum_001",
      "card_reference": "ref_lorem_ipsum_001",
      "card_number": "XXXX-XXXX-XXXX-1111",
      "card_isin": "001",
      "exp_year": 2025,
      "exp_month": 5,
      "card_type": "credit",
      "card_issuer": "ICIC",
      "card_brand": "VISA",
      "nickname": "Visa",
      "card_name": "Lorem Ipsum",
      "expired": false,
      "card_fingerprint": null,
      "card_brand_image": "https://hdn-1.fynd.com/payment/visa.png",
      "compliant_with_tokenisation_guidelines": true
    }
  ]
}
```
</details>









---


### deleteUserCard
Delete a card




```python
try:
    result = await client.payment.deleteUserCard(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [DeletehCardRequest](#DeletehCardRequest) | yes | Request body |


Use this API to delete a card added by a user on the payment gateway and clear the cache.

*Returned Response:*




[DeleteCardsResponse](#DeleteCardsResponse)

Success. Returns a success message if card is deleted.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true
}
```
</details>









---


### verifyCustomerForPayment
Validate customer for payment




```python
try:
    result = await client.payment.verifyCustomerForPayment(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [ValidateCustomerRequest](#ValidateCustomerRequest) | yes | Request body |


Use this API to check if the customer is eligible to use credit-line facilities such as Simpl Pay Later and Rupifi.

*Returned Response:*




[ValidateCustomerResponse](#ValidateCustomerResponse)

Success. Check the example shown below or refer `ValidateCustomerResponse` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "message": "data fetched",
  "data": {
    "api_version": 2,
    "data": {
      "approved": true,
      "button_text": "Buy Now, Pay Later",
      "first_transaction": false
    },
    "aggregator": "Simpl"
  }
}
```
</details>









---


### verifyAndChargePayment
Verify and charge payment




```python
try:
    result = await client.payment.verifyAndChargePayment(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [ChargeCustomerRequest](#ChargeCustomerRequest) | yes | Request body |


Use this API to verify and check the status of a payment transaction (server-to-server) made through aggregators like Simpl and Mswipe.

*Returned Response:*




[ChargeCustomerResponse](#ChargeCustomerResponse)

Success. Check the example shown below or refer `ChargeCustomerResponse` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "message": "Payment Successful",
  "status": "complete",
  "order_id": "FY000000001000000101",
  "aggregator": "Simpl",
  "cart_id": "0000000",
  "delivery_address_id": "0000000"
}
```
</details>









---


### initialisePayment
Initialize a payment (server-to-server) for UPI and BharatQR




```python
try:
    result = await client.payment.initialisePayment(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [PaymentInitializationRequest](#PaymentInitializationRequest) | yes | Request body |


PUse this API to inititate payment using UPI, BharatQR, wherein the UPI requests are send to the app and QR code is displayed on the screen.

*Returned Response:*




[PaymentInitializationResponse](#PaymentInitializationResponse)

Success. Check the example shown below or refer `PaymentInitializationResponse` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "aggregator": "UPI_Razorpay",
  "method": "upi",
  "status": "success",
  "merchant_order_id": "FY000120000101",
  "aggregator_order_id": "lorem_GX8W00p2ipsum",
  "polling_url": "https://api.fynd.com/service/application/payment/v0.1/payments/confirm/polling/?app_id=000000000000000000000001",
  "timeout": 240,
  "virtual_id": null,
  "razorpay_payment_id": "pay_dummy_001",
  "customer_id": "cust_dummy_001"
}
```
</details>









---


### checkAndUpdatePaymentStatus
Performs continuous polling to check status of payment on the server




```python
try:
    result = await client.payment.checkAndUpdatePaymentStatus(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [PaymentStatusUpdateRequest](#PaymentStatusUpdateRequest) | yes | Request body |


Use this API to perform continuous polling at intervals to check the status of payment until timeout.

*Returned Response:*




[PaymentStatusUpdateResponse](#PaymentStatusUpdateResponse)

Success. Returns the status of payment. Check the example shown below or refer `PaymentStatusUpdateResponse` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "aggregator_name": "UPI_Razorpay",
  "status": "success",
  "retry": false
}
```
</details>









---


### getPaymentModeRoutes
Get applicable payment options




```python
try:
    result = await client.payment.getPaymentModeRoutes(amount=amount, cartId=cartId, pincode=pincode, checkoutMode=checkoutMode, refresh=refresh, cardReference=cardReference, userDetails=userDetails)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| amount | Int | yes | Payable amount. |   
| cartId | String | yes | Identifier of the cart. |   
| pincode | String | yes | The PIN Code of the destination address, e.g. 400059 |   
| checkoutMode | String | yes | Option to checkout for self or for others. |   
| refresh | Boolean? | no | This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one. |   
| cardReference | String? | no | Card reference id of user's debit or credit card. |   
| userDetails | String? | no | URIencoded JSON containing details of an anonymous user. |  



Use this API to get all valid payment options for doing a payment.

*Returned Response:*




[PaymentModeRouteResponse](#PaymentModeRouteResponse)

Success. Returns all available options for payment. Check the example shown below or refer `PaymentModeRouteResponse` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "payment_options": {
    "payment_option": [
      {
        "name": "CARD",
        "display_priority": 2,
        "payment_mode_id": 2,
        "display_name": "Card",
        "list": [],
        "anonymous_enable": true,
        "aggregator_name": "Razorpay",
        "add_card_enabled": false,
        "save_card": true
      },
      {
        "name": "NB",
        "display_priority": 3,
        "payment_mode_id": 3,
        "display_name": "Net Banking",
        "list": [
          {
            "aggregator_name": "Razorpay",
            "name": "ICICI Bank",
            "code": "ICIC",
            "bank_name": "ICICI Bank",
            "bank_code": "ICIC",
            "url": "https://hdn-1.fynd.com/payment/NB_ICICI.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_ICICI.png",
              "large": "https://hdn-1.fynd.com/payment/NB_ICICI.png"
            },
            "merchant_code": "NB_ICICI",
            "display_priority": 1,
            "display_name": "ICICI Bank"
          },
          {
            "aggregator_name": "Razorpay",
            "name": "HDFC Bank",
            "code": "HDFC",
            "bank_name": "HDFC Bank",
            "bank_code": "HDFC",
            "url": "https://hdn-1.fynd.com/payment/NB_HDFC.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_HDFC.png",
              "large": "https://hdn-1.fynd.com/payment/NB_HDFC.png"
            },
            "merchant_code": "NB_HDFC",
            "display_priority": 2,
            "display_name": "HDFC Bank"
          },
          {
            "aggregator_name": "Razorpay",
            "name": "Axis Bank",
            "code": "UTIB",
            "bank_name": "Axis Bank",
            "bank_code": "UTIB",
            "url": "https://hdn-1.fynd.com/payment/NB_AXIS.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_AXIS.png",
              "large": "https://hdn-1.fynd.com/payment/NB_AXIS.png"
            },
            "merchant_code": "NB_AXIS",
            "display_priority": 3,
            "display_name": "Axis Bank"
          },
          {
            "aggregator_name": "Razorpay",
            "name": "State Bank of India",
            "code": "SBIN",
            "bank_name": "State Bank of India",
            "bank_code": "SBIN",
            "url": "https://hdn-1.fynd.com/payment/NB_SBI.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_SBI.png",
              "large": "https://hdn-1.fynd.com/payment/NB_SBI.png"
            },
            "merchant_code": "NB_SBI",
            "display_priority": 4,
            "display_name": "State Bank of India"
          },
          {
            "aggregator_name": "Razorpay",
            "name": "Kotak Mahindra Bank",
            "code": "KKBK",
            "bank_name": "Kotak Mahindra Bank",
            "bank_code": "KKBK",
            "url": "https://hdn-1.fynd.com/payment/NB_KOTAK.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_KOTAK.png",
              "large": "https://hdn-1.fynd.com/payment/NB_KOTAK.png"
            },
            "merchant_code": "NB_KOTAK",
            "display_priority": 5,
            "display_name": "Kotak Mahindra Bank"
          },
          {
            "aggregator_name": "Razorpay",
            "name": "Indusind Bank",
            "code": "INDB",
            "bank_name": "Indusind Bank",
            "bank_code": "INDB",
            "url": "https://hdn-1.fynd.com/payment/NB_INDUS.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_INDUS.png",
              "large": "https://hdn-1.fynd.com/payment/NB_INDUS.png"
            },
            "merchant_code": "INDB",
            "display_priority": 6,
            "display_name": "Indusind Bank"
          },
          {
            "aggregator_name": "Razorpay",
            "name": "City Union Bank",
            "code": "CIUB",
            "bank_name": "City Union Bank",
            "bank_code": "CIUB",
            "url": "https://hdn-1.fynd.com/payment/NB_generic.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_generic.png",
              "large": "https://hdn-1.fynd.com/payment/NB_generic.png"
            },
            "merchant_code": "NB_CUB",
            "display_priority": 9,
            "display_name": "City Union Bank"
          },
          {
            "aggregator_name": "Razorpay",
            "name": "Catholic Syrian Bank",
            "code": "CSBK",
            "bank_name": "Catholic Syrian Bank",
            "bank_code": "CSBK",
            "url": "https://hdn-1.fynd.com/payment/NB_generic.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_generic.png",
              "large": "https://hdn-1.fynd.com/payment/NB_generic.png"
            },
            "merchant_code": "CSBK",
            "display_priority": 11,
            "display_name": "Catholic Syrian Bank"
          },
          {
            "aggregator_name": "Razorpay",
            "name": "State Bank of Hyderabad",
            "code": "SBHY",
            "bank_name": "State Bank of Hyderabad",
            "bank_code": "SBHY",
            "url": "https://hdn-1.fynd.com/payment/NB_generic.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_generic.png",
              "large": "https://hdn-1.fynd.com/payment/NB_generic.png"
            },
            "merchant_code": "NB_SBH",
            "display_priority": 12,
            "display_name": "State Bank of Hyderabad"
          },
          {
            "aggregator_name": "Razorpay",
            "name": "Allahabad Bank",
            "code": "ALLA",
            "bank_name": "Allahabad Bank",
            "bank_code": "ALLA",
            "url": "https://hdn-1.fynd.com/payment/NB_generic.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_generic.png",
              "large": "https://hdn-1.fynd.com/payment/NB_generic.png"
            },
            "merchant_code": "ALLA",
            "display_priority": 15,
            "display_name": "Allahabad Bank"
          },
          {
            "aggregator_name": "Razorpay",
            "name": "Syndicate Bank",
            "code": "SYNB",
            "bank_name": "Syndicate Bank",
            "bank_code": "SYNB",
            "url": "https://hdn-1.fynd.com/payment/NB_generic.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_generic.png",
              "large": "https://hdn-1.fynd.com/payment/NB_generic.png"
            },
            "merchant_code": "SYNB",
            "display_priority": 17,
            "display_name": "Syndicate Bank"
          }
        ]
      },
      {
        "name": "WL",
        "display_priority": 4,
        "payment_mode_id": 4,
        "display_name": "Wallet",
        "list": [
          {
            "wallet_name": "Paytm",
            "wallet_code": "paytm",
            "name": "Paytm",
            "display_name": "Paytm",
            "code": "paytm",
            "wallet_id": 4,
            "merchant_code": "PAYTM",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/paytm_logo_small.png",
              "large": "https://hdn-1.fynd.com/payment/paytm_logo_large.png"
            },
            "aggregator_name": "Juspay",
            "display_priority": 1
          },
          {
            "wallet_name": "Amazon Pay",
            "wallet_code": "amazonpay",
            "name": "Amazon Pay",
            "display_name": "Amazon Pay",
            "code": "amazonpay",
            "wallet_id": 10,
            "merchant_code": "AMAZONPAY",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/amazon-pay.png",
              "large": "https://hdn-1.fynd.com/payment/amazon-pay.png"
            },
            "aggregator_name": "Razorpay",
            "display_priority": 9
          }
        ]
      },
      {
        "name": "UPI",
        "display_priority": 9,
        "payment_mode_id": 7,
        "display_name": "UPI",
        "list": [
          {
            "aggregator_name": "Razorpay",
            "name": "UPI",
            "display_name": "BHIM UPI",
            "code": "UPI",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/upi_100x78.png",
              "large": "https://hdn-1.fynd.com/payment/upi_150x100.png"
            },
            "merchant_code": "UPI",
            "timeout": 310,
            "retry_count": 0,
            "fynd_vpa": "shopsense.rzp@hdfcbank",
            "intent_flow": true,
            "intent_app": [
              {
                "code": "google_pay",
                "display_name": "Google Pay",
                "package_name": "com.google.android.apps.nbu.paisa.user",
                "logos": {
                  "small": "https://hdn-1.fynd.com/payment/upi-google-pay.png",
                  "large": "https://hdn-1.fynd.com/payment/upi-google-pay.png"
                }
              }
            ],
            "intent_app_error_list": [
              "com.csam.icici.bank.imobile",
              "in.org.npci.upiapp",
              "com.whatsapp"
            ],
            "intent_app_error_dict_list": [
              {
                "package_name": "com.csam.icici.bank.imobile",
                "code": "icici"
              },
              {
                "package_name": "in.org.npci.upiapp",
                "code": "upiapp"
              },
              {
                "package_name": "com.whatsapp",
                "code": "whatsapp"
              }
            ]
          }
        ]
      },
      {
        "name": "JUSPAYPG",
        "display_priority": 18,
        "payment_mode_id": 24,
        "display_name": "Pay Using Juspay",
        "list": []
      },
      {
        "name": "PL",
        "display_priority": 21,
        "display_name": "Pay Later",
        "list": [
          {
            "aggregator_name": "Simpl",
            "name": "Simpl",
            "display_name": "Simpl",
            "code": "simpl",
            "merchant_code": "SIMPL",
            "logo": "https://hdn-1.fynd.com/payment/simpl_logo.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/simpl_logo.png",
              "large": "https://hdn-1.fynd.com/payment/simpl_logo.png"
            }
          },
          {
            "aggregator_name": "Potlee",
            "name": "POTLEE",
            "display_name": "Potlee",
            "code": "POTLEE",
            "merchant_code": "POTLEE",
            "logo_url": {
              "large": "https://hdn-1.fynd.com/payment/Potlee.png",
              "small": "https://hdn-1.fynd.com/payment/Potlee.png"
            }
          }
        ]
      }
    ],
    "payment_flows": {
      "simpl": {
        "data": {
          "gateway": {
            "route": "simpl",
            "entity": "sdk",
            "is_customer_validation_required": true,
            "cust_validation_url": "https://api.fyndx0.de/gringotts/api/v1/validate-customer/?app_id=000000000000000000000001",
            "sdk": {
              "config": {
                "redirect": false,
                "callback_url": null,
                "action_url": "https://api.fyndx0.de/platform/payment/v2/external/payments/confirm/charge/?app_id=000000000000000000000001"
              },
              "data": {
                "user_phone": "9999632145",
                "user_email": "app@fynd.com"
              }
            },
            "return_url": null
          }
        },
        "api_link": "",
        "payment_flow": "sdk",
        "payment_flow_data": {
          "is_customer_validation_required": true,
          "cust_validation_url": "https://api.fyndx0.de/platform/payment/api/v1/validate-customer/?app_id=000000000000000000000001",
          "config": {
            "redirect": false,
            "final_payment_action_url": "https://api.fyndx0.de/platform/payment/v2/external/payments/confirm/charge/?app_id=000000000000000000000001"
          },
          "data": {
            "user_phone": null,
            "user_email": null
          },
          "return_url": null
        }
      },
      "potlee": {
        "data": {
          "gateway": {
            "route": "potlee",
            "entity": "api",
            "is_customer_validation_required": true,
            "cust_validation_url": "https://api.fyndx0.de/gringotts/api/v1/validate-customer/",
            "return_url": null
          },
          "payment_flow_data": {
            "is_customer_validation_required": true,
            "cust_validation_url": "https://api.fyndx0.de/platform/payment/v2/external/payments/callback/",
            "config": {
              "redirect": true,
              "final_payment_action_url": "https://api.fyndx0.de/platform/payment/v2/external/payments/callback/"
            },
            "return_url": null
          }
        },
        "api_link": "",
        "payment_flow": "api",
        "payment_flow_data": {
          "return_url": null,
          "cust_validation_url": "https://api.fyndx0.de/gringotts/api/v1/validate-customer/",
          "is_customer_validation_required": true
        }
      },
      "mswipe": {
        "data": {
          "gateway": {
            "sdk": {
              "config": {
                "redirect": false,
                "action_url": "url",
                "webhook_url": "url",
                "timeout": 60
              }
            }
          }
        },
        "api_link": "",
        "payment_flow": "sdk"
      },
      "juspay": {
        "data": {},
        "api_link": "https://sandbox.juspay.in/txns",
        "payment_flow": "api"
      },
      "razorpay": {
        "data": {},
        "api_link": "",
        "payment_flow": "sdk"
      },
      "bqr_razorpay": {
        "data": {},
        "api_link": "https://api.fyndx0.de/platform/payment/v2/external/payments/request/?app_id=000000000000000000000001",
        "payment_flow": "api"
      },
      "fynd": {
        "data": {},
        "api_link": "",
        "payment_flow": "api"
      },
      "jio": {
        "data": {},
        "api_link": "",
        "payment_flow": "api"
      },
      "stripe": {
        "data": {},
        "api_link": "",
        "payment_flow": "sdk"
      },
      "ccavenue": {
        "data": {},
        "api_link": "",
        "payment_flow": "sdk"
      },
      "payumoney": {
        "data": {},
        "api_link": "",
        "payment_flow": "sdk"
      },
      "rupifi": {
        "data": {},
        "api_link": "",
        "return_url": "",
        "payment_flow": "api",
        "cust_validation_url": "https://api.jiox0.de/gringotts/api/v1/validate-customer/",
        "payment_flow_data": {
          "is_customer_validation_required": true,
          "cust_validation_url": "https://api.fyndx0.de/platform/payment/api/v1/validate-customer/?app_id=000000000000000000000001",
          "config": {
            "redirect": false,
            "final_payment_action_url": "https://api.fyndx0.de/platform/payment/v2/external/payments/confirm/charge/?app_id=000000000000000000000001"
          },
          "data": {
            "user_phone": null,
            "user_email": null
          },
          "return_url": null
        }
      },
      "jiopay": {
        "api_link": "http://psp-mandate-merchant-sit.jiomoney.com:3003/pg",
        "payment_flow": "api",
        "data": {}
      },
      "epaylater": {
        "data": {},
        "api_link": "https://api-blackbox.epaylater.in/web/process-transaction/",
        "payment_flow": "api"
      }
    }
  }
}
```
</details>









---


### getPosPaymentModeRoutes
Get applicable payment options for Point-of-Sale (POS)




```python
try:
    result = await client.payment.getPosPaymentModeRoutes(amount=amount, cartId=cartId, pincode=pincode, checkoutMode=checkoutMode, refresh=refresh, cardReference=cardReference, orderType=orderType, userDetails=userDetails)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| amount | Int | yes | Payable amount. |   
| cartId | String | yes | Identifier of the cart. |   
| pincode | String | yes | The PIN Code of the destination address, e.g. 400059 |   
| checkoutMode | String | yes | Option to checkout for self or for others. |   
| refresh | Boolean? | no | This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one. |   
| cardReference | String? | no | Card reference id of user's debit or credit card. |   
| orderType | String | yes | The order type of shipment * HomeDelivery - If the customer wants the order home-delivered * PickAtStore - If the customer wants the handover of an order at the store itself. |   
| userDetails | String? | no | URIencoded JSON containing details of an anonymous user. |  



Use this API to get all valid payment options for doing a payment in POS.

*Returned Response:*




[PaymentModeRouteResponse](#PaymentModeRouteResponse)

Success. Returns all available options for payment. Check the example shown below or refer `PaymentModeRouteResponse` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "payment_options": {
    "payment_option": [
      {
        "name": "CAS",
        "display_priority": 21,
        "payment_mode_id": 39,
        "display_name": "Cash at Store",
        "list": [
          {
            "aggregator_name": "Fynd",
            "name": "CAS",
            "display_name": "CASH",
            "code": "CAS",
            "logo_url": {
              "large": "https://hdn-1.fynd.com/payment/cod.png",
              "small": "https://hdn-1.fynd.com/payment/cod.png"
            },
            "merchant_code": "CAS"
          }
        ]
      },
      {
        "name": "CSAS",
        "display_priority": 21,
        "payment_mode_id": 40,
        "display_name": "Card Swiped at Store",
        "list": [
          {
            "aggregator_name": "Fynd",
            "name": "CSAS",
            "display_name": "Card Swipe",
            "code": "CSAS",
            "logo_url": {
              "large": "https://hdn-1.fynd.com/payment/cod.png",
              "small": "https://hdn-1.fynd.com/payment/cod.png"
            },
            "merchant_code": "CSAS"
          }
        ]
      },
      {
        "name": "UPI",
        "display_priority": 9,
        "payment_mode_id": 7,
        "display_name": "UPI",
        "list": [
          {
            "aggregator_name": "Razorpay",
            "name": "UPI",
            "display_name": "BHIM UPI",
            "code": "UPI",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/upi_100x78.png",
              "large": "https://hdn-1.fynd.com/payment/upi_150x100.png"
            },
            "merchant_code": "UPI",
            "timeout": 240,
            "retry_count": 0,
            "fynd_vpa": "shopsense.rzp@hdfcbank",
            "intent_flow": true,
            "intent_app": [
              {
                "code": "google_pay",
                "display_name": "Google Pay",
                "package_name": "com.google.android.apps.nbu.paisa.user",
                "logos": {
                  "small": "https://hdn-1.fynd.com/payment/upi-google-pay.png",
                  "large": "https://hdn-1.fynd.com/payment/upi-google-pay.png"
                }
              }
            ],
            "intent_app_error_list": [
              "com.csam.icici.bank.imobile",
              "in.org.npci.upiapp",
              "com.whatsapp"
            ],
            "intent_app_error_dict_list": [
              {
                "package_name": "com.csam.icici.bank.imobile",
                "code": "icici"
              },
              {
                "package_name": "in.org.npci.upiapp",
                "code": "upiapp"
              },
              {
                "package_name": "com.whatsapp",
                "code": "whatsapp"
              }
            ]
          }
        ]
      }
    ],
    "payment_flows": {
      "simpl": {
        "data": {
          "gateway": {
            "route": "simpl",
            "entity": "sdk",
            "is_customer_validation_required": true,
            "cust_validation_url": "https://api.fyndx0.de/gringotts/api/v1/validate-customer/?app_id=000000000000000000000001",
            "sdk": {
              "config": {
                "redirect": false,
                "callback_url": null,
                "action_url": "https://api.fyndx0.de/platform/payment/v2/external/payments/confirm/charge/?app_id=000000000000000000000001"
              },
              "data": {
                "user_phone": "9999632145",
                "user_email": "app@fynd.com"
              }
            },
            "return_url": null
          }
        },
        "api_link": "",
        "payment_flow": "sdk"
      },
      "juspay": {
        "data": {},
        "api_link": "https://sandbox.juspay.in/txns",
        "payment_flow": "api"
      },
      "razorpay": {
        "data": {},
        "api_link": "",
        "payment_flow": "sdk"
      },
      "upi_razorpay": {
        "data": {},
        "api_link": "https://api.fyndx0.de/platform/payment/v2/external/payments/request/?app_id=000000000000000000000001",
        "payment_flow": "api"
      },
      "bqr_razorpay": {
        "data": {},
        "api_link": "https://api.fyndx0.de/platform/payment/v2/external/payments/request/?app_id=000000000000000000000001",
        "payment_flow": "api"
      },
      "cashfree": {
        "data": {},
        "api_link": "",
        "payment_flow": "api"
      },
      "fynd": {
        "data": {},
        "api_link": "",
        "payment_flow": "api"
      },
      "jio": {
        "data": {},
        "api_link": "",
        "payment_flow": "api"
      },
      "stripe": {
        "data": {},
        "api_link": "",
        "payment_flow": "sdk"
      },
      "ccavenue": {
        "data": {},
        "api_link": "",
        "payment_flow": "sdk"
      },
      "payumoney": {
        "data": {},
        "api_link": "",
        "payment_flow": "sdk"
      },
      "rupifi": {
        "data": {},
        "api_link": "",
        "return_url": "",
        "payment_flow": "api",
        "cust_validation_url": "https://api.jiox0.de/gringotts/api/v1/validate-customer/"
      }
    }
  }
}
```
</details>









---


### getRupifiBannerDetails
Get CreditLine Offer




```python
try:
    result = await client.payment.getRupifiBannerDetails()
    # use result
except Exception as e:
    print(e)
```






Get CreditLine Offer if user is tentatively approved by rupifi

*Returned Response:*




[RupifiBannerResponse](#RupifiBannerResponse)

Success. Return CreditLine Offer detail. Check the example shown below or refer `RupifiBannerResponseSchema` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "data": {
    "kyc_url": "http://rupifi.kyc1.com/",
    "status": "APPROVED"
  }
}
```
</details>









---


### getEpaylaterBannerDetails
Get Epaylater Enabled




```python
try:
    result = await client.payment.getEpaylaterBannerDetails()
    # use result
except Exception as e:
    print(e)
```






Get Epaylater Enabled if user is tentatively approved by epaylater

*Returned Response:*




[EpaylaterBannerResponse](#EpaylaterBannerResponse)

Success. Return Epaylater Offer detail. Check the example shown below or refer `EpaylaterBannerResponseSchema` for more details. if `display=True`, then show banner otherwise do not show.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; User is registered successfully</i></summary>

```json
{
  "value": {
    "success": true,
    "data": {
      "display": false,
      "message": "User is Active",
      "status": "ACTIVE"
    }
  }
}
```
</details>

<details>
<summary><i>&nbsp; User is not registered or KYC not done or approval pending</i></summary>

```json
{
  "value": {
    "success": true,
    "data": {
      "display": true,
      "message": "User is not registered",
      "status": "NOT REGISTERED"
    }
  }
}
```
</details>

</details>









---


### resendOrCancelPayment
API to resend and cancel a payment link which was already generated.




```python
try:
    result = await client.payment.resendOrCancelPayment(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [ResendOrCancelPaymentRequest](#ResendOrCancelPaymentRequest) | yes | Request body |


Use this API to perform resend or cancel a payment link based on request payload.

*Returned Response:*




[ResendOrCancelPaymentResponse](#ResendOrCancelPaymentResponse)

Success. Returns the status of payment. Check the example shown below or refer `ResendOrCancelPaymentResponse` for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; request_type is cancel</i></summary>

```json
{
  "value": {
    "success": true,
    "data": {
      "message": "Payment link Cancelled.",
      "status": true
    }
  }
}
```
</details>

<details>
<summary><i>&nbsp; request_type is resend</i></summary>

```json
{
  "value": {
    "success": true,
    "data": {
      "message": "Notification triggered.",
      "status": true
    }
  }
}
```
</details>

</details>









---


### getActiveRefundTransferModes
Lists the mode of refund




```python
try:
    result = await client.payment.getActiveRefundTransferModes()
    # use result
except Exception as e:
    print(e)
```






Use this API to retrieve eligible refund modes (such as Netbanking) and add the beneficiary details.

*Returned Response:*




[TransferModeResponse](#TransferModeResponse)

Success. Shows the available refund mode to choose, e.g. Netbanking. Check the example shown below or refer `TransferModeResponse` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "data": [
    {
      "display_name": "BANK",
      "items": [
        {
          "id": 6,
          "name": "bank",
          "display_name": "BANK",
          "logo_small": "https://hdn-1.fynd.com/payment/netbanking.png",
          "logo_large": "https://hdn-1.fynd.com/payment/netbanking.png"
        }
      ]
    }
  ]
}
```
</details>









---


### enableOrDisableRefundTransferMode
Enable/Disable a mode for transferring a refund




```python
try:
    result = await client.payment.enableOrDisableRefundTransferMode(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [UpdateRefundTransferModeRequest](#UpdateRefundTransferModeRequest) | yes | Request body |


Activate or Deactivate Transfer Mode to collect Beneficiary Details for Refund

*Returned Response:*




[UpdateRefundTransferModeResponse](#UpdateRefundTransferModeResponse)

Success. Shows whether the refund mode was successfully enabled or disabled.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true
}
```
</details>









---


### getUserBeneficiariesDetail
Lists the beneficiary of a refund




```python
try:
    result = await client.payment.getUserBeneficiariesDetail(orderId=orderId)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| orderId | String | yes | A unique number used for identifying and tracking your orders. |  



Use this API to get the details of all active beneficiary added by a user for refund.

*Returned Response:*




[OrderBeneficiaryResponse](#OrderBeneficiaryResponse)

Success. Returns the details of the beneficiary getting a refund. Check the example shown below or refer `OrderBeneficiaryResponse` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "beneficiaries": [
    {
      "id": 221,
      "beneficiary_id": "0f7e44a922df352c05c5f73cb40ba115",
      "bank_name": "State Bank of India",
      "branch_name": "State Bank of India",
      "account_holder": "SHASHI TEST",
      "account_no": "1234567891",
      "ifsc_code": "SBIN0005611",
      "mobile": "9112042174",
      "email": "payment@gofynd.com",
      "address": "204A",
      "comment": "",
      "is_active": null,
      "created_on": "2020-06-29 12:38:39",
      "modified_on": "2020-06-29 12:38:39",
      "display_name": "BANK",
      "transfer_mode": "bank",
      "title": "Bank Account",
      "subtitle": "1234567891",
      "delights_user_name": null
    }
  ],
  "show_beneficiary_details": false
}
```
</details>









---


### verifyIfscCode
Verify IFSC Code




```python
try:
    result = await client.payment.verifyIfscCode(ifscCode=ifscCode)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| ifscCode | String? | no | A 11-digit alphanumeric code that uniquely identifies a bank branch. |  



Use this API to check whether the 11-digit IFSC code is valid and to fetch the bank details for refund.

*Returned Response:*




[IfscCodeResponse](#IfscCodeResponse)

Success. Shows whether the IFSC code is valid, and returns the bank details. Check the example shown below or refer `IfscCodeResponse` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "branch_name": "MANPUR",
  "bank_name": "GAYA",
  "BRANCH": "MANPUR",
  "CENTRE": "GAYA",
  "DISTRICT": "GAYA",
  "STATE": "BIHAR",
  "ADDRESS": "POBUNIYADGANJBIHAR",
  "CONTACT": "00",
  "MICR": "816002103",
  "UPI": true,
  "RTGS": true,
  "CITY": "GAYA",
  "NEFT": true,
  "IMPS": true,
  "SWIFT": "",
  "BANK": "State Bank of India",
  "BANKCODE": "SBIN",
  "IFSC": "SBIN0005611",
  "success": true
}
```
</details>









---


### getOrderBeneficiariesDetail
Lists the beneficiary of a refund




```python
try:
    result = await client.payment.getOrderBeneficiariesDetail(orderId=orderId)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| orderId | String | yes | A unique number used for identifying and tracking your orders. |  



Use this API to get the details of all active beneficiary added by a user for refund.

*Returned Response:*




[OrderBeneficiaryResponse](#OrderBeneficiaryResponse)

Success. Returns the details of the beneficiary getting a refund. Check the example shown below or refer `OrderBeneficiaryResponse` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "beneficiaries": [
    {
      "id": 3695,
      "beneficiary_id": "4c86dd56e634a4c6a8fb51d195bc7b83",
      "bank_name": "State Bank of India",
      "branch_name": "BHOGAT",
      "account_holder": "PRAKASH TEST",
      "account_no": "3566342455454",
      "ifsc_code": "SBIN0014982",
      "mobile": "7819064010",
      "email": "prakashtest@gmail.com",
      "address": "49A, Dabhi seri, jodhpur, kalyanpur",
      "comment": "COD Refund",
      "is_active": null,
      "created_on": "2021-01-22 11:31:02",
      "modified_on": "2021-01-22 11:31:02",
      "display_name": "BANK",
      "transfer_mode": "bank",
      "title": "Bank Account",
      "subtitle": "35663423659",
      "delights_user_name": "shreeniwas_24x7_gmail_com_45978_16624463"
    }
  ]
}
```
</details>









---


### verifyOtpAndAddBeneficiaryForBank
Verify the beneficiary details using OTP




```python
try:
    result = await client.payment.verifyOtpAndAddBeneficiaryForBank(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [AddBeneficiaryViaOtpVerificationRequest](#AddBeneficiaryViaOtpVerificationRequest) | yes | Request body |


Use this API to perform an OTP validation before saving the beneficiary details added for a refund.

*Returned Response:*




[AddBeneficiaryViaOtpVerificationResponse](#AddBeneficiaryViaOtpVerificationResponse)

Success. Check the example shown below or refer `AddBeneficiaryViaOtpVerificationRequest` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "message": "Account successfully created"
}
```
</details>









---


### addBeneficiaryDetails
Save bank details for cancelled/returned order




```python
try:
    result = await client.payment.addBeneficiaryDetails(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [AddBeneficiaryDetailsRequest](#AddBeneficiaryDetailsRequest) | yes | Request body |


Use this API to save the bank details for a returned or cancelled order to refund the amount.

*Returned Response:*




[RefundAccountResponse](#RefundAccountResponse)

Success. Shows whether the beneficiary details were saved to a returned/cancelled order or not.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "message": "Account successfully created",
  "data": {},
  "is_verified_flag": true
}
```
</details>









---


### addRefundBankAccountUsingOTP
Save bank details for cancelled/returned order




```python
try:
    result = await client.payment.addRefundBankAccountUsingOTP(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [AddBeneficiaryDetailsOTPRequest](#AddBeneficiaryDetailsOTPRequest) | yes | Request body |


Use this API to save bank details for returned/cancelled order to refund amount in his account.

*Returned Response:*




[RefundAccountResponse](#RefundAccountResponse)

Success. Shows whether the beneficiary details were saved to a returned/cancelled order or not.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "message": "Account successfully created",
  "data": {},
  "is_verified_flag": true
}
```
</details>









---


### verifyOtpAndAddBeneficiaryForWallet
Send OTP on adding a wallet beneficiary




```python
try:
    result = await client.payment.verifyOtpAndAddBeneficiaryForWallet(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [WalletOtpRequest](#WalletOtpRequest) | yes | Request body |


Use this API to send an OTP while adding a wallet beneficiary by mobile no. verification.

*Returned Response:*




[WalletOtpResponse](#WalletOtpResponse)

Success. Sends the OTP to the given mobile number. Check the example shown below or refer `WalletOtpResponse` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "is_verified_flag": false,
  "request_id": "c3ca6c13d490c885a125d106b45697b7"
}
```
</details>









---


### updateDefaultBeneficiary
Set a default beneficiary for a refund




```python
try:
    result = await client.payment.updateDefaultBeneficiary(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [SetDefaultBeneficiaryRequest](#SetDefaultBeneficiaryRequest) | yes | Request body |


Use this API to set a default beneficiary for getting a refund.

*Returned Response:*




[SetDefaultBeneficiaryResponse](#SetDefaultBeneficiaryResponse)

Success. Check the example shown below or refer `SetDefaultBeneficiaryResponse` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "is_beneficiary_set": true
}
```
</details>









---


### getPaymentLink
Get payment link




```python
try:
    result = await client.payment.getPaymentLink(paymentLinkId=paymentLinkId)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| paymentLinkId | String? | no |  |  



Use this API to get a payment link

*Returned Response:*




[GetPaymentLinkResponse](#GetPaymentLinkResponse)

Success. Check the example shown below




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "message": "Payment link",
  "status_code": 200,
  "payment_link_current_status": "resent",
  "payment_link_url": "https://api.fyndx0.de/service/application/payment/v1.0/payment/options/link/?id=4adb4451720a82ee69a3c1c4cc9ab442&refresh=false",
  "external_order_id": "FY62614DF9D5CF31D3D0",
  "amount": 21900,
  "merchant_name": "Fynd",
  "polling_timeout": 1800
}
```
</details>









---


### createPaymentLink
Create payment link




```python
try:
    result = await client.payment.createPaymentLink(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [CreatePaymentLinkRequest](#CreatePaymentLinkRequest) | yes | Request body |


Use this API to create a payment link for the customer

*Returned Response:*




[CreatePaymentLinkResponse](#CreatePaymentLinkResponse)

Success. Check the example shown below




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "message": "Payment link created",
  "status_code": 200,
  "payment_link_url": "https://api.fyndx0.de/service/application/payment/v1.0/payment/options/link/?id=96b15ea2014a76c8d2774783e239ce26&refresh=false",
  "payment_link_id": "96b15ea2014a76c8d2774783e239ce26",
  "polling_timeout": 480
}
```
</details>









---


### resendPaymentLink
Resend payment link




```python
try:
    result = await client.payment.resendPaymentLink(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [CancelOrResendPaymentLinkRequest](#CancelOrResendPaymentLinkRequest) | yes | Request body |


Use this API to resend a payment link for the customer

*Returned Response:*




[ResendPaymentLinkResponse](#ResendPaymentLinkResponse)

Success. Check the example shown below




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "message": "Payment link resent",
  "status_code": 200,
  "polling_timeout": 480
}
```
</details>









---


### cancelPaymentLink
Cancel payment link




```python
try:
    result = await client.payment.cancelPaymentLink(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [CancelOrResendPaymentLinkRequest](#CancelOrResendPaymentLinkRequest) | yes | Request body |


Use this API to cancel a payment link for the customer

*Returned Response:*




[CancelPaymentLinkResponse](#CancelPaymentLinkResponse)

Success. Check the example shown below




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "message": "Payment link cancelled",
  "status_code": 200
}
```
</details>









---


### getPaymentModeRoutesPaymentLink
Get applicable payment options for payment link




```python
try:
    result = await client.payment.getPaymentModeRoutesPaymentLink(paymentLinkId=paymentLinkId)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| paymentLinkId | String | yes | Payment link id |  



Use this API to get all valid payment options for doing a payment through payment link

*Returned Response:*




[PaymentModeRouteResponse](#PaymentModeRouteResponse)

Success. Returns all available options for payment. Check the example shown below or refer `PaymentModeRouteResponse` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "payment_options": {
    "payment_option": [
      {
        "name": "CARD",
        "display_priority": 2,
        "payment_mode_id": 2,
        "display_name": "Card",
        "list": [],
        "anonymous_enable": true,
        "aggregator_name": "Razorpay",
        "add_card_enabled": false,
        "is_pay_by_card_pl": true
      },
      {
        "name": "NB",
        "display_priority": 3,
        "payment_mode_id": 3,
        "display_name": "Net Banking",
        "list": [
          {
            "aggregator_name": "Razorpay",
            "name": "ICICI Bank",
            "code": "ICIC",
            "bank_name": "ICICI Bank",
            "bank_code": "ICIC",
            "url": "https://hdn-1.fynd.com/payment/NB_ICICI.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_ICICI.png",
              "large": "https://hdn-1.fynd.com/payment/NB_ICICI.png"
            },
            "merchant_code": "NB_ICICI",
            "display_priority": 1,
            "display_name": "ICICI Bank"
          },
          {
            "aggregator_name": "Razorpay",
            "name": "HDFC Bank",
            "code": "HDFC",
            "bank_name": "HDFC Bank",
            "bank_code": "HDFC",
            "url": "https://hdn-1.fynd.com/payment/NB_HDFC.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_HDFC.png",
              "large": "https://hdn-1.fynd.com/payment/NB_HDFC.png"
            },
            "merchant_code": "NB_HDFC",
            "display_priority": 2,
            "display_name": "HDFC Bank"
          },
          {
            "aggregator_name": "Razorpay",
            "name": "Axis Bank",
            "code": "UTIB",
            "bank_name": "Axis Bank",
            "bank_code": "UTIB",
            "url": "https://hdn-1.fynd.com/payment/NB_AXIS.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_AXIS.png",
              "large": "https://hdn-1.fynd.com/payment/NB_AXIS.png"
            },
            "merchant_code": "NB_AXIS",
            "display_priority": 3,
            "display_name": "Axis Bank"
          },
          {
            "aggregator_name": "Razorpay",
            "name": "State Bank of India",
            "code": "SBIN",
            "bank_name": "State Bank of India",
            "bank_code": "SBIN",
            "url": "https://hdn-1.fynd.com/payment/NB_SBI.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_SBI.png",
              "large": "https://hdn-1.fynd.com/payment/NB_SBI.png"
            },
            "merchant_code": "NB_SBI",
            "display_priority": 4,
            "display_name": "State Bank of India"
          },
          {
            "aggregator_name": "Razorpay",
            "name": "Kotak Mahindra Bank",
            "code": "KKBK",
            "bank_name": "Kotak Mahindra Bank",
            "bank_code": "KKBK",
            "url": "https://hdn-1.fynd.com/payment/NB_KOTAK.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_KOTAK.png",
              "large": "https://hdn-1.fynd.com/payment/NB_KOTAK.png"
            },
            "merchant_code": "NB_KOTAK",
            "display_priority": 5,
            "display_name": "Kotak Mahindra Bank"
          },
          {
            "aggregator_name": "Razorpay",
            "name": "Indusind Bank",
            "code": "INDB",
            "bank_name": "Indusind Bank",
            "bank_code": "INDB",
            "url": "https://hdn-1.fynd.com/payment/NB_INDUS.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_INDUS.png",
              "large": "https://hdn-1.fynd.com/payment/NB_INDUS.png"
            },
            "merchant_code": "INDB",
            "display_priority": 6,
            "display_name": "Indusind Bank"
          },
          {
            "aggregator_name": "Razorpay",
            "name": "City Union Bank",
            "code": "CIUB",
            "bank_name": "City Union Bank",
            "bank_code": "CIUB",
            "url": "https://hdn-1.fynd.com/payment/NB_generic.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_generic.png",
              "large": "https://hdn-1.fynd.com/payment/NB_generic.png"
            },
            "merchant_code": "NB_CUB",
            "display_priority": 9,
            "display_name": "City Union Bank"
          },
          {
            "aggregator_name": "Razorpay",
            "name": "Catholic Syrian Bank",
            "code": "CSBK",
            "bank_name": "Catholic Syrian Bank",
            "bank_code": "CSBK",
            "url": "https://hdn-1.fynd.com/payment/NB_generic.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_generic.png",
              "large": "https://hdn-1.fynd.com/payment/NB_generic.png"
            },
            "merchant_code": "CSBK",
            "display_priority": 11,
            "display_name": "Catholic Syrian Bank"
          },
          {
            "aggregator_name": "Razorpay",
            "name": "State Bank of Hyderabad",
            "code": "SBHY",
            "bank_name": "State Bank of Hyderabad",
            "bank_code": "SBHY",
            "url": "https://hdn-1.fynd.com/payment/NB_generic.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_generic.png",
              "large": "https://hdn-1.fynd.com/payment/NB_generic.png"
            },
            "merchant_code": "NB_SBH",
            "display_priority": 12,
            "display_name": "State Bank of Hyderabad"
          },
          {
            "aggregator_name": "Razorpay",
            "name": "Allahabad Bank",
            "code": "ALLA",
            "bank_name": "Allahabad Bank",
            "bank_code": "ALLA",
            "url": "https://hdn-1.fynd.com/payment/NB_generic.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_generic.png",
              "large": "https://hdn-1.fynd.com/payment/NB_generic.png"
            },
            "merchant_code": "ALLA",
            "display_priority": 15,
            "display_name": "Allahabad Bank"
          },
          {
            "aggregator_name": "Razorpay",
            "name": "Syndicate Bank",
            "code": "SYNB",
            "bank_name": "Syndicate Bank",
            "bank_code": "SYNB",
            "url": "https://hdn-1.fynd.com/payment/NB_generic.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/NB_generic.png",
              "large": "https://hdn-1.fynd.com/payment/NB_generic.png"
            },
            "merchant_code": "SYNB",
            "display_priority": 17,
            "display_name": "Syndicate Bank"
          }
        ]
      },
      {
        "name": "WL",
        "display_priority": 4,
        "payment_mode_id": 4,
        "display_name": "Wallet",
        "list": [
          {
            "wallet_name": "Paytm",
            "wallet_code": "paytm",
            "name": "Paytm",
            "display_name": "Paytm",
            "code": "paytm",
            "wallet_id": 4,
            "merchant_code": "PAYTM",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/paytm_logo_small.png",
              "large": "https://hdn-1.fynd.com/payment/paytm_logo_large.png"
            },
            "aggregator_name": "Juspay",
            "display_priority": 1
          },
          {
            "wallet_name": "Amazon Pay",
            "wallet_code": "amazonpay",
            "name": "Amazon Pay",
            "display_name": "Amazon Pay",
            "code": "amazonpay",
            "wallet_id": 10,
            "merchant_code": "AMAZONPAY",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/amazon-pay.png",
              "large": "https://hdn-1.fynd.com/payment/amazon-pay.png"
            },
            "aggregator_name": "Razorpay",
            "display_priority": 9
          }
        ]
      },
      {
        "name": "UPI",
        "display_priority": 9,
        "payment_mode_id": 7,
        "display_name": "UPI",
        "list": [
          {
            "aggregator_name": "Razorpay",
            "name": "UPI",
            "display_name": "BHIM UPI",
            "code": "UPI",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/upi_100x78.png",
              "large": "https://hdn-1.fynd.com/payment/upi_150x100.png"
            },
            "merchant_code": "UPI",
            "timeout": 310,
            "retry_count": 0,
            "fynd_vpa": "shopsense.rzp@hdfcbank",
            "intent_flow": true,
            "intent_app": [
              {
                "code": "google_pay",
                "display_name": "Google Pay",
                "logos": {
                  "small": "https://hdn-1.fynd.com/payment/upi-google-pay.png",
                  "large": "https://hdn-1.fynd.com/payment/upi-google-pay.png"
                }
              }
            ],
            "intent_app_error_list": [
              "com.csam.icici.bank.imobile",
              "in.org.npci.upiapp",
              "com.whatsapp"
            ]
          }
        ]
      },
      {
        "name": "JUSPAYPG",
        "display_priority": 18,
        "payment_mode_id": 24,
        "display_name": "Pay Using Juspay",
        "list": []
      },
      {
        "name": "PL",
        "display_priority": 21,
        "display_name": "Pay Later",
        "list": [
          {
            "aggregator_name": "Simpl",
            "name": "Simpl",
            "display_name": "Simpl",
            "code": "simpl",
            "merchant_code": "SIMPL",
            "logo": "https://hdn-1.fynd.com/payment/simpl_logo.png",
            "logo_url": {
              "small": "https://hdn-1.fynd.com/payment/simpl_logo.png",
              "large": "https://hdn-1.fynd.com/payment/simpl_logo.png"
            }
          }
        ]
      }
    ],
    "payment_flows": {
      "simpl": {
        "data": {
          "gateway": {
            "route": "simpl",
            "entity": "sdk",
            "is_customer_validation_required": true,
            "cust_validation_url": "https://api.fyndx0.de/gringotts/api/v1/validate-customer/?app_id=000000000000000000000001",
            "sdk": {
              "config": {
                "redirect": false,
                "callback_url": null,
                "action_url": "https://api.fyndx0.de/platform/payment/v2/external/payments/confirm/charge/?app_id=000000000000000000000001"
              },
              "data": {
                "user_phone": "9999632145",
                "user_email": "app@fynd.com"
              }
            },
            "return_url": null
          }
        },
        "api_link": "",
        "payment_flow": "sdk",
        "payment_flow_data": {
          "is_customer_validation_required": true,
          "cust_validation_url": "https://api.fyndx0.de/platform/payment/api/v1/validate-customer/?app_id=000000000000000000000001",
          "config": {
            "redirect": false,
            "final_payment_action_url": "https://api.fyndx0.de/platform/payment/v2/external/payments/confirm/charge/?app_id=000000000000000000000001"
          },
          "data": {
            "user_phone": null,
            "user_email": null
          },
          "return_url": null
        }
      },
      "mswipe": {
        "data": {
          "gateway": {
            "sdk": {
              "config": {
                "redirect": false,
                "action_url": "url",
                "webhook_url": "url",
                "timeout": 60
              }
            }
          }
        },
        "api_link": "",
        "payment_flow": "sdk"
      },
      "juspay": {
        "data": {},
        "api_link": "https://sandbox.juspay.in/txns",
        "payment_flow": "api"
      },
      "razorpay": {
        "data": {},
        "api_link": "",
        "payment_flow": "sdk"
      },
      "bqr_razorpay": {
        "data": {},
        "api_link": "https://api.fyndx0.de/platform/payment/v2/external/payments/request/?app_id=000000000000000000000001",
        "payment_flow": "api"
      },
      "fynd": {
        "data": {},
        "api_link": "",
        "payment_flow": "api"
      },
      "jio": {
        "data": {},
        "api_link": "",
        "payment_flow": "api"
      },
      "stripe": {
        "data": {},
        "api_link": "",
        "payment_flow": "sdk"
      },
      "ccavenue": {
        "data": {},
        "api_link": "",
        "payment_flow": "sdk"
      },
      "payumoney": {
        "data": {},
        "api_link": "",
        "payment_flow": "sdk"
      },
      "rupifi": {
        "data": {},
        "api_link": "",
        "return_url": "",
        "payment_flow": "api",
        "cust_validation_url": "https://api.jiox0.de/gringotts/api/v1/validate-customer/",
        "payment_flow_data": {
          "is_customer_validation_required": true,
          "cust_validation_url": "https://api.fyndx0.de/platform/payment/api/v1/validate-customer/?app_id=000000000000000000000001",
          "config": {
            "redirect": false,
            "final_payment_action_url": "https://api.fyndx0.de/platform/payment/v2/external/payments/confirm/charge/?app_id=000000000000000000000001"
          },
          "data": {
            "user_phone": null,
            "user_email": null
          },
          "return_url": null
        }
      }
    }
  }
}
```
</details>









---


### pollingPaymentLink
Used for polling if payment successful or not




```python
try:
    result = await client.payment.pollingPaymentLink(paymentLinkId=paymentLinkId)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| paymentLinkId | String? | no |  |  



Use this API to poll if payment through payment was successful or not

*Returned Response:*




[PollingPaymentLinkResponse](#PollingPaymentLinkResponse)

Success. Check the example shown below




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "aggregator_name": "Fynd",
  "status": "complete",
  "redirect_url": "https://api.fyndx0.de/service/application/order/v1.0/orders/?success=true&order_id=FY62B3FF87016F24A4E6&aggregator_name=Fynd&cart_id=412&delivery_address_id=136&billing_address_id=136",
  "payment_link_id": "223d2a8df39a5dcdd8525498bee73199",
  "amount": 21900,
  "order_id": "FY62B3FF87016F24A4E6",
  "status_code": 200
}
```
</details>









---


### createOrderHandlerPaymentLink
Create Order user




```python
try:
    result = await client.payment.createOrderHandlerPaymentLink(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [CreateOrderUserRequest](#CreateOrderUserRequest) | yes | Request body |


Use this API to create a order and payment on aggregator side

*Returned Response:*




[CreateOrderUserResponse](#CreateOrderUserResponse)

Success. Check the example shown below




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "message": "",
  "success": true,
  "data": {
    "amount": 2190000,
    "order_id": "order_JeaZ5ryKO01rno",
    "email": "pratikpatel@gofynd.com",
    "contact": "8879805874",
    "currency": "INR",
    "customer_id": "cust_CZgcLVGsGP8BUQ",
    "callback_url": "https://api.fyndx0.com/service/webhooks/payment/v1.0/callback/link/?razorpay_order_id=order_JeaZ5ryKO01rno",
    "method": "upi",
    "aggregator": "Razorpay",
    "merchant_order_id": "FY629EDC0980B6A8C1EA"
  },
  "callback_url": "https://api.fyndx0.com/service/webhooks/payment/v1.0/callback/link/?razorpay_order_id=order_JeaZ5ryKO01rno",
  "payment_confirm_url": "https://api.fyndx0.com/service/webhooks/payment/v1.0/callback/link/?razorpay_order_id=order_JeaZ5ryKO01rno",
  "order_id": "FY629EDC0980B6A8C1EA"
}
```
</details>









---


### initialisePaymentPaymentLink
Initialize a payment (server-to-server) for UPI and BharatQR




```python
try:
    result = await client.payment.initialisePaymentPaymentLink(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [PaymentInitializationRequest](#PaymentInitializationRequest) | yes | Request body |


Use this API to inititate payment using UPI, BharatQR, wherein the UPI requests are send to the app and QR code is displayed on the screen.

*Returned Response:*




[PaymentInitializationResponse](#PaymentInitializationResponse)

Success. Check the example shown below or refer `PaymentInitializationResponse` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "aggregator": "UPI_Razorpay",
  "method": "upi",
  "status": "success",
  "merchant_order_id": "FY000120000101",
  "aggregator_order_id": "lorem_GX8W00p2ipsum",
  "polling_url": "https://api.fynd.com/service/application/payment/v0.1/payments/confirm/polling/?app_id=000000000000000000000001",
  "timeout": 240,
  "virtual_id": null,
  "razorpay_payment_id": "pay_dummy_001",
  "customer_id": "cust_dummy_001"
}
```
</details>









---


### checkAndUpdatePaymentStatusPaymentLink
Performs continuous polling to check status of payment on the server




```python
try:
    result = await client.payment.checkAndUpdatePaymentStatusPaymentLink(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [PaymentStatusUpdateRequest](#PaymentStatusUpdateRequest) | yes | Request body |


Use this API to perform continuous polling at intervals to check the status of payment until timeout.

*Returned Response:*




[PaymentStatusUpdateResponse](#PaymentStatusUpdateResponse)

Success. Returns the status of payment. Check the example shown below or refer `PaymentStatusUpdateResponse` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "aggregator_name": "UPI_Razorpay",
  "status": "success",
  "retry": false
}
```
</details>









---


### customerCreditSummary
API to fetch the customer credit summary




```python
try:
    result = await client.payment.customerCreditSummary(aggregator=aggregator)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| aggregator | String? | no |  |  



Use this API to fetch the customer credit summary.

*Returned Response:*




[CustomerCreditSummaryResponse](#CustomerCreditSummaryResponse)

Success. Returns the status of payment. Check the example shown below or refer `CustomerCreditSummaryResponseSchema` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "data": {
    "merchant_customer_ref_id": "ABHI0002",
    "status": "Bill Due",
    "status_message": "Pay now to avoid interest charges",
    "balance": {
      "value": 87424,
      "formatted_value": "₹ 87,424.00",
      "currency": "INR"
    },
    "limit": {
      "value": 100000,
      "formatted_value": "₹ 100,000.00",
      "currency": "INR"
    },
    "due_amount": {
      "value": 12576,
      "formatted_value": "₹ 12,576.00",
      "currency": "INR"
    },
    "used_amount": {
      "value": 12576,
      "formatted_value": "₹ 12,576.00",
      "currency": "INR"
    },
    "due_date": "Oct 22 2021",
    "days_overdue": 123
  }
}
```
</details>









---


### redirectToAggregator
API to get the redirect url to redirect the user to aggregator's page




```python
try:
    result = await client.payment.redirectToAggregator(source=source, aggregator=aggregator)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| source | String? | no | This is a String value that contains callback URL as value. |   
| aggregator | String? | no | This is a String value that contains aggregator name as value. |  



Use this API to get the redirect url to redirect the user to aggregator's page

*Returned Response:*




[RedirectToAggregatorResponse](#RedirectToAggregatorResponse)

Success. Returns the status of payment. Check the example shown below or refer `RedirectToAggregatorResponseSchema` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "data": {
    "redirect_url": "https://api-blackbox.epaylater.in//marketplace/customer/transactions/v2?encryptedPayload=dpPuB2+kZ6NyIrg0eWAwk7TbF14502RkIARgullt3PGWMh7Ix0Tc720b6idZzXNxzwaA3BOi2DHUALpqSfOagra+i0wRIVc36O62fwPscQE=checksum=6F06AEAE2A3CBBC81457FB2287C4DEFCFC16DEA8F33482D682134D64E43E34C2merchantId=Sample1234567890redirectConfirmUrl=http://localhost:8000/",
    "status": true
  }
}
```
</details>









---


### checkCredit
API to fetch the customer credit summary




```python
try:
    result = await client.payment.checkCredit(aggregator=aggregator)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| aggregator | String? | no |  |  



Use this API to fetch the customer credit summary.

*Returned Response:*




[CheckCreditResponse](#CheckCreditResponse)

Success. Returns the status of payment. Check the example shown below or refer `CheckCreditResponseSchema` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "data": {
    "is_registered": false,
    "status": true,
    "signup_url": "https://merchant.epaylater.in"
  }
}
```
</details>









---


### customerOnboard
API to fetch the customer credit summary




```python
try:
    result = await client.payment.customerOnboard(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [CustomerOnboardingRequest](#CustomerOnboardingRequest) | yes | Request body |


Use this API to fetch the customer credit summary.

*Returned Response:*




[CustomerOnboardingResponse](#CustomerOnboardingResponse)

Success. Returns the status of payment. Check the example shown below or refer `CustomerOnboardingResponseSchema` for more details.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "data": {
    "session": {
      "session_id": "109dae9a-9fe0-4277-979c-0bebb0136930"
    },
    "redirect_url": "https://retail-dev.epaylater.in?sessionId=109dae9a-9fe0-4277-979c-0bebb0136930",
    "status": true
  }
}
```
</details>









---



### Schemas

 
 
 #### [AggregatorConfigDetail](#AggregatorConfigDetail)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | verifyApi | String? |  yes  | Payment gateway verify payment api endpoint |
 | configType | String |  no  | Fynd or self payment gateway |
 | merchantKey | String? |  yes  | Unique merchant key |
 | key | String |  no  | Payment gateway api key |
 | secret | String |  no  | Masked payment gateway api secret |
 | api | String? |  yes  | Payment gateway api endpoint |
 | userId | String? |  yes  | Registered User id |
 | pin | String? |  yes  | Masked pin |
 | sdk | Boolean? |  yes  | SDK |
 | merchantId | String? |  yes  | Unique merchant id |

---


 
 
 #### [AggregatorsConfigDetailResponse](#AggregatorsConfigDetailResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | razorpay | [AggregatorConfigDetail](#AggregatorConfigDetail)? |  yes  |  |
 | ccavenue | [AggregatorConfigDetail](#AggregatorConfigDetail)? |  yes  |  |
 | mswipe | [AggregatorConfigDetail](#AggregatorConfigDetail)? |  yes  |  |
 | stripe | [AggregatorConfigDetail](#AggregatorConfigDetail)? |  yes  |  |
 | juspay | [AggregatorConfigDetail](#AggregatorConfigDetail)? |  yes  |  |
 | success | Boolean |  no  |  |
 | simpl | [AggregatorConfigDetail](#AggregatorConfigDetail)? |  yes  |  |
 | rupifi | [AggregatorConfigDetail](#AggregatorConfigDetail)? |  yes  |  |
 | payumoney | [AggregatorConfigDetail](#AggregatorConfigDetail)? |  yes  |  |
 | env | String |  no  | Environment i.e Live or Test |

---


 
 
 #### [ErrorCodeAndDescription](#ErrorCodeAndDescription)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | description | String |  no  | Error human understandable description. |
 | code | String |  no  | Error descrption code. |

---


 
 
 #### [HttpErrorCodeAndResponse](#HttpErrorCodeAndResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | error | [ErrorCodeAndDescription](#ErrorCodeAndDescription) |  no  |  |
 | success | Boolean |  no  | Response is successful or not |

---


 
 
 #### [AttachCardRequest](#AttachCardRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | refresh | Boolean? |  yes  | Refresh cache flag. |
 | nameOnCard | String? |  yes  |  |
 | cardId | String |  no  | Card token of payment gateway. |
 | nickname | String? |  yes  |  |

---


 
 
 #### [AttachCardsResponse](#AttachCardsResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | data | HashMap<String,Any> |  no  | List of cards of customer. |
 | message | String? |  yes  | Human readable message. |
 | success | Boolean |  no  | Response is successful or not. |

---


 
 
 #### [CardPaymentGateway](#CardPaymentGateway)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | aggregator | String |  no  | Payment gateway name. |
 | customerId | String? |  yes  | Payment gateway customer id. |
 | api | String? |  yes  | Payment gateway CARD api endpoint |

---


 
 
 #### [ActiveCardPaymentGatewayResponse](#ActiveCardPaymentGatewayResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | cards | [CardPaymentGateway](#CardPaymentGateway) |  no  | Card's payment gateway with customer id. |
 | message | String |  no  | Human readable message. |
 | success | Boolean |  no  | Response is successful or not. |

---


 
 
 #### [Card](#Card)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | cardIssuer | String? |  yes  | card_issuer |
 | nickname | String? |  yes  | nickname |
 | cardToken | String? |  yes  | card_token |
 | cardId | String? |  yes  | card_id |
 | cardNumber | String? |  yes  | card_number |
 | cardBrandImage | String? |  yes  | card_brand_image |
 | expYear | Int? |  yes  | exp_year |
 | cardType | String? |  yes  | card_type |
 | cardName | String? |  yes  | card_name |
 | expMonth | Int? |  yes  | exp_month |
 | compliantWithTokenisationGuidelines | Boolean? |  yes  | If card is tokenised or not |
 | cardBrand | String? |  yes  | card_brand |
 | expired | Boolean? |  yes  | expired |
 | cardReference | String? |  yes  | card_reference |
 | cardFingerprint | String? |  yes  | card_fingerprint |
 | aggregatorName | String |  no  | aggregator_name |
 | cardIsin | String? |  yes  | card_isin |

---


 
 
 #### [ListCardsResponse](#ListCardsResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | data | ArrayList<[Card](#Card)>? |  yes  | List of cards of customer. |
 | message | String |  no  | Human readable message. |
 | success | Boolean |  no  | Response is successful or not. |

---


 
 
 #### [DeletehCardRequest](#DeletehCardRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | cardId | String |  no  | Card token of payment gateway. |

---


 
 
 #### [DeleteCardsResponse](#DeleteCardsResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | message | String? |  yes  | Human readable message. |
 | success | Boolean |  no  | Response is successful or not. |

---


 
 
 #### [ValidateCustomerRequest](#ValidateCustomerRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | orderItems | ArrayList<HashMap<String,Any>>? |  yes  | Extra meta fields. |
 | aggregator | String |  no  | Payment gateway name in camel case i.e Simpl, Rupifi |
 | deliveryAddress | HashMap<String,Any>? |  yes  | Extra meta fields. |
 | payload | String? |  yes  | Hashed payload string. |
 | transactionAmountInPaise | Int |  no  | Payable amount in paise |
 | phoneNumber | String |  no  | User mobile number without country code. |
 | merchantParams | HashMap<String,Any>? |  yes  | Extra meta fields. |
 | billingAddress | HashMap<String,Any>? |  yes  | Extra meta fields. |

---


 
 
 #### [ValidateCustomerResponse](#ValidateCustomerResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | data | HashMap<String,Any> |  no  | Payment gateway response data |
 | message | String |  no  | Error or success message. |
 | success | Boolean |  no  | Response is successful or not |

---


 
 
 #### [ChargeCustomerRequest](#ChargeCustomerRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | amount | Int |  no  | Chargable amount of order. |
 | aggregator | String |  no  | Payment gateway name i.e Simpl, Mswipe |
 | transactionToken | String? |  yes  | Transaction token of payment gateway. |
 | verified | Boolean? |  yes  | Already Verified flag from payment gateway i.e Mswipe |
 | orderId | String |  no  | Unique order id. |

---


 
 
 #### [ChargeCustomerResponse](#ChargeCustomerResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | aggregator | String |  no  | Payment gateway name i.e Simpl, Mswipe |
 | cartId | String? |  yes  | Cart id of customer |
 | deliveryAddressId | String? |  yes  | Delivery adddress id of customer |
 | orderId | String |  no  | Unique order id. |
 | status | String |  no  | Status of charged payment. |
 | message | String |  no  | Human readable message. |
 | success | Boolean |  no  | Response is successful or not. |

---


 
 
 #### [PaymentInitializationRequest](#PaymentInitializationRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | vpa | String? |  yes  | Customer vpa address |
 | currency | String |  no  | Currency code. |
 | amount | Int |  no  | Payable amount. |
 | email | String |  no  | Customer valid email |
 | contact | String |  no  | Customer valid mobile number |
 | aggregator | String |  no  | Payment gateway name |
 | timeout | Int? |  yes  | Payment polling timeout if not recieved response |
 | merchantOrderId | String |  no  | Unique fynd order id |
 | method | String |  no  | Payment method |
 | orderId | String |  no  | Payment gateway order id |
 | customerId | String |  no  | Payment gateway customer id. |
 | razorpayPaymentId | String? |  yes  | Payment gateway payment id |

---


 
 
 #### [PaymentInitializationResponse](#PaymentInitializationResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | vpa | String? |  yes  | Customer vpa address |
 | currency | String? |  yes  | Currency code. |
 | amount | Int? |  yes  | Payable amount. |
 | timeout | Int? |  yes  | timeout. |
 | aggregator | String |  no  | Payment gateway name |
 | merchantOrderId | String |  no  | order id |
 | upiPollUrl | String? |  yes  | UPI poll url. |
 | bqrImage | String? |  yes  | Bharath qr image url. |
 | method | String |  no  | Payment method |
 | pollingUrl | String |  no  | Polling url. |
 | aggregatorOrderId | String? |  yes  | Payment order id |
 | virtualId | String? |  yes  | Payment virtual address. |
 | status | String? |  yes  | Status of payment. |
 | customerId | String? |  yes  | Payment gateway customer id. |
 | success | Boolean |  no  | Response is successful or not. |
 | razorpayPaymentId | String? |  yes  | Payment  id. |

---


 
 
 #### [PaymentStatusUpdateRequest](#PaymentStatusUpdateRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | vpa | String |  no  | Customer vpa address |
 | currency | String |  no  | Currency code. |
 | amount | Int |  no  | Payable amount. |
 | email | String |  no  | Customer valid email |
 | aggregator | String |  no  | Payment gateway name |
 | contact | String |  no  | Customer valid mobile number |
 | merchantOrderId | String |  no  | Unique fynd order id |
 | method | String |  no  | Payment method |
 | orderId | String |  no  | Payment gateway order id |
 | status | String |  no  | Status of payment. |
 | customerId | String |  no  | Payment gateway customer id. |

---


 
 
 #### [PaymentStatusUpdateResponse](#PaymentStatusUpdateResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | retry | Boolean |  no  | Response is successful or not. |
 | redirectUrl | String? |  yes  | Redirect url |
 | status | String |  no  | Payment status |
 | aggregatorName | String |  no  | Payment gateway name |
 | success | Boolean? |  yes  | Response is successful or not |

---


 
 
 #### [AggregatorRoute](#AggregatorRoute)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | apiLink | String? |  yes  | api_link |
 | paymentFlow | String? |  yes  | payment_flow |
 | data | HashMap<String,Any>? |  yes  | Data |
 | paymentFlowData | String? |  yes  | payment_flow_data |

---


 
 
 #### [PaymentFlow](#PaymentFlow)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | jiopay | [AggregatorRoute](#AggregatorRoute)? |  yes  | Jiopay |
 | razorpay | [AggregatorRoute](#AggregatorRoute)? |  yes  | Razorpay |
 | ccavenue | [AggregatorRoute](#AggregatorRoute)? |  yes  | Ccavenue |
 | fynd | [AggregatorRoute](#AggregatorRoute)? |  yes  | Fynd |
 | mswipe | [AggregatorRoute](#AggregatorRoute)? |  yes  | mswipe |
 | stripe | [AggregatorRoute](#AggregatorRoute)? |  yes  | Stripe |
 | bqrRazorpay | [AggregatorRoute](#AggregatorRoute)? |  yes  | BQR_Razorpay |
 | payubiz | [AggregatorRoute](#AggregatorRoute)? |  yes  | Payubiz |
 | juspay | [AggregatorRoute](#AggregatorRoute)? |  yes  | Juspay |
 | upiRazorpay | [AggregatorRoute](#AggregatorRoute)? |  yes  | UPI_Razorpay |
 | simpl | [AggregatorRoute](#AggregatorRoute)? |  yes  | simpl |
 | rupifi | [AggregatorRoute](#AggregatorRoute)? |  yes  | Rupifi |
 | epaylater | [AggregatorRoute](#AggregatorRoute)? |  yes  | Epaylater |

---


 
 
 #### [IntentAppErrorList](#IntentAppErrorList)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | code | String? |  yes  | code |
 | packageName | String? |  yes  | package_name |

---


 
 
 #### [PaymentModeLogo](#PaymentModeLogo)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | large | String |  no  | large |
 | small | String |  no  | smalll |

---


 
 
 #### [IntentApp](#IntentApp)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | code | String? |  yes  | code |
 | logos | [PaymentModeLogo](#PaymentModeLogo)? |  yes  | logos |
 | packageName | String? |  yes  | package_name |
 | displayName | String? |  yes  | display_name |

---


 
 
 #### [PaymentModeList](#PaymentModeList)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | nickname | String? |  yes  | nickname |
 | cardBrandImage | String? |  yes  | card_brand_image |
 | timeout | Int? |  yes  | timeout |
 | expYear | Int? |  yes  | exp_year |
 | expMonth | Int? |  yes  | exp_month |
 | cardFingerprint | String? |  yes  | card_fingerprint |
 | aggregatorName | String |  no  | aggregator_name |
 | intentAppErrorDictList | ArrayList<[IntentAppErrorList](#IntentAppErrorList)>? |  yes  | intent_app_error_dict_list |
 | cardIssuer | String? |  yes  | card_issuer |
 | cardToken | String? |  yes  | card_token |
 | intentApp | ArrayList<[IntentApp](#IntentApp)>? |  yes  | intent_app |
 | cardType | String? |  yes  | card_type |
 | cardName | String? |  yes  | card_name |
 | cardReference | String? |  yes  | card_reference |
 | merchantCode | String? |  yes  | merchant code |
 | retryCount | Int? |  yes  | retry_count |
 | cardId | String? |  yes  | card_id |
 | cardNumber | String? |  yes  | card_number |
 | displayPriority | Int? |  yes  | Dispaly Priority |
 | compliantWithTokenisationGuidelines | Boolean? |  yes  | If card is tokenised or not |
 | intentFlow | Boolean? |  yes  | intent_flow |
 | fyndVpa | String? |  yes  | fynd_vpa |
 | displayName | String? |  yes  | display name |
 | intentAppErrorList | ArrayList<String>? |  yes  | intent_app_error_list |
 | code | String? |  yes  | code |
 | cardBrand | String? |  yes  | card_brand |
 | expired | Boolean? |  yes  | expired |
 | name | String? |  yes  | name |
 | logoUrl | [PaymentModeLogo](#PaymentModeLogo)? |  yes  | Logo |
 | cardIsin | String? |  yes  | card_isin |

---


 
 
 #### [RootPaymentMode](#RootPaymentMode)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | isPayByCardPl | Boolean? |  yes  | This flag will be true in case of Payment link payment through card |
 | displayName | String |  no  | Payment mode display name |
 | list | ArrayList<[PaymentModeList](#PaymentModeList)>? |  yes  | Payment mode |
 | addCardEnabled | Boolean? |  yes  | Annonymous card flag |
 | anonymousEnable | Boolean? |  yes  | Annonymous card flag |
 | displayPriority | Int |  no  | Dispaly Priority |
 | saveCard | Boolean? |  yes  | Card save or not |
 | name | String |  no  | Payment mode name |
 | aggregatorName | String? |  yes  | Dispaly Priority |

---


 
 
 #### [PaymentOptionAndFlow](#PaymentOptionAndFlow)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | paymentFlows | [PaymentFlow](#PaymentFlow) |  no  | payment_flows |
 | paymentOption | ArrayList<[RootPaymentMode](#RootPaymentMode)> |  no  | Payment options |

---


 
 
 #### [PaymentModeRouteResponse](#PaymentModeRouteResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | paymentOptions | [PaymentOptionAndFlow](#PaymentOptionAndFlow) |  no  | payment_options |
 | success | Boolean |  no  | Response is successful or not |

---


 
 
 #### [RupifiBannerData](#RupifiBannerData)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | status | String? |  yes  | Rupifi KYC status |
 | kycUrl | String? |  yes  | Rupifi KYC banner url. |

---


 
 
 #### [RupifiBannerResponse](#RupifiBannerResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | data | [RupifiBannerData](#RupifiBannerData) |  no  | Rupifi KYC banner details. |
 | success | Boolean |  no  | Successful or not. |

---


 
 
 #### [EpaylaterBannerData](#EpaylaterBannerData)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | display | Boolean |  no  | Need to display banner or not |
 | status | String? |  yes  | Epaylater KYC status |
 | message | String? |  yes  | ePayLater message |

---


 
 
 #### [EpaylaterBannerResponse](#EpaylaterBannerResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | data | [EpaylaterBannerData](#EpaylaterBannerData) |  no  | Epaylater KYC banner details. |
 | success | Boolean |  no  | Successful or not. |

---


 
 
 #### [ResendOrCancelPaymentRequest](#ResendOrCancelPaymentRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | requestType | String |  no  | Either resend or cancel |
 | orderId | String |  no  | Unique order id |

---


 
 
 #### [LinkStatus](#LinkStatus)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | status | Boolean |  no  | Link action status |
 | message | String |  no  | Message |

---


 
 
 #### [ResendOrCancelPaymentResponse](#ResendOrCancelPaymentResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | data | [LinkStatus](#LinkStatus) |  no  | Data about link action status. |
 | success | Boolean |  no  | Response is successful or not. |

---


 
 
 #### [TransferItemsDetails](#TransferItemsDetails)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | logoSmall | String |  no  | Beneficiary small Logo |
 | displayName | String? |  yes  | Beneficiary Display Name |
 | id | Int |  no  |   |
 | logoLarge | String |  no  | Beneficiary large Logo |
 | name | String |  no  |  Beneficiary Name |

---


 
 
 #### [TransferModeDetails](#TransferModeDetails)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | items | ArrayList<[TransferItemsDetails](#TransferItemsDetails)>? |  yes  | Beneficiary Mode Items |
 | displayName | String |  no  | Beneficiary Mode Name |

---


 
 
 #### [TransferModeResponse](#TransferModeResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | data | ArrayList<[TransferModeDetails](#TransferModeDetails)> |  no  | Response Object |

---


 
 
 #### [UpdateRefundTransferModeRequest](#UpdateRefundTransferModeRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | transferMode | String |  no  | Transfer Mode of the Beneficiary to be added |
 | enable | Boolean |  no  | True for enabling the Transfer Mode |

---


 
 
 #### [UpdateRefundTransferModeResponse](#UpdateRefundTransferModeResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | success | Boolean? |  yes  | Response is successful or not |

---


 
 
 #### [OrderBeneficiaryDetails](#OrderBeneficiaryDetails)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | transferMode | String |  no  | Transfer Mode Of Account |
 | accountNo | String |  no  | Account Number |
 | delightsUserName | String? |  yes  | User Id Who filled the Beneficiary  |
 | address | String |  no  | Address of User |
 | comment | Boolean? |  yes  | Remarks |
 | subtitle | String |  no  | SHort Title Of Account |
 | isActive | Boolean |  no  | Boolean Flag whether Beneficiary set or not |
 | beneficiaryId | String |  no  | Benenficiary Id |
 | modifiedOn | String |  no  | MOdification Date of Beneficiary |
 | id | Int |  no  |   |
 | email | String |  no  | EMail of User |
 | branchName | Boolean? |  yes  | Branch Name Of Account |
 | bankName | String |  no  | Bank Name Of Account |
 | createdOn | String |  no  | Creation Date of Beneficiary |
 | title | String |  no  | Title Of Account |
 | displayName | String |  no  | Display Name Of Account |
 | mobile | Boolean? |  yes  | MObile no of User |
 | accountHolder | String |  no  | Account Holder Name |
 | ifscCode | String |  no  | Ifsc Code Of Account |

---


 
 
 #### [OrderBeneficiaryResponse](#OrderBeneficiaryResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | showBeneficiaryDetails | Boolean? |  yes  | Show beneficiary details or not. |
 | beneficiaries | ArrayList<[OrderBeneficiaryDetails](#OrderBeneficiaryDetails)>? |  yes  | All Beneficiaries Of An Order |

---


 
 
 #### [NotFoundResourceError](#NotFoundResourceError)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | description | String |  no  | Not Found |
 | code | String |  no  | Bad Request Data |
 | success | Boolean |  no  | Response is successful or not |

---


 
 
 #### [IfscCodeResponse](#IfscCodeResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | bankName | String |  no  | Bank Name Of Account |
 | branchName | String |  no  | Branch Name Of Account |
 | success | Boolean? |  yes  | Response is successful or not |

---


 
 
 #### [ErrorCodeDescription](#ErrorCodeDescription)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | description | String |  no  | Error human understandable description. |
 | code | String |  no  | Error descrption code. |
 | success | Boolean |  no  | Response is successful or not |

---


 
 
 #### [AddBeneficiaryViaOtpVerificationRequest](#AddBeneficiaryViaOtpVerificationRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | requestId | String |  no  | Request Id sent in  |
 | hashKey | String |  no  | Hash key of the beneficiary Id |
 | otp | String |  no  | Otp sent to the given Mobile No |

---


 
 
 #### [AddBeneficiaryViaOtpVerificationResponse](#AddBeneficiaryViaOtpVerificationResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | message | String |  no  | Aggregator Response of beneficicary  |
 | success | Boolean? |  yes  | Response is successful or not |

---


 
 
 #### [WrongOtpError](#WrongOtpError)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | isVerifiedFlag | Boolean |  no  | Vefified flag. |
 | success | String |  no  | Response is successful or not |
 | description | String |  no  | Wrong OTP Code |

---


 
 
 #### [BeneficiaryModeDetails](#BeneficiaryModeDetails)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | vpa | String? |  yes  |  |
 | accountNo | String |  no  | Account NUmber of the Account Holder |
 | wallet | String? |  yes  |  |
 | mobile | String |  no  | Moblie Number of the User |
 | email | String |  no  | Email of the Account Holder |
 | address | String? |  yes  | Address of the User |
 | accountHolder | String |  no  | Name of the Account Holder |
 | branchName | String |  no  | Branch Name of the Account |
 | comment | String? |  yes  | Remarks added by The user |
 | bankName | String |  no  | Bank Name of the Account |
 | ifscCode | String |  no  | Ifsc Code of the Account |

---


 
 
 #### [AddBeneficiaryDetailsRequest](#AddBeneficiaryDetailsRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | transferMode | String |  no  | Transfer Mode of the Beneficiary to be added |
 | requestId | String? |  yes  |  |
 | otp | String? |  yes  |  |
 | shipmentId | String |  no  | Shipment Id of the respective Merchant Order Id |
 | orderId | String |  no  | Merchant Order Id |
 | delights | Boolean |  no  | True if  beneficiary to be added by delights or False if by User |
 | details | [BeneficiaryModeDetails](#BeneficiaryModeDetails) |  no  | Beneficiary bank details |

---


 
 
 #### [RefundAccountResponse](#RefundAccountResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | data | HashMap<String,Any>? |  yes  | Refund account data. |
 | message | String |  no  | Response message |
 | isVerifiedFlag | Boolean? |  yes  |  |
 | success | Boolean |  no  | Success or failure flag. |

---


 
 
 #### [BankDetailsForOTP](#BankDetailsForOTP)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | accountNo | String |  no  |  |
 | branchName | String |  no  |  |
 | accountHolder | String |  no  |  |
 | bankName | String |  no  |  |
 | ifscCode | String |  no  |  |

---


 
 
 #### [AddBeneficiaryDetailsOTPRequest](#AddBeneficiaryDetailsOTPRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | orderId | String |  no  |  |
 | details | [BankDetailsForOTP](#BankDetailsForOTP) |  no  |  |

---


 
 
 #### [WalletOtpRequest](#WalletOtpRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | mobile | String |  no  | Wallet Moblie Number of the User |
 | countryCode | String |  no  | Country Code of the Mobile Number |

---


 
 
 #### [WalletOtpResponse](#WalletOtpResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | requestId | String |  no  | request id  |
 | isVerifiedFlag | String |  no  | Boolean Flag whether OTP Validation is already done or not |
 | success | Boolean? |  yes  | Response is successful or not |

---


 
 
 #### [SetDefaultBeneficiaryRequest](#SetDefaultBeneficiaryRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | beneficiaryId | String |  no  | Beneficiary Hash Id of the beneficiary added |
 | orderId | String |  no  | Merchant Order Id |

---


 
 
 #### [SetDefaultBeneficiaryResponse](#SetDefaultBeneficiaryResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | isBeneficiarySet | Boolean |  no  | Boolean Flag whether Beneficiary set or not |
 | success | Boolean? |  yes  | Response is successful or not |

---


 
 
 #### [GetPaymentLinkResponse](#GetPaymentLinkResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | merchantName | String? |  yes  | Merchant name |
 | pollingTimeout | Int? |  yes  | Polling request timeout |
 | amount | Double? |  yes  | Total value of order |
 | statusCode | Int |  no  | HTTP status code |
 | success | Boolean |  no  | Successful or failure |
 | externalOrderId | String? |  yes  | Merchant order id |
 | paymentLinkCurrentStatus | String? |  yes  | Status of payment link |
 | message | String |  no  | Message |
 | paymentLinkUrl | String? |  yes  | Url of payment link |

---


 
 
 #### [ErrorDescription](#ErrorDescription)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | merchantName | String? |  yes  | Name of merchant that created payment link |
 | cancelled | Boolean? |  yes  | Payment link is cancelled or not |
 | msg | String? |  yes  | Message |
 | amount | Double? |  yes  | Amount paid |
 | merchantOrderId | String? |  yes  | Order id |
 | paymentTransactionId | String? |  yes  | Payment transaction id |
 | invalidId | Boolean? |  yes  | Payment link id is valid or not |
 | expired | Boolean? |  yes  | Payment link expired or not |

---


 
 
 #### [ErrorResponse](#ErrorResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | statusCode | Int |  no  | HTTP status code |
 | error | [ErrorDescription](#ErrorDescription)? |  yes  |  |
 | message | String |  no  | Message |
 | success | Boolean |  no  | Successful or failure |

---


 
 
 #### [CreatePaymentLinkMeta](#CreatePaymentLinkMeta)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | assignCardId | String? |  yes  |  |
 | amount | String |  no  |  |
 | cartId | String |  no  |  |
 | pincode | String |  no  |  |
 | checkoutMode | String |  no  |  |

---


 
 
 #### [CreatePaymentLinkRequest](#CreatePaymentLinkRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | meta | [CreatePaymentLinkMeta](#CreatePaymentLinkMeta) |  no  | Meta |
 | amount | Double |  no  | Total value of order |
 | email | String |  no  | Email to which the payment link is to be sent |
 | externalOrderId | String |  no  | Merchant order id |
 | description | String? |  yes  | Merchant order id |
 | mobileNumber | String |  no  | Mobile number to which the payment link is to be sent |

---


 
 
 #### [CreatePaymentLinkResponse](#CreatePaymentLinkResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | pollingTimeout | Int? |  yes  | Polling request timeout |
 | statusCode | Int |  no  | HTTP status code |
 | paymentLinkId | String? |  yes  | Unique id of payment link |
 | success | Boolean |  no  | Successful or failure |
 | message | String |  no  | Message |
 | paymentLinkUrl | String? |  yes  | Url of payment link |

---


 
 
 #### [CancelOrResendPaymentLinkRequest](#CancelOrResendPaymentLinkRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | paymentLinkId | String |  no  | Unique id of payment link |

---


 
 
 #### [ResendPaymentLinkResponse](#ResendPaymentLinkResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | statusCode | Int |  no  | HTTP status code |
 | pollingTimeout | Int? |  yes  | Polling request timeout |
 | message | String |  no  | Message |
 | success | Boolean |  no  | Successful or failure |

---


 
 
 #### [CancelPaymentLinkResponse](#CancelPaymentLinkResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | statusCode | Int |  no  | HTTP status code |
 | message | String |  no  | Message |
 | success | Boolean |  no  | Successful or failure |

---


 
 
 #### [PollingPaymentLinkResponse](#PollingPaymentLinkResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | amount | Double? |  yes  | Amount |
 | redirectUrl | String? |  yes  | Url to redirect to |
 | statusCode | Int? |  yes  | HTTP status code |
 | paymentLinkId | String? |  yes  | Payment link id |
 | aggregatorName | String? |  yes  | Aggregator name |
 | orderId | String? |  yes  | Fynd order id |
 | httpStatus | Int? |  yes  | HTTP status code |
 | status | String? |  yes  | Status of payment link |
 | message | String? |  yes  | Message |
 | success | Boolean? |  yes  | Successful or failure |

---


 
 
 #### [PaymentMethodsMeta](#PaymentMethodsMeta)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | paymentGateway | String |  no  | Payment gateway name |
 | paymentIdentifier | String |  no  | Payment identifier |
 | merchantCode | String |  no  | Merchant code |

---


 
 
 #### [CreateOrderUserPaymentMethods](#CreateOrderUserPaymentMethods)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | mode | String |  no  | Payment mode |
 | meta | [PaymentMethodsMeta](#PaymentMethodsMeta) |  no  | Meta |
 | name | String |  no  | Payment mode name |

---


 
 
 #### [CreateOrderUserRequest](#CreateOrderUserRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | meta | HashMap<String,Any>? |  yes  | Meta |
 | currency | String |  no  | Currency |
 | failureCallbackUrl | String |  no  | Failure page url |
 | paymentMethods | [CreateOrderUserPaymentMethods](#CreateOrderUserPaymentMethods) |  no  | Payment method details |
 | paymentLinkId | String |  no  | Unique id of payment link |
 | successCallbackUrl | String |  no  | Success  page url |

---


 
 
 #### [CreateOrderUserData](#CreateOrderUserData)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | currency | String? |  yes  | Currency |
 | callbackUrl | String? |  yes  | Callback url for aggregator |
 | amount | Double? |  yes  | Amount |
 | email | String? |  yes  | Email |
 | contact | String? |  yes  | Mobile number |
 | aggregator | String? |  yes  | Aggregator name |
 | merchantOrderId | String? |  yes  | Merchant order id |
 | method | String? |  yes  | Method |
 | orderId | String? |  yes  | Aggregator order id |
 | customerId | String? |  yes  | Aggregator customer id |

---


 
 
 #### [CreateOrderUserResponse](#CreateOrderUserResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | paymentConfirmUrl | String? |  yes  | Payment confirm url for aggregator |
 | callbackUrl | String? |  yes  | Callback url for aggregator |
 | statusCode | Int |  no  | HTTP status code |
 | orderId | String? |  yes  | Merchant order id |
 | data | [CreateOrderUserData](#CreateOrderUserData)? |  yes  |  |
 | message | String |  no  | Message |
 | success | Boolean |  no  | Successful or failure |

---


 
 
 #### [BalanceDetails](#BalanceDetails)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | value | Double |  no  | Payment amount |
 | currency | String |  no  | Currency Code |
 | formattedValue | String |  no  | Formated Amount with currency symbol |

---


 
 
 #### [CreditSummary](#CreditSummary)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | statusMessage | String |  no  | message to customer |
 | balance | [BalanceDetails](#BalanceDetails)? |  yes  | Credit summary of user. |
 | status | String |  no  | Customer Credit status |
 | merchantCustomerRefId | String |  no  | Unique aggregator customer id |

---


 
 
 #### [CustomerCreditSummaryResponse](#CustomerCreditSummaryResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | data | [CreditSummary](#CreditSummary)? |  yes  | Credit summary of user. |
 | success | Boolean |  no  | Payment confirmation updated or not. |

---


 
 
 #### [RedirectURL](#RedirectURL)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | signupUrl | String |  no  | URL to which the user may redirect. |
 | status | Boolean |  no  | Aggregator's Operation is successful or not. |

---


 
 
 #### [RedirectToAggregatorResponse](#RedirectToAggregatorResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | data | [RedirectURL](#RedirectURL) |  no  | Redirect URL. |
 | success | Boolean |  no  | Status updated or not. |

---


 
 
 #### [CreditDetail](#CreditDetail)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | signupUrl | String |  no  | URL to which the user may redirect. |
 | status | Boolean |  no  | Operation is successful or not. |
 | isRegistered | Boolean |  no  | User is registered with aggregator or not. |

---


 
 
 #### [CheckCreditResponse](#CheckCreditResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | data | [CreditDetail](#CreditDetail) |  no  | Credit summary of user. |
 | success | Boolean |  no  | Operation is successful or not. |

---


 
 
 #### [KYCAddress](#KYCAddress)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | city | String |  no  | City |
 | state | String |  no  | State |
 | landMark | String? |  yes  | Land Mark |
 | addressline1 | String |  no  | Address Line 1 |
 | pincode | String |  no  | Pincode |
 | addressline2 | String? |  yes  | Address Line 2 |
 | ownershipType | String? |  yes  | Address Owner Type |

---


 
 
 #### [BusinessDetails](#BusinessDetails)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | fssai | String? |  yes  | FDA License Number |
 | fda | String? |  yes  | Driver License |
 | vintage | String? |  yes  | Vintage |
 | pan | String? |  yes  | Pan Number |
 | entityType | String? |  yes  | Busineess Entity Type |
 | businessOwnershipType | String? |  yes  | business Ownershipp type(e.g Rented) |
 | address | [KYCAddress](#KYCAddress)? |  yes  | Address details |
 | businessType | String? |  yes  | Business Type |
 | gstin | String? |  yes  | GSTIN Number |
 | shopAndEstablishment | HashMap<String,Any>? |  yes  | Shop Establishment |
 | name | String? |  yes  | Business Name |

---


 
 
 #### [DeviceDetails](#DeviceDetails)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | deviceMake | String? |  yes  | Device maker |
 | os | String? |  yes  | OS Name |
 | identifierType | String? |  yes  | Static value = ip |
 | identificationNumber | String? |  yes  | IP |
 | deviceModel | String? |  yes  | Device Model |
 | osVersion | String? |  yes  | OS Version |
 | deviceType | String? |  yes  | Device Type(E.g. Mobile) |

---


 
 
 #### [UserPersonalInfoInDetails](#UserPersonalInfoInDetails)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | pan | String? |  yes  | Pan Number |
 | drivingLicense | String? |  yes  | Driver License |
 | passport | String? |  yes  | Passport |
 | middleName | String? |  yes  | middle Name |
 | mobileVerified | Boolean |  no  | Is Mobile Verified or not |
 | email | String |  no  | Email |
 | fathersName | String? |  yes  | Father's Name |
 | emailVerified | Boolean |  no  | Is Email Verified or not |
 | lastName | String? |  yes  | Last Name |
 | dob | String |  no  | DOB |
 | phone | String |  no  | Email |
 | gender | String? |  yes  | Gender |
 | mothersName | String? |  yes  | Mother's Name |
 | voterId | String? |  yes  | Voter ID Number |
 | firstName | String |  no  | First Name |
 | addressAsPerId | [KYCAddress](#KYCAddress) |  no  | Address details |

---


 
 
 #### [MarketplaceInfo](#MarketplaceInfo)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | membershipId | String |  no  | merchant id |
 | dateOfJoining | String? |  yes  | Date of joining |
 | name | String |  no  | Name of store |

---


 
 
 #### [CustomerOnboardingRequest](#CustomerOnboardingRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | businessInfo | [BusinessDetails](#BusinessDetails)? |  yes  | Business summary. |
 | device | [DeviceDetails](#DeviceDetails)? |  yes  | Device Details. |
 | aggregator | String |  no  | Aggregator Name |
 | personalInfo | [UserPersonalInfoInDetails](#UserPersonalInfoInDetails) |  no  | Credit summary of user. |
 | source | String |  no  | callbackURL |
 | marketplaceInfo | [MarketplaceInfo](#MarketplaceInfo)? |  yes  | Market Place info. |

---


 
 
 #### [OnboardSummary](#OnboardSummary)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | redirectUrl | String |  no  | URL to which the user may redirect. |
 | session | HashMap<String,Any> |  no  | User Session |
 | status | Boolean |  no  | Operation Status |

---


 
 
 #### [CustomerOnboardingResponse](#CustomerOnboardingResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | data | [OnboardSummary](#OnboardSummary) |  no  | Redirect URL. |
 | success | Boolean |  no  | Status updated or not. |

---



