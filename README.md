# gasr
Google Chrome SODA Offline Speech Recognition command line client

##### Intro:
This is a proof of concept how to write code against the libsoda library found in the Chrome browser, which uses it for Live Transcribe.
It's not a full application, but it will write out a live transcription to stdout of audio fed through stdin using for example ALSA or SoX.
SoX for real-time audio is actually not real-time enough, and results in a lot of warning messages about a lagging pipeline. Good
results are obtained with `ecasound`.

##### Prepare:
Get a copy of libsoda from Chrome for your platform. At the time of this writing only Windows and OSX libraries are available,
I'm still waiting for the Linux version to be available. The windows library is actually usable for the time being,
by cross compiling using mingw (make target included), and running the client through `wine`.

##### Compile:
```
make
```
or when using the Windows DLL:
```
make mingw
```

##### Testrun using Google TTS [biemster/gtts](https://github.com/biemster/gtts):
Run the pipeline from the `gtts` repo directory so it can find `libchrometts`, and symlink the `SODAModels` directory
thats in the `gasr` repo to the `gtts` repo dir.
```
./gtts "Full Text to Speech to Text pipeline!" | sox -tf32 -L -r22050 -c1 - -ts16 - | wine ../gasr/gasr.exe --stream-delay
```
It should produce an output similar to this:
```
I1215 18:38:28.336217    6448 chrome_tts.cc:108] Init pipeline_path=./en-us/pipeline
I1215 18:38:28.336266    6448 tts_controller.cc:192] Reading ./en-us/pipeline as text file
I1215 18:38:28.339873    6448 data_source.cc:103] Opening data source "./en-us/acoustic_frame_config.pb" (as: FILE) ...
I1215 18:38:28.339906    6448 data_source.cc:110] ... Opened data source "./en-us/acoustic_frame_config.pb" of size 68
I1215 18:38:28.339980    6448 data_source.cc:103] Opening data source "./en-us/roman_numeral_android.far" (as: FILE) ...
I1215 18:38:28.339992    6448 data_source.cc:110] ... Opened data source "./en-us/roman_numeral_android.far" of size 2903
I1215 18:38:28.340006    6448 grm-manager.h:129] Loading FST archive from "./en-us/roman_numeral_android.far" ...
I1215 18:38:28.340132    6448 data_source.cc:103] Opening data source "./en-us/disambiguation_rules_en_us.pb" (as: FILE) ...
I1215 18:38:28.340146    6448 data_source.cc:110] ... Opened data source "./en-us/disambiguation_rules_en_us.pb" of size 311330
E1215 18:38:28.343703    6448 homograph_disambiguation_rules_data.cc:53] There are token-only rules for "ne" but there are also word-only rules for this key. The token rules will not be applied.
I1215 18:38:28.351753    6448 data_source.cc:103] Opening data source "./en-us/engine_config_en_us_x_greco_embedded_lstm.pb" (as: FILE) ...
I1215 18:38:28.352459    6448 data_source.cc:110] ... Opened data source "./en-us/engine_config_en_us_x_greco_embedded_lstm.pb" of size 446
I1215 18:38:28.352540    6448 data_source.cc:103] Opening data source "./en-us/mapping_grammar_en.far" (as: FILE) ...
I1215 18:38:28.352550    6448 data_source.cc:110] ... Opened data source "./en-us/mapping_grammar_en.far" of size 1071
I1215 18:38:28.352560    6448 grm-manager.h:129] Loading FST archive from "./en-us/mapping_grammar_en.far" ...
I1215 18:38:28.565851    6448 data_source.cc:103] Opening data source "./en-us/feats_android.far" (as: FILE) ...
I1215 18:38:28.565894    6448 data_source.cc:110] ... Opened data source "./en-us/feats_android.far" of size 950
I1215 18:38:28.565913    6448 grm-manager.h:129] Loading FST archive from "./en-us/feats_android.far" ...
I1215 18:38:28.566008    6448 data_source.cc:103] Opening data source "./en-us/lstm_dur_model.tflite" (as: MEMORY) ...
I1215 18:38:28.566026    6448 data_source.cc:110] ... Opened data source "./en-us/lstm_dur_model.tflite" of size 184960
I1215 18:38:28.566032    6448 lstm_model_load.cc:86] Loading memory mapped tflite model.
I1215 18:38:28.566178    6448 data_source.cc:103] Opening data source "./en-us/lstm_dur_model_input_mean_std_dev" (as: FILE) ...
I1215 18:38:28.566191    6448 data_source.cc:110] ... Opened data source "./en-us/lstm_dur_model_input_mean_std_dev" of size 2574
I1215 18:38:28.566221    6448 data_source.cc:103] Opening data source "./en-us/lstm_dur_model_output_mean_std_dev" (as: FILE) ...
I1215 18:38:28.566229    6448 data_source.cc:110] ... Opened data source "./en-us/lstm_dur_model_output_mean_std_dev" of size 12
I1215 18:38:28.566258    6448 data_source.cc:103] Opening data source "./en-us/lstm_speech_model.tflite" (as: MEMORY) ...
I1215 18:38:28.566271    6448 data_source.cc:110] ... Opened data source "./en-us/lstm_speech_model.tflite" of size 371072
I1215 18:38:28.566277    6448 lstm_model_load.cc:86] Loading memory mapped tflite model.
I1215 18:38:28.566384    6448 data_source.cc:103] Opening data source "./en-us/lstm_speech_model_input_mean_std_dev" (as: FILE) ...
I1215 18:38:28.566395    6448 data_source.cc:110] ... Opened data source "./en-us/lstm_speech_model_input_mean_std_dev" of size 2606
I1215 18:38:28.566414    6448 data_source.cc:103] Opening data source "./en-us/lstm_speech_model_output_mean_std_dev" (as: FILE) ...
I1215 18:38:28.566422    6448 data_source.cc:110] ... Opened data source "./en-us/lstm_speech_model_output_mean_std_dev" of size 1574
I1215 18:38:28.566448    6448 data_source.cc:103] Opening data source "./en-us/morphosyntactic_mapping.pb" (as: FILE) ...
I1215 18:38:28.566456    6448 data_source.cc:110] ... Opened data source "./en-us/morphosyntactic_mapping.pb" of size 6
I1215 18:38:28.566562    6448 data_source.cc:103] Opening data source "./en-us/resource.pb" (as: FILE) ...
I1215 18:38:28.566572    6448 data_source.cc:110] ... Opened data source "./en-us/resource.pb" of size 399460
I1215 18:38:28.567817    6448 parametric_playback.cc:47] Loaded playback info: 26
I1215 18:38:28.567954    6448 data_source.cc:103] Opening data source "./en-us/en_us_phonology.pb" (as: FILE) ...
I1215 18:38:28.568047    6448 data_source.cc:110] ... Opened data source "./en-us/en_us_phonology.pb" of size 3034
W1215 18:38:28.568237    6448 phonology.cc:79] Phonemes l, r have non-distinctive features.
W1215 18:38:28.568245    6448 phonology.cc:79] Phonemes ax, er have non-distinctive features.
I1215 18:38:28.568421    6448 data_source.cc:103] Opening data source "./en-us/en_morphology" (as: FILE) ...
I1215 18:38:28.568439    6448 data_source.cc:110] ... Opened data source "./en-us/en_morphology" of size 2753822
I1215 18:38:28.570110    6448 model-api.cc:45] Registered model under key morphology
I1215 18:38:28.571883    6448 data_source.cc:103] Opening data source "./en-us/compressed_lexicon_en_us.blex" (as: MEMORY) ...
I1215 18:38:28.571918    6448 data_source.cc:110] ... Opened data source "./en-us/compressed_lexicon_en_us.blex" of size 4931028
I1215 18:38:28.572056    6448 data_source.cc:103] Opening data source "./en-us/ipa_to_tts_to-en_us.far" (as: FILE) ...
I1215 18:38:28.572070    6448 data_source.cc:110] ... Opened data source "./en-us/ipa_to_tts_to-en_us.far" of size 27848
I1215 18:38:28.572095    6448 grm-manager.h:129] Loading FST archive from "./en-us/ipa_to_tts_to-en_us.far" ...
I1215 18:38:28.572247    6448 data_source.cc:103] Opening data source "./en-us/g2p_m3_syls0_stress0_en-US.fst" (as: FILE) ...
I1215 18:38:28.572266    6448 data_source.cc:110] ... Opened data source "./en-us/g2p_m3_syls0_stress0_en-US.fst" of size 702096
I1215 18:38:28.572281    6448 compact_fst.cc:19] Loading FST from "./en-us/g2p_m3_syls0_stress0_en-US.fst" ...
I1215 18:38:28.587721    6448 decoder.cc:57] G2P FST loaded (52 graphemes and 41 phonemes).
I1215 18:38:28.590200    6448 data_source.cc:103] Opening data source "./en-us/compressed_lexicon_en_us.blex" (as: MEMORY) ...
I1215 18:38:28.590239    6448 data_source.cc:110] ... Opened data source "./en-us/compressed_lexicon_en_us.blex" of size 4931028
I1215 18:38:28.590357    6448 data_source.cc:103] Opening data source "./en-us/homographs_model_en_us_embedded.pb" (as: FILE) ...
I1215 18:38:28.590369    6448 data_source.cc:110] ... Opened data source "./en-us/homographs_model_en_us_embedded.pb" of size 236059
I1215 18:38:28.595699    6448 data_source.cc:103] Opening data source "./en-us/feature_set.pb" (as: FILE) ...
I1215 18:38:28.595743    6448 data_source.cc:110] ... Opened data source "./en-us/feature_set.pb" of size 4128
I1215 18:38:28.595948    6448 data_source.cc:103] Opening data source "./en-us/converter_en_us_android.far" (as: FILE) ...
I1215 18:38:28.595964    6448 data_source.cc:110] ... Opened data source "./en-us/converter_en_us_android.far" of size 1825
I1215 18:38:28.595980    6448 grm-manager.h:129] Loading FST archive from "./en-us/converter_en_us_android.far" ...
I1215 18:38:28.596049    6448 data_source.cc:103] Opening data source "./en-us/roman_numeral_contexts.pb" (as: FILE) ...
I1215 18:38:28.596063    6448 data_source.cc:110] ... Opened data source "./en-us/roman_numeral_contexts.pb" of size 9136
I1215 18:38:28.596316    6448 data_source.cc:103] Opening data source "./en-us/sb_model.pb" (as: FILE) ...
I1215 18:38:28.596328    6448 data_source.cc:110] ... Opened data source "./en-us/sb_model.pb" of size 126111
I1215 18:38:28.598537    6448 data_source.cc:103] Opening data source "./en-us/en_verbalize_spec.pb" (as: FILE) ...
I1215 18:38:28.598571    6448 data_source.cc:110] ... Opened data source "./en-us/en_verbalize_spec.pb" of size 3723
I1215 18:38:28.598656    6448 data_source.cc:103] Opening data source "./en-us/textnorm_params_en_us.pb" (as: FILE) ...
I1215 18:38:28.598667    6448 data_source.cc:110] ... Opened data source "./en-us/textnorm_params_en_us.pb" of size 737
I1215 18:38:28.598701    6448 data_source.cc:103] Opening data source "./en-us/tokenize_and_classify_embedded_us_android.far" (as: FILE) ...
I1215 18:38:28.598710    6448 data_source.cc:110] ... Opened data source "./en-us/tokenize_and_classify_embedded_us_android.far" of size 2428079
I1215 18:38:28.598721    6448 grm-manager.h:129] Loading FST archive from "./en-us/tokenize_and_classify_embedded_us_android.far" ...
I1215 18:38:28.608832    6448 data_source.cc:103] Opening data source "./en-us/model_farm32.pb" (as: FILE) ...
I1215 18:38:28.608861    6448 data_source.cc:110] ... Opened data source "./en-us/model_farm32.pb" of size 400016
I1215 18:38:28.656269    6448 ranker.cc:117] LinearLseqRanker: using FarmHash32
I1215 18:38:28.656314    6448 data_source.cc:103] Opening data source "./en-us/variant_overrides_us.pb" (as: FILE) ...
I1215 18:38:28.656331    6448 data_source.cc:110] ... Opened data source "./en-us/variant_overrides_us.pb" of size 122
I1215 18:38:28.656387    6448 data_source.cc:103] Opening data source "./en-us/variant_selection_model_en_us_embedded.pb" (as: FILE) ...
I1215 18:38:28.656396    6448 data_source.cc:110] ... Opened data source "./en-us/variant_selection_model_en_us_embedded.pb" of size 370215
I1215 18:38:28.667836    6448 select_variants.cc:83] Word with override has only one variant: can_nou
I1215 18:38:28.667906    6448 data_source.cc:103] Opening data source "./en-us/us_verbalization_capabilities.pb" (as: FILE) ...
I1215 18:38:28.667938    6448 data_source.cc:110] ... Opened data source "./en-us/us_verbalization_capabilities.pb" of size 4669
I1215 18:38:28.668072    6448 data_source.cc:103] Opening data source "./en-us/verbalize_embedded_android.far" (as: FILE) ...
I1215 18:38:28.668092    6448 data_source.cc:110] ... Opened data source "./en-us/verbalize_embedded_android.far" of size 1624335
I1215 18:38:28.668104    6448 grm-manager.h:129] Loading FST archive from "./en-us/verbalize_embedded_android.far" ...
I1215 18:38:28.671195    6448 data_source.cc:103] Opening data source "./en-us/speech_morphing_palette.pb" (as: FILE) ...
I1215 18:38:28.671221    6448 data_source.cc:110] ... Opened data source "./en-us/speech_morphing_palette.pb" of size 41268
I1215 18:38:28.681164    6448 voice_params_resource.cc:31] Voice information: description: "embedded_lstm voice with embedded textnorm for en_us (speaker sfg; sample rate 22050)"
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

I1215 18:38:28.681219    6448 data_source.cc:103] Opening data source "./en-us/regexp_rewrite.pb" (as: FILE) ...
I1215 18:38:28.681234    6448 data_source.cc:110] ... Opened data source "./en-us/regexp_rewrite.pb" of size 4863
I1215 18:38:28.681309    6448 data_source.cc:103] Opening data source "./en-us/punctuation.pb" (as: FILE) ...
I1215 18:38:28.681327    6448 data_source.cc:110] ... Opened data source "./en-us/punctuation.pb" of size 297
I1215 18:38:28.720094    6448 data_source.cc:103] Opening data source "./en-us/xsampa_to_tts_to-en_us.far" (as: FILE) ...
I1215 18:38:28.720136    6448 data_source.cc:110] ... Opened data source "./en-us/xsampa_to_tts_to-en_us.far" of size 5136
I1215 18:38:28.720167    6448 grm-manager.h:129] Loading FST archive from "./en-us/xsampa_to_tts_to-en_us.far" ...
I1215 18:38:28.720247    6448 local_pipeline_runner.cc:115] Done loading all resources from: {./en-us/}
I1215 18:38:28.785235    6448 chrome_tts.cc:134] Shutting down
W1215 18:38:29.381753      44 soda_async_impl.cc:231] Creating soda_impl
002d:fixme:ver:GetCurrentPackageId (0x1e8fda0 (nil)): stub
002e:fixme:ver:GetCurrentPackageId (0x209fda0 (nil)): stub
W1215 18:38:29.469075      44 terse_processor.cc:242] TISID disabled.
W1215 18:38:29.492691      44 decoder_endpointer_stream.cc:35] Acoustic ep reader thread cancelled.
W1215 18:38:29.494543      44 soda_async_impl.cc:390] Soda session starting (require_hotword:0, hotword_timeout_in_millis:0)
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
* added 105380 bytes of audio
W1215 18:38:30.552996      80 portable_intended_query_stream.cc:234] Exiting due to stream cancellation.
W1215 18:38:30.555854      45 soda_async_impl.cc:765] Soda session stopped due to: STOP_CALLED
E1215 18:38:30.569007      44 mapped-file.cc:44] Failed to unmap region: 2
E1215 18:38:30.569202      44 mapped-file.cc:44] Failed to unmap region: 2
E1215 18:38:30.569348      44 mapped-file.cc:44] Failed to unmap region: 2
E1215 18:38:30.569424      44 mapped-file.cc:44] Failed to unmap region: 2
E1215 18:38:30.571428      44 mapped-file.cc:44] Failed to unmap region: 2
W1215 18:38:30.571547      44 soda_async_impl.cc:793] Deleting soda_impl
```
There is also a French model available:
```
./gtts ./fr-fr1/ "Texte intégral de la parole au pipeline de texte!" | sox -tf32 -L -r22050 -c1 - -ts16 - | wine ../gasr/gasr.exe --stream-delay
```
although that seems to be still a bit rough around the edges:
```
W1216 11:50:02.203720      43 soda_async_impl.cc:390] Soda session starting (require_hotword:0, hotword_timeout_in_millis:0)
I1216 11:50:02.648613    6891 chrome_tts.cc:134] Shutting down
>>> texte
>>> texte
>>> texte int
>>> texte int
>>> texte int├⌐g
>>> texte int├⌐g
>>> texte int├⌐gra
>>> texte int├⌐gra
>>> texte int├⌐gral
>>> texte int├⌐gral
>>> texte int├⌐gral
>>> texte int├⌐gral de
>>> texte int├⌐gral de
>>> texte int├⌐gral de
>>> texte int├⌐gral de
>>> texte int├⌐gral de la
>>> texte int├⌐gral de la
>>> texte int├⌐gral de la paro
>>> texte int├⌐gral de la parole
>>> texte int├⌐gral de la parole
W1216 11:50:03.837144      44 soda_async_impl.cc:765] Soda session stopped due to: STOP_CALLED
```

##### Run (through wine for now):
```
ecasound -f:16,1,16000 -i alsa -o:stdout|wine gasr.exe
```
