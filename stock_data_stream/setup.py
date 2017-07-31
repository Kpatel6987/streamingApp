from distutils.core import setup

setup(name='stock_data_stream',
      version='1.0',
      description='Stock streaming app',
      author='Kavish Patel',
      packages=['json', 'kafka', 'schedule', 'googlefinance'],
     )
