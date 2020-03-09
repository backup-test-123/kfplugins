from __future__ import absolute_import

from setuptools import setup, find_packages  # noqa
import tfoperatorplugin

setup(
    name='tfoperatorplugin',
    version=tfoperatorplugin.__version__,
    maintainer='Adhita Selvaraj',
    maintainer_email='adhita.selvaraj@gmail.com',
    url="https://github.com/flyteorg/kfplugins",
    description='FlyteKit TF Operator plugin',
    long_description=open('README.md').read(),
    packages=find_packages(include=("sdk*",), exclude=["tests*"]),
    package_data={},
    include_package_data=False,
    entry_points={'console_scripts': []},
    setup_requires=["pip>10.0.0,<19.2.0"],
    install_requires=[
        "protobuf>=3.6.1,<4",
        "flytekit>=0.5.3",
    ],
    scripts=[],
    license="apache2",
    python_requires=">=2.7"
)
