#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define USERDEF0 "10593362"
#define USERDEF1 106

char msg[] = \
"To thwart static analysis, code and data are often encrypted by packers\n\
using a random key.  In this level, we have taken the password and packed\n\
it using a sophisticated XOR scheme. To find the password, you will need to\n\
unpack it by analyzing the binary using \"objdump -d\" or \"gdb\".\n\n";

void print_msg() {
        printf("%s",msg);
}

char c[9]=USERDEF0;
char in[9];

main() {
    int i,len;

    print_msg();

    printf("Enter your password: ");
    len = strlen(c);
    for (i=0; i < len; i++) 
	c[i] ^= (unsigned char) USERDEF1;
    scanf("%8s",in);
    for (i=0; i < len; i++) {
      if (c[i] != in[i]) {
	printf("Try again\n");
	exit(0);
      }
    }
    printf("Good Job\n");
}
