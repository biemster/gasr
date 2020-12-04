CC=g++
LDFLAGS=-L. -Wl,-rpath,. -lsoda

gasr: gasr.c
	$(CC) -o $@ $< $(LDFLAGS)
