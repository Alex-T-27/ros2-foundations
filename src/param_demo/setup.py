from setuptools import find_packages, setup

package_name = 'param_demo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='alex-tran',
    maintainer_email='alextran201007@gmail.com',
    description='Python Param demo',
    license='Apache License 2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'param_demo = param_demo.param_demo:main',
            'random_pub = param_demo.random_pub:main',
            'two_timer = param_demo.two_timer:main'
        ],
    },
)
