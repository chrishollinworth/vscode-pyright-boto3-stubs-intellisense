from mypy_boto3_gamelift.type_defs import (
    AliasTypeDef,
    AttributeValueTypeDef,
    AwsCredentialsTypeDef,
    BuildTypeDef,
    CertificateConfigurationTypeDef,
    EC2InstanceCountsTypeDef,
    EC2InstanceLimitTypeDef,
    EventTypeDef,
    FleetAttributesTypeDef,
    FleetCapacityTypeDef,
    FleetUtilizationTypeDef,
    GamePropertyTypeDef,
    GameServerGroupTypeDef,
    GameServerTypeDef,
    GameSessionConnectionInfoTypeDef,
    GameSessionDetailTypeDef,
    GameSessionPlacementTypeDef,
    GameSessionQueueDestinationTypeDef,
    GameSessionQueueTypeDef,
    GameSessionTypeDef,
    InstanceAccessTypeDef,
    InstanceCredentialsTypeDef,
    InstanceDefinitionTypeDef,
    InstanceTypeDef,
    IpPermissionTypeDef,
    MatchedPlayerSessionTypeDef,
    MatchmakingConfigurationTypeDef,
    MatchmakingRuleSetTypeDef,
    MatchmakingTicketTypeDef,
    PlacedPlayerSessionTypeDef,
    PlayerLatencyPolicyTypeDef,
    PlayerLatencyTypeDef,
    PlayerSessionTypeDef,
    PlayerTypeDef,
    ResourceCreationLimitPolicyTypeDef,
    RoutingStrategyTypeDef,
    RuntimeConfigurationTypeDef,
    S3LocationTypeDef,
    ScalingPolicyTypeDef,
    ScriptTypeDef,
    ServerProcessTypeDef,
    TagTypeDef,
    TargetConfigurationTypeDef,
    TargetTrackingConfigurationTypeDef,
    VpcPeeringAuthorizationTypeDef,
    VpcPeeringConnectionStatusTypeDef,
    VpcPeeringConnectionTypeDef,
    ClaimGameServerOutputTypeDef,
    CreateAliasOutputTypeDef,
    CreateBuildOutputTypeDef,
    CreateFleetOutputTypeDef,
    CreateGameServerGroupOutputTypeDef,
    CreateGameSessionOutputTypeDef,
    CreateGameSessionQueueOutputTypeDef,
    CreateMatchmakingConfigurationOutputTypeDef,
    CreateMatchmakingRuleSetOutputTypeDef,
    CreatePlayerSessionOutputTypeDef,
    CreatePlayerSessionsOutputTypeDef,
    CreateScriptOutputTypeDef,
    CreateVpcPeeringAuthorizationOutputTypeDef,
    DeleteGameServerGroupOutputTypeDef,
    DescribeAliasOutputTypeDef,
    DescribeBuildOutputTypeDef,
    DescribeEC2InstanceLimitsOutputTypeDef,
    DescribeFleetAttributesOutputTypeDef,
    DescribeFleetCapacityOutputTypeDef,
    DescribeFleetEventsOutputTypeDef,
    DescribeFleetPortSettingsOutputTypeDef,
    DescribeFleetUtilizationOutputTypeDef,
    DescribeGameServerGroupOutputTypeDef,
    DescribeGameServerOutputTypeDef,
    DescribeGameSessionDetailsOutputTypeDef,
    DescribeGameSessionPlacementOutputTypeDef,
    DescribeGameSessionQueuesOutputTypeDef,
    DescribeGameSessionsOutputTypeDef,
    DescribeInstancesOutputTypeDef,
    DescribeMatchmakingConfigurationsOutputTypeDef,
    DescribeMatchmakingOutputTypeDef,
    DescribeMatchmakingRuleSetsOutputTypeDef,
    DescribePlayerSessionsOutputTypeDef,
    DescribeRuntimeConfigurationOutputTypeDef,
    DescribeScalingPoliciesOutputTypeDef,
    DescribeScriptOutputTypeDef,
    DescribeVpcPeeringAuthorizationsOutputTypeDef,
    DescribeVpcPeeringConnectionsOutputTypeDef,
    DesiredPlayerSessionTypeDef,
    GameServerGroupAutoScalingPolicyTypeDef,
    GetGameSessionLogUrlOutputTypeDef,
    GetInstanceAccessOutputTypeDef,
    LaunchTemplateSpecificationTypeDef,
    ListAliasesOutputTypeDef,
    ListBuildsOutputTypeDef,
    ListFleetsOutputTypeDef,
    ListGameServerGroupsOutputTypeDef,
    ListGameServersOutputTypeDef,
    ListScriptsOutputTypeDef,
    ListTagsForResourceResponseTypeDef,
    PaginatorConfigTypeDef,
    PutScalingPolicyOutputTypeDef,
    RegisterGameServerOutputTypeDef,
    RequestUploadCredentialsOutputTypeDef,
    ResolveAliasOutputTypeDef,
    ResumeGameServerGroupOutputTypeDef,
    SearchGameSessionsOutputTypeDef,
    StartGameSessionPlacementOutputTypeDef,
    StartMatchBackfillOutputTypeDef,
    StartMatchmakingOutputTypeDef,
    StopGameSessionPlacementOutputTypeDef,
    SuspendGameServerGroupOutputTypeDef,
    UpdateAliasOutputTypeDef,
    UpdateBuildOutputTypeDef,
    UpdateFleetAttributesOutputTypeDef,
    UpdateFleetCapacityOutputTypeDef,
    UpdateFleetPortSettingsOutputTypeDef,
    UpdateGameServerGroupOutputTypeDef,
    UpdateGameServerOutputTypeDef,
    UpdateGameSessionOutputTypeDef,
    UpdateGameSessionQueueOutputTypeDef,
    UpdateMatchmakingConfigurationOutputTypeDef,
    UpdateRuntimeConfigurationOutputTypeDef,
    UpdateScriptOutputTypeDef,
    ValidateMatchmakingRuleSetOutputTypeDef,
)

__all__ = (
    "AliasTypeDef",
    "AttributeValueTypeDef",
    "AwsCredentialsTypeDef",
    "BuildTypeDef",
    "CertificateConfigurationTypeDef",
    "EC2InstanceCountsTypeDef",
    "EC2InstanceLimitTypeDef",
    "EventTypeDef",
    "FleetAttributesTypeDef",
    "FleetCapacityTypeDef",
    "FleetUtilizationTypeDef",
    "GamePropertyTypeDef",
    "GameServerGroupTypeDef",
    "GameServerTypeDef",
    "GameSessionConnectionInfoTypeDef",
    "GameSessionDetailTypeDef",
    "GameSessionPlacementTypeDef",
    "GameSessionQueueDestinationTypeDef",
    "GameSessionQueueTypeDef",
    "GameSessionTypeDef",
    "InstanceAccessTypeDef",
    "InstanceCredentialsTypeDef",
    "InstanceDefinitionTypeDef",
    "InstanceTypeDef",
    "IpPermissionTypeDef",
    "MatchedPlayerSessionTypeDef",
    "MatchmakingConfigurationTypeDef",
    "MatchmakingRuleSetTypeDef",
    "MatchmakingTicketTypeDef",
    "PlacedPlayerSessionTypeDef",
    "PlayerLatencyPolicyTypeDef",
    "PlayerLatencyTypeDef",
    "PlayerSessionTypeDef",
    "PlayerTypeDef",
    "ResourceCreationLimitPolicyTypeDef",
    "RoutingStrategyTypeDef",
    "RuntimeConfigurationTypeDef",
    "S3LocationTypeDef",
    "ScalingPolicyTypeDef",
    "ScriptTypeDef",
    "ServerProcessTypeDef",
    "TagTypeDef",
    "TargetConfigurationTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "VpcPeeringAuthorizationTypeDef",
    "VpcPeeringConnectionStatusTypeDef",
    "VpcPeeringConnectionTypeDef",
    "ClaimGameServerOutputTypeDef",
    "CreateAliasOutputTypeDef",
    "CreateBuildOutputTypeDef",
    "CreateFleetOutputTypeDef",
    "CreateGameServerGroupOutputTypeDef",
    "CreateGameSessionOutputTypeDef",
    "CreateGameSessionQueueOutputTypeDef",
    "CreateMatchmakingConfigurationOutputTypeDef",
    "CreateMatchmakingRuleSetOutputTypeDef",
    "CreatePlayerSessionOutputTypeDef",
    "CreatePlayerSessionsOutputTypeDef",
    "CreateScriptOutputTypeDef",
    "CreateVpcPeeringAuthorizationOutputTypeDef",
    "DeleteGameServerGroupOutputTypeDef",
    "DescribeAliasOutputTypeDef",
    "DescribeBuildOutputTypeDef",
    "DescribeEC2InstanceLimitsOutputTypeDef",
    "DescribeFleetAttributesOutputTypeDef",
    "DescribeFleetCapacityOutputTypeDef",
    "DescribeFleetEventsOutputTypeDef",
    "DescribeFleetPortSettingsOutputTypeDef",
    "DescribeFleetUtilizationOutputTypeDef",
    "DescribeGameServerGroupOutputTypeDef",
    "DescribeGameServerOutputTypeDef",
    "DescribeGameSessionDetailsOutputTypeDef",
    "DescribeGameSessionPlacementOutputTypeDef",
    "DescribeGameSessionQueuesOutputTypeDef",
    "DescribeGameSessionsOutputTypeDef",
    "DescribeInstancesOutputTypeDef",
    "DescribeMatchmakingConfigurationsOutputTypeDef",
    "DescribeMatchmakingOutputTypeDef",
    "DescribeMatchmakingRuleSetsOutputTypeDef",
    "DescribePlayerSessionsOutputTypeDef",
    "DescribeRuntimeConfigurationOutputTypeDef",
    "DescribeScalingPoliciesOutputTypeDef",
    "DescribeScriptOutputTypeDef",
    "DescribeVpcPeeringAuthorizationsOutputTypeDef",
    "DescribeVpcPeeringConnectionsOutputTypeDef",
    "DesiredPlayerSessionTypeDef",
    "GameServerGroupAutoScalingPolicyTypeDef",
    "GetGameSessionLogUrlOutputTypeDef",
    "GetInstanceAccessOutputTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "ListAliasesOutputTypeDef",
    "ListBuildsOutputTypeDef",
    "ListFleetsOutputTypeDef",
    "ListGameServerGroupsOutputTypeDef",
    "ListGameServersOutputTypeDef",
    "ListScriptsOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutScalingPolicyOutputTypeDef",
    "RegisterGameServerOutputTypeDef",
    "RequestUploadCredentialsOutputTypeDef",
    "ResolveAliasOutputTypeDef",
    "ResumeGameServerGroupOutputTypeDef",
    "SearchGameSessionsOutputTypeDef",
    "StartGameSessionPlacementOutputTypeDef",
    "StartMatchBackfillOutputTypeDef",
    "StartMatchmakingOutputTypeDef",
    "StopGameSessionPlacementOutputTypeDef",
    "SuspendGameServerGroupOutputTypeDef",
    "UpdateAliasOutputTypeDef",
    "UpdateBuildOutputTypeDef",
    "UpdateFleetAttributesOutputTypeDef",
    "UpdateFleetCapacityOutputTypeDef",
    "UpdateFleetPortSettingsOutputTypeDef",
    "UpdateGameServerGroupOutputTypeDef",
    "UpdateGameServerOutputTypeDef",
    "UpdateGameSessionOutputTypeDef",
    "UpdateGameSessionQueueOutputTypeDef",
    "UpdateMatchmakingConfigurationOutputTypeDef",
    "UpdateRuntimeConfigurationOutputTypeDef",
    "UpdateScriptOutputTypeDef",
    "ValidateMatchmakingRuleSetOutputTypeDef",
)
