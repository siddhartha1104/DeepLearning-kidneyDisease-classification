import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_descriptoin = f.read()


__version__ = "0.0.0"

REPO_NAME = "DeepLearning-kidneyDisease-classification"
AUTHOR_USER_NAME = "siddhartha1104"
SRC_REPO = "kidneyDiseaseClassification"
AUTHOR_EMAIL = "mail@siddharthapathak.com.np"

setuptools.setup(
     name= SRC_REPO,
     version=__version__,
     author= AUTHOR_USER_NAME,
     author_email= AUTHOR_EMAIL,
     description= "A small python package for CNN app",
     long_description= long_descriptoin,
     url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
     project_urls = {
         "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
     },
     package_dir= {"": "src"},
     packages=setuptools.find_packages(where="src")
) 

