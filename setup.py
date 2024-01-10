import setuptools 

with open("README.md",encoding="utf-8") as f: # encoding="utf-8" is added to avoid the error: UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 777: character maps to <undefined>
    long_description = f.read() # read the contents of README.md

__version__ = "0.0.0" # version of the package
REPO_NAME="-Text-Summarizer-Project" # name of the repository
AUTHOR_USER_NAME = "lokesh182"
SRC_REPO="-Text-Summarizer-Project"
AUTHOR_EMAIL = "lokeshbapte.18@gmail.com"

setuptools.setup(
    name="TextSummarizer",
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A package to summarize text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"htts://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Yracker":f"htts://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where="src")
)