from setuptools import setup

setup(
	name='setuptest',
	packages=['setuptest'],
	entry_points={
		'console_scripts': [
			'setuptest-run = setuptest.app:main'
			]
	}
)