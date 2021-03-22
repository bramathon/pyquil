# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ""

setup(
    long_description=readme,
    name="pyquil",
    version="3.0.0-rc.3",
    python_requires="==3.*,>=3.7.0",
    packages=[
        "pyquil",
        "pyquil._parser",
        "pyquil.api",
        "pyquil.api.tests",
        "pyquil.device",
        "pyquil.device.tests",
        "pyquil.device.transformers",
        "pyquil.experiment",
        "pyquil.experiment.tests",
        "pyquil.external",
        "pyquil.latex",
        "pyquil.latex.tests",
        "pyquil.simulation",
        "pyquil.simulation.tests",
        "pyquil.tests",
    ],
    package_dir={"": "."},
    package_data={
        "pyquil": ["*.typed"],
        "pyquil._parser": ["*.lark", "*.md"],
        "pyquil.api.tests": ["data/*.ini", "data/*.json"],
        "pyquil.external": ["*.md"],
        "pyquil.tests": ["data/*.json", "data/*.quil", "data/*.toml"],
    },
    install_requires=[
        'importlib-metadata==3.*,>=3.7.3; python_version < "3.8"',
        "ipython==7.*,>=7.21.0",
        "lark==0.*,>=0.11.1",
        "networkx==2.*,>=2.5.0",
        "numpy==1.19.*",
        "qcs-api-client==0.*,>=0.7.0",
        "rpcq==3.*,>=3.6.0",
        "scipy==1.*,>=1.6.1",
    ],
    extras_require={
        "dev": [
            "black==20.*,>=20.8.0.b1",
            "flake8==3.*,>=3.8.1",
            "mypy==0.740",
            "pytest==6.*,>=6.2.2",
            "pytest-cov==2.*,>=2.11.1",
            "pytest-httpx==0.*,>=0.9.0",
            "pytest-xdist==2.*,>=2.2.1",
        ],
        "docs": [
            "nbsphinx==0.*,>=0.8.2",
            "recommonmark==0.*,>=0.7.1",
            "sphinx==3.*,>=3.5.2",
            "sphinx-autodoc-typehints==1.*,>=1.11.1",
            "sphinx-rtd-theme==0.*,>=0.5.1",
        ],
    },
)
