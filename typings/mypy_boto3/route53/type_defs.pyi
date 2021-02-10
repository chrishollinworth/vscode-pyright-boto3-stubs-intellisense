from mypy_boto3_route53.type_defs import (
    AccountLimitTypeDef,
    AlarmIdentifierTypeDef,
    AliasTargetTypeDef,
    ChangeInfoTypeDef,
    ChangeTypeDef,
    CloudWatchAlarmConfigurationTypeDef,
    DNSSECStatusTypeDef,
    DelegationSetTypeDef,
    DimensionTypeDef,
    GeoLocationDetailsTypeDef,
    GeoLocationTypeDef,
    HealthCheckConfigTypeDef,
    HealthCheckObservationTypeDef,
    HealthCheckTypeDef,
    HostedZoneConfigTypeDef,
    HostedZoneLimitTypeDef,
    HostedZoneOwnerTypeDef,
    HostedZoneSummaryTypeDef,
    HostedZoneTypeDef,
    KeySigningKeyTypeDef,
    LinkedServiceTypeDef,
    QueryLoggingConfigTypeDef,
    ResourceRecordSetTypeDef,
    ResourceRecordTypeDef,
    ResourceTagSetTypeDef,
    ReusableDelegationSetLimitTypeDef,
    StatusReportTypeDef,
    TagTypeDef,
    TrafficPolicyInstanceTypeDef,
    TrafficPolicySummaryTypeDef,
    TrafficPolicyTypeDef,
    VPCTypeDef,
    ActivateKeySigningKeyResponseTypeDef,
    AssociateVPCWithHostedZoneResponseTypeDef,
    ChangeBatchTypeDef,
    ChangeResourceRecordSetsResponseTypeDef,
    CreateHealthCheckResponseTypeDef,
    CreateHostedZoneResponseTypeDef,
    CreateKeySigningKeyResponseTypeDef,
    CreateQueryLoggingConfigResponseTypeDef,
    CreateReusableDelegationSetResponseTypeDef,
    CreateTrafficPolicyInstanceResponseTypeDef,
    CreateTrafficPolicyResponseTypeDef,
    CreateTrafficPolicyVersionResponseTypeDef,
    CreateVPCAssociationAuthorizationResponseTypeDef,
    DeactivateKeySigningKeyResponseTypeDef,
    DeleteHostedZoneResponseTypeDef,
    DeleteKeySigningKeyResponseTypeDef,
    DisableHostedZoneDNSSECResponseTypeDef,
    DisassociateVPCFromHostedZoneResponseTypeDef,
    EnableHostedZoneDNSSECResponseTypeDef,
    GetAccountLimitResponseTypeDef,
    GetChangeResponseTypeDef,
    GetCheckerIpRangesResponseTypeDef,
    GetDNSSECResponseTypeDef,
    GetGeoLocationResponseTypeDef,
    GetHealthCheckCountResponseTypeDef,
    GetHealthCheckLastFailureReasonResponseTypeDef,
    GetHealthCheckResponseTypeDef,
    GetHealthCheckStatusResponseTypeDef,
    GetHostedZoneCountResponseTypeDef,
    GetHostedZoneLimitResponseTypeDef,
    GetHostedZoneResponseTypeDef,
    GetQueryLoggingConfigResponseTypeDef,
    GetReusableDelegationSetLimitResponseTypeDef,
    GetReusableDelegationSetResponseTypeDef,
    GetTrafficPolicyInstanceCountResponseTypeDef,
    GetTrafficPolicyInstanceResponseTypeDef,
    GetTrafficPolicyResponseTypeDef,
    ListGeoLocationsResponseTypeDef,
    ListHealthChecksResponseTypeDef,
    ListHostedZonesByNameResponseTypeDef,
    ListHostedZonesByVPCResponseTypeDef,
    ListHostedZonesResponseTypeDef,
    ListQueryLoggingConfigsResponseTypeDef,
    ListResourceRecordSetsResponseTypeDef,
    ListReusableDelegationSetsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTagsForResourcesResponseTypeDef,
    ListTrafficPoliciesResponseTypeDef,
    ListTrafficPolicyInstancesByHostedZoneResponseTypeDef,
    ListTrafficPolicyInstancesByPolicyResponseTypeDef,
    ListTrafficPolicyInstancesResponseTypeDef,
    ListTrafficPolicyVersionsResponseTypeDef,
    ListVPCAssociationAuthorizationsResponseTypeDef,
    PaginatorConfigTypeDef,
    TestDNSAnswerResponseTypeDef,
    UpdateHealthCheckResponseTypeDef,
    UpdateHostedZoneCommentResponseTypeDef,
    UpdateTrafficPolicyCommentResponseTypeDef,
    UpdateTrafficPolicyInstanceResponseTypeDef,
    WaiterConfigTypeDef,
)

__all__ = (
    "AccountLimitTypeDef",
    "AlarmIdentifierTypeDef",
    "AliasTargetTypeDef",
    "ChangeInfoTypeDef",
    "ChangeTypeDef",
    "CloudWatchAlarmConfigurationTypeDef",
    "DNSSECStatusTypeDef",
    "DelegationSetTypeDef",
    "DimensionTypeDef",
    "GeoLocationDetailsTypeDef",
    "GeoLocationTypeDef",
    "HealthCheckConfigTypeDef",
    "HealthCheckObservationTypeDef",
    "HealthCheckTypeDef",
    "HostedZoneConfigTypeDef",
    "HostedZoneLimitTypeDef",
    "HostedZoneOwnerTypeDef",
    "HostedZoneSummaryTypeDef",
    "HostedZoneTypeDef",
    "KeySigningKeyTypeDef",
    "LinkedServiceTypeDef",
    "QueryLoggingConfigTypeDef",
    "ResourceRecordSetTypeDef",
    "ResourceRecordTypeDef",
    "ResourceTagSetTypeDef",
    "ReusableDelegationSetLimitTypeDef",
    "StatusReportTypeDef",
    "TagTypeDef",
    "TrafficPolicyInstanceTypeDef",
    "TrafficPolicySummaryTypeDef",
    "TrafficPolicyTypeDef",
    "VPCTypeDef",
    "ActivateKeySigningKeyResponseTypeDef",
    "AssociateVPCWithHostedZoneResponseTypeDef",
    "ChangeBatchTypeDef",
    "ChangeResourceRecordSetsResponseTypeDef",
    "CreateHealthCheckResponseTypeDef",
    "CreateHostedZoneResponseTypeDef",
    "CreateKeySigningKeyResponseTypeDef",
    "CreateQueryLoggingConfigResponseTypeDef",
    "CreateReusableDelegationSetResponseTypeDef",
    "CreateTrafficPolicyInstanceResponseTypeDef",
    "CreateTrafficPolicyResponseTypeDef",
    "CreateTrafficPolicyVersionResponseTypeDef",
    "CreateVPCAssociationAuthorizationResponseTypeDef",
    "DeactivateKeySigningKeyResponseTypeDef",
    "DeleteHostedZoneResponseTypeDef",
    "DeleteKeySigningKeyResponseTypeDef",
    "DisableHostedZoneDNSSECResponseTypeDef",
    "DisassociateVPCFromHostedZoneResponseTypeDef",
    "EnableHostedZoneDNSSECResponseTypeDef",
    "GetAccountLimitResponseTypeDef",
    "GetChangeResponseTypeDef",
    "GetCheckerIpRangesResponseTypeDef",
    "GetDNSSECResponseTypeDef",
    "GetGeoLocationResponseTypeDef",
    "GetHealthCheckCountResponseTypeDef",
    "GetHealthCheckLastFailureReasonResponseTypeDef",
    "GetHealthCheckResponseTypeDef",
    "GetHealthCheckStatusResponseTypeDef",
    "GetHostedZoneCountResponseTypeDef",
    "GetHostedZoneLimitResponseTypeDef",
    "GetHostedZoneResponseTypeDef",
    "GetQueryLoggingConfigResponseTypeDef",
    "GetReusableDelegationSetLimitResponseTypeDef",
    "GetReusableDelegationSetResponseTypeDef",
    "GetTrafficPolicyInstanceCountResponseTypeDef",
    "GetTrafficPolicyInstanceResponseTypeDef",
    "GetTrafficPolicyResponseTypeDef",
    "ListGeoLocationsResponseTypeDef",
    "ListHealthChecksResponseTypeDef",
    "ListHostedZonesByNameResponseTypeDef",
    "ListHostedZonesByVPCResponseTypeDef",
    "ListHostedZonesResponseTypeDef",
    "ListQueryLoggingConfigsResponseTypeDef",
    "ListResourceRecordSetsResponseTypeDef",
    "ListReusableDelegationSetsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTagsForResourcesResponseTypeDef",
    "ListTrafficPoliciesResponseTypeDef",
    "ListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    "ListTrafficPolicyInstancesByPolicyResponseTypeDef",
    "ListTrafficPolicyInstancesResponseTypeDef",
    "ListTrafficPolicyVersionsResponseTypeDef",
    "ListVPCAssociationAuthorizationsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "TestDNSAnswerResponseTypeDef",
    "UpdateHealthCheckResponseTypeDef",
    "UpdateHostedZoneCommentResponseTypeDef",
    "UpdateTrafficPolicyCommentResponseTypeDef",
    "UpdateTrafficPolicyInstanceResponseTypeDef",
    "WaiterConfigTypeDef",
)
