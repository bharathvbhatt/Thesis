/*
 ============================================================================
 Name        : FFT_example.c
 Author      : Bharath Vikram Bhatt
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <fftw3.h>
#include <math.h>

int main()
{
	FILE *fp,*fp1;
	fftw_complex data[5000000];
	fftw_complex in[5000],out[5000];
	fftw_plan my_plan;
	int a,b;
	char buf;
	int mag,sqrt_val;
	fp =fopen("rx.bin","r");
	fp1 =fopen("check.txt","a");
	if(fp==NULL)
	{
		printf("Error opening File\n");
	}
/*	int index=0;
	while((buf = fgetc(fp)) != EOF)
    {
     fscanf(fp,"%d %d",&a,&b);
     data[index][0]=a;
     data[index][1]=b;
     index++;
    }*/
	int count =0;
	for(int i=0;i<5000;i++)
	{
		fscanf(fp,"%d %d",&a,&b);
		mag = ((a*a)+(b*b));
		sqrt_val =sqrt(mag);
		if((sqrt_val>110))
		{
			if(count>115)
			{
				in[i][0]=a;
				in[i][1]=b;
			}

			else
			{
				in[i][0]=0;
				in[i][1]=0;
				count++;
			}
		}
		else
		{
			in[i][0]=0;
			in[i][1]=0;
		}

	}

	my_plan = fftw_plan_dft_1d(5000, in, out, FFTW_FORWARD, FFTW_ESTIMATE);
	fftw_execute(my_plan);

	for(int i=0;i<5000;i++)
	{
		fprintf(fp1,"%lf %lf\n",out[i][0],out[i][1]);

	}



	return 0;
}


