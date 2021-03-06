from mypy_boto3_ecs.type_defs import (
    AttachmentTypeDef,
    AttributeTypeDef,
    AutoScalingGroupProviderTypeDef,
    AwsVpcConfigurationTypeDef,
    CapacityProviderStrategyItemTypeDef,
    CapacityProviderTypeDef,
    ClusterSettingTypeDef,
    ClusterTypeDef,
    ContainerDefinitionTypeDef,
    ContainerDependencyTypeDef,
    ContainerInstanceTypeDef,
    ContainerOverrideTypeDef,
    ContainerTypeDef,
    DeploymentCircuitBreakerTypeDef,
    DeploymentConfigurationTypeDef,
    DeploymentControllerTypeDef,
    DeploymentTypeDef,
    DeviceTypeDef,
    DockerVolumeConfigurationTypeDef,
    EFSAuthorizationConfigTypeDef,
    EFSVolumeConfigurationTypeDef,
    EnvironmentFileTypeDef,
    FSxWindowsFileServerAuthorizationConfigTypeDef,
    FSxWindowsFileServerVolumeConfigurationTypeDef,
    FailureTypeDef,
    FirelensConfigurationTypeDef,
    HealthCheckTypeDef,
    HostEntryTypeDef,
    HostVolumePropertiesTypeDef,
    InferenceAcceleratorOverrideTypeDef,
    InferenceAcceleratorTypeDef,
    KernelCapabilitiesTypeDef,
    KeyValuePairTypeDef,
    LinuxParametersTypeDef,
    LoadBalancerTypeDef,
    LogConfigurationTypeDef,
    ManagedScalingTypeDef,
    MountPointTypeDef,
    NetworkBindingTypeDef,
    NetworkConfigurationTypeDef,
    NetworkInterfaceTypeDef,
    PlacementConstraintTypeDef,
    PlacementStrategyTypeDef,
    PortMappingTypeDef,
    ProxyConfigurationTypeDef,
    RepositoryCredentialsTypeDef,
    ResourceRequirementTypeDef,
    ResourceTypeDef,
    ScaleTypeDef,
    SecretTypeDef,
    ServiceEventTypeDef,
    ServiceRegistryTypeDef,
    ServiceTypeDef,
    SettingTypeDef,
    SystemControlTypeDef,
    TagTypeDef,
    TaskDefinitionPlacementConstraintTypeDef,
    TaskDefinitionTypeDef,
    TaskOverrideTypeDef,
    TaskSetTypeDef,
    TaskTypeDef,
    TmpfsTypeDef,
    UlimitTypeDef,
    VersionInfoTypeDef,
    VolumeFromTypeDef,
    VolumeTypeDef,
    AttachmentStateChangeTypeDef,
    AutoScalingGroupProviderUpdateTypeDef,
    ContainerStateChangeTypeDef,
    CreateCapacityProviderResponseTypeDef,
    CreateClusterResponseTypeDef,
    CreateServiceResponseTypeDef,
    CreateTaskSetResponseTypeDef,
    DeleteAccountSettingResponseTypeDef,
    DeleteAttributesResponseTypeDef,
    DeleteCapacityProviderResponseTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteServiceResponseTypeDef,
    DeleteTaskSetResponseTypeDef,
    DeregisterContainerInstanceResponseTypeDef,
    DeregisterTaskDefinitionResponseTypeDef,
    DescribeCapacityProvidersResponseTypeDef,
    DescribeClustersResponseTypeDef,
    DescribeContainerInstancesResponseTypeDef,
    DescribeServicesResponseTypeDef,
    DescribeTaskDefinitionResponseTypeDef,
    DescribeTaskSetsResponseTypeDef,
    DescribeTasksResponseTypeDef,
    DiscoverPollEndpointResponseTypeDef,
    ListAccountSettingsResponseTypeDef,
    ListAttributesResponseTypeDef,
    ListClustersResponseTypeDef,
    ListContainerInstancesResponseTypeDef,
    ListServicesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTaskDefinitionFamiliesResponseTypeDef,
    ListTaskDefinitionsResponseTypeDef,
    ListTasksResponseTypeDef,
    PaginatorConfigTypeDef,
    PlatformDeviceTypeDef,
    PutAccountSettingDefaultResponseTypeDef,
    PutAccountSettingResponseTypeDef,
    PutAttributesResponseTypeDef,
    PutClusterCapacityProvidersResponseTypeDef,
    RegisterContainerInstanceResponseTypeDef,
    RegisterTaskDefinitionResponseTypeDef,
    RunTaskResponseTypeDef,
    StartTaskResponseTypeDef,
    StopTaskResponseTypeDef,
    SubmitAttachmentStateChangesResponseTypeDef,
    SubmitContainerStateChangeResponseTypeDef,
    SubmitTaskStateChangeResponseTypeDef,
    UpdateCapacityProviderResponseTypeDef,
    UpdateClusterSettingsResponseTypeDef,
    UpdateContainerAgentResponseTypeDef,
    UpdateContainerInstancesStateResponseTypeDef,
    UpdateServicePrimaryTaskSetResponseTypeDef,
    UpdateServiceResponseTypeDef,
    UpdateTaskSetResponseTypeDef,
    WaiterConfigTypeDef,
)

__all__ = (
    "AttachmentTypeDef",
    "AttributeTypeDef",
    "AutoScalingGroupProviderTypeDef",
    "AwsVpcConfigurationTypeDef",
    "CapacityProviderStrategyItemTypeDef",
    "CapacityProviderTypeDef",
    "ClusterSettingTypeDef",
    "ClusterTypeDef",
    "ContainerDefinitionTypeDef",
    "ContainerDependencyTypeDef",
    "ContainerInstanceTypeDef",
    "ContainerOverrideTypeDef",
    "ContainerTypeDef",
    "DeploymentCircuitBreakerTypeDef",
    "DeploymentConfigurationTypeDef",
    "DeploymentControllerTypeDef",
    "DeploymentTypeDef",
    "DeviceTypeDef",
    "DockerVolumeConfigurationTypeDef",
    "EFSAuthorizationConfigTypeDef",
    "EFSVolumeConfigurationTypeDef",
    "EnvironmentFileTypeDef",
    "FSxWindowsFileServerAuthorizationConfigTypeDef",
    "FSxWindowsFileServerVolumeConfigurationTypeDef",
    "FailureTypeDef",
    "FirelensConfigurationTypeDef",
    "HealthCheckTypeDef",
    "HostEntryTypeDef",
    "HostVolumePropertiesTypeDef",
    "InferenceAcceleratorOverrideTypeDef",
    "InferenceAcceleratorTypeDef",
    "KernelCapabilitiesTypeDef",
    "KeyValuePairTypeDef",
    "LinuxParametersTypeDef",
    "LoadBalancerTypeDef",
    "LogConfigurationTypeDef",
    "ManagedScalingTypeDef",
    "MountPointTypeDef",
    "NetworkBindingTypeDef",
    "NetworkConfigurationTypeDef",
    "NetworkInterfaceTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "PortMappingTypeDef",
    "ProxyConfigurationTypeDef",
    "RepositoryCredentialsTypeDef",
    "ResourceRequirementTypeDef",
    "ResourceTypeDef",
    "ScaleTypeDef",
    "SecretTypeDef",
    "ServiceEventTypeDef",
    "ServiceRegistryTypeDef",
    "ServiceTypeDef",
    "SettingTypeDef",
    "SystemControlTypeDef",
    "TagTypeDef",
    "TaskDefinitionPlacementConstraintTypeDef",
    "TaskDefinitionTypeDef",
    "TaskOverrideTypeDef",
    "TaskSetTypeDef",
    "TaskTypeDef",
    "TmpfsTypeDef",
    "UlimitTypeDef",
    "VersionInfoTypeDef",
    "VolumeFromTypeDef",
    "VolumeTypeDef",
    "AttachmentStateChangeTypeDef",
    "AutoScalingGroupProviderUpdateTypeDef",
    "ContainerStateChangeTypeDef",
    "CreateCapacityProviderResponseTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateServiceResponseTypeDef",
    "CreateTaskSetResponseTypeDef",
    "DeleteAccountSettingResponseTypeDef",
    "DeleteAttributesResponseTypeDef",
    "DeleteCapacityProviderResponseTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteServiceResponseTypeDef",
    "DeleteTaskSetResponseTypeDef",
    "DeregisterContainerInstanceResponseTypeDef",
    "DeregisterTaskDefinitionResponseTypeDef",
    "DescribeCapacityProvidersResponseTypeDef",
    "DescribeClustersResponseTypeDef",
    "DescribeContainerInstancesResponseTypeDef",
    "DescribeServicesResponseTypeDef",
    "DescribeTaskDefinitionResponseTypeDef",
    "DescribeTaskSetsResponseTypeDef",
    "DescribeTasksResponseTypeDef",
    "DiscoverPollEndpointResponseTypeDef",
    "ListAccountSettingsResponseTypeDef",
    "ListAttributesResponseTypeDef",
    "ListClustersResponseTypeDef",
    "ListContainerInstancesResponseTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTaskDefinitionFamiliesResponseTypeDef",
    "ListTaskDefinitionsResponseTypeDef",
    "ListTasksResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PlatformDeviceTypeDef",
    "PutAccountSettingDefaultResponseTypeDef",
    "PutAccountSettingResponseTypeDef",
    "PutAttributesResponseTypeDef",
    "PutClusterCapacityProvidersResponseTypeDef",
    "RegisterContainerInstanceResponseTypeDef",
    "RegisterTaskDefinitionResponseTypeDef",
    "RunTaskResponseTypeDef",
    "StartTaskResponseTypeDef",
    "StopTaskResponseTypeDef",
    "SubmitAttachmentStateChangesResponseTypeDef",
    "SubmitContainerStateChangeResponseTypeDef",
    "SubmitTaskStateChangeResponseTypeDef",
    "UpdateCapacityProviderResponseTypeDef",
    "UpdateClusterSettingsResponseTypeDef",
    "UpdateContainerAgentResponseTypeDef",
    "UpdateContainerInstancesStateResponseTypeDef",
    "UpdateServicePrimaryTaskSetResponseTypeDef",
    "UpdateServiceResponseTypeDef",
    "UpdateTaskSetResponseTypeDef",
    "WaiterConfigTypeDef",
)
