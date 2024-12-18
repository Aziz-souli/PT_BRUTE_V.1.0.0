from setuptools import setup, find_packages

setup(
    name="PT_BRUTE",  
    version="1.0.0",
    description="A command-line tool to Path Traversal Bruteforcing.",
    author="Aziz Souli",
    author_email="aziz.souli@enicar.ucar.tn",
    url="https://github.com/Aziz-souli/PT_BRUTE_V.1.0.0",  
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),  
    entry_points={
        "console_scripts": [
            "PT_BRUTE=app.main:main",  
        ],
    },
    install_requires=[

        "requests",  # For making HTTP requests
        "colorama",  # For colored terminal text
        "beautifulsoup4"  # For parsing HTML (bs4)
    ],  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version
)

