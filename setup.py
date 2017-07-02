from distutils.core import setup

setup(name='streamingApp',
      version='1.0',
      description='Stock streaming app',
      author='Kavish Patel',
      packages=['json', 'kafka', 'schedule', 'googlefinance'],
     )