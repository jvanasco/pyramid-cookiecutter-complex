# stdlib
import os
import re

# pypi
from setuptools import find_packages
from setuptools import setup

# ==============================================================================


with open(os.path.join(os.path.dirname(__file__), "README.txt")) as r_file:
    README = r_file.read()
    README = README.split("\n\n", 1)[0] + "\n"

# store version in the init.py
with open(
    os.path.join(os.path.dirname(__file__), "src", "{{cookiecutter.repo_name}}_model", "__init__.py")
) as v_file:
    VERSION = re.compile(r'.*__VERSION__ = "(.*?)"', re.S).match(v_file.read()).group(1)

install_requires = [
    "pyramid_sqlassist",
    "pyramid<2",  # for `reify`
    "SQLAlchemy>1.4.7",  # 1.4.7 required for `transaction`
]

tests_require = []

setup(
    name="{{cookiecutter.repo_name}}_model",
    author="{{cookiecutter.author_name}},
    author_email="{{cookiecutter.author_email}},
    version=VERSION,
    url="",
    py_modules=["{{cookiecutter.repo_name}}_model"],
    description="models",
    long_description=README,
    zip_safe=False,
    keywords="",
    test_suite="tests_unit",
    packages=find_packages(
        where="src",
    ),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
    ],
)
