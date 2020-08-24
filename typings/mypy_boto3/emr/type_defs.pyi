from mypy_boto3_emr.type_defs import (
    ApplicationTypeDef,
    AutoScalingPolicyDescriptionTypeDef,
    AutoScalingPolicyStateChangeReasonTypeDef,
    AutoScalingPolicyStatusTypeDef,
    AutoScalingPolicyTypeDef,
    BlockPublicAccessConfigurationMetadataTypeDef,
    BlockPublicAccessConfigurationTypeDef,
    BootstrapActionConfigTypeDef,
    BootstrapActionDetailTypeDef,
    CancelStepsInfoTypeDef,
    CloudWatchAlarmDefinitionTypeDef,
    ClusterStateChangeReasonTypeDef,
    ClusterStatusTypeDef,
    ClusterSummaryTypeDef,
    ClusterTimelineTypeDef,
    ClusterTypeDef,
    CommandTypeDef,
    ComputeLimitsTypeDef,
    EbsBlockDeviceConfigTypeDef,
    EbsBlockDeviceTypeDef,
    EbsConfigurationTypeDef,
    EbsVolumeTypeDef,
    Ec2InstanceAttributesTypeDef,
    FailureDetailsTypeDef,
    HadoopJarStepConfigTypeDef,
    HadoopStepConfigTypeDef,
    InstanceFleetConfigTypeDef,
    InstanceFleetProvisioningSpecificationsTypeDef,
    InstanceFleetStateChangeReasonTypeDef,
    InstanceFleetStatusTypeDef,
    InstanceFleetTimelineTypeDef,
    InstanceFleetTypeDef,
    InstanceGroupConfigTypeDef,
    InstanceGroupDetailTypeDef,
    InstanceGroupStateChangeReasonTypeDef,
    InstanceGroupStatusTypeDef,
    InstanceGroupTimelineTypeDef,
    InstanceGroupTypeDef,
    InstanceResizePolicyTypeDef,
    InstanceStateChangeReasonTypeDef,
    InstanceStatusTypeDef,
    InstanceTimelineTypeDef,
    InstanceTypeConfigTypeDef,
    InstanceTypeDef,
    InstanceTypeSpecificationTypeDef,
    JobFlowDetailTypeDef,
    JobFlowExecutionStatusDetailTypeDef,
    JobFlowInstancesDetailTypeDef,
    KerberosAttributesTypeDef,
    KeyValueTypeDef,
    ManagedScalingPolicyTypeDef,
    MetricDimensionTypeDef,
    OnDemandProvisioningSpecificationTypeDef,
    PlacementTypeTypeDef,
    PortRangeTypeDef,
    ScalingActionTypeDef,
    ScalingConstraintsTypeDef,
    ScalingRuleTypeDef,
    ScalingTriggerTypeDef,
    ScriptBootstrapActionConfigTypeDef,
    SecurityConfigurationSummaryTypeDef,
    ShrinkPolicyTypeDef,
    SimpleScalingPolicyConfigurationTypeDef,
    SpotProvisioningSpecificationTypeDef,
    StepConfigTypeDef,
    StepDetailTypeDef,
    StepExecutionStatusDetailTypeDef,
    StepStateChangeReasonTypeDef,
    StepStatusTypeDef,
    StepSummaryTypeDef,
    StepTimelineTypeDef,
    StepTypeDef,
    TagTypeDef,
    VolumeSpecificationTypeDef,
    AddInstanceFleetOutputTypeDef,
    AddInstanceGroupsOutputTypeDef,
    AddJobFlowStepsOutputTypeDef,
    CancelStepsOutputTypeDef,
    CreateSecurityConfigurationOutputTypeDef,
    DescribeClusterOutputTypeDef,
    DescribeJobFlowsOutputTypeDef,
    DescribeSecurityConfigurationOutputTypeDef,
    DescribeStepOutputTypeDef,
    ConfigurationTypeDef,
    GetBlockPublicAccessConfigurationOutputTypeDef,
    GetManagedScalingPolicyOutputTypeDef,
    InstanceFleetModifyConfigTypeDef,
    InstanceGroupModifyConfigTypeDef,
    JobFlowInstancesConfigTypeDef,
    ListBootstrapActionsOutputTypeDef,
    ListClustersOutputTypeDef,
    ListInstanceFleetsOutputTypeDef,
    ListInstanceGroupsOutputTypeDef,
    ListInstancesOutputTypeDef,
    ListSecurityConfigurationsOutputTypeDef,
    ListStepsOutputTypeDef,
    ModifyClusterOutputTypeDef,
    PaginatorConfigTypeDef,
    PutAutoScalingPolicyOutputTypeDef,
    RunJobFlowOutputTypeDef,
    SupportedProductConfigTypeDef,
    WaiterConfigTypeDef,
)

__all__ = (
    "ApplicationTypeDef",
    "AutoScalingPolicyDescriptionTypeDef",
    "AutoScalingPolicyStateChangeReasonTypeDef",
    "AutoScalingPolicyStatusTypeDef",
    "AutoScalingPolicyTypeDef",
    "BlockPublicAccessConfigurationMetadataTypeDef",
    "BlockPublicAccessConfigurationTypeDef",
    "BootstrapActionConfigTypeDef",
    "BootstrapActionDetailTypeDef",
    "CancelStepsInfoTypeDef",
    "CloudWatchAlarmDefinitionTypeDef",
    "ClusterStateChangeReasonTypeDef",
    "ClusterStatusTypeDef",
    "ClusterSummaryTypeDef",
    "ClusterTimelineTypeDef",
    "ClusterTypeDef",
    "CommandTypeDef",
    "ComputeLimitsTypeDef",
    "EbsBlockDeviceConfigTypeDef",
    "EbsBlockDeviceTypeDef",
    "EbsConfigurationTypeDef",
    "EbsVolumeTypeDef",
    "Ec2InstanceAttributesTypeDef",
    "FailureDetailsTypeDef",
    "HadoopJarStepConfigTypeDef",
    "HadoopStepConfigTypeDef",
    "InstanceFleetConfigTypeDef",
    "InstanceFleetProvisioningSpecificationsTypeDef",
    "InstanceFleetStateChangeReasonTypeDef",
    "InstanceFleetStatusTypeDef",
    "InstanceFleetTimelineTypeDef",
    "InstanceFleetTypeDef",
    "InstanceGroupConfigTypeDef",
    "InstanceGroupDetailTypeDef",
    "InstanceGroupStateChangeReasonTypeDef",
    "InstanceGroupStatusTypeDef",
    "InstanceGroupTimelineTypeDef",
    "InstanceGroupTypeDef",
    "InstanceResizePolicyTypeDef",
    "InstanceStateChangeReasonTypeDef",
    "InstanceStatusTypeDef",
    "InstanceTimelineTypeDef",
    "InstanceTypeConfigTypeDef",
    "InstanceTypeDef",
    "InstanceTypeSpecificationTypeDef",
    "JobFlowDetailTypeDef",
    "JobFlowExecutionStatusDetailTypeDef",
    "JobFlowInstancesDetailTypeDef",
    "KerberosAttributesTypeDef",
    "KeyValueTypeDef",
    "ManagedScalingPolicyTypeDef",
    "MetricDimensionTypeDef",
    "OnDemandProvisioningSpecificationTypeDef",
    "PlacementTypeTypeDef",
    "PortRangeTypeDef",
    "ScalingActionTypeDef",
    "ScalingConstraintsTypeDef",
    "ScalingRuleTypeDef",
    "ScalingTriggerTypeDef",
    "ScriptBootstrapActionConfigTypeDef",
    "SecurityConfigurationSummaryTypeDef",
    "ShrinkPolicyTypeDef",
    "SimpleScalingPolicyConfigurationTypeDef",
    "SpotProvisioningSpecificationTypeDef",
    "StepConfigTypeDef",
    "StepDetailTypeDef",
    "StepExecutionStatusDetailTypeDef",
    "StepStateChangeReasonTypeDef",
    "StepStatusTypeDef",
    "StepSummaryTypeDef",
    "StepTimelineTypeDef",
    "StepTypeDef",
    "TagTypeDef",
    "VolumeSpecificationTypeDef",
    "AddInstanceFleetOutputTypeDef",
    "AddInstanceGroupsOutputTypeDef",
    "AddJobFlowStepsOutputTypeDef",
    "CancelStepsOutputTypeDef",
    "CreateSecurityConfigurationOutputTypeDef",
    "DescribeClusterOutputTypeDef",
    "DescribeJobFlowsOutputTypeDef",
    "DescribeSecurityConfigurationOutputTypeDef",
    "DescribeStepOutputTypeDef",
    "ConfigurationTypeDef",
    "GetBlockPublicAccessConfigurationOutputTypeDef",
    "GetManagedScalingPolicyOutputTypeDef",
    "InstanceFleetModifyConfigTypeDef",
    "InstanceGroupModifyConfigTypeDef",
    "JobFlowInstancesConfigTypeDef",
    "ListBootstrapActionsOutputTypeDef",
    "ListClustersOutputTypeDef",
    "ListInstanceFleetsOutputTypeDef",
    "ListInstanceGroupsOutputTypeDef",
    "ListInstancesOutputTypeDef",
    "ListSecurityConfigurationsOutputTypeDef",
    "ListStepsOutputTypeDef",
    "ModifyClusterOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PutAutoScalingPolicyOutputTypeDef",
    "RunJobFlowOutputTypeDef",
    "SupportedProductConfigTypeDef",
    "WaiterConfigTypeDef",
)
