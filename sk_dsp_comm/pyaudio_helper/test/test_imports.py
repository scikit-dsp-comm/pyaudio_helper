from unittest import TestCase


class TestImports(TestCase):
    _multiprocess_can_split_ = True

    def test_pyaudio_helper_from(self):
        from sk_dsp_comm.pyaudio_helper import pyaudio_helper

    def test_pyaudio_helper_import(self):
        import sk_dsp_comm.pyaudio_helper.pyaudio_helper
