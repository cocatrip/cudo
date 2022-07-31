from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    install_requires = fh.read()
    install_requires = install_requires.split("\n")

setup(
    name="cudo",
    description="Command Untuk Deploy Object",
    long_description=long_description,
    author="Adrianus Vian",
    author_email="cocatrip@yahoo.com",
    packages=find_packages(),
    install_requires=install_requires,
)
