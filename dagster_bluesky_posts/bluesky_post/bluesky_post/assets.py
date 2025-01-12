from dagster import AssetExecutionContext
from dagster_embedded_elt.dlt import DagsterDltResource, dlt_assets
from dlt import pipeline
from bluesky_posts_dagster import bluesky_source


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
def dagster_git_assets(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context)
