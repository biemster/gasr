#!/usr/bin/env python3
import sys
import ctypes
from soda_api_pb2 import ExtendedSodaConfigMsg, SodaResponse, SodaRecognitionResult

CHANNEL_COUNT = 1
SAMPLE_RATE = 16000
CHUNK_SIZE = 2048 # 2 chunks per frame, a frame is a single s16

CALLBACK = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_byte), ctypes.c_int, ctypes.c_void_p)
class SodaConfig(ctypes.Structure):
    _fields_ = [('soda_config', ctypes.c_char_p),
                ('soda_config_size', ctypes.c_int),
                ('callback', CALLBACK),
                ('callback_handle', ctypes.c_void_p)]


class SodaClient():
    def __init__(self, callback=None):
        self.sodalib = ctypes.CDLL('./libsoda.so')
        if callback == None:
            callback = CALLBACK(self.resultHandler)
        else:
            callback = CALLBACK(callback)
        cfg_proto = ExtendedSodaConfigMsg()
        cfg_proto.channel_count = CHANNEL_COUNT
        cfg_proto.sample_rate = SAMPLE_RATE
        cfg_proto.api_key = 'dummy_api_key'
        cfg_proto.language_pack_directory = './SODAModels/'
        cfg_serialized = cfg_proto.SerializeToString()
        self.config = SodaConfig(cfg_serialized, len(cfg_serialized), callback, None)
        self.sodalib.CreateExtendedSodaAsync.restype = ctypes.c_void_p
        
    def start(self):
        self.handle = ctypes.c_void_p(self.sodalib.CreateExtendedSodaAsync(self.config))
        self.sodalib.ExtendedSodaStart(self.handle)
        while True:
            audio = sys.stdin.buffer.read(CHUNK_SIZE)
            self.sodalib.ExtendedAddAudio(self.handle, audio, len(audio))

    def delete(self):
        self.sodalib.DeleteExtendedSodaAsync(self.handle)

    def resultHandler(self, response, rlen, instance):
        res = SodaResponse()
        res.ParseFromString(ctypes.string_at(response, rlen))
        if res.soda_type == SodaResponse.SodaMessageType.RECOGNITION:
            if res.recognition_result.result_type == SodaRecognitionResult.ResultType.FINAL:
                print(f'* {res.recognition_result.hypothesis[0]}')
            elif res.recognition_result.result_type == SodaRecognitionResult.ResultType.PARTIAL:
                print(f'* {res.recognition_result.hypothesis[0]}', end='\r')


if __name__ == '__main__':
    client = SodaClient()
    try:
        client.start()
    except KeyboardInterrupt:
        client.delete()
