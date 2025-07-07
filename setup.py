from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="MLOPS-PROJECT-HOTEL-RESERVATION",
    version="0.1",
    author="MichaelLiao",
    packages=find_packages(),
    install_requires=requirements
)