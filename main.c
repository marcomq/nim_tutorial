#include "nmath.h"
#include <stdio.h>

// nim c --noMain --noLinking --header:fib.h fib.nim
// gcc -o m -I$HOME/.cache/nim/nmath -Ipath/to/nim/lib $HOME/.cache/nim/nmath/*.c main.c

int main(void) {
  NimMain();
  for (int f = 0; f < 10; f++)
    printf("Fib of %d is %d\n", f, fib(f));
  return 0;
}