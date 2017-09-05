/**Curtis Humm, etch-a-sketch homework one. Due 9/5/17**/

#include <stdio.h>
#include <stdlib.h>


int width;
int height;
int x;
int y;

int printGrid(char grid[][width]);

int main(int argc, char **argv) {

  if (argc != 3) {
    printf("Height Width\n");
    exit(-1);
  }

  height = atoi(argv[1]);
  width = atoi(argv[2]);

  char grid[height][width];
  int i;
  int j;
  char space = ' ';
  for(i = 0; i < height; i++) {
    for(j = 0; j < width; j++) {
     grid[i][j] = space;
    }
  }
  x = 0;
  y = 0;
  grid[0][0] = 'X';

  /**Opening Remarks**/

  printf("Welcome to BeagleSketch! Here are the rules.\n");
  printf("w -> Move Up\n");
  printf("s -> Move Down\n");
  printf("a -> Move Left\n");
  printf("d -> Move Right\n");
  printf("c -> Clear Board\n");
  printf("x -> Exit Program\n");
  printf("Enjoy!\n");



  /**User Input*/
  int persist = 0;
  while(persist == 0) {
    printGrid(grid);
    char in;
    scanf(" %c", &in);

    if(in == 'w'){
      if(y > 0) {
        y--;
        grid[y][x] = 'X';
      }
    }

    if(in == 's'){
      if(y < height - 1) {
        y++;
        grid[y][x] = 'X';
      }
    }

    if(in == 'a'){
      if(x > 0) {
        x--;
        grid[y][x] = 'X';
      }
    }

    if(in == 'd'){
      if(x < width - 1) {
        x++;
        grid[y][x] = 'X';
      }
    }

    if(in == 'c') {
      for(i = 0; i < height; i++) {
        for(j = 0; j < width; j++) {
          grid[i][j] = ' ';
        }
      }
    }

    if(in == 'x') {
      persist = 1;
    }

  }
  /**End User Input**/

  return 0;
}


/**Used to print the board**/
int printGrid(char grid[][width]){

  int i = 0;
  int j = 0;
  int k = 0;
  int temp;
  int count = 0;
  printf("   ");
  for(i = 0; i < width; i++) {
    printf("%d ", count);
    count++;
  }
  printf("\n");
  count = 0;
  for(i = 0; i < height; i++) {
    printf("%d: ",count);
    count++;
    for(j = 0; j < width; j++) {
      printf("%c ", grid[i][j]);
      temp = j/10;
      while(temp > 0) {
        printf(" ");
        temp = temp/10;
      }
    }
    printf("\n");
  }
  return 0;
}
