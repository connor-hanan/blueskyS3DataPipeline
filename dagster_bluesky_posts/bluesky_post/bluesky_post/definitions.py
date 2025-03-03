from dagster import Definitions, load_assets_from_modules
from dagster_embedded_elt.dlt import DagsterDltResource
from bluesky_post import assets  # noqa: TID252


dlt_resource = DagsterDltResource()

#  Unpack the list returned by load_assets_from_modules
all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    resources={
        "dlt": dlt_resource,
    },
)
