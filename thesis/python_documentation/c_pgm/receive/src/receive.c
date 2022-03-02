#include <iio.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fftw3.h>
#include <math.h>
#include <netdb.h>
#include <string.h>
#include <sys/socket.h>
#include <time.h>





#define MAX 80
#define PORT 9999
#define SA struct sockaddr
#define No 1000
#define N 4096
int sockfd, connfd;
int cyc_buf[No];

void make_client()
{

	struct sockaddr_in servaddr, cli;
    // socket create and varification
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1) {
        printf("socket creation failed...\n");
        exit(0);
    }
    else
        printf("Socket successfully created..\n");
    bzero(&servaddr, sizeof(servaddr));

    // assign IP, PORT
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = inet_addr("192.168.3.10");
    servaddr.sin_port = htons(PORT);

    // connect the client socket to server socket
    if (connect(sockfd, (SA*)&servaddr, sizeof(servaddr)) != 0) {
        printf("connection with the server failed...\n");
        exit(0);
    }
    else
        printf("connected to the server..\n");

}
int count=0;

void compute_avg(int index)
{
	int avg=0;
	char buff[3]={'\0'};
	if(((count%No)==0)&&(count!=0))
	{

		count=0;
		for(int i=0;i<No;i++)
		{
			avg+=cyc_buf[i];
		}
		avg/=No;
        //printf("%d\n",avg);
		//sprintf(buff,"%d",avg);
		//write(sockfd, buff, sizeof(buff));
	}
	    cyc_buf[count]=index;
	    count++;

}


void compute_max(fftw_complex *out)
{
	int max_index;
	FILE *fp;
    double max_val=0;
    char buff[4]={'\0'};
	for(int i=0;i<N;i++)
	{
		if(max_val<out[i][0])
		{
			max_val = out[i][0];
			max_index=i;
		}
     }
    //printf("Index is: %d\n",max_index);
	//sprintf(buff,"%d",max_index);
	//write(sockfd, buff, sizeof(buff));
   compute_avg(max_index);
}




void compute_mag(fftw_complex *out)
{

	for(int i=0;i<N;i++)
	{
		out[i][0] = (out[i][0]*out[i][0])+(out[i][1]*out[i][1]);
	}
	compute_max(out);
}


void compute_fft(fftw_complex *in)
{
	fftw_plan my_plan;
	fftw_complex out[N];
	FILE *fp;
	my_plan = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);
	fftw_execute(my_plan);
	compute_mag(out);
	fftw_destroy_plan(my_plan);
    fftw_cleanup();
}

void signal_processing(fftw_complex *in)
{
	int mag,sqrt_val;
	int count=0;
	FILE *fp;

	for(int i=0;i<N;i++)
	{
		mag = ( (in[i][0]*in[i][0])+(in[i][1]*in[i][1]));
		sqrt_val =sqrt(mag);
		if((sqrt_val<150)) //110:
		{
			in[i][0]=0;
			in[i][1]=0;
		}
		else
		{
			if(count<115)
			{
				in[i][0]=0;
				in[i][1]=0;
				count++;
			}
		}
	}
	compute_fft(in);
}


void buffer_split(struct iio_buffer *rxbuf,void *start,void *end,ptrdiff_t inc)
{
	void *p_dat;
	FILE *fp;
	//fp = fopen("rx.bin", "a");
	fftw_complex in[N];
	//if(fp == NULL)
	//{
	//	fprintf(stderr,"Cannot open file for reading");
	//}
	//for (p_dat = start; p_dat < end; p_dat+=inc)
	//{
	//	const int16_t i = ((int16_t*)p_dat)[0]; // Real (I)
	//	const int16_t q = ((int16_t*)p_dat)[1]; // Imag (Q)
	//	fprintf(fp,"%d %d\n",i,q);
	//}

	int index =0;
	end = start+N*inc;

	while(index<No)
	{
		int i=0;
		for(p_dat=start;p_dat<end;p_dat+=inc)
		{
			in[i][0] =((int16_t*)p_dat)[0];
			in[i][1] =((int16_t*)p_dat)[1];
			i++;
		}
		signal_processing(in);
		start =end;
		end = end+N*inc;
		index++;
	}

}




int receive(struct iio_context *ctx)
{
	struct iio_device *dev;
	struct iio_channel *rx0_i, *rx0_q;
	struct iio_buffer *rxbuf;

	fftw_complex in[5000],out[5000];
	fftw_plan my_plan;
	dev = iio_context_find_device(ctx, "cf-ad9361-lpc");

	rx0_i = iio_device_find_channel(dev, "voltage0", 0);
	rx0_q = iio_device_find_channel(dev, "voltage1", 0);

	iio_channel_enable(rx0_i);
	iio_channel_enable(rx0_q);

	rxbuf = iio_device_create_buffer(dev,4096000,false);


	if (!rxbuf)
	{
		perror("Could not create RX buffer");
		//shutdown();
	}
	int count =0;

	//	while (count<10)
	//	{
	void *p_dat, *p_end, *t_dat;
	ptrdiff_t p_inc;

	iio_buffer_refill(rxbuf);
	p_dat = iio_buffer_first(rxbuf, rx0_i);
	p_inc = iio_buffer_step(rxbuf);
	p_end = iio_buffer_end(rxbuf);
	//	count++;
	buffer_split(rxbuf,p_dat,p_end,p_inc);
	//	}

	iio_buffer_destroy(rxbuf);
	return 0;
}


int main ()
{
	struct iio_context *ctx;
	struct iio_device *phy;

	ctx = iio_create_context_from_uri("ip:192.168.3.1");

	phy = iio_context_find_device(ctx, "ad9361-phy");

	iio_channel_attr_write_longlong(iio_device_find_channel(phy, "altvoltage0", true),"frequency",2410000000); /* RX LO frequency 2.415GHz */

	iio_channel_attr_write_longlong(iio_device_find_channel(phy, "voltage0", false),"sampling_frequency",40960000); /* RX baseband rate 50 MSPS */

	//make_client();
    //while(1)
    //{
    	receive(ctx);
    //}


	iio_context_destroy(ctx);

	return 0;
}
