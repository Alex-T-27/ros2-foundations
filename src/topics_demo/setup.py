from setuptools import find_packages, setup

package_name = 'topics_demo'

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
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'talker = topics_demo.talker:main',
            'listener = topics_demo.listener:main',
            'driver = topics_demo.driver:main',
        ],
    },
)
