# gasr
ChromeOS SODA Offline Speech Recognition command line client

##### Intro:
This is a proof of concept how to write code against the libsoda library found in the ChromeOS, which uses it for Live Transcribe.
It's not a full application, but it will write out a live transcription to stdout of audio fed through stdin using for example ALSA.
Previous versions used the library found in the Chrome browser, and this is still available in the `chrome-browser` branch although
not actively maintained. Since ChromeOS is linux under the hood, Windows is not supported anymore and users requiring this should
use the `chrome-browser` branch.

##### Prepare:
Use the `prep.py` script to download the library for your platform, the language model of your choosing and patch the dynamic linker
to accept the relative relocations used in `libsoda.so`. Some examples are:
```bash
./prep.py -c # check if the dynamic linker is copied, patched and ready
```
```bash
./prep.py -c -p hana # check if libsoda.so for RPi4 is downloaded, fixed and ready
```
```bash
./prep.py -c -p hana -l "en-us" # check if libsoda.so for RPi4 is ready, and the en-us model
```
```bash
./prep.py -s -p hana # setup the ld-linux interpreter and libsoda.so for RPi4
```
If your platform is not available, please respond in https://github.com/biemster/gasr/issues/24

##### Run:
```bash
arecord -Dplughw:3,0 -fS16_LE -c1 -r16000 | ./ld-linux.so $(which python3) gasr.py 2>/dev/null
```
where `hw:3,0` should be changed to where your microphone lives in your ALSA setup.
