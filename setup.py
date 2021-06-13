from setuptools import setup

setup(
    name='hello-world',
    author='me',
    version='1.0.0',
    packages=['hello'],
    package_dir={'': 'src'},
    scripts=['src/hello-world'],
    include_package_data=True,
    python_requires='>=3.7',
)
