from __future__ import absolute_import

from setuptools import setup, find_packages  # noqa

setup(
    name='flytepluginexample',
    version=flytesampleplugin.__version__,
    maintainer='Flyte team',
    maintainer_email='ketan.umare@gmail.com',
    packages=find_packages(exclude=["tests*"]),
    url='https://github.com/flyteorg/flytepluginexample',
    description='FlyteKit Example plugin',
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts': [
        ]
    },
    setup_requires=[
        "pip>10.0.0,<19.2.0"
    ],
    install_requires=[
        "protobuf>=3.6.1,<4",
        "flytekit>=0.2.0",
    ],
    scripts=[
    ],
    license="apache2",
    python_requires=">=2.7"
))
