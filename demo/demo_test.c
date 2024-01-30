#include <stdio.h>

void swap(int **p, int **q) {
   int temp = *p;
   *p = *q;
   *q = temp;
}

int main() {
   int num1 = 1;
   int num2 = 2;
   int *k = &num1;
   int *x = &num2;
   swap(&k, &x);
   printf("%d\n", *k);
   printf("%d\n", *x);
   // swap(&num1, &num2);

   // printf("%d\n", num1);
   // printf("%d\n", num2);
}

// void swap(int *p, int *q) {
//    int q = 10;
//    *p = &q;
// }

// int main() {
//    int ko = 4;
//    int *p = &ko;
//    foo(&p);

//    return 0;
// }

// int main() {
//    int kraft = 4;

//    return 0;
// }