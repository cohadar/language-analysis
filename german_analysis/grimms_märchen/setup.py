from setuptools import setup, find_packages
setup(
    name="grimms_märchen",
    packages=find_packages("код"),
    package_dir={"": "код"},
    install_requires=[
        "requests",
        "beautifulsoup4",
        "dependency-injector",
    ],
    extras_require={
        "dev": [
            "pytest",
        ],
    },
)
