#include <stdio.h>
#include <cs50.h>


int main(void) {

// declaração das variáveis

    int h, i, j;

// pedir a altura da pirâmide ao utilizador

    do
    {
        h = get_int("Insira a altura da pirâmide (entre 1 e 9): ");

    }
    while (h >= 10);

// construção da parte esquerda da pirâmide
    for( i = 0; i <= h; i++)
    {
        for(j = h - i; j >= 0; j--)
            printf(" ");
        for( j = 0; j <= h ;j++){
            if(j > i){
                break;
            }
            printf("#");
        }

        // construção do espaço entre os dois lados da pirâmide

        printf(" ");
        printf(" ");

        // construção do lado direito da pirâmide

        for( j = 0; j <= h ;j++){
            if(j > i){
                break;
            }
            printf("#");
        }
        printf("\n");
    }

    // construção da base da pirâmide

    for (j = 0; j < 2 * h+6; j++) {
        printf("=");
    }

    printf("\n");

    return 0;
}
