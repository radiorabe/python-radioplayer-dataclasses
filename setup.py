"""Set up radioplayer-dataclasses."""

from setuptools import setup

with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()


setup(
    name="radioplayer-dataclasses",
    description="Dataclasses for building Radioplayer XML.",
    url="https://github.com/radiorabe/python-radioplayer-dataclasses",
    author="RaBe IT-Reaktion",
    author_email="it@rabe.ch",
    license="AGPL-3",
    packages=["radioplayer.dataclasses"],
    version_config={"starting_version": "0.1.0"},
    setup_requires=["setuptools-git-versioning"],
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 3.10",
    ],
)
