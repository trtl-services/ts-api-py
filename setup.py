import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ts_api_py",
    version="0.1.4",
    author="fexra",
    author_email="fexra@protonmail.com",
    description="Library to interact with the TRLT Services API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trtl-services/ts-api-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: GNU Affero General Public License v3",
    ],
)