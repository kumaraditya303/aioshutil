# -*- coding: utf-8 -*-
from pathlib import Path

from setuptools import setup

setup(
    name="aioshutil",
    author="Kumar Aditya",
    author_email="",
    url="https://github.com/kumaraditya303/aioshutil",
    description="Asynchronous shutil module.",
    keywords=["asyncio", "io", "shutil"],
    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    use_scm_version=True,
    packages=["aioshutil"],
    license="BSD License",
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: AsyncIO",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
    ],
    setup_requires=["setuptools_scm"],
)
