import setuptools

setup_params = dict(
	name='myns.sub.pkgA',
	version="1.0",
	author="Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	description="myns.sub.pkgA",
	packages=setuptools.find_packages(),
	namespace_packages=['myns', 'myns.sub'],
)
if __name__ == '__main__':
	setuptools.setup(**setup_params)
