/*
 ============================================================================
 Name        : file.c
 Author      : Bharath Vikram Bhatt
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 1000000
int main(void) {
	FILE *fp;
//    char buf[255]="1685 -32586.23";
//    int a,b;
//    sscanf(buf,"%d %d",&a,&b);
//    printf("%d,%d\n",a,b);



	int linect = 0;
	char buf[128];
	int i_data[5000];
	int q_data[5000];

	fp = fopen("fmcw_2.bin", "r");
	if(fp == NULL)
	{
		fprintf(stderr,"Cannot open file for reading");
		exit(EXIT_FAILURE);
	}
	while( fgets(buf,sizeof(buf),fp) != NULL )
	{
		sscanf(buf,"%d %d", &i_data[linect], &q_data[linect]);
		printf("Set %d - 1st: %d, 2nd: %d\n", linect, i_data[linect], q_data[linect]);
		linect++;
		if ((linect+1)>=MAX_SIZE) {
			fprintf(stderr,"Max data size exceeded");
			exit(EXIT_FAILURE);
		}


	}
	return 0;
}
