//Curtis Humm, etch-a-sketch homework one. Due 9/5/17

#include <stdio.h>
#include <stdlib.h>

char grid[2][2];

int main(int argc, char **argv) {

  printf("Let's begin\n");
  //char grid[2][2];
  char th = 'A';
  grid[0][0] = 'a';
  grid[0][1] = 'b';
  grid[1][0] = 'c';
  grid[1][1] = 'd';
  printf("%c\n",grid[0][0]);
  printGrid(2,2);
  return 0;
}

int printGrid(int width, int height){

  int i = 0;
  int j = 0;

  for(i = 0; i < height; i++) {
    for(j = 0; j < width; j++) {
      printf("%c", grid[i][j]);
    }
    printf("\n");
  }
  printf("done\n");
  return 0;
}
