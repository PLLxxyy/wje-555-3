def apply_property_filters(queryset, params):
    if params.get("type"):
        queryset = queryset.filter(type=params["type"])
    if params.get("status"):
        queryset = queryset.filter(status=params["status"])
    if params.get("min_price"):
        queryset = queryset.filter(price__gte=params["min_price"])
    if params.get("max_price"):
        queryset = queryset.filter(price__lte=params["max_price"])
    if params.get("min_area"):
        queryset = queryset.filter(area__gte=params["min_area"])
    if params.get("max_area"):
        queryset = queryset.filter(area__lte=params["max_area"])
    if params.get("rooms"):
        queryset = queryset.filter(rooms__icontains=params["rooms"])
    ordering = params.get("ordering")
    if ordering in ["price", "-price", "createdAt", "-createdAt"]:
        queryset = queryset.order_by(ordering)
    return queryset

