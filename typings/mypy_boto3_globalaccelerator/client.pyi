"""
Main interface for globalaccelerator service client

Usage::

    ```python
    import boto3
    from mypy_boto3_globalaccelerator import GlobalAcceleratorClient

    client: GlobalAcceleratorClient = boto3.client("globalaccelerator")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_globalaccelerator.paginator import (
    ListAcceleratorsPaginator,
    ListByoipCidrsPaginator,
    ListCustomRoutingAcceleratorsPaginator,
    ListCustomRoutingListenersPaginator,
    ListCustomRoutingPortMappingsByDestinationPaginator,
    ListCustomRoutingPortMappingsPaginator,
    ListEndpointGroupsPaginator,
    ListListenersPaginator,
)
from mypy_boto3_globalaccelerator.type_defs import (
    AddCustomRoutingEndpointsResponseTypeDef,
    AdvertiseByoipCidrResponseTypeDef,
    CidrAuthorizationContextTypeDef,
    CreateAcceleratorResponseTypeDef,
    CreateCustomRoutingAcceleratorResponseTypeDef,
    CreateCustomRoutingEndpointGroupResponseTypeDef,
    CreateCustomRoutingListenerResponseTypeDef,
    CreateEndpointGroupResponseTypeDef,
    CreateListenerResponseTypeDef,
    CustomRoutingDestinationConfigurationTypeDef,
    CustomRoutingEndpointConfigurationTypeDef,
    DeprovisionByoipCidrResponseTypeDef,
    DescribeAcceleratorAttributesResponseTypeDef,
    DescribeAcceleratorResponseTypeDef,
    DescribeCustomRoutingAcceleratorAttributesResponseTypeDef,
    DescribeCustomRoutingAcceleratorResponseTypeDef,
    DescribeCustomRoutingEndpointGroupResponseTypeDef,
    DescribeCustomRoutingListenerResponseTypeDef,
    DescribeEndpointGroupResponseTypeDef,
    DescribeListenerResponseTypeDef,
    EndpointConfigurationTypeDef,
    ListAcceleratorsResponseTypeDef,
    ListByoipCidrsResponseTypeDef,
    ListCustomRoutingAcceleratorsResponseTypeDef,
    ListCustomRoutingEndpointGroupsResponseTypeDef,
    ListCustomRoutingListenersResponseTypeDef,
    ListCustomRoutingPortMappingsByDestinationResponseTypeDef,
    ListCustomRoutingPortMappingsResponseTypeDef,
    ListEndpointGroupsResponseTypeDef,
    ListListenersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PortOverrideTypeDef,
    PortRangeTypeDef,
    ProvisionByoipCidrResponseTypeDef,
    TagTypeDef,
    UpdateAcceleratorAttributesResponseTypeDef,
    UpdateAcceleratorResponseTypeDef,
    UpdateCustomRoutingAcceleratorAttributesResponseTypeDef,
    UpdateCustomRoutingAcceleratorResponseTypeDef,
    UpdateCustomRoutingListenerResponseTypeDef,
    UpdateEndpointGroupResponseTypeDef,
    UpdateListenerResponseTypeDef,
    WithdrawByoipCidrResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GlobalAcceleratorClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AcceleratorNotDisabledException: Type[BotocoreClientError]
    AcceleratorNotFoundException: Type[BotocoreClientError]
    AccessDeniedException: Type[BotocoreClientError]
    AssociatedEndpointGroupFoundException: Type[BotocoreClientError]
    AssociatedListenerFoundException: Type[BotocoreClientError]
    ByoipCidrNotFoundException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    EndpointAlreadyExistsException: Type[BotocoreClientError]
    EndpointGroupAlreadyExistsException: Type[BotocoreClientError]
    EndpointGroupNotFoundException: Type[BotocoreClientError]
    EndpointNotFoundException: Type[BotocoreClientError]
    IncorrectCidrStateException: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidPortRangeException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ListenerNotFoundException: Type[BotocoreClientError]


class GlobalAcceleratorClient:
    """
    [GlobalAccelerator.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_custom_routing_endpoints(
        self,
        EndpointConfigurations: List[CustomRoutingEndpointConfigurationTypeDef],
        EndpointGroupArn: str,
    ) -> AddCustomRoutingEndpointsResponseTypeDef:
        """
        [Client.add_custom_routing_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.add_custom_routing_endpoints)
        """

    def advertise_byoip_cidr(self, Cidr: str) -> AdvertiseByoipCidrResponseTypeDef:
        """
        [Client.advertise_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.advertise_byoip_cidr)
        """

    def allow_custom_routing_traffic(
        self,
        EndpointGroupArn: str,
        EndpointId: str,
        DestinationAddresses: List[str] = None,
        DestinationPorts: List[int] = None,
        AllowAllTrafficToEndpoint: bool = None,
    ) -> None:
        """
        [Client.allow_custom_routing_traffic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.allow_custom_routing_traffic)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.can_paginate)
        """

    def create_accelerator(
        self,
        Name: str,
        IdempotencyToken: str,
        IpAddressType: Literal["IPV4"] = None,
        IpAddresses: List[str] = None,
        Enabled: bool = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateAcceleratorResponseTypeDef:
        """
        [Client.create_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_accelerator)
        """

    def create_custom_routing_accelerator(
        self,
        Name: str,
        IdempotencyToken: str,
        IpAddressType: Literal["IPV4"] = None,
        IpAddresses: List[str] = None,
        Enabled: bool = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateCustomRoutingAcceleratorResponseTypeDef:
        """
        [Client.create_custom_routing_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_custom_routing_accelerator)
        """

    def create_custom_routing_endpoint_group(
        self,
        ListenerArn: str,
        EndpointGroupRegion: str,
        DestinationConfigurations: List[CustomRoutingDestinationConfigurationTypeDef],
        IdempotencyToken: str,
    ) -> CreateCustomRoutingEndpointGroupResponseTypeDef:
        """
        [Client.create_custom_routing_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_custom_routing_endpoint_group)
        """

    def create_custom_routing_listener(
        self, AcceleratorArn: str, PortRanges: List["PortRangeTypeDef"], IdempotencyToken: str
    ) -> CreateCustomRoutingListenerResponseTypeDef:
        """
        [Client.create_custom_routing_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_custom_routing_listener)
        """

    def create_endpoint_group(
        self,
        ListenerArn: str,
        EndpointGroupRegion: str,
        IdempotencyToken: str,
        EndpointConfigurations: List[EndpointConfigurationTypeDef] = None,
        TrafficDialPercentage: float = None,
        HealthCheckPort: int = None,
        HealthCheckProtocol: Literal["TCP", "HTTP", "HTTPS"] = None,
        HealthCheckPath: str = None,
        HealthCheckIntervalSeconds: int = None,
        ThresholdCount: int = None,
        PortOverrides: List["PortOverrideTypeDef"] = None,
    ) -> CreateEndpointGroupResponseTypeDef:
        """
        [Client.create_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_endpoint_group)
        """

    def create_listener(
        self,
        AcceleratorArn: str,
        PortRanges: List["PortRangeTypeDef"],
        Protocol: Literal["TCP", "UDP"],
        IdempotencyToken: str,
        ClientAffinity: Literal["NONE", "SOURCE_IP"] = None,
    ) -> CreateListenerResponseTypeDef:
        """
        [Client.create_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_listener)
        """

    def delete_accelerator(self, AcceleratorArn: str) -> None:
        """
        [Client.delete_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_accelerator)
        """

    def delete_custom_routing_accelerator(self, AcceleratorArn: str) -> None:
        """
        [Client.delete_custom_routing_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_custom_routing_accelerator)
        """

    def delete_custom_routing_endpoint_group(self, EndpointGroupArn: str) -> None:
        """
        [Client.delete_custom_routing_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_custom_routing_endpoint_group)
        """

    def delete_custom_routing_listener(self, ListenerArn: str) -> None:
        """
        [Client.delete_custom_routing_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_custom_routing_listener)
        """

    def delete_endpoint_group(self, EndpointGroupArn: str) -> None:
        """
        [Client.delete_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_endpoint_group)
        """

    def delete_listener(self, ListenerArn: str) -> None:
        """
        [Client.delete_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_listener)
        """

    def deny_custom_routing_traffic(
        self,
        EndpointGroupArn: str,
        EndpointId: str,
        DestinationAddresses: List[str] = None,
        DestinationPorts: List[int] = None,
        DenyAllTrafficToEndpoint: bool = None,
    ) -> None:
        """
        [Client.deny_custom_routing_traffic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.deny_custom_routing_traffic)
        """

    def deprovision_byoip_cidr(self, Cidr: str) -> DeprovisionByoipCidrResponseTypeDef:
        """
        [Client.deprovision_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.deprovision_byoip_cidr)
        """

    def describe_accelerator(self, AcceleratorArn: str) -> DescribeAcceleratorResponseTypeDef:
        """
        [Client.describe_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_accelerator)
        """

    def describe_accelerator_attributes(
        self, AcceleratorArn: str
    ) -> DescribeAcceleratorAttributesResponseTypeDef:
        """
        [Client.describe_accelerator_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_accelerator_attributes)
        """

    def describe_custom_routing_accelerator(
        self, AcceleratorArn: str
    ) -> DescribeCustomRoutingAcceleratorResponseTypeDef:
        """
        [Client.describe_custom_routing_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_custom_routing_accelerator)
        """

    def describe_custom_routing_accelerator_attributes(
        self, AcceleratorArn: str
    ) -> DescribeCustomRoutingAcceleratorAttributesResponseTypeDef:
        """
        [Client.describe_custom_routing_accelerator_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_custom_routing_accelerator_attributes)
        """

    def describe_custom_routing_endpoint_group(
        self, EndpointGroupArn: str
    ) -> DescribeCustomRoutingEndpointGroupResponseTypeDef:
        """
        [Client.describe_custom_routing_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_custom_routing_endpoint_group)
        """

    def describe_custom_routing_listener(
        self, ListenerArn: str
    ) -> DescribeCustomRoutingListenerResponseTypeDef:
        """
        [Client.describe_custom_routing_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_custom_routing_listener)
        """

    def describe_endpoint_group(
        self, EndpointGroupArn: str
    ) -> DescribeEndpointGroupResponseTypeDef:
        """
        [Client.describe_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_endpoint_group)
        """

    def describe_listener(self, ListenerArn: str) -> DescribeListenerResponseTypeDef:
        """
        [Client.describe_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_listener)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.generate_presigned_url)
        """

    def list_accelerators(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListAcceleratorsResponseTypeDef:
        """
        [Client.list_accelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_accelerators)
        """

    def list_byoip_cidrs(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListByoipCidrsResponseTypeDef:
        """
        [Client.list_byoip_cidrs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_byoip_cidrs)
        """

    def list_custom_routing_accelerators(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListCustomRoutingAcceleratorsResponseTypeDef:
        """
        [Client.list_custom_routing_accelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_custom_routing_accelerators)
        """

    def list_custom_routing_endpoint_groups(
        self, ListenerArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListCustomRoutingEndpointGroupsResponseTypeDef:
        """
        [Client.list_custom_routing_endpoint_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_custom_routing_endpoint_groups)
        """

    def list_custom_routing_listeners(
        self, AcceleratorArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListCustomRoutingListenersResponseTypeDef:
        """
        [Client.list_custom_routing_listeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_custom_routing_listeners)
        """

    def list_custom_routing_port_mappings(
        self,
        AcceleratorArn: str,
        EndpointGroupArn: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListCustomRoutingPortMappingsResponseTypeDef:
        """
        [Client.list_custom_routing_port_mappings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_custom_routing_port_mappings)
        """

    def list_custom_routing_port_mappings_by_destination(
        self,
        EndpointId: str,
        DestinationAddress: str,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListCustomRoutingPortMappingsByDestinationResponseTypeDef:
        """
        [Client.list_custom_routing_port_mappings_by_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_custom_routing_port_mappings_by_destination)
        """

    def list_endpoint_groups(
        self, ListenerArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListEndpointGroupsResponseTypeDef:
        """
        [Client.list_endpoint_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_endpoint_groups)
        """

    def list_listeners(
        self, AcceleratorArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListListenersResponseTypeDef:
        """
        [Client.list_listeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_listeners)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_tags_for_resource)
        """

    def provision_byoip_cidr(
        self, Cidr: str, CidrAuthorizationContext: CidrAuthorizationContextTypeDef
    ) -> ProvisionByoipCidrResponseTypeDef:
        """
        [Client.provision_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.provision_byoip_cidr)
        """

    def remove_custom_routing_endpoints(
        self, EndpointIds: List[str], EndpointGroupArn: str
    ) -> None:
        """
        [Client.remove_custom_routing_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.remove_custom_routing_endpoints)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.untag_resource)
        """

    def update_accelerator(
        self,
        AcceleratorArn: str,
        Name: str = None,
        IpAddressType: Literal["IPV4"] = None,
        Enabled: bool = None,
    ) -> UpdateAcceleratorResponseTypeDef:
        """
        [Client.update_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_accelerator)
        """

    def update_accelerator_attributes(
        self,
        AcceleratorArn: str,
        FlowLogsEnabled: bool = None,
        FlowLogsS3Bucket: str = None,
        FlowLogsS3Prefix: str = None,
    ) -> UpdateAcceleratorAttributesResponseTypeDef:
        """
        [Client.update_accelerator_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_accelerator_attributes)
        """

    def update_custom_routing_accelerator(
        self,
        AcceleratorArn: str,
        Name: str = None,
        IpAddressType: Literal["IPV4"] = None,
        Enabled: bool = None,
    ) -> UpdateCustomRoutingAcceleratorResponseTypeDef:
        """
        [Client.update_custom_routing_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_custom_routing_accelerator)
        """

    def update_custom_routing_accelerator_attributes(
        self,
        AcceleratorArn: str,
        FlowLogsEnabled: bool = None,
        FlowLogsS3Bucket: str = None,
        FlowLogsS3Prefix: str = None,
    ) -> UpdateCustomRoutingAcceleratorAttributesResponseTypeDef:
        """
        [Client.update_custom_routing_accelerator_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_custom_routing_accelerator_attributes)
        """

    def update_custom_routing_listener(
        self, ListenerArn: str, PortRanges: List["PortRangeTypeDef"]
    ) -> UpdateCustomRoutingListenerResponseTypeDef:
        """
        [Client.update_custom_routing_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_custom_routing_listener)
        """

    def update_endpoint_group(
        self,
        EndpointGroupArn: str,
        EndpointConfigurations: List[EndpointConfigurationTypeDef] = None,
        TrafficDialPercentage: float = None,
        HealthCheckPort: int = None,
        HealthCheckProtocol: Literal["TCP", "HTTP", "HTTPS"] = None,
        HealthCheckPath: str = None,
        HealthCheckIntervalSeconds: int = None,
        ThresholdCount: int = None,
        PortOverrides: List["PortOverrideTypeDef"] = None,
    ) -> UpdateEndpointGroupResponseTypeDef:
        """
        [Client.update_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_endpoint_group)
        """

    def update_listener(
        self,
        ListenerArn: str,
        PortRanges: List["PortRangeTypeDef"] = None,
        Protocol: Literal["TCP", "UDP"] = None,
        ClientAffinity: Literal["NONE", "SOURCE_IP"] = None,
    ) -> UpdateListenerResponseTypeDef:
        """
        [Client.update_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_listener)
        """

    def withdraw_byoip_cidr(self, Cidr: str) -> WithdrawByoipCidrResponseTypeDef:
        """
        [Client.withdraw_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Client.withdraw_byoip_cidr)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_accelerators"]
    ) -> ListAcceleratorsPaginator:
        """
        [Paginator.ListAccelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListAccelerators)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_byoip_cidrs"]) -> ListByoipCidrsPaginator:
        """
        [Paginator.ListByoipCidrs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListByoipCidrs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_routing_accelerators"]
    ) -> ListCustomRoutingAcceleratorsPaginator:
        """
        [Paginator.ListCustomRoutingAccelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingAccelerators)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_routing_listeners"]
    ) -> ListCustomRoutingListenersPaginator:
        """
        [Paginator.ListCustomRoutingListeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingListeners)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_routing_port_mappings"]
    ) -> ListCustomRoutingPortMappingsPaginator:
        """
        [Paginator.ListCustomRoutingPortMappings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingPortMappings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_routing_port_mappings_by_destination"]
    ) -> ListCustomRoutingPortMappingsByDestinationPaginator:
        """
        [Paginator.ListCustomRoutingPortMappingsByDestination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingPortMappingsByDestination)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_endpoint_groups"]
    ) -> ListEndpointGroupsPaginator:
        """
        [Paginator.ListEndpointGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListEndpointGroups)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_listeners"]) -> ListListenersPaginator:
        """
        [Paginator.ListListeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListListeners)
        """
