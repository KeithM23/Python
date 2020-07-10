# PaymentCardVerificationRequest

Used to request account verification using a payment card. The expiryDate in paymentCard object is required to perform a PaymentCardVerificationRequest.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** | Object name of the account verification request. | 
**billing_address** | [**Address**](Address.md) |  | [optional] 
**store_id** | **str** | An optional outlet ID for clients that support multiple stores in the same app. | [optional] 
**additional_details** | [**AdditionalDetails**](AdditionalDetails.md) |  | [optional] 
**payment_card** | [**PaymentCard**](PaymentCard.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

