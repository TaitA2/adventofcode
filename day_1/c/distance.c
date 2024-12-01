#include <stdio.h>
#include <stdlib.h>

int comp(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

void main() {
  int distance = 0;

  int arr[2000];
  for (int i = 0; i < 2000; i++) {
    scanf("%d", &arr[i]);
  }

  int n = 1000;

  int left[n];
  int right[n];

  for (int i = 0; i < n; i++) {
    left[i] = arr[i * 2];
    right[i] = arr[(i * 2) + 1];
  }
  qsort(left, n, sizeof(int), comp);
  qsort(right, n, sizeof(int), comp);

  for (int i = 0; i < n; i++) {
    distance += abs(left[i] - right[i]);
  }
  printf("%i\n", distance);
}
