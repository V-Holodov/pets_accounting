from rest_framework.routers import DefaultRouter, DynamicRoute, Route


class CustomBulkDeleteRouter(DefaultRouter):
    """
    A custom URL router for the Product API that correctly routes
    DELETE requests with multiple query parameters.
    """

    routes = [
        Route(
            url=r"^{prefix}$",
            mapping={"get": "list", "post": "create", "delete": "destroy"},
            name="{basename}-list",
            detail=False,
            initkwargs={"suffix": "List"},
        ),
        Route(
            url=r"^{prefix}/{lookup}$",
            mapping={
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
            },
            name="{basename}-detail",
            detail=True,
            initkwargs={"suffix": "Detail"},
        ),
        DynamicRoute(
            url=r"^{prefix}/{lookup}/{url_path}$",
            name="{basename}-{url_name}",
            detail=True,
            initkwargs={},
        ),
    ]
