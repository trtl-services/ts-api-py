import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ts-api-py",
    version="0.2.1",
    author="fexra",
    author_email="fexra@protonmail.com",
    description="Library to interact with the TRTL Services API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trtl-services/ts-api-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
    ],
)