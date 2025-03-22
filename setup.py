from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    description="A simple greeting package",
    author="Your Name",
    author_email="your_email@example.com",
    url="https://github.com/yourusername/mypackage",  # Optional
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)