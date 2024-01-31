#include <stdio.h>

int main () {
   // int week = 3;
   // int *ptr = &week;

   // printf("%d\n", week);
   // printf("%p\n", &week);
   // printf("%p\n", ptr);
   // printf("%d\n", *ptr);
   // printf("%p\n", &ptr);

   // printf("%s\n", "---------------------");

   char alphabet[3] = {'a', 'b', 'c'};

   printf("%s\n", "alphabet char array");
   printf("%p\n", alphabet);
   for (int i = 0; i < 3; i++) {
      printf("%p\n", &alphabet[i]);
   }

   printf("%s\n", "---------------------");

   int number[3] = {15, 22, 3};

   printf("%s\n", "number int array");
   printf("%p\n", number);
   for (int i = 0; i < 3; i++) {
      printf("%p\n", &number[i]);
   }

   return 0;
}


//    printf("%d\n", *alphabet); // output = a
//    printf("%d\n", *(alphabet + 1)); // output = b
//    *(alphabet + 2) = 'd';
//    printf("%d\n", *(alphabet + 2)); // output = d

//    printf("%s\n", "---------------------");

//    int ko = 4;
//    int *p = &ko; // 포인터 p는 ko의 주소를 가르키고 있다
//    foo(&p);
//    printf("%d\n", *p);

//    printf("%s\n", "---------------------");


//    char *c[] = {"SOS", "Death", "Chaos", "Nihil"};
//    char **cp[] = {c+3, c+2, c+1, c};
//    char ***cpp = cp;

//    printf("%s\n", **++cpp); // output = Chaos (c+2를 가르킨다)

//    printf("%s\n", "---------------------");

//    return 0;
// }