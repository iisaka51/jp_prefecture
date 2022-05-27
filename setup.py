from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="jp_prefecture",
    version="0.1.2",
    license="MIT",
    install_requirements=["pandas"],
    author="iisaka51",
    author_email="iisaka51@gmail.com",
    url="https://github.com/iisaka51/jp_prefecture",
    description="Simple utiliti convert name of japanese prefectures.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)
