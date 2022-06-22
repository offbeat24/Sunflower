from setuptools import setup
import os
from glob import glob

package_name = 'stem_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/stem.launch.py'))
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
            "serial_talker=stem_pkg.serial_talker:main",
            "cmd_selector=stem_pkg.cmd_selector:main",
            "calculator=stem_pkg.calculator:main",
            "tensor_publisher=stem_pkg.tensor_publisher:main",
            "tensor=stem_pkg.tensor:main"
            #"tester=stem_pkg.tester:main",
            #"controller=stem_pkg.controller:main"
        ],
    },
)