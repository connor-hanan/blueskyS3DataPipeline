from datetime import datetime, timedelta
from typing import Any
import dlt
from dlt.sources.rest_api import RESTAPIConfig, rest_api_resources


# Funtion to calculate date range
def getDateRange() -> tuple[str, str]:
    """
    Calculates date range for the API call
    Returns
    tuple:since, until
    """

    yesterday = datetime.now() - timedelta(days=1)

    since = yesterday.replace(hour=0, minute=0, second=0,
                              microsecond=0).isoformat() + 'Z'
    until = yesterday.replace(hour=23, minute=59, second=59,
                              microsecond=999999).isoformat() + 'Z'

    return since, until


# Define the Bluesky posts resource
@dlt.source
def blueskySource() -> Any:
    """
    Configure the API call
    """

    # Get the date range
    since, until = getDateRange()

    # Define RESTAPIConfig for Bluesky API
    config: RESTAPIConfig = {
        "client": {"base_url": "https://public.api.bsky.app/xrpc/"},
        "resources": [
            {
                "name": "posts",
                "endpoint": {
                    "path": "app.bsky.feed.searchPosts",
                    "params": {
                        "q": "data engineer",  # Search term
                        "sort": "latest",
                        "since": since,
                        "until": until,
                        "tag": ["dataBS", "datasky"],
                        "limit": 100,
                    },
                },
            },
        ],
    }

    # Generate resources using RESTAPIConfig
    yield from rest_api_resources(config)


# Create and configure the pipeline
pipeline = dlt.pipeline(
    pipeline_name="blueskyAPI",
    destination="filesystem",
    dataset_name="blueskyData"
)

# Run the pipeline
loadInfo = pipeline.run(blueskySource())
print(loadInfo)
