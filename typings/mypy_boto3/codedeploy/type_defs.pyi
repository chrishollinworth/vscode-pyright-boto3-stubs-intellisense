from mypy_boto3_codedeploy.type_defs import (
    AlarmConfigurationTypeDef,
    AlarmTypeDef,
    AppSpecContentTypeDef,
    ApplicationInfoTypeDef,
    AutoRollbackConfigurationTypeDef,
    AutoScalingGroupTypeDef,
    BlueGreenDeploymentConfigurationTypeDef,
    BlueInstanceTerminationOptionTypeDef,
    CloudFormationTargetTypeDef,
    DeploymentConfigInfoTypeDef,
    DeploymentGroupInfoTypeDef,
    DeploymentInfoTypeDef,
    DeploymentOverviewTypeDef,
    DeploymentReadyOptionTypeDef,
    DeploymentStyleTypeDef,
    DeploymentTargetTypeDef,
    DiagnosticsTypeDef,
    EC2TagFilterTypeDef,
    EC2TagSetTypeDef,
    ECSServiceTypeDef,
    ECSTargetTypeDef,
    ECSTaskSetTypeDef,
    ELBInfoTypeDef,
    ErrorInformationTypeDef,
    GenericRevisionInfoTypeDef,
    GitHubLocationTypeDef,
    GreenFleetProvisioningOptionTypeDef,
    InstanceInfoTypeDef,
    InstanceSummaryTypeDef,
    InstanceTargetTypeDef,
    LambdaFunctionInfoTypeDef,
    LambdaTargetTypeDef,
    LastDeploymentInfoTypeDef,
    LifecycleEventTypeDef,
    LoadBalancerInfoTypeDef,
    MinimumHealthyHostsTypeDef,
    OnPremisesTagSetTypeDef,
    RawStringTypeDef,
    RevisionInfoTypeDef,
    RevisionLocationTypeDef,
    RollbackInfoTypeDef,
    S3LocationTypeDef,
    TagFilterTypeDef,
    TagTypeDef,
    TargetGroupInfoTypeDef,
    TargetGroupPairInfoTypeDef,
    TargetInstancesTypeDef,
    TimeBasedCanaryTypeDef,
    TimeBasedLinearTypeDef,
    TrafficRouteTypeDef,
    TrafficRoutingConfigTypeDef,
    TriggerConfigTypeDef,
    BatchGetApplicationRevisionsOutputTypeDef,
    BatchGetApplicationsOutputTypeDef,
    BatchGetDeploymentGroupsOutputTypeDef,
    BatchGetDeploymentInstancesOutputTypeDef,
    BatchGetDeploymentTargetsOutputTypeDef,
    BatchGetDeploymentsOutputTypeDef,
    BatchGetOnPremisesInstancesOutputTypeDef,
    CreateApplicationOutputTypeDef,
    CreateDeploymentConfigOutputTypeDef,
    CreateDeploymentGroupOutputTypeDef,
    CreateDeploymentOutputTypeDef,
    DeleteDeploymentGroupOutputTypeDef,
    DeleteGitHubAccountTokenOutputTypeDef,
    GetApplicationOutputTypeDef,
    GetApplicationRevisionOutputTypeDef,
    GetDeploymentConfigOutputTypeDef,
    GetDeploymentGroupOutputTypeDef,
    GetDeploymentInstanceOutputTypeDef,
    GetDeploymentOutputTypeDef,
    GetDeploymentTargetOutputTypeDef,
    GetOnPremisesInstanceOutputTypeDef,
    ListApplicationRevisionsOutputTypeDef,
    ListApplicationsOutputTypeDef,
    ListDeploymentConfigsOutputTypeDef,
    ListDeploymentGroupsOutputTypeDef,
    ListDeploymentInstancesOutputTypeDef,
    ListDeploymentTargetsOutputTypeDef,
    ListDeploymentsOutputTypeDef,
    ListGitHubAccountTokenNamesOutputTypeDef,
    ListOnPremisesInstancesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    PaginatorConfigTypeDef,
    PutLifecycleEventHookExecutionStatusOutputTypeDef,
    StopDeploymentOutputTypeDef,
    TimeRangeTypeDef,
    UpdateDeploymentGroupOutputTypeDef,
    WaiterConfigTypeDef,
)

__all__ = (
    "AlarmConfigurationTypeDef",
    "AlarmTypeDef",
    "AppSpecContentTypeDef",
    "ApplicationInfoTypeDef",
    "AutoRollbackConfigurationTypeDef",
    "AutoScalingGroupTypeDef",
    "BlueGreenDeploymentConfigurationTypeDef",
    "BlueInstanceTerminationOptionTypeDef",
    "CloudFormationTargetTypeDef",
    "DeploymentConfigInfoTypeDef",
    "DeploymentGroupInfoTypeDef",
    "DeploymentInfoTypeDef",
    "DeploymentOverviewTypeDef",
    "DeploymentReadyOptionTypeDef",
    "DeploymentStyleTypeDef",
    "DeploymentTargetTypeDef",
    "DiagnosticsTypeDef",
    "EC2TagFilterTypeDef",
    "EC2TagSetTypeDef",
    "ECSServiceTypeDef",
    "ECSTargetTypeDef",
    "ECSTaskSetTypeDef",
    "ELBInfoTypeDef",
    "ErrorInformationTypeDef",
    "GenericRevisionInfoTypeDef",
    "GitHubLocationTypeDef",
    "GreenFleetProvisioningOptionTypeDef",
    "InstanceInfoTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTargetTypeDef",
    "LambdaFunctionInfoTypeDef",
    "LambdaTargetTypeDef",
    "LastDeploymentInfoTypeDef",
    "LifecycleEventTypeDef",
    "LoadBalancerInfoTypeDef",
    "MinimumHealthyHostsTypeDef",
    "OnPremisesTagSetTypeDef",
    "RawStringTypeDef",
    "RevisionInfoTypeDef",
    "RevisionLocationTypeDef",
    "RollbackInfoTypeDef",
    "S3LocationTypeDef",
    "TagFilterTypeDef",
    "TagTypeDef",
    "TargetGroupInfoTypeDef",
    "TargetGroupPairInfoTypeDef",
    "TargetInstancesTypeDef",
    "TimeBasedCanaryTypeDef",
    "TimeBasedLinearTypeDef",
    "TrafficRouteTypeDef",
    "TrafficRoutingConfigTypeDef",
    "TriggerConfigTypeDef",
    "BatchGetApplicationRevisionsOutputTypeDef",
    "BatchGetApplicationsOutputTypeDef",
    "BatchGetDeploymentGroupsOutputTypeDef",
    "BatchGetDeploymentInstancesOutputTypeDef",
    "BatchGetDeploymentTargetsOutputTypeDef",
    "BatchGetDeploymentsOutputTypeDef",
    "BatchGetOnPremisesInstancesOutputTypeDef",
    "CreateApplicationOutputTypeDef",
    "CreateDeploymentConfigOutputTypeDef",
    "CreateDeploymentGroupOutputTypeDef",
    "CreateDeploymentOutputTypeDef",
    "DeleteDeploymentGroupOutputTypeDef",
    "DeleteGitHubAccountTokenOutputTypeDef",
    "GetApplicationOutputTypeDef",
    "GetApplicationRevisionOutputTypeDef",
    "GetDeploymentConfigOutputTypeDef",
    "GetDeploymentGroupOutputTypeDef",
    "GetDeploymentInstanceOutputTypeDef",
    "GetDeploymentOutputTypeDef",
    "GetDeploymentTargetOutputTypeDef",
    "GetOnPremisesInstanceOutputTypeDef",
    "ListApplicationRevisionsOutputTypeDef",
    "ListApplicationsOutputTypeDef",
    "ListDeploymentConfigsOutputTypeDef",
    "ListDeploymentGroupsOutputTypeDef",
    "ListDeploymentInstancesOutputTypeDef",
    "ListDeploymentTargetsOutputTypeDef",
    "ListDeploymentsOutputTypeDef",
    "ListGitHubAccountTokenNamesOutputTypeDef",
    "ListOnPremisesInstancesOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PutLifecycleEventHookExecutionStatusOutputTypeDef",
    "StopDeploymentOutputTypeDef",
    "TimeRangeTypeDef",
    "UpdateDeploymentGroupOutputTypeDef",
    "WaiterConfigTypeDef",
)
