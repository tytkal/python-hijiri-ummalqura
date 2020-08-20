import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="umalqurra",
    version="1.0.0",
    author="tytkal",
    author_email="tytkal@gmail.com",
    description="Islamic calendar (hijri).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tytkal/python-hijiri-ummalqura",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)