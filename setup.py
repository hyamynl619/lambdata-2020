
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="s2t2-lambdata-1",
    version="0.1",
    author="MJ Rossetti",
    author_email="datacreativellc@gmail.com",
    description="Example package for lambda school",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/hyamynl619/lambdata-2020.git", 
    keywords="lambda school",
    packages=find_packages() # ["my_lambda"]
)