from setuptools import setup

setup(
    name='hello-world',
    packages=['helloworld'],
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'hello-world = helloworld:main'
        ]
    }
)
