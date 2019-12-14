from setuptools import setup

setup(
    name='RDRSS',
    version='0.2.1',
    author='Michal Dobes',
    scripts=['rdrss/RDRSS.py'],
    install_requires=[
          'requests',
          'feedparser',
          'argparse',
      ],
    license='MIT',
    download_url = 'https://github.com/CaptainMishan/RDRSS/archive/0.2.1.tar.gz',
    long_description=open('README.md').read(),
)
