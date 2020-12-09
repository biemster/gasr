# gasr
Google Chrome SODA Offline Speech Recognition command line client

## ** STUB, STILL WAITING FOR THE LINUX LIBRARY TO BECOME AVAILABLE **

##### Intro:
This is a proof of concept how to write code against the libsoda library found in the Chrome browser, which uses it for Live Transcribe.
It's not a full application, but it will write out a live transcription to stdout of audio fed through stdin using for example ALSA or SoX.

##### Prepare:
Get a copy of libsoda from Chrome for your platform. At the time of this writing only Windows and OSX libraries are available,
I'm still waiting for the Linux version to be available.

##### Compile:
```
make
```

##### Run:
```
arecord | ./gasr
```
