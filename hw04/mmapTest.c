// From : http://stackoverflow.com/questions/13124271/driving-beaglebone-gpio-through-dev-mem
//
// Read one gpio pin and write it out to another using mmap.
// Be sure to set -O3 when compiling.
// Modified by Mark A. Yoder  26-Sept-2013
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 
#include <signal.h>    // Defines signal-handling functions (i.e. trap Ctrl-C)
#include "beaglebone_gpio.h"

/****************************************************************
 * Global variables
 ****************************************************************/
int keepgoing = 1;    // Set to 0 when ctrl-c is pressed

/****************************************************************
 * signal_handler
 ****************************************************************/
void signal_handler(int sig);
// Callback called when SIGINT is sent to the process (Ctrl-C)
void signal_handler(int sig)
{
    printf( "\nCtrl-C pressed, cleaning up and exiting...\n" );
	keepgoing = 0;
}

int main(int argc, char *argv[]) {
    volatile void *gpio_addr;
    volatile unsigned int *gpio_oe_addr;
    volatile unsigned int *gpio_datain;
    volatile unsigned int *gpio_setdataout_addr;
    volatile unsigned int *gpio_cleardataout_addr;
    
    volatile void *gpio_addr_light;
    volatile unsigned int *gpio_oe_addr_light;
    volatile unsigned int *gpio_datain_light;
    volatile unsigned int *gpio_setdataout_addr_light;
    volatile unsigned int *gpio_cleardataout_addr_light;
    
    unsigned int reg;

    // Set the signal callback for Ctrl-C
    signal(SIGINT, signal_handler);

    int fd = open("/dev/mem", O_RDWR);

    printf("Mapping %X - %X (size: %X)\n", GPIO1_START_ADDR, GPIO1_END_ADDR, 
                                           GPIO1_SIZE);
                                           
    printf("Mapping %X - %X (size: %X)\n", GPIO3_START_ADDR, GPIO3_END_ADDR, 
                                           GPIO3_SIZE);

    gpio_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 
                        GPIO1_START_ADDR);
    
    gpio_addr_light = mmap(0, GPIO3_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 
                        GPIO3_START_ADDR);

    gpio_oe_addr           = gpio_addr + GPIO_OE;
    gpio_datain            = gpio_addr + GPIO_DATAIN;
    gpio_setdataout_addr   = gpio_addr + GPIO_SETDATAOUT;
    gpio_cleardataout_addr = gpio_addr + GPIO_CLEARDATAOUT;
    
    gpio_oe_addr_light           = gpio_addr_light + GPIO_OE;
    gpio_datain_light            = gpio_addr_light + GPIO_DATAIN;
    gpio_setdataout_addr_light   = gpio_addr_light + GPIO_SETDATAOUT;
    gpio_cleardataout_addr_light = gpio_addr_light + GPIO_CLEARDATAOUT;

    if(gpio_addr == MAP_FAILED) {
        printf("Unable to map GPIO\n");
        exit(1);
    }
    
    if(gpio_addr_light == MAP_FAILED) {
        printf("Unable to map GPIO light\n");
        exit(1);
    }
    
    printf("GPIO mapped to %p\n", gpio_addr);
    printf("GPIO OE mapped to %p\n", gpio_oe_addr);
    printf("GPIO SETDATAOUTADDR mapped to %p\n", gpio_setdataout_addr);
    printf("GPIO CLEARDATAOUT mapped to %p\n", gpio_cleardataout_addr);
    
    
    printf("\n\nGPIO mapped to %p\n", gpio_addr_light);
    printf("GPIO OE mapped to %p\n", gpio_oe_addr_light);
    printf("GPIO SETDATAOUTADDR mapped to %p\n", gpio_setdataout_addr_light);
    printf("GPIO CLEARDATAOUT mapped to %p\n", gpio_cleardataout_addr_light);

    printf("Start copying Stuff\n");
    
        // Set USR3 to be an output pin
    reg = *gpio_oe_addr_light;
    printf("GPIO1 configuration: %X\n", reg);
    reg &= ~USR3;       // Set USR3 bit to 0
    *gpio_oe_addr_light = reg;
    printf("GPIO1 configuration: %X\n", reg);
    
    
    while(keepgoing) {
        if(*gpio_datain_light & GPIO_17){
            //printf("Stuff\n");
            *gpio_setdataout_addr = USR3;
            usleep(250000);
    	} if(*gpio_datain & GPIO_17){
            //printf("Stuff\n");
            *gpio_setdataout_addr = USR2;
            usleep(250000);
        } else {
            *gpio_cleardataout_addr = USR3;
            *gpio_cleardataout_addr = USR2;
            usleep(250000);
    	}
        //usleep(1);
    }

    munmap((void *)gpio_addr, GPIO0_SIZE);
        munmap((void *)gpio_addr_light, GPIO0_SIZE);
    close(fd);
    return 0;
}
