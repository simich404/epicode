#include<stdio.h>
#include<string.h>
int main()
{
    char newGame;
    int punteggio;
    char risposta;

    do {
        printf("#########################\n"
               "#  Benvenuto nel gioco! #\n"
               "# Rispondi alle domande #\n"
               "#    ti verrà dato un   #\n"
               "#       punteggio!      #\n"
               "#########################\n");
        punteggio=0;
        printf("\n\niniziare una nuova partita? (s/N)"); ;
        scanf(" %c", &newGame);
        system("clear");
        if(newGame=='s' || newGame=='S')
        {
            printf("Di che colore era il cavallo bianco di napoleone? \n"
                   "a) bianco\n"
                   "b) nero\n"
                   "c) arcobaleno\n");
            scanf(" %c", &risposta);
            if(risposta=='c')
            {
                punteggio++;
            }
            system("clear");
            printf("Prima regola del fight club?\n"
                   "a) mai parlare del fight club\n"
                   "b) fight che?\n"
                   "c) non parlate mai del fight club\n");
            scanf(" %c", &risposta);
            if(risposta=='c')
            {
                punteggio++;
            }
            system("clear");
            printf("se in una gara sei quarto e superi i primi 2 in che posizione sarai?\n"
                   "a) ultimo\n"
                   "b) io arrivo sempre primo\n"
                   "c) secondo\n");
            scanf(" %c", &risposta);
            if(risposta=='c')
            {
                punteggio++;
            }
            system("clear");

            printf("bravo, hai fatto %d punti\n\n", punteggio);
            printf("premi [ENTER] per continuare\n", punteggio);
            
            char x = getchar();
            x = getchar();
            
            system("clear");
            
        }
    } while(newGame=='s' || newGame=='S');
        printf("addiosss :)\n\n");

    return 0;
}