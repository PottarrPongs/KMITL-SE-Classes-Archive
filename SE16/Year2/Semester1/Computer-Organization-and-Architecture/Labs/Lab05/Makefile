all: main
main: main.o add.o
	gcc -o main main.o add.o
main.o: lab05_02.c
	gcc -g -c lab05_02.c -o main.o
add.o:
	as -g lab05_02.s -o add.o
clean:
	rm -r *.o main
