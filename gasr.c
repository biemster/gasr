#include <iostream>
#include <vector>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

#define CHANNEL_COUNT 1
#define SAMPLE_RATE 16000
#define CHUNK_SIZE 2048 // 2 chunks per frame, a frame is a single s16


#ifdef __cplusplus
extern "C" {
#endif
typedef void (*RecognitionResultHandler)(const char*, const bool, void*);

typedef struct {
	// The channel count and sample rate of the audio stream. SODA does not
	// support changing these values mid-stream, so a new SODA instance must be
	// created if these values change.
	int channel_count;
	int sample_rate;

	// The fully-qualified path to the language pack.
	const char* language_pack_directory;

	// The callback that gets executed on a recognition event. It takes in a
	// char*, representing the transcribed text; a bool, representing whether the
	// result is final or not; and a void* pointer to the SodaRecognizerImpl
	// instance associated with the stream.
	RecognitionResultHandler callback;

	// A void pointer to the SodaRecognizerImpl instance associated with the
	// stream.
	void* callback_handle;

	const char* api_key;
} SodaConfig;

// Creates and instantiates an instance of SODA.
extern void* CreateSodaAsync(SodaConfig config);

// Destroys the instance of SODA, called on the destruction of the SodaClient.
extern void DeleteSodaAsync(void* soda_async_handle);

// Feeds raw audio to SODA in the form of a contiguous stream of characters.
extern void AddAudio(void* soda_async_handle, const char* audio_buffer, int audio_buffer_size);
#ifdef __cplusplus
}
#endif

void resultHandler(const char* text, const bool isFinal, void* instance) {
	std::cout << "* " << text << (isFinal ? '\n' : '\r') << std::flush;
	
	if(!strncmp(text,"stop",4) && isFinal) {
		exit(0);
	}
}


int main(int argc, char *argv[]) {
	bool add_stream_delay = false;
	if(argc == 2 && !strncmp(argv[1], "--stream-delay", strlen("--stream-delay"))) {
		add_stream_delay = true;
	}

	SodaConfig config = {CHANNEL_COUNT, SAMPLE_RATE, "./SODAModels/", resultHandler, nullptr, "api_key_dummy"};
	void* handle = CreateSodaAsync(config);

#ifdef __MINGW32__
	setmode(fileno(stdin), O_BINARY);
#else
	freopen(nullptr, "rb", stdin);
#endif

	char audio[CHUNK_SIZE] = {};
	size_t len = 0;
	while((len = fread(audio, sizeof(audio[0]), CHUNK_SIZE, stdin)) > 0) {
		AddAudio(handle, audio, len);
		if(add_stream_delay) {
			// Sleep for 20ms to simulate real-time audio. SODA requires audio streaming in order to return events.
			usleep(20000);
		}
	}

	DeleteSodaAsync(handle);

	return 0;
}
