from setuptools import setup, find_packages


setup(
    name='netbox-animal-sounds',
    version='0.1',
    description='NetBox plugin example',
    url='https://github.com/jeremystretch/netbox-animal-sounds',
    author='Jeremy Stretch',
    author_email='stretch@packetlife.net',
    license='Apache 2.0',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    # entry_points={
    #     'netbox_plugins': 'netbox_animal_sounds=netbox_animal_sounds:AnimalSoundsConfig'
    # }
)

