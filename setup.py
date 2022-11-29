from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

def get_version(rel_path):
    for line in (this_directory / rel_path).read_text().splitlines():
        if line.startswith('__VERSION__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    name="jp_prefecture",
    version=get_version('jp_prefecture/versions.py'),
    license="MIT",
    install_requires=["pandas"],
    author="iisaka51",
    author_email="iisaka51@gmail.com",
    url="https://github.com/iisaka51/jp_prefecture",
    description="Simple utilitiy convert name of japanese prefectures",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    package_data={'': [ 'data/*.csv' ]},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)
