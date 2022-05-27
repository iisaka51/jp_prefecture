from setuptools import setup, find_packages

setup(
    name="jp_prefecture",
    version="0.1.1",
    license="MIT",
    install_requirements=["pandas"],
    author="iisaka51",
    author_email="iisaka51@gmail.com",
    url="https://github.com/iisaka51/jp_prefecture",
    description="Simple utiliti convert name of japanese prefectures.",
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)
