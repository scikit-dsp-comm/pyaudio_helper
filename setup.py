from setuptools import setup
import os
import codecs

here = os.path.abspath(os.path.dirname(__file__))


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return codecs.open(fpath(fname), encoding='utf-8').read()


requirements = read(fpath('requirements.txt'))

with open("README.md", "r") as fh:
    long_description = fh.read()

about = {}
with codecs.open(os.path.join(here, 'pyaudio_helper', '__version__.py'), encoding='utf-8') as f:
    exec(f.read(), about)

setup(name='pyaudio-helper',
      version=about['__version__'],
      description='PyAudio Helper',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Mark Wickert',
      author_email='mwickert@uccs.edu',
      url='https://github.com/scikit-dsp-comm/pyaudio_helper',
      package_dir={'pyaudio_helper': 'pyaudio_helper'},
      packages=['pyaudio_helper'],
      include_package_data=True,
      license='BSD',
      install_requires=requirements.split(),
      python_requires='>=3.5',
     )
