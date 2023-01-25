#include <iostream>
#include <fstream>

#include "soda_api.pb.h"

#define CHANNEL_COUNT (1)
#define SAMPLE_RATE (16000)
#define CHUNK_SIZE 2048 // 2 chunks per frame, a frame is a single s16
#define API_KEY "dummy_api_key"
#define LANG_PACK "./SODAModels/"


typedef void (*RecognitionResultHandler)(char *, int, void *);

struct SodaConfig {
    const char *soda_config;
    int soda_config_size;
    RecognitionResultHandler callback;
    void *callback_handle;
};

extern "C" {

extern void *CreateExtendedSodaAsync(SodaConfig config);

extern void ExtendedSodaStart(void *soda_async_handle);

extern void DeleteExtendedSodaAsync(void *soda_async_handle);

extern void ExtendedAddAudio(void *soda_async_handle, const char *audio_buffer, int audio_buffer_size);
extern void ExtendedSodaMarkDone(void *soda_async_handle);
}

using namespace speech::soda::chrome;

class SodaClient {
public:
    std::string cfg_serialized;
    SodaConfig config;
    void *handle = nullptr;

    SodaClient(RecognitionResultHandler cb) {
        ExtendedSodaConfigMsg cfg_proto;
        cfg_proto.set_channel_count(CHANNEL_COUNT);
        cfg_proto.set_sample_rate(SAMPLE_RATE);
        cfg_proto.set_api_key(API_KEY);
        cfg_proto.set_language_pack_directory(LANG_PACK);
        cfg_serialized = cfg_proto.SerializeAsString();
        config.soda_config = cfg_serialized.c_str();
        config.soda_config_size = cfg_serialized.length();
        config.callback = cb;
        config.callback_handle = nullptr;
        handle = CreateExtendedSodaAsync(config);
    }

    void start() {
        ExtendedSodaStart(handle);
    }

    void addAudio(char *audio, int len) {
        ExtendedAddAudio(handle, audio, len);
    }

    void markDone() {
        ExtendedSodaMarkDone(handle);
    }

    ~SodaClient() {
        DeleteExtendedSodaAsync(handle);
    }


};

bool final = false;

static void resultHandler(char *response, int rlen, void *instance) {
    SodaResponse res;
    res.ParseFromString(std::string(response, rlen));
    if (res.soda_type() == SodaResponse::RECOGNITION) {
        if (res.recognition_result().result_type() == SodaRecognitionResult::FINAL) {
            std::cout << res.recognition_result().hypothesis()[0] << std::endl;
            final = true;
        }
    }
}

int main(int argc, char *argv[]) {

    SodaClient client(resultHandler);
    final = false;
    client.start();

    char audio[CHUNK_SIZE] = {};
    int audio_len = 0;

    std::ifstream f;
    f.open("a.bin", std::ios_base::in);
    if (f.is_open()) {
        while ((audio_len = f.readsome(audio, CHUNK_SIZE)) > 0) {
            client.addAudio(audio, audio_len);
        }
    }
    client.markDone();
    while (!final) {
    }
    return 0;
}
