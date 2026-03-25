from setuptools import setup, find_packages

setup(
    name="multiple-testing-toolkit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib"
    ],
    author="Alani Odunlami",
    description="A toolkit for multiple hypothesis testing corrections (FDR, Bonferroni)",
)
