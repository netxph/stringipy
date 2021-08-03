from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='StringiPy',
      version='0.1.0',
      description='Python Functional String Utilities',
      long_description=long_description,
      long_description_content_type='text/markdown',
      license='MIT',
      author='Marc Vitalis',
      author_email='marc.vitalis@live.com',
      url='https://github.com/netxph/stringipy',
      packages=['stringipy'])