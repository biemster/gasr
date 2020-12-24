#!/usr/bin/env python3
import sys
import ctypes
import time

CHANNEL_COUNT = 1
SAMPLE_RATE = 16000
CHUNK_SIZE = 2048 # 2 chunks per frame, a frame is a single s16

class SodaConfig(ctypes.Structure):
    _fields_ = [('channel_count', ctypes.c_int),
                ('sample_rate', ctypes.c_int),
                ('language_pack_directory', ctypes.c_char_p),
                ('callback', ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_bool, ctypes.c_void_p)),
                ('callback_handle', ctypes.c_void_p),
                ('api_key', ctypes.c_char_p)]

sodalib = ctypes.CDLL('./libsoda.so')
is_stop_called = False

@ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_bool, ctypes.c_void_p)
def resultHandler(text, isFinal, instance):
    print(isFinal, text)

    if isFinal and text == 'stop':
        is_stop_called = True


if __name__ == '__main__':
    config = SodaConfig(CHANNEL_COUNT, SAMPLE_RATE, b'./SODAModels/', resultHandler, None, b'api_key_dummy')
    handle = sodalib.CreateSodaAsync(config)

    while not is_stop_called:
        audio = sys.stdin.buffer.read(CHUNK_SIZE)
        sodalib.AddAudio(handle, audio, CHUNK_SIZE //2)

    sodalib.DeleteSodaAsync(handle)