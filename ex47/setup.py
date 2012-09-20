try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'ex46',
	'author': 'Brian Dant',
	'url': 'URL to get it at.'
	'download_url': 'Where to download it.',
	'author_email': 'Brian.R.Dant@gmail.com.',
	'version': '0.1',
	'install_requires': ['nose']
	'packages': ['ex46'], 
	'scripts': [],
	'name': 'Zeds ex46'
}

setup(**config)
