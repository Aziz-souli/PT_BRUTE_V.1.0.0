from setuptools import setup, find_packages

setup(
    name="PT_BRUTE",  # Name of your tool/package
    version="1.0.0",  # Tool version
    description="A command-line tool to Path Traversal Bruteforcing.",
    author="Aziz Souli",
    author_email="aziz.souli@enicar.ucar.tn",
    url="https://github.com/Aziz-souli/PATH_TRAVERSAL_BRUTEFORCING_TOOL_V1",  # Optional GitHub link
    packages=find_packages(),  # Automatically find `my_tool` package
    entry_points={
        "console_scripts": [
            "PT_BRUTE=app.main:main",  # Command name ->s module:function
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
    python_requires='>=3.5',  # Minimum Python version
)
