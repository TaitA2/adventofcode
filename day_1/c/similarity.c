#include <stdio.h>
#include <stdlib.h>

int count(int arr[], int n) {
  int count = 0;
  for (int i = 0; i < 1000; i++) {
    if (arr[i] == n) {
      count++;
    }
  }  
  return count;
}

void main() {

  int arr[2000];
  for (int i = 0; i < 2000; i++) {
    scanf("%d", &arr[i]);
  }

  int similarity = 0;

  int n = 1000;
  int left[n];
  int right[n];

  for (int i = 0; i < n; i++) {
    left[i] = arr[i * 2];
    right[i] = arr[(i * 2) + 1];
  }

  for (int i = 0; i < n; i++) {
    similarity += left[i] * count(right, left[i]);
  }
  printf("%i\n", similarity);
}
