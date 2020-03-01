from __future__ import absolute_import

from setuptools import setup, find_packages  # noqa
import tfoperatorplugin

setup(
    name='tfoperatorplugin',
    version=flyteexampleplugin.__version__,
    maintainer='Adhita Selvaraj <adhita.selvaraj@gmail.com>',
    maintainer_email='adhita.selvaraj@gmail.com',
    packages=find_packages(exclude=["tests*"]),
    url='https://github.com/flyteorg/kfplugins/tfoperator',
    description='TF Operator plugin',
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
        "flytekit>=0.3.0b0,<0.4.0",
    ],
    tests_require=['pytest'],
    scripts=[
    ],
    license="apache2",
    python_requires=">=2.7"
)
