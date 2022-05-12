import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='amanda',
     version='0.2',
     scripts=['amanda'] ,
     author="Pierre Schaus",
     author_email="pschaus@gmail.com",
     description="Strip your java source code to make it naked.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/pschaus/strip",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )