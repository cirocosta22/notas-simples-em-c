#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	
    int idade,idade_nova; 
    
     
    printf("digite a sua idade:  ");
    scanf("%d",&idade);
    
    
    idade_nova = idade + 1; 
    
    printf("no ano que vem voce tera %d\n",idade_nova);
    
    if(idade_nova >= 18 ){ 
    
    
     printf("uau, voce e maior de idade\n ");
	}
	else{
		
	 printf("infelizmente voce nao podera entrar\n  ");
	}
    
    
	
	return 0;
}
