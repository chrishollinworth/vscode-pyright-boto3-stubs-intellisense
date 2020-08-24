from mypy_boto3_cognito_idp.type_defs import (
    AccountRecoverySettingTypeTypeDef,
    AccountTakeoverActionTypeTypeDef,
    AccountTakeoverActionsTypeTypeDef,
    AccountTakeoverRiskConfigurationTypeTypeDef,
    AdminCreateUserConfigTypeTypeDef,
    AnalyticsConfigurationTypeTypeDef,
    AttributeTypeTypeDef,
    AuthEventTypeTypeDef,
    AuthenticationResultTypeTypeDef,
    ChallengeResponseTypeTypeDef,
    CodeDeliveryDetailsTypeTypeDef,
    CompromisedCredentialsActionsTypeTypeDef,
    CompromisedCredentialsRiskConfigurationTypeTypeDef,
    CustomDomainConfigTypeTypeDef,
    DeviceConfigurationTypeTypeDef,
    DeviceTypeTypeDef,
    DomainDescriptionTypeTypeDef,
    EmailConfigurationTypeTypeDef,
    EventContextDataTypeTypeDef,
    EventFeedbackTypeTypeDef,
    EventRiskTypeTypeDef,
    GroupTypeTypeDef,
    HttpHeaderTypeDef,
    IdentityProviderTypeTypeDef,
    LambdaConfigTypeTypeDef,
    MFAOptionTypeTypeDef,
    MessageTemplateTypeTypeDef,
    NewDeviceMetadataTypeTypeDef,
    NotifyConfigurationTypeTypeDef,
    NotifyEmailTypeTypeDef,
    NumberAttributeConstraintsTypeTypeDef,
    PasswordPolicyTypeTypeDef,
    ProviderDescriptionTypeDef,
    RecoveryOptionTypeTypeDef,
    ResourceServerScopeTypeTypeDef,
    ResourceServerTypeTypeDef,
    RiskConfigurationTypeTypeDef,
    RiskExceptionConfigurationTypeTypeDef,
    SchemaAttributeTypeTypeDef,
    SmsConfigurationTypeTypeDef,
    SmsMfaConfigTypeTypeDef,
    SoftwareTokenMfaConfigTypeTypeDef,
    StringAttributeConstraintsTypeTypeDef,
    TokenValidityUnitsTypeTypeDef,
    UICustomizationTypeTypeDef,
    UserImportJobTypeTypeDef,
    UserPoolAddOnsTypeTypeDef,
    UserPoolClientDescriptionTypeDef,
    UserPoolClientTypeTypeDef,
    UserPoolDescriptionTypeTypeDef,
    UserPoolPolicyTypeTypeDef,
    UserPoolTypeTypeDef,
    UserTypeTypeDef,
    UsernameConfigurationTypeTypeDef,
    VerificationMessageTemplateTypeTypeDef,
    AdminCreateUserResponseTypeDef,
    AdminGetDeviceResponseTypeDef,
    AdminGetUserResponseTypeDef,
    AdminInitiateAuthResponseTypeDef,
    AdminListDevicesResponseTypeDef,
    AdminListGroupsForUserResponseTypeDef,
    AdminListUserAuthEventsResponseTypeDef,
    AdminRespondToAuthChallengeResponseTypeDef,
    AnalyticsMetadataTypeTypeDef,
    AssociateSoftwareTokenResponseTypeDef,
    ConfirmDeviceResponseTypeDef,
    ContextDataTypeTypeDef,
    CreateGroupResponseTypeDef,
    CreateIdentityProviderResponseTypeDef,
    CreateResourceServerResponseTypeDef,
    CreateUserImportJobResponseTypeDef,
    CreateUserPoolClientResponseTypeDef,
    CreateUserPoolDomainResponseTypeDef,
    CreateUserPoolResponseTypeDef,
    DescribeIdentityProviderResponseTypeDef,
    DescribeResourceServerResponseTypeDef,
    DescribeRiskConfigurationResponseTypeDef,
    DescribeUserImportJobResponseTypeDef,
    DescribeUserPoolClientResponseTypeDef,
    DescribeUserPoolDomainResponseTypeDef,
    DescribeUserPoolResponseTypeDef,
    DeviceSecretVerifierConfigTypeTypeDef,
    ForgotPasswordResponseTypeDef,
    GetCSVHeaderResponseTypeDef,
    GetDeviceResponseTypeDef,
    GetGroupResponseTypeDef,
    GetIdentityProviderByIdentifierResponseTypeDef,
    GetSigningCertificateResponseTypeDef,
    GetUICustomizationResponseTypeDef,
    GetUserAttributeVerificationCodeResponseTypeDef,
    GetUserPoolMfaConfigResponseTypeDef,
    GetUserResponseTypeDef,
    InitiateAuthResponseTypeDef,
    ListDevicesResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListIdentityProvidersResponseTypeDef,
    ListResourceServersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUserImportJobsResponseTypeDef,
    ListUserPoolClientsResponseTypeDef,
    ListUserPoolsResponseTypeDef,
    ListUsersInGroupResponseTypeDef,
    ListUsersResponseTypeDef,
    PaginatorConfigTypeDef,
    ProviderUserIdentifierTypeTypeDef,
    ResendConfirmationCodeResponseTypeDef,
    RespondToAuthChallengeResponseTypeDef,
    SMSMfaSettingsTypeTypeDef,
    SetRiskConfigurationResponseTypeDef,
    SetUICustomizationResponseTypeDef,
    SetUserPoolMfaConfigResponseTypeDef,
    SignUpResponseTypeDef,
    SoftwareTokenMfaSettingsTypeTypeDef,
    StartUserImportJobResponseTypeDef,
    StopUserImportJobResponseTypeDef,
    UpdateGroupResponseTypeDef,
    UpdateIdentityProviderResponseTypeDef,
    UpdateResourceServerResponseTypeDef,
    UpdateUserAttributesResponseTypeDef,
    UpdateUserPoolClientResponseTypeDef,
    UpdateUserPoolDomainResponseTypeDef,
    UserContextDataTypeTypeDef,
    VerifySoftwareTokenResponseTypeDef,
)

__all__ = (
    "AccountRecoverySettingTypeTypeDef",
    "AccountTakeoverActionTypeTypeDef",
    "AccountTakeoverActionsTypeTypeDef",
    "AccountTakeoverRiskConfigurationTypeTypeDef",
    "AdminCreateUserConfigTypeTypeDef",
    "AnalyticsConfigurationTypeTypeDef",
    "AttributeTypeTypeDef",
    "AuthEventTypeTypeDef",
    "AuthenticationResultTypeTypeDef",
    "ChallengeResponseTypeTypeDef",
    "CodeDeliveryDetailsTypeTypeDef",
    "CompromisedCredentialsActionsTypeTypeDef",
    "CompromisedCredentialsRiskConfigurationTypeTypeDef",
    "CustomDomainConfigTypeTypeDef",
    "DeviceConfigurationTypeTypeDef",
    "DeviceTypeTypeDef",
    "DomainDescriptionTypeTypeDef",
    "EmailConfigurationTypeTypeDef",
    "EventContextDataTypeTypeDef",
    "EventFeedbackTypeTypeDef",
    "EventRiskTypeTypeDef",
    "GroupTypeTypeDef",
    "HttpHeaderTypeDef",
    "IdentityProviderTypeTypeDef",
    "LambdaConfigTypeTypeDef",
    "MFAOptionTypeTypeDef",
    "MessageTemplateTypeTypeDef",
    "NewDeviceMetadataTypeTypeDef",
    "NotifyConfigurationTypeTypeDef",
    "NotifyEmailTypeTypeDef",
    "NumberAttributeConstraintsTypeTypeDef",
    "PasswordPolicyTypeTypeDef",
    "ProviderDescriptionTypeDef",
    "RecoveryOptionTypeTypeDef",
    "ResourceServerScopeTypeTypeDef",
    "ResourceServerTypeTypeDef",
    "RiskConfigurationTypeTypeDef",
    "RiskExceptionConfigurationTypeTypeDef",
    "SchemaAttributeTypeTypeDef",
    "SmsConfigurationTypeTypeDef",
    "SmsMfaConfigTypeTypeDef",
    "SoftwareTokenMfaConfigTypeTypeDef",
    "StringAttributeConstraintsTypeTypeDef",
    "TokenValidityUnitsTypeTypeDef",
    "UICustomizationTypeTypeDef",
    "UserImportJobTypeTypeDef",
    "UserPoolAddOnsTypeTypeDef",
    "UserPoolClientDescriptionTypeDef",
    "UserPoolClientTypeTypeDef",
    "UserPoolDescriptionTypeTypeDef",
    "UserPoolPolicyTypeTypeDef",
    "UserPoolTypeTypeDef",
    "UserTypeTypeDef",
    "UsernameConfigurationTypeTypeDef",
    "VerificationMessageTemplateTypeTypeDef",
    "AdminCreateUserResponseTypeDef",
    "AdminGetDeviceResponseTypeDef",
    "AdminGetUserResponseTypeDef",
    "AdminInitiateAuthResponseTypeDef",
    "AdminListDevicesResponseTypeDef",
    "AdminListGroupsForUserResponseTypeDef",
    "AdminListUserAuthEventsResponseTypeDef",
    "AdminRespondToAuthChallengeResponseTypeDef",
    "AnalyticsMetadataTypeTypeDef",
    "AssociateSoftwareTokenResponseTypeDef",
    "ConfirmDeviceResponseTypeDef",
    "ContextDataTypeTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateIdentityProviderResponseTypeDef",
    "CreateResourceServerResponseTypeDef",
    "CreateUserImportJobResponseTypeDef",
    "CreateUserPoolClientResponseTypeDef",
    "CreateUserPoolDomainResponseTypeDef",
    "CreateUserPoolResponseTypeDef",
    "DescribeIdentityProviderResponseTypeDef",
    "DescribeResourceServerResponseTypeDef",
    "DescribeRiskConfigurationResponseTypeDef",
    "DescribeUserImportJobResponseTypeDef",
    "DescribeUserPoolClientResponseTypeDef",
    "DescribeUserPoolDomainResponseTypeDef",
    "DescribeUserPoolResponseTypeDef",
    "DeviceSecretVerifierConfigTypeTypeDef",
    "ForgotPasswordResponseTypeDef",
    "GetCSVHeaderResponseTypeDef",
    "GetDeviceResponseTypeDef",
    "GetGroupResponseTypeDef",
    "GetIdentityProviderByIdentifierResponseTypeDef",
    "GetSigningCertificateResponseTypeDef",
    "GetUICustomizationResponseTypeDef",
    "GetUserAttributeVerificationCodeResponseTypeDef",
    "GetUserPoolMfaConfigResponseTypeDef",
    "GetUserResponseTypeDef",
    "InitiateAuthResponseTypeDef",
    "ListDevicesResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "ListIdentityProvidersResponseTypeDef",
    "ListResourceServersResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUserImportJobsResponseTypeDef",
    "ListUserPoolClientsResponseTypeDef",
    "ListUserPoolsResponseTypeDef",
    "ListUsersInGroupResponseTypeDef",
    "ListUsersResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ProviderUserIdentifierTypeTypeDef",
    "ResendConfirmationCodeResponseTypeDef",
    "RespondToAuthChallengeResponseTypeDef",
    "SMSMfaSettingsTypeTypeDef",
    "SetRiskConfigurationResponseTypeDef",
    "SetUICustomizationResponseTypeDef",
    "SetUserPoolMfaConfigResponseTypeDef",
    "SignUpResponseTypeDef",
    "SoftwareTokenMfaSettingsTypeTypeDef",
    "StartUserImportJobResponseTypeDef",
    "StopUserImportJobResponseTypeDef",
    "UpdateGroupResponseTypeDef",
    "UpdateIdentityProviderResponseTypeDef",
    "UpdateResourceServerResponseTypeDef",
    "UpdateUserAttributesResponseTypeDef",
    "UpdateUserPoolClientResponseTypeDef",
    "UpdateUserPoolDomainResponseTypeDef",
    "UserContextDataTypeTypeDef",
    "VerifySoftwareTokenResponseTypeDef",
)
