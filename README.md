# pyaudio-helper

[![Docs](https://readthedocs.org/projects/pyaudio-helper/badge/?version=latest)](http://pyaudio-helper.readthedocs.io/en/latest/?badge=latest)

[![pypi](https://img.shields.io/pypi/v/pyaudio-helper.svg)](https://pypi.python.org/pypi/pyaudio-helper)
[![travis](https://travis-ci.com/scikit-dsp-comm/pyaudio_helper.svg?branch=master)](https://travis-ci.com/github/scikit-dsp-comm/pyaudio_helper)

### Dependencies for `pyaudio`

Across the three popular platforms, Windows, macOS, and Linux, `pyaudio`, is 
the underlying framework that `pyaudio_helper` relies upon. Getting `PyAudio` configured is  different for all three OS's. Conda and CondaForge have support for installing `pyaudio` 
on both Linux and Windows. Under Python 3.6 and below PyAudio will install when `pip` installing the scikit-dsp-comm package, as described below. For Python 3.7+ `PyAudio` **first** needs to be installed using `conda install pyaudio` to obtain binary (`whl`) files.

All the capability of the package is available less `PyAudio` and the RTL-SDR radio, without doing any special installations. See the [wiki pages](https://github.com/mwickert/SP-Comm-Tutorial-using-scikit-dsp-comm/wiki) for more information. Just keep in mind that now a Python 3.7+ install on windows must include the installation `PyAudio` as described above.

## Authors

[@mwickert](https://github.com/mwickert)

[@andrewsmitty](https://github.com/andrewsmitty)
