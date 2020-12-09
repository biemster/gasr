#include <iostream>
#include <fstream>
#include <vector>
#include <string.h>
#include <unistd.h>

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


using namespace std;

void resultHandler(const char* text, const bool isFinal, void* instance) {
	cout << (isFinal ? "final: " : "") << text << endl;
}

int main(int argc, char *argv[]) {
	SodaConfig config = {1, 16000, "./SODAModels/", resultHandler, nullptr, "api_key_dummy"};
	void* handle = CreateSodaAsync(config);

	ifstream stream("whatstheweatherlike.wav", ios::in | ios::binary);
	vector<char> audio((istreambuf_iterator<char>(stream)), istreambuf_iterator<char>());
	int data_start = 42;
	int data_len = *(int*)&audio[data_start -2];
	if(string(&audio[data_start -6], 4) == "data" && data_len < audio.size()) {
		AddAudio(handle, &audio[data_start], data_len);
		sleep(3); // give everything some time to do their thing
	}
	else {
		cout << "Error reading wav file" << endl;
	}

	DeleteSodaAsync(handle);

	return 0;
}
