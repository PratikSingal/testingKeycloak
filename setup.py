import setuptools


setuptools.setup(
    name="testingKeycloak",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description_content_type="text/markdown",
    url="https://github.com/PratikSingal/testingKeycloak",
    packages=setuptools.find_packages(),
    install_requires=[
        'asn1crypto==0.24.0',
        'certifi==2022.12.7',
        'cffi==1.11.5',
        'chardet==3.0.4',
        'cryptography==2.4.2',
        'idna==2.7',
        'pycparser==2.19',
        'PyJWT==1.7.1',
        'requests==2.20.1',
        'six==1.11.0',
        'typing==3.5.3.0',
        'urllib3==1.24.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
