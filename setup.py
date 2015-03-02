import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

install_requires = [
    'requests',
]

test_requires = [
]

setup(name='pagespeed',
      version='0.1.0',
      description='Run a given URL against Google\'s PageSpeed tool',
      long_description = README,
      license='MIT License',
      author='Brandon J. Schwartz',
      author_email='brandon@boomajoom.com',
      url='http://www.boomajoom.com',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='pagespeed',
      install_requires=install_requires,
      test_requires=test_requires,
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
      )