from distutils.core import setup
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
  name = 'Multi Function Runner',         
  packages = ['Multi Function Runner'],   
  version = '1.0.2',      
  license='MIT',        
  description = 'A simple library for Python to run multiple functions in a lambda function.',   
  author = 'Tejas',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author_email = 'help.a.helpcenter@gmail.com',      
  url = 'https://github.com/avibhardwaj233/Multi-Function-Runner',   
  download_url = 'https://github.com/avibhardwaj233/Multi-Function-Runner/archive/refs/tags/1.0.0.tar.gz',    
  keywords = ['Function', 'Multi Function runner', 'Multi function', 'Function runner'],   
  install_requires=[],

  classifiers=[
    'Development Status :: 4 - Beta',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)