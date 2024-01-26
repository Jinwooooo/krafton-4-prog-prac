void foo(int **p) {
   int q = 10;
   *p = &q;
}

int main() {
   int ko = 4;
   int *p = &ko;
   foo(&p);

   return 0;
}