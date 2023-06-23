#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    bool shouldContinue;
    
    do
    {
        system("clear");
        
        int lato = 0;
        printf("Immettere misura lato (o raggio): ");

        scanf("%d", &lato);

        int areaQuadrato = lato * lato;
        // nei prossimi calcoli al posto di usare il quadrato 
        // del lato useró la variabile già calcolata
        // M_PI é il pigreco già calcolato nella libreria math.io
        float areaCerchio = M_PI * areaQuadrato;
        // formula per l'area del triangolo equilatero dato solo un lato
        // radice quadrata di 3 diviso 4  tutto per il quadrato del lato
        float areaTriangolo = (sqrt(3)/4) * areaQuadrato;
 
        printf("area quadrato equilatero: %d \n", areaQuadrato);
        printf("area cerchio: %f \n", areaCerchio);
        printf("area triangolo equilatero: %f \n", areaTriangolo);
        
        printf("\n \n \ncontinuare? (s/N): ");
        char wantToContinue;
        scanf(" %c", &wantToContinue);
        
        shouldContinue = wantToContinue == 's' || wantToContinue == 'S';
    }while(shouldContinue);
    return 0;
}