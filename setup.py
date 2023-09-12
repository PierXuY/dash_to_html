from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

setup(
    name="html_to_dash",
    version='{{VERSION_PLACEHOLDER}}',
    author="PierXuY",
    author_email="wxuymail@163.com",
    description="Convert HTML to dash format.",
    url="https://github.com/PierXuY/html_to_dash",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['re', 'dash', 'black', 'lxml'],
    keywords=['html', 'dash'],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)
