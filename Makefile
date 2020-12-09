CC=g++
LDFLAGS=-L. -Wl,-rpath,. -lsoda

gasr: gasr.c
	$(CC) -o $@ $< $(LDFLAGS)

mingw: gasr.c
	x86_64-w64-mingw32-g++ -o gasr.exe $< -static-libstdc++ -static-libgcc -L. -lSODA