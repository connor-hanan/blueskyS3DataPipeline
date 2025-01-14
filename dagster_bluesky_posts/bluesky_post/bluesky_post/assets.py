from dagster import AssetExecutionContext
from dagster_embedded_elt.dlt import DagsterDltResource, dlt_assets
from dlt import pipeline
from .bluesky_posts_dagster import bluesky_source
from typing import Generator, Any


@dlt_assets(
    dlt_source=bluesky_source(),
    dlt_pipeline=pipeline(
        pipeline_name="blueskyPosts",
        dataset_name="blueskyData",
        destination="filesystem",
        progress="log",
    ),
    name="bluesky",
    group_name="bluesky",
)
def dagster_bluesky_assets(
        context: AssetExecutionContext,
        dlt: DagsterDltResource
        ) -> Generator[Any, DagsterDltResource, None]:
    yield from dlt.run(context=context)
