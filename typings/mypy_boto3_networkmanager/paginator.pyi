"""
Main interface for networkmanager service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_networkmanager import NetworkManagerClient
    from mypy_boto3_networkmanager.paginator import (
        DescribeGlobalNetworksPaginator,
        GetConnectionsPaginator,
        GetCustomerGatewayAssociationsPaginator,
        GetDevicesPaginator,
        GetLinkAssociationsPaginator,
        GetLinksPaginator,
        GetSitesPaginator,
        GetTransitGatewayConnectPeerAssociationsPaginator,
        GetTransitGatewayRegistrationsPaginator,
    )

    client: NetworkManagerClient = boto3.client("networkmanager")

    describe_global_networks_paginator: DescribeGlobalNetworksPaginator = client.get_paginator("describe_global_networks")
    get_connections_paginator: GetConnectionsPaginator = client.get_paginator("get_connections")
    get_customer_gateway_associations_paginator: GetCustomerGatewayAssociationsPaginator = client.get_paginator("get_customer_gateway_associations")
    get_devices_paginator: GetDevicesPaginator = client.get_paginator("get_devices")
    get_link_associations_paginator: GetLinkAssociationsPaginator = client.get_paginator("get_link_associations")
    get_links_paginator: GetLinksPaginator = client.get_paginator("get_links")
    get_sites_paginator: GetSitesPaginator = client.get_paginator("get_sites")
    get_transit_gateway_connect_peer_associations_paginator: GetTransitGatewayConnectPeerAssociationsPaginator = client.get_paginator("get_transit_gateway_connect_peer_associations")
    get_transit_gateway_registrations_paginator: GetTransitGatewayRegistrationsPaginator = client.get_paginator("get_transit_gateway_registrations")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_networkmanager.type_defs import (
    DescribeGlobalNetworksResponseTypeDef,
    GetConnectionsResponseTypeDef,
    GetCustomerGatewayAssociationsResponseTypeDef,
    GetDevicesResponseTypeDef,
    GetLinkAssociationsResponseTypeDef,
    GetLinksResponseTypeDef,
    GetSitesResponseTypeDef,
    GetTransitGatewayConnectPeerAssociationsResponseTypeDef,
    GetTransitGatewayRegistrationsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeGlobalNetworksPaginator",
    "GetConnectionsPaginator",
    "GetCustomerGatewayAssociationsPaginator",
    "GetDevicesPaginator",
    "GetLinkAssociationsPaginator",
    "GetLinksPaginator",
    "GetSitesPaginator",
    "GetTransitGatewayConnectPeerAssociationsPaginator",
    "GetTransitGatewayRegistrationsPaginator",
)


class DescribeGlobalNetworksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeGlobalNetworks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/networkmanager.html#NetworkManager.Paginator.DescribeGlobalNetworks)
    """

    def paginate(
        self, GlobalNetworkIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeGlobalNetworksResponseTypeDef]:
        """
        [DescribeGlobalNetworks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/networkmanager.html#NetworkManager.Paginator.DescribeGlobalNetworks.paginate)
        """


class GetConnectionsPaginator(Boto3Paginator):
    """
    [Paginator.GetConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/networkmanager.html#NetworkManager.Paginator.GetConnections)
    """

    def paginate(
        self,
        GlobalNetworkId: str,
        ConnectionIds: List[str] = None,
        DeviceId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetConnectionsResponseTypeDef]:
        """
        [GetConnections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/networkmanager.html#NetworkManager.Paginator.GetConnections.paginate)
        """


class GetCustomerGatewayAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.GetCustomerGatewayAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/networkmanager.html#NetworkManager.Paginator.GetCustomerGatewayAssociations)
    """

    def paginate(
        self,
        GlobalNetworkId: str,
        CustomerGatewayArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetCustomerGatewayAssociationsResponseTypeDef]:
        """
        [GetCustomerGatewayAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/networkmanager.html#NetworkManager.Paginator.GetCustomerGatewayAssociations.paginate)
        """


class GetDevicesPaginator(Boto3Paginator):
    """
    [Paginator.GetDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/networkmanager.html#NetworkManager.Paginator.GetDevices)
    """

    def paginate(
        self,
        GlobalNetworkId: str,
        DeviceIds: List[str] = None,
        SiteId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetDevicesResponseTypeDef]:
        """
        [GetDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/networkmanager.html#NetworkManager.Paginator.GetDevices.paginate)
        """


class GetLinkAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.GetLinkAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinkAssociations)
    """

    def paginate(
        self,
        GlobalNetworkId: str,
        DeviceId: str = None,
        LinkId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetLinkAssociationsResponseTypeDef]:
        """
        [GetLinkAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinkAssociations.paginate)
        """


class GetLinksPaginator(Boto3Paginator):
    """
    [Paginator.GetLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinks)
    """

    def paginate(
        self,
        GlobalNetworkId: str,
        LinkIds: List[str] = None,
        SiteId: str = None,
        Type: str = None,
        Provider: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetLinksResponseTypeDef]:
        """
        [GetLinks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinks.paginate)
        """


class GetSitesPaginator(Boto3Paginator):
    """
    [Paginator.GetSites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/networkmanager.html#NetworkManager.Paginator.GetSites)
    """

    def paginate(
        self,
        GlobalNetworkId: str,
        SiteIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetSitesResponseTypeDef]:
        """
        [GetSites.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/networkmanager.html#NetworkManager.Paginator.GetSites.paginate)
        """


class GetTransitGatewayConnectPeerAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.GetTransitGatewayConnectPeerAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayConnectPeerAssociations)
    """

    def paginate(
        self,
        GlobalNetworkId: str,
        TransitGatewayConnectPeerArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetTransitGatewayConnectPeerAssociationsResponseTypeDef]:
        """
        [GetTransitGatewayConnectPeerAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayConnectPeerAssociations.paginate)
        """


class GetTransitGatewayRegistrationsPaginator(Boto3Paginator):
    """
    [Paginator.GetTransitGatewayRegistrations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayRegistrations)
    """

    def paginate(
        self,
        GlobalNetworkId: str,
        TransitGatewayArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetTransitGatewayRegistrationsResponseTypeDef]:
        """
        [GetTransitGatewayRegistrations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayRegistrations.paginate)
        """
