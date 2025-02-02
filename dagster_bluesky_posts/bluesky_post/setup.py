from setuptools import find_packages, setup

setup(
    name="bluesky_post",
    packages=find_packages(exclude=["bluesky_post_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
