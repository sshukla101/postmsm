from setuptools import setup, Extension, find_packages


__version__='0.1dev'

setup(name='postmsm',
      description='Post MSMBuilder analysis, for doing more biology, less coding',
      author='Saurabh Shukla',
      author_email='sshukla4@illinois.edu',
      version=__version__,
      url='https://github.com/sshukla101/postmsm',
      packages=['postmsm'],
      install_requires=['msmbuilder','pytraj']
)
      
