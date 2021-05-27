#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>

#define IMAX 10000000

unsigned long hash1(char str[]){
  register int i;
  register char c;
  unsigned long w=0;

  while(1){
    c = str[i++];
    w += w + (w*257 +(int)c) ;
    if(str[i] == '\0') break;
  }
  return w;
}

uint32_t hash2(uint32_t K){
  K ^= K >> (8-4);
  return (140503*K) >> (8-4);
}


int main(){
  size_t i=0,h=0,k=0;
  
  char str[100];
  char hash[100];
  double elap;
  
  printf("Enter a string: ");
  scanf("%s",str);

  // Create numerical key
  for(i=0,k=123;i<strlen(str);i++,k+=321){
    printf("%d ",str[i]);
    k += k*(int)str[i];
  }
  
  printf("\nKey = %lu\n",k);
  
  clock_t start_time = clock();

  for(i=0;i<IMAX;i++)
    h = hash2(k);

  elap = (double)(clock() - start_time)/CLOCKS_PER_SEC;
  //h=2749832470;
  
  printf("%lu %s -> %lu in %f s\n",i,str,h,elap);

  return 0;
  
}
