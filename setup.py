from distutils.core import setup
from setuptools import find_packages

#############################
# avoid ModuleNotFoundError: No module named 'pip.req'
# from: https://stackoverflow.com/questions/21823649/how-to-upload-image-through-python-eve-to-some-external-storage-server-e-g-s3
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements
#############################

install_reqs = parse_requirements('requirements.txt', session=False)
reqs = [str(ir.req) for ir in install_reqs]

setup(name='eve-s3storage',
      version='0.1',
      description='python-eve S3 MediaStorage extension',
      author='Gabriel Wainer',
      author_email='gabrielcw@gmail.com',
      packages=find_packages(),
      install_requires=reqs,
      include_package_data=True,
      zip_safe=False,
      url='https://github.com/ebadia/eve-s3storage',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ],
      )
