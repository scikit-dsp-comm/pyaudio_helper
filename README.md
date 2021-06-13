# PyAudio Helper

## Dependencies for `pyaudio`

Across the three popular platforms, Windows, macOS, and Linux, `pyaudio`, is 
the underlying framework that `pyaudio_helper` relies upon. Getting `PyAudio` configured is  different for all three OS's. Conda and CondaForge have support for installing `pyaudio` 
on both Linux and Windows. Under Python 3.6 and below PyAudio will install when `pip` installing the scikit-dsp-comm package, as described below. For Python 3.7+ `PyAudio` **first** needs to be installed using `conda install pyaudio` to obtain binary (`whl`) files.

The real-time audio DSP capabilities of `pyaudio_helper` allow for two channel algorithm development with real-time user control enabled by the `ipywidgets` when running in the Jupyter notebook.

Finally, we now can utilize the real-time DSP capabilities of `pyaudio_helper` to work in combination with streaming of I/Q samples using new functions `rtlsdr_helper`. This allows in particular demodulation of radio signals and downsampling to baseband analog signals for streaming playback of say an FM broadcast station. This new capability is featured as a short *article* at the end of this readme file.

All the capability of the package is available less `PyAudio` and the RTL-SDR radio, without doing any special installations. See the [wiki pages](https://github.com/mwickert/SP-Comm-Tutorial-using-scikit-dsp-comm/wiki) for more information. Just keep in mind that now a Python 3.7+ install on windows must include the installation `PyAudio` as described above.

## Installation Notes

Part of the processing architecture makes use of `ipwidgets`. These can be installed for you by specifying the `extras` option:

```py
pip install pyaudio-helper[extras]
```

Installation is described in greater detail below.

1. `pyaudio_helper.py` wraps a class around the code required in `PyAudio` (wraps the C++ library `PortAudio`) to set up a non-blocking audio input/output stream. The user only has to write the callback function to implement real-time DSP processing using any of the input/output devices available on the platform. This resulting object also contains a capture buffer for use in post processing and a timing markers for assessing the processing time utilized by the callback function. When developing apps in the Jupyter Notebook there is support for the `IPywidgets` along with threading.

## Authors

[@mwickert](https://github.com/mwickert)

[@andrewsmitty](https://github.com/andrewsmitty)

