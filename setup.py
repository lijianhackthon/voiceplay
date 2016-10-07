try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'The package which is used for playing human voice',
    'author': 'Li Jian',
    'url': 'http://www.iplayvoice.com',
    'download_url': 'https://github.com/lijianhackthon/voiceplay',
    'author_email': 'lijianhackthon@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['voiceplay'],
    'scripts': [],
    'name': 'voiceplay'
    }

    setup(**config)
