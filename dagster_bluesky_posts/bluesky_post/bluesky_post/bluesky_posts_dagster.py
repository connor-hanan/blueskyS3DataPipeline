from datetime import datetime, timedelta
from typing import Any
import dlt
from dlt.sources.rest_api import (RESTAPIConfig,  # type: ignore
                                  rest_api_resources)


# Funtion to calculate date range
def get_date_range() -> tuple[str, str]:
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
def bluesky_source() -> Any:
    """
    Configure the API call
    """

    # Get the date range
    since, until = get_date_range()

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