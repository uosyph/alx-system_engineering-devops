#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_loop - Forever looping.
 * Return: 1
 */
int infinite_loop(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
 * main - Creates 5 zombie processes.
 * Return: Always 1
 */
int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		if (fork() == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_loop();

	return (0);
}
