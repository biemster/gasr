# gasr
Google Chrome SODA Offline Speech Recognition command line client

##### Intro:
This is a proof of concept how to write code against the libsoda library found in the Chrome browser, which uses it for Live Transcribe.
It's not a full application, but it will write out a live transcription to stdout of audio fed through stdin using for example ALSA or SoX.
SoX for real-time audio is actually not real-time enough, and results in a lot of warning messages about a lagging pipeline. Good
results are obtained with `ecasound`.

##### Prepare:
Get a copy of libsoda from Chrome for your platform by enabling Live Caption (Chrome 90+, or a canary build). It should be somewhere in
your profile directory then. Copy the shared library or DLL to the repo directory.

##### Compile:
```
make
```
or on Windows:
```
make mingw
```

##### Testrun using Google TTS [biemster/gtts](https://github.com/biemster/gtts):
Symlink `libchrometts.so` from the `gtts` repo directory here and run the following:
```
../gtts/gtts ../gtts/en-us/ "Full Text to Speech to Text pipeline!" | sox -tf32 -L -r22050 -c1 - -ts16 - | ./gasr --stream-delay
```
It should produce an output similar to this:
```
I1218 18:46:56.476600   31547 chrome_tts.cc:108] Init pipeline_path=./en-us/pipeline
I1218 18:46:56.476664   31547 tts_controller.cc:192] Reading ./en-us/pipeline as text file
I1218 18:46:56.479860   31547 data_source.cc:103] Opening data source "./en-us/acoustic_frame_config.pb" (as: FILE) ...
I1218 18:46:56.479903   31547 data_source.cc:110] ... Opened data source "./en-us/acoustic_frame_config.pb" of size 68
I1218 18:46:56.479978   31547 data_source.cc:103] Opening data source "./en-us/roman_numeral_android.far" (as: FILE) ...
I1218 18:46:56.479995   31547 data_source.cc:110] ... Opened data source "./en-us/roman_numeral_android.far" of size 2903
I1218 18:46:56.480014   31547 grm-manager.h:129] Loading FST archive from "./en-us/roman_numeral_android.far" ...
I1218 18:46:56.480142   31547 data_source.cc:103] Opening data source "./en-us/disambiguation_rules_en_us.pb" (as: FILE) ...
I1218 18:46:56.480160   31547 data_source.cc:110] ... Opened data source "./en-us/disambiguation_rules_en_us.pb" of size 311330
E1218 18:46:56.483696   31547 homograph_disambiguation_rules_data.cc:53] There are token-only rules for "ne" but there are also word-only rules for this key. The token rules will not be applied.
I1218 18:46:56.491837   31547 data_source.cc:103] Opening data source "./en-us/engine_config_en_us_x_greco_embedded_lstm.pb" (as: FILE) ...
I1218 18:46:56.492528   31547 data_source.cc:110] ... Opened data source "./en-us/engine_config_en_us_x_greco_embedded_lstm.pb" of size 446
I1218 18:46:56.492587   31547 data_source.cc:103] Opening data source "./en-us/mapping_grammar_en.far" (as: FILE) ...
I1218 18:46:56.492596   31547 data_source.cc:110] ... Opened data source "./en-us/mapping_grammar_en.far" of size 1071
I1218 18:46:56.492605   31547 grm-manager.h:129] Loading FST archive from "./en-us/mapping_grammar_en.far" ...
WARNING: Logging before InitGoogle() is written to STDERR
W1218 18:46:56.506150   31549 soda_async_impl.cc:231] Creating soda_impl
I1218 18:46:56.506286   31549 soda_impl.cc:275] Maximum audio history (ms): 30000
I1218 18:46:56.506309   31549 soda_impl.cc:304] Adding Resampler from 16000 to 16000
I1218 18:46:56.506430   31549 soda_impl.cc:482] Enabling power evaluator.
I1218 18:46:56.506439   31549 soda_impl.cc:492] Adding preamble processor.
I1218 18:46:56.506446   31549 soda_impl.cc:512] Enabling On Device ASR
I1218 18:46:56.506561   31549 terse_processor.cc:634] Config file: ./SODAModels/configs/ONDEVICE_MEDIUM_CONTINUOUS.config
I1218 18:46:56.506794   31549 terse_processor.cc:163] Loaded PipelineDef.
I1218 18:46:56.506808   31549 dir_path.cc:52] Checking FileExists: ./endtoendmodel/marble_rnnt_model.syms.compact
I1218 18:46:56.506825   31549 dir_path.cc:57] Not Found FileExists: ./endtoendmodel/marble_rnnt_model.syms.compact
I1218 18:46:56.506836   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/endtoendmodel/marble_rnnt_model.syms.compact
I1218 18:46:56.506846   31549 dir_path.cc:54] Found FileExists: ./SODAModels/endtoendmodel/marble_rnnt_model.syms.compact
I1218 18:46:56.506994   31549 dir_path.cc:52] Checking FileExists: ./endtoendmodel/marble_rnnt_dictation_frontend_params.mean_stddev
I1218 18:46:56.507004   31549 dir_path.cc:57] Not Found FileExists: ./endtoendmodel/marble_rnnt_dictation_frontend_params.mean_stddev
I1218 18:46:56.507016   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/endtoendmodel/marble_rnnt_dictation_frontend_params.mean_stddev
I1218 18:46:56.507021   31549 dir_path.cc:54] Found FileExists: ./SODAModels/endtoendmodel/marble_rnnt_dictation_frontend_params.mean_stddev
I1218 18:46:56.507073   31549 dir_path.cc:52] Checking FileExists: ./endtoendmodel/marble_rnnt_model.wpm.portable
I1218 18:46:56.507089   31549 dir_path.cc:57] Not Found FileExists: ./endtoendmodel/marble_rnnt_model.wpm.portable
I1218 18:46:56.507100   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/endtoendmodel/marble_rnnt_model.wpm.portable
I1218 18:46:56.507105   31549 dir_path.cc:54] Found FileExists: ./SODAModels/endtoendmodel/marble_rnnt_model.wpm.portable
I1218 18:46:56.509747   31549 dir_path.cc:52] Checking FileExists: ./endtoendmodel/marble_rnnt_model.word_classifier
I1218 18:46:56.509894   31549 dir_path.cc:57] Not Found FileExists: ./endtoendmodel/marble_rnnt_model.word_classifier
I1218 18:46:56.509897   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/endtoendmodel/marble_rnnt_model.word_classifier
I1218 18:46:56.509902   31549 dir_path.cc:54] Found FileExists: ./SODAModels/endtoendmodel/marble_rnnt_model.word_classifier
I1218 18:46:56.509955   31549 dir_path.cc:52] Checking FileExists: ./denorm/embedded_replace_annotated_punct_words_dash.mfar
I1218 18:46:56.509961   31549 dir_path.cc:57] Not Found FileExists: ./denorm/embedded_replace_annotated_punct_words_dash.mfar
I1218 18:46:56.509973   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/denorm/embedded_replace_annotated_punct_words_dash.mfar
I1218 18:46:56.509980   31549 dir_path.cc:54] Found FileExists: ./SODAModels/denorm/embedded_replace_annotated_punct_words_dash.mfar
I1218 18:46:56.510028   31549 dir_path.cc:52] Checking FileExists: ./denorm/embedded_fix_ampm.mfar
I1218 18:46:56.510044   31549 dir_path.cc:57] Not Found FileExists: ./denorm/embedded_fix_ampm.mfar
I1218 18:46:56.510056   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/denorm/embedded_fix_ampm.mfar
I1218 18:46:56.510061   31549 dir_path.cc:54] Found FileExists: ./SODAModels/denorm/embedded_fix_ampm.mfar
I1218 18:46:56.510093   31549 dir_path.cc:52] Checking FileExists: ./denorm/embedded_class_denorm.mfar
I1218 18:46:56.510108   31549 dir_path.cc:57] Not Found FileExists: ./denorm/embedded_class_denorm.mfar
I1218 18:46:56.510120   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/denorm/embedded_class_denorm.mfar
I1218 18:46:56.510126   31549 dir_path.cc:54] Found FileExists: ./SODAModels/denorm/embedded_class_denorm.mfar
I1218 18:46:56.510156   31549 dir_path.cc:52] Checking FileExists: ./denorm/embedded_normalizer.mfar
I1218 18:46:56.510162   31549 dir_path.cc:57] Not Found FileExists: ./denorm/embedded_normalizer.mfar
I1218 18:46:56.510166   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/denorm/embedded_normalizer.mfar
I1218 18:46:56.510172   31549 dir_path.cc:54] Found FileExists: ./SODAModels/denorm/embedded_normalizer.mfar
I1218 18:46:56.510219   31549 dir_path.cc:52] Checking FileExists: ./denorm/porn_normalizer_on_device.mfar
I1218 18:46:56.510226   31549 dir_path.cc:57] Not Found FileExists: ./denorm/porn_normalizer_on_device.mfar
I1218 18:46:56.510230   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/denorm/porn_normalizer_on_device.mfar
I1218 18:46:56.510235   31549 dir_path.cc:54] Found FileExists: ./SODAModels/denorm/porn_normalizer_on_device.mfar
I1218 18:46:56.510290   31549 dir_path.cc:52] Checking FileExists: ./acousticmodel/MARBLE_DICTATION_EP.endpointer_portable_lstm_model
I1218 18:46:56.510298   31549 dir_path.cc:57] Not Found FileExists: ./acousticmodel/MARBLE_DICTATION_EP.endpointer_portable_lstm_model
I1218 18:46:56.510302   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/acousticmodel/MARBLE_DICTATION_EP.endpointer_portable_lstm_model
I1218 18:46:56.510308   31549 dir_path.cc:54] Found FileExists: ./SODAModels/acousticmodel/MARBLE_DICTATION_EP.endpointer_portable_lstm_model
I1218 18:46:56.510312   31549 neural_network_resource.cc:71] Initializing for TENSORFLOW_LITE
I1218 18:46:56.510481   31549 dir_path.cc:52] Checking FileExists: ./acousticmodel/MARBLE_DICTATION_EP.endpointer_portable_lstm_mean_stddev
I1218 18:46:56.510489   31549 dir_path.cc:57] Not Found FileExists: ./acousticmodel/MARBLE_DICTATION_EP.endpointer_portable_lstm_mean_stddev
I1218 18:46:56.510493   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/acousticmodel/MARBLE_DICTATION_EP.endpointer_portable_lstm_mean_stddev
I1218 18:46:56.510499   31549 dir_path.cc:54] Found FileExists: ./SODAModels/acousticmodel/MARBLE_DICTATION_EP.endpointer_portable_lstm_mean_stddev
I1218 18:46:56.510521   31549 dir_path.cc:52] Checking FileExists: ./magic_mic/MARBLE_V2_acoustic_model.int8.tflite
I1218 18:46:56.510527   31549 dir_path.cc:57] Not Found FileExists: ./magic_mic/MARBLE_V2_acoustic_model.int8.tflite
I1218 18:46:56.510531   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/magic_mic/MARBLE_V2_acoustic_model.int8.tflite
I1218 18:46:56.510536   31549 dir_path.cc:54] Found FileExists: ./SODAModels/magic_mic/MARBLE_V2_acoustic_model.int8.tflite
I1218 18:46:56.510540   31549 neural_network_resource.cc:71] Initializing for TENSORFLOW_LITE
I1218 18:46:56.510677   31549 dir_path.cc:52] Checking FileExists: ./magic_mic/MARBLE_V2_acoustic_meanstddev_vector
I1218 18:46:56.510685   31549 dir_path.cc:57] Not Found FileExists: ./magic_mic/MARBLE_V2_acoustic_meanstddev_vector
I1218 18:46:56.510689   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/magic_mic/MARBLE_V2_acoustic_meanstddev_vector
I1218 18:46:56.510694   31549 dir_path.cc:54] Found FileExists: ./SODAModels/magic_mic/MARBLE_V2_acoustic_meanstddev_vector
I1218 18:46:56.510714   31549 dir_path.cc:52] Checking FileExists: ./magic_mic/MARBLE_V2_vocabulary.syms
I1218 18:46:56.510720   31549 dir_path.cc:57] Not Found FileExists: ./magic_mic/MARBLE_V2_vocabulary.syms
I1218 18:46:56.510732   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/magic_mic/MARBLE_V2_vocabulary.syms
I1218 18:46:56.510746   31549 dir_path.cc:54] Found FileExists: ./SODAModels/magic_mic/MARBLE_V2_vocabulary.syms
I1218 18:46:56.513907   31549 dir_path.cc:52] Checking FileExists: ./magic_mic/MARBLE_V2_model.int8.tflite
I1218 18:46:56.513918   31549 dir_path.cc:57] Not Found FileExists: ./magic_mic/MARBLE_V2_model.int8.tflite
I1218 18:46:56.513922   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/magic_mic/MARBLE_V2_model.int8.tflite
I1218 18:46:56.513928   31549 dir_path.cc:54] Found FileExists: ./SODAModels/magic_mic/MARBLE_V2_model.int8.tflite
I1218 18:46:56.515482   31549 dir_path.cc:52] Checking FileExists: ./endtoendmodel/marble_rnnt_model-encoder.part_0.tflite
I1218 18:46:56.515508   31549 dir_path.cc:57] Not Found FileExists: ./endtoendmodel/marble_rnnt_model-encoder.part_0.tflite
I1218 18:46:56.515512   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/endtoendmodel/marble_rnnt_model-encoder.part_0.tflite
I1218 18:46:56.515518   31549 dir_path.cc:54] Found FileExists: ./SODAModels/endtoendmodel/marble_rnnt_model-encoder.part_0.tflite
I1218 18:46:56.515524   31549 neural_network_resource.cc:71] Initializing for PLAIN_TENSORFLOW_LITE
I1218 18:46:56.521165   31549 dir_path.cc:52] Checking FileExists: ./endtoendmodel/marble_rnnt_model-encoder.part_1.tflite
I1218 18:46:56.521195   31549 dir_path.cc:57] Not Found FileExists: ./endtoendmodel/marble_rnnt_model-encoder.part_1.tflite
I1218 18:46:56.521209   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/endtoendmodel/marble_rnnt_model-encoder.part_1.tflite
I1218 18:46:56.521221   31549 dir_path.cc:54] Found FileExists: ./SODAModels/endtoendmodel/marble_rnnt_model-encoder.part_1.tflite
I1218 18:46:56.521228   31549 neural_network_resource.cc:71] Initializing for PLAIN_TENSORFLOW_LITE
I1218 18:46:56.539461   31549 dir_path.cc:52] Checking FileExists: ./endtoendmodel/marble_rnnt_model-rnnt.decoder.tflite
I1218 18:46:56.539494   31549 dir_path.cc:57] Not Found FileExists: ./endtoendmodel/marble_rnnt_model-rnnt.decoder.tflite
I1218 18:46:56.539498   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/endtoendmodel/marble_rnnt_model-rnnt.decoder.tflite
I1218 18:46:56.539506   31549 dir_path.cc:54] Found FileExists: ./SODAModels/endtoendmodel/marble_rnnt_model-rnnt.decoder.tflite
I1218 18:46:56.539511   31549 neural_network_resource.cc:71] Initializing for PLAIN_TENSORFLOW_LITE
I1218 18:46:56.544801   31549 dir_path.cc:52] Checking FileExists: ./endtoendmodel/marble_rnnt_model-rnnt.joint.tflite
I1218 18:46:56.544831   31549 dir_path.cc:57] Not Found FileExists: ./endtoendmodel/marble_rnnt_model-rnnt.joint.tflite
I1218 18:46:56.544837   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/endtoendmodel/marble_rnnt_model-rnnt.joint.tflite
I1218 18:46:56.544844   31549 dir_path.cc:54] Found FileExists: ./SODAModels/endtoendmodel/marble_rnnt_model-rnnt.joint.tflite
I1218 18:46:56.544849   31549 neural_network_resource.cc:71] Initializing for PLAIN_TENSORFLOW_LITE
I1218 18:46:56.546628   31549 dir_path.cc:52] Checking FileExists: ./voice_match/MARBLE_speakerid.tflite
I1218 18:46:56.546661   31549 dir_path.cc:57] Not Found FileExists: ./voice_match/MARBLE_speakerid.tflite
I1218 18:46:56.546665   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/voice_match/MARBLE_speakerid.tflite
I1218 18:46:56.546671   31549 dir_path.cc:54] Found FileExists: ./SODAModels/voice_match/MARBLE_speakerid.tflite
I1218 18:46:56.550709   31549 terse_processor.cc:173] Initialized ResourceManager.
I1218 18:46:56.550899   31549 terse_processor.cc:184] Initialized GoogleRecognizer.
I1218 18:46:56.550972   31549 context-module-factory.cc:35] ContextModuleFactory: Initializing ContextModule.
I1218 18:46:56.551114   31549 dir_path.cc:52] Checking FileExists: ./context_prebuilt/apps.txt
I1218 18:46:56.551138   31549 dir_path.cc:57] Not Found FileExists: ./context_prebuilt/apps.txt
I1218 18:46:56.551141   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/context_prebuilt/apps.txt
I1218 18:46:56.551152   31549 dir_path.cc:54] Found FileExists: ./SODAModels/context_prebuilt/apps.txt
I1218 18:46:56.551222   31549 dir_path.cc:52] Checking FileExists: ./context_prebuilt/en-US_android-auto_car_automation.action.union_STD_FST.fst
I1218 18:46:56.551229   31549 dir_path.cc:57] Not Found FileExists: ./context_prebuilt/en-US_android-auto_car_automation.action.union_STD_FST.fst
I1218 18:46:56.551232   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/context_prebuilt/en-US_android-auto_car_automation.action.union_STD_FST.fst
I1218 18:46:56.551237   31549 dir_path.cc:54] Found FileExists: ./SODAModels/context_prebuilt/en-US_android-auto_car_automation.action.union_STD_FST.fst
I1218 18:46:56.570781   31549 dir_path.cc:52] Checking FileExists: ./context_prebuilt/contacts.txt
I1218 18:46:56.570816   31549 dir_path.cc:57] Not Found FileExists: ./context_prebuilt/contacts.txt
I1218 18:46:56.570820   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/context_prebuilt/contacts.txt
I1218 18:46:56.570830   31549 dir_path.cc:54] Found FileExists: ./SODAModels/context_prebuilt/contacts.txt
I1218 18:46:56.570967   31549 dir_path.cc:52] Checking FileExists: ./context_prebuilt/songs.txt
I1218 18:46:56.570984   31549 dir_path.cc:57] Not Found FileExists: ./context_prebuilt/songs.txt
I1218 18:46:56.570987   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/context_prebuilt/songs.txt
I1218 18:46:56.570991   31549 dir_path.cc:54] Found FileExists: ./SODAModels/context_prebuilt/songs.txt
I1218 18:46:56.571015   31549 dir_path.cc:52] Checking FileExists: ./context_prebuilt/en-US_android-auto_top_radio_station_frequencies_STD_FST.fst
I1218 18:46:56.571030   31549 dir_path.cc:57] Not Found FileExists: ./context_prebuilt/en-US_android-auto_top_radio_station_frequencies_STD_FST.fst
I1218 18:46:56.571042   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/context_prebuilt/en-US_android-auto_top_radio_station_frequencies_STD_FST.fst
I1218 18:46:56.571047   31549 dir_path.cc:54] Found FileExists: ./SODAModels/context_prebuilt/en-US_android-auto_top_radio_station_frequencies_STD_FST.fst
I1218 18:46:56.571117   31549 dir_path.cc:52] Checking FileExists: ./context_prebuilt/en-US_android-auto_manual_fixes_STD_FST.fst
I1218 18:46:56.571124   31549 dir_path.cc:57] Not Found FileExists: ./context_prebuilt/en-US_android-auto_manual_fixes_STD_FST.fst
I1218 18:46:56.571135   31549 dir_path.cc:52] Checking FileExists: ./SODAModels/context_prebuilt/en-US_android-auto_manual_fixes_STD_FST.fst
I1218 18:46:56.571140   31549 dir_path.cc:54] Found FileExists: ./SODAModels/context_prebuilt/en-US_android-auto_manual_fixes_STD_FST.fst
W1218 18:46:56.571333   31549 terse_processor.cc:242] TISID disabled.
I1218 18:46:56.571341   31549 terse_processor.cc:718] Domain: CAPTION
I1218 18:46:56.571730   31549 context-module-impl.cc:244] ContextModule starts to provide model resources: 2020-12-18T18:46:56.571730087+01:00
I1218 18:46:56.572394   31549 context-module-impl.cc:281] ContextModule finished providing model resources : 2020-12-18T18:46:56.572394328+01:00 elapsed: 664.241us
I1218 18:46:56.576062   31549 terse_processor.cc:1293] Resetting Terse Processor
I1218 18:46:56.576084   31549 terse_processor.cc:838] Cancelling session.
I1218 18:46:56.578963   31549 terse_processor.cc:755] Setup completed
I1218 18:46:56.579003   31549 soda_impl.cc:558] Server ASR Disabled
I1218 18:46:56.579008   31549 soda_impl.cc:606] Initializing audio logger
W1218 18:46:56.579031   31549 soda_async_impl.cc:390] Soda session starting (require_hotword:0, hotword_timeout_in_millis:0)
I1218 18:46:56.579047   31549 soda_async_impl.cc:577] Session parameters updated. Reconfiguring SODA.
I1218 18:46:56.695091   31547 data_source.cc:103] Opening data source "./en-us/feats_android.far" (as: FILE) ...
I1218 18:46:56.695129   31547 data_source.cc:110] ... Opened data source "./en-us/feats_android.far" of size 950
I1218 18:46:56.695157   31547 grm-manager.h:129] Loading FST archive from "./en-us/feats_android.far" ...
I1218 18:46:56.695260   31547 data_source.cc:103] Opening data source "./en-us/lstm_dur_model.tflite" (as: MEMORY) ...
I1218 18:46:56.695280   31547 data_source.cc:110] ... Opened data source "./en-us/lstm_dur_model.tflite" of size 184960
I1218 18:46:56.695285   31547 lstm_model_load.cc:86] Loading memory mapped tflite model.
I1218 18:46:56.695417   31547 data_source.cc:103] Opening data source "./en-us/lstm_dur_model_input_mean_std_dev" (as: FILE) ...
I1218 18:46:56.695430   31547 data_source.cc:110] ... Opened data source "./en-us/lstm_dur_model_input_mean_std_dev" of size 2574
I1218 18:46:56.695465   31547 data_source.cc:103] Opening data source "./en-us/lstm_dur_model_output_mean_std_dev" (as: FILE) ...
I1218 18:46:56.695473   31547 data_source.cc:110] ... Opened data source "./en-us/lstm_dur_model_output_mean_std_dev" of size 12
I1218 18:46:56.695500   31547 data_source.cc:103] Opening data source "./en-us/lstm_speech_model.tflite" (as: MEMORY) ...
I1218 18:46:56.695514   31547 data_source.cc:110] ... Opened data source "./en-us/lstm_speech_model.tflite" of size 371072
I1218 18:46:56.695518   31547 lstm_model_load.cc:86] Loading memory mapped tflite model.
I1218 18:46:56.695629   31547 data_source.cc:103] Opening data source "./en-us/lstm_speech_model_input_mean_std_dev" (as: FILE) ...
I1218 18:46:56.695639   31547 data_source.cc:110] ... Opened data source "./en-us/lstm_speech_model_input_mean_std_dev" of size 2606
I1218 18:46:56.695657   31547 data_source.cc:103] Opening data source "./en-us/lstm_speech_model_output_mean_std_dev" (as: FILE) ...
I1218 18:46:56.695673   31547 data_source.cc:110] ... Opened data source "./en-us/lstm_speech_model_output_mean_std_dev" of size 1574
I1218 18:46:56.695710   31547 data_source.cc:103] Opening data source "./en-us/morphosyntactic_mapping.pb" (as: FILE) ...
I1218 18:46:56.695727   31547 data_source.cc:110] ... Opened data source "./en-us/morphosyntactic_mapping.pb" of size 6
I1218 18:46:56.695831   31547 data_source.cc:103] Opening data source "./en-us/resource.pb" (as: FILE) ...
I1218 18:46:56.695840   31547 data_source.cc:110] ... Opened data source "./en-us/resource.pb" of size 399460
I1218 18:46:56.697087   31547 parametric_playback.cc:47] Loaded playback info: 26
I1218 18:46:56.697222   31547 data_source.cc:103] Opening data source "./en-us/en_us_phonology.pb" (as: FILE) ...
I1218 18:46:56.697314   31547 data_source.cc:110] ... Opened data source "./en-us/en_us_phonology.pb" of size 3034
W1218 18:46:56.697496   31547 phonology.cc:79] Phonemes ax, er have non-distinctive features.
W1218 18:46:56.697504   31547 phonology.cc:79] Phonemes l, r have non-distinctive features.
I1218 18:46:56.697675   31547 data_source.cc:103] Opening data source "./en-us/en_morphology" (as: FILE) ...
I1218 18:46:56.697693   31547 data_source.cc:110] ... Opened data source "./en-us/en_morphology" of size 2753822
I1218 18:46:56.699361   31547 model-api.cc:45] Registered model under key morphology
I1218 18:46:56.700778   31547 data_source.cc:103] Opening data source "./en-us/compressed_lexicon_en_us.blex" (as: MEMORY) ...
I1218 18:46:56.700815   31547 data_source.cc:110] ... Opened data source "./en-us/compressed_lexicon_en_us.blex" of size 4931028
I1218 18:46:56.700959   31547 data_source.cc:103] Opening data source "./en-us/ipa_to_tts_to-en_us.far" (as: FILE) ...
I1218 18:46:56.700973   31547 data_source.cc:110] ... Opened data source "./en-us/ipa_to_tts_to-en_us.far" of size 27848
I1218 18:46:56.700988   31547 grm-manager.h:129] Loading FST archive from "./en-us/ipa_to_tts_to-en_us.far" ...
I1218 18:46:56.701132   31547 data_source.cc:103] Opening data source "./en-us/g2p_m3_syls0_stress0_en-US.fst" (as: FILE) ...
I1218 18:46:56.701143   31547 data_source.cc:110] ... Opened data source "./en-us/g2p_m3_syls0_stress0_en-US.fst" of size 702096
I1218 18:46:56.701155   31547 compact_fst.cc:19] Loading FST from "./en-us/g2p_m3_syls0_stress0_en-US.fst" ...
I1218 18:46:56.715819   31547 decoder.cc:57] G2P FST loaded (52 graphemes and 41 phonemes).
I1218 18:46:56.718214   31547 data_source.cc:103] Opening data source "./en-us/compressed_lexicon_en_us.blex" (as: MEMORY) ...
I1218 18:46:56.718274   31547 data_source.cc:110] ... Opened data source "./en-us/compressed_lexicon_en_us.blex" of size 4931028
I1218 18:46:56.718411   31547 data_source.cc:103] Opening data source "./en-us/homographs_model_en_us_embedded.pb" (as: FILE) ...
I1218 18:46:56.718431   31547 data_source.cc:110] ... Opened data source "./en-us/homographs_model_en_us_embedded.pb" of size 236059
I1218 18:46:56.723177   31547 data_source.cc:103] Opening data source "./en-us/feature_set.pb" (as: FILE) ...
I1218 18:46:56.723210   31547 data_source.cc:110] ... Opened data source "./en-us/feature_set.pb" of size 4128
I1218 18:46:56.723429   31547 data_source.cc:103] Opening data source "./en-us/converter_en_us_android.far" (as: FILE) ...
I1218 18:46:56.723448   31547 data_source.cc:110] ... Opened data source "./en-us/converter_en_us_android.far" of size 1825
I1218 18:46:56.723461   31547 grm-manager.h:129] Loading FST archive from "./en-us/converter_en_us_android.far" ...
I1218 18:46:56.723551   31547 data_source.cc:103] Opening data source "./en-us/roman_numeral_contexts.pb" (as: FILE) ...
I1218 18:46:56.723560   31547 data_source.cc:110] ... Opened data source "./en-us/roman_numeral_contexts.pb" of size 9136
I1218 18:46:56.723831   31547 data_source.cc:103] Opening data source "./en-us/sb_model.pb" (as: FILE) ...
I1218 18:46:56.723842   31547 data_source.cc:110] ... Opened data source "./en-us/sb_model.pb" of size 126111
I1218 18:46:56.726081   31547 data_source.cc:103] Opening data source "./en-us/en_verbalize_spec.pb" (as: FILE) ...
I1218 18:46:56.726112   31547 data_source.cc:110] ... Opened data source "./en-us/en_verbalize_spec.pb" of size 3723
I1218 18:46:56.726197   31547 data_source.cc:103] Opening data source "./en-us/textnorm_params_en_us.pb" (as: FILE) ...
I1218 18:46:56.726207   31547 data_source.cc:110] ... Opened data source "./en-us/textnorm_params_en_us.pb" of size 737
I1218 18:46:56.726238   31547 data_source.cc:103] Opening data source "./en-us/tokenize_and_classify_embedded_us_android.far" (as: FILE) ...
I1218 18:46:56.726246   31547 data_source.cc:110] ... Opened data source "./en-us/tokenize_and_classify_embedded_us_android.far" of size 2428079
I1218 18:46:56.726255   31547 grm-manager.h:129] Loading FST archive from "./en-us/tokenize_and_classify_embedded_us_android.far" ...
I1218 18:46:56.735716   31547 data_source.cc:103] Opening data source "./en-us/model_farm32.pb" (as: FILE) ...
I1218 18:46:56.735754   31547 data_source.cc:110] ... Opened data source "./en-us/model_farm32.pb" of size 400016
I1218 18:46:56.782095   31547 ranker.cc:117] LinearLseqRanker: using FarmHash32
I1218 18:46:56.782137   31547 data_source.cc:103] Opening data source "./en-us/variant_overrides_us.pb" (as: FILE) ...
I1218 18:46:56.782183   31547 data_source.cc:110] ... Opened data source "./en-us/variant_overrides_us.pb" of size 122
I1218 18:46:56.782250   31547 data_source.cc:103] Opening data source "./en-us/variant_selection_model_en_us_embedded.pb" (as: FILE) ...
I1218 18:46:56.782258   31547 data_source.cc:110] ... Opened data source "./en-us/variant_selection_model_en_us_embedded.pb" of size 370215
I1218 18:46:56.793109   31547 select_variants.cc:83] Word with override has only one variant: can_nou
I1218 18:46:56.793159   31547 data_source.cc:103] Opening data source "./en-us/us_verbalization_capabilities.pb" (as: FILE) ...
I1218 18:46:56.793181   31547 data_source.cc:110] ... Opened data source "./en-us/us_verbalization_capabilities.pb" of size 4669
I1218 18:46:56.793315   31547 data_source.cc:103] Opening data source "./en-us/verbalize_embedded_android.far" (as: FILE) ...
I1218 18:46:56.793334   31547 data_source.cc:110] ... Opened data source "./en-us/verbalize_embedded_android.far" of size 1624335
I1218 18:46:56.793345   31547 grm-manager.h:129] Loading FST archive from "./en-us/verbalize_embedded_android.far" ...
I1218 18:46:56.796072   31547 data_source.cc:103] Opening data source "./en-us/speech_morphing_palette.pb" (as: FILE) ...
I1218 18:46:56.796089   31547 data_source.cc:110] ... Opened data source "./en-us/speech_morphing_palette.pb" of size 41268
I1218 18:46:56.806077   31547 voice_params_resource.cc:31] Voice information: description: "embedded_lstm voice with embedded textnorm for en_us (speaker sfg; sample rate 22050)"
language: "en"
region: "us"
speaker: "sfg"
gender: "female"
quality: "normal"
sample_rate: 22050
server_voice_name: "sfg-greco-embedded-zeong"
supports_set_sample_rate: true
multi_speaker: false
voice_platform: EMBEDDED_LSTM

I1218 18:46:56.806117   31547 data_source.cc:103] Opening data source "./en-us/regexp_rewrite.pb" (as: FILE) ...
I1218 18:46:56.806130   31547 data_source.cc:110] ... Opened data source "./en-us/regexp_rewrite.pb" of size 4863
I1218 18:46:56.806196   31547 data_source.cc:103] Opening data source "./en-us/punctuation.pb" (as: FILE) ...
I1218 18:46:56.806208   31547 data_source.cc:110] ... Opened data source "./en-us/punctuation.pb" of size 297
I1218 18:46:56.843344   31547 data_source.cc:103] Opening data source "./en-us/xsampa_to_tts_to-en_us.far" (as: FILE) ...
I1218 18:46:56.843383   31547 data_source.cc:110] ... Opened data source "./en-us/xsampa_to_tts_to-en_us.far" of size 5136
I1218 18:46:56.843413   31547 grm-manager.h:129] Loading FST archive from "./en-us/xsampa_to_tts_to-en_us.far" ...
I1218 18:46:56.843493   31547 local_pipeline_runner.cc:115] Done loading all resources from: {./en-us/}
I1218 18:46:56.865037   31550 terse_processor.cc:1199] No terse session, starting a new one on input audio.
I1218 18:46:56.865155   31550 context-module-impl.cc:244] ContextModule starts to provide model resources: 2020-12-18T18:46:56.865155261+01:00
I1218 18:46:56.865224   31550 context-module-impl.cc:281] ContextModule finished providing model resources : 2020-12-18T18:46:56.865224371+01:00 elapsed: 69.11us
I1218 18:46:56.903899   31547 chrome_tts.cc:134] Shutting down
>>> full
>>> full text
>>> full text
>>> full text to
>>> full text to spe
>>> full text to speech
>>> full text to speech
>>> full text to speech to
>>> full text to speech to text
>>> full text to speech to text
>>> full text to speech to text
>>> full text to speech to text pip
>>> full text to speech to text pipel
>>> full text to speech to text pipeline
I1218 18:46:57.910340   31550 terse_processor.cc:1293] Resetting Terse Processor
I1218 18:46:57.910382   31550 terse_processor.cc:838] Cancelling session.
W1218 18:46:57.910688   31580 portable_intended_query_stream.cc:234] Exiting due to stream cancellation.
W1218 18:46:57.911648   31550 decoder_endpointer_stream.cc:35] Acoustic ep reader thread cancelled.
W1218 18:46:57.912300   31550 soda_async_impl.cc:765] Soda session stopped due to: STOP_CALLED
I1218 18:46:57.912334   31551 recognition_event_delegate.cc:37] Soda session stopped due to: STOP_CALLED
W1218 18:46:57.925960   31549 soda_async_impl.cc:793] Deleting soda_impl

```
There is also a French model available:
```
../gtts/gtts ../gtts/fr-fr1/ "Texte intégral de la parole au pipeline de texte!" | sox -tf32 -L -r22050 -c1 - -ts16 - | ./gasr --stream-delay
```
which gives just as impressive results:
```
I1218 18:50:34.835950   32078 terse_processor.cc:718] Domain: CAPTION
I1218 18:50:34.836489   32078 context-module-impl.cc:244] ContextModule starts to provide model resources: 2020-12-18T18:50:34.836489043+01:00
I1218 18:50:34.837275   32078 context-module-impl.cc:281] ContextModule finished providing model resources : 2020-12-18T18:50:34.837275013+01:00 elapsed: 785.97us
I1218 18:50:35.178336   32078 terse_processor.cc:1293] Resetting Terse Processor
I1218 18:50:35.178368   32078 terse_processor.cc:838] Cancelling session.
W1218 18:50:35.178920   32078 decoder_endpointer_stream.cc:35] Acoustic ep reader thread cancelled.
I1218 18:50:35.179139   32078 terse_processor.cc:755] Setup completed
I1218 18:50:35.179162   32078 soda_impl.cc:558] Server ASR Disabled
I1218 18:50:35.179169   32078 soda_impl.cc:606] Initializing audio logger
W1218 18:50:35.179186   32078 soda_async_impl.cc:390] Soda session starting (require_hotword:0, hotword_timeout_in_millis:0)
I1218 18:50:35.179196   32078 soda_async_impl.cc:577] Session parameters updated. Reconfiguring SODA.
W1218 18:50:35.179385   32079 lag_detector.cc:30] Pipeline lagging by 1476 ms. Continue processing samples.
I1218 18:50:35.179451   32079 terse_processor.cc:1199] No terse session, starting a new one on input audio.
I1218 18:50:35.179534   32079 context-module-impl.cc:244] ContextModule starts to provide model resources: 2020-12-18T18:50:35.179534314+01:00
I1218 18:50:35.179597   32079 context-module-impl.cc:281] ContextModule finished providing model resources : 2020-12-18T18:50:35.179596955+01:00 elapsed: 62.641us
W1218 18:50:35.239753   32079 lag_detector.cc:30] Pipeline lagging by 1336 ms. Continue processing samples.
W1218 18:50:35.300031   32079 lag_detector.cc:30] Pipeline lagging by 1196 ms. Continue processing samples.
W1218 18:50:35.360346   32079 lag_detector.cc:30] Pipeline lagging by 1057 ms. Continue processing samples.
W1218 18:50:35.420614   32079 lag_detector.cc:30] Pipeline lagging by 917 ms. Continue processing samples.
I1218 18:50:35.626037   32076 chrome_tts.cc:134] Shutting down
>>> texte
>>> texte
>>> texte int
>>> texte int
>>> texte intég
>>> texte intég
>>> texte intégra
>>> texte intégra
>>> texte intégral
>>> texte intégral
>>> texte intégral
>>> texte intégral de
>>> texte intégral de
>>> texte intégral de
>>> texte intégral de
>>> texte intégral de
>>> texte intégral de la
>>> texte intégral de la
>>> texte intégral de la paro
>>> texte intégral de la parole
>>> texte intégral de la parole
>>> texte intégral de la parole
>>> texte intégral de la parole au
>>> texte intégral de la parole au
>>> texte intégral de la parole au
>>> texte intégral de la parole au
>>> texte intégral de la parole au pa
>>> texte intégral de la parole au pip
>>> texte intégral de la parole au pip
>>> texte intégral de la parole au pipeline
>>> texte intégral de la parole au pipeline
>>> texte intégral de la parole au pipeline
>>> texte intégral de la parole au pipeline
>>> texte intégral de la parole au pipeline de
>>> texte intégral de la parole au pipeline de
>>> texte intégral de la parole au pipeline de
>>> texte intégral de la parole au pipeline de texte
>>> texte intégral de la parole au pipeline de texte
>>> texte intégral de la parole au pipeline de texte
I1218 18:50:36.708943   32079 terse_processor.cc:1293] Resetting Terse Processor
I1218 18:50:36.708986   32079 terse_processor.cc:838] Cancelling session.
W1218 18:50:36.709852   32079 decoder_endpointer_stream.cc:35] Acoustic ep reader thread cancelled.
W1218 18:50:36.711074   32079 soda_async_impl.cc:765] Soda session stopped due to: STOP_CALLED
I1218 18:50:36.711110   32080 recognition_event_delegate.cc:37] Soda session stopped due to: STOP_CALLED
W1218 18:50:36.725131   32078 soda_async_impl.cc:793] Deleting soda_impl
```

##### Run:
```
ecasound -f:16,1,16000 -i alsa -o:stdout | ./gasr 2>/dev/null
```
Remove `2>/dev/null` to see the debug output.

There is also a Python wrapper now (gasr.py, put that, and libsoda.so in the working directory):
```
#!/usr/bin/env python3
from gasr import SodaClient

def callback(text, isFinal, handle): print(isFinal, f'got {text}')

client = SodaClient(callback)
client.start()
```
