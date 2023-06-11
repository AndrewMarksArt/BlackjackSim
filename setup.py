from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name="blackjack-simulator",
    version="0.1.0",
    description="A Python package for simulating and analyzing blackjack strategies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Andrew Marks",
    author_email="andrew.colin.marks@gmail.com",
    url="https://github.com/AndrewMarksArt/BlackjackSim",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    install_requires=[
        'numpy>=1.20.0',
        'pandas>=1.2.0',
        'matplotlib>=3.4.0',
    ]
)
