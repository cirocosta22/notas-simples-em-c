#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	
	 setlocale(LC_ALL, "portuguese");
	 
    float A,B;
    float i;
     
    printf("digite a sua primeira nota: ");
    scanf("%f",&A);
    printf("digite a sua segunda nota: ");
    scanf("%f",&B);
    
    i = (A+B)/2;
    
        if (i < 6){
    	
    	printf("você foi reprovado , infelizmente , sua nota foi %f  ",i);
    	scanf("%f",i);
	}
    if(i>=8){
    	
    	
    	printf("você foi genial , parabens sua nota está acima da media %f",i);
	}
	
	else{
		
	   printf("muito bem , voce atingiu a media e tirou %f",i);
	}
      
	return 0;
}
