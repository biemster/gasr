#!/usr/bin/env python3
import sys
import ctypes

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

@ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_bool, ctypes.c_void_p)
def resultHandler(text, isFinal, instance):
    if isFinal:
        print(f'* {text.decode()}')
    else:
        print(f'* {text.decode()}', end='\r')


if __name__ == '__main__':
    config = SodaConfig(CHANNEL_COUNT, SAMPLE_RATE, b'./SODAModels/', resultHandler, None, b'api_key_dummy')
    handle = sodalib.CreateSodaAsync(config)

    try:
        while True:
            audio = sys.stdin.buffer.read(CHUNK_SIZE)
            sodalib.AddAudio(handle, audio, len(audio))
    except KeyboardInterrupt:
        print('Closing up')

    sodalib.DeleteSodaAsync(handle)