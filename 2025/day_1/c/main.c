#include <stdio.h>
#include <stdlib.h>

const int max = 100;
const int start = 50;

typedef struct rotation {
  char direction;
  int n;
} rotation;

// function headers
rotation *get_rotations(int *count);
int rotate_dial(rotation rotations[], int start, int count);

int main() {
  // get rotations array
  int count = 0;
  rotation *rotations = get_rotations(&count);
  // solve
  int ans = rotate_dial(rotations, start, count);

  // print answer
  printf("%d\n", ans);

  // free used memory
  free(rotations);

  return 0;
}

rotation *get_rotations(int *count) {
  FILE *file = fopen("../input.txt", "r");

  // rotations array
  rotation *rotations = malloc(sizeof(rotation) * 5000);

  char content[10];

  while (fgets(content, 10, file)) {
    struct rotation rotation;
    rotation.direction = content[0];
    rotation.n = atoi(&content[1]);

    rotations[(*count)++] = rotation;
  }

  fclose(file);
  return rotations;
}

int rotate_dial(rotation rotations[], int start, int count) {
  int pos = start;
  int zero_count = 0;
  for (int i = 0; i <= count; i++) {
    rotation rotation = rotations[i];
    switch (rotation.direction) {
    case 'L':
      pos -= (rotation.n % max);
      if (pos < 0) {
        pos += max;
      }
      break;
    case 'R':
      pos += (rotation.n % max);
      if (pos >= max) {
        pos -= max;
      }
      break;
    }
    if (pos == 0) {
      zero_count++;
    }
  }
  return zero_count;
}
