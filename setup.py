# chardet's setup.py
from distutils.core import setup
import setuptools
setup(
    name = "codex",
    packages = ["codex"],
    version = "0.1",
    description = "Coding domain expertise: the dynamic ontology workbench",
    author = "The Indiana Philosophy Ontology (InPhO) Project",
    author_email = "inpho@indiana.edu",
    url = "http://inpho.cogs.indiana.edu/",
    download_url = "http://www.github.com/inpho/codex",
    keywords = ["taxonomy", "ontology"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
        "Topic :: Text Processing :: Linguistic",
        ],
    install_requires=[
        "SQLAlchemy>=0.6.0,<=0.6.99",
        "SPARQLWrapper>=1.4.0,<=1.4.99"
    ],

    long_description = """\
Coding Expertise (CodEx): A Dynamic Ontology Workbench
----------------------------------------------------------

Modularizes the dynamic ontology techniques pioneered at the Indiana Philosophy
Ontology (InPhO) Project

"""
)
