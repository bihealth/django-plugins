import os.path

from setuptools import find_packages, setup


def read_docs(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    return open(path).read()


long_description = """
``django-plugins`` offers functionality to make Django apps them more reusable.

For maintained by @bihealth, aims at Django >=3.0.

Home page
    http://pypi.python.org/pypi/django-plugins-bihealth

Source code:
    https://github.com/bihealth/django-plugins\n\n""".lstrip()

setup(
    name="django-plugins-bihealth",
    version="0.5.2",
    author="Mikko Nieminen, Manuel Holtgrewe, Oliver Stolpe",
    author_email="mikko.nieminen@bih-charite.de, manuel.holtgrewe@bih-charite.de, oliver.stolpe@bih-charite.de",
    packages=find_packages(exclude=["sample-project"]),
    install_requires=[
        "django>=3.0",
        "django-dirtyfields",
    ],
    url="https://github.com/bihealth/django-plugins",
    download_url="http://pypi.python.org/pypi/django-plugins-bihealth",
    license="LGPL",
    description="django-plugins-bihealth",
    long_description=long_description,
    include_package_data=True,
    exclude_package_data={"": ["sample-project"]},
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: " "GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
