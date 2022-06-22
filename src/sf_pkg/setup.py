from setuptools import setup
import os
from glob import glob

package_name = 'sf_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/sf.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pi',
    maintainer_email='pi@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "serial_talker=sf_pkg.serial_talker:main",
            "cmd_selector=sf_pkg.cmd_selector:main",
            "calculator=sf_pkg.calculator:main",
            "tensor_publisher=sf_pkg.tensor_publisher:main",
        ],
    },
)
