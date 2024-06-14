from setuptools import find_packages, setup

packages = [
    "pytest<7,>=5",
    "pytest-timeout",
]

setup(
    name="junior-python-developer-dna-analyser",
    version="1.0.1",
    author="Devskiller",
    author_email="support@devskiller.com",
    packages=find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
    zip_safe=False,
    install_requires=packages
    + [
        "wheel",
        "setuptools==41.0.1",
    ],
    setup_requires=["pytest-runner"],
    tests_require=packages,
)
