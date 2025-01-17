from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='shipvision_backend',
      version="0.0.1",
      description="ShipVision Model",
      license="MIT",
      author="Le Wagon",
      author_email="contact@lewagon.org",
      #url="",
      install_requires=requirements,
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False)
