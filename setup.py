import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ts-api-py",
    version="0.1.1",
    author="Fexra",
    author_email="fexra@protonmail.com",
    description="Library to interact with the TRLT Services API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trtl-services/ts-api-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
    ],
)