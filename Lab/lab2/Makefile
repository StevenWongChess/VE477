CC = clang
CFLAGS = -std=gnu11 -O2 -Wall 
MUMSH_SRC = main.c

MUMSH = main
.PHONY: clean

all: $(MUMSH) 
	@echo $(MUMSH) successfully constructed

$(MUMSH): $(MUMSH_SRC)
	$(CC) $(CFLAGS) -o $(MUMSH) $(MUMSH_SRC)

.c.o:
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) *.o *.a *~ $(MUMSH) 
