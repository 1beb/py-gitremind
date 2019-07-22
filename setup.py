import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gitremind",
    version="0.0.1",
    author="Brandon Bertelsen",
    author_email="brandon@bertelsen.ca",
    description="Scripts to automatically commit over time",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/credoinc/pytmx",
    packages=setuptools.find_packages(),
    install_requires = [
        'gitpython'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)