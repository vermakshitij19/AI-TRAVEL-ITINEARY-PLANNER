from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ai-travel-agent",
    version="0.1.0",
    author="Kshitij Verma",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=requirements,
)