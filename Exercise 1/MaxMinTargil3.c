#include <stdio.h>

int calculate(int num1, int num2, char sign)
{
    int greater = (num1 > num2)*num1 + (num2 > num1)*num2 + (num2 == num1)*num1;
    int smaller = (num1 < num2)*num1 + (num2 < num1)*num2 + (num2 == num1)*num1;

    return ('>' == sign)*greater + ('<' == sign)*smaller;
}

int main(void)
{
	printf("result = %d \n", calculate(-4,-2,'<'));
}