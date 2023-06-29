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
        printf("\n\niniziare una nuova partita? (s/N)");
	do
	{
        scanf(" %c", &newGame);
		if(newGame != 's' || newGame != 'S' || newGame != 'n' || newGame != 'N') {
			printf("\nsono accettati valori solo s/n \n");
		}
	}while(newGame != 's' && newGame != 'S' && newGame != 'n' && newGame != 'N');
        system("clear");
        if(newGame=='s' || newGame=='S')
        {
            printf("Di che colore era il cavallo bianco di napoleone? \n"
                   "a) bianco\n"
                   "b) nero\n"
                   "c) arcobaleno\n");
	    do
	    {
            scanf(" %c", &risposta);
            if((risposta >= 'd' && risposta <= 'z') || (risposta >= 'D' && risposta <= 'Z')) {
                printf("\nsono accettati valori solo a/b/c \n");
            }
	    }while((risposta >= 'a' && risposta <= 'c') || (risposta >= 'A' && risposta <= 'C'));

            if(risposta=='c' || risposta=='C')
            {
               	punteggio++;
            }


            system("clear");
            printf("Prima regola del fight club?\n"
                   "a) mai parlare del fight club\n"
                   "b) fight che?\n"
                   "c) non parlate mai del fight club\n");
            do
            {
                scanf(" %c", &risposta);
                if((risposta >= 'd' && risposta <= 'z') || (risposta >= 'D' && risposta <= 'Z')) {
                    printf("\nsono accettati valori solo a/b/c \n");
                }
            }while((risposta >= 'a' && risposta <= 'c') || (risposta >= 'A' && risposta <= 'C'));

            if(risposta=='c' || risposta=='C')
            {
               	punteggio++;
            }


            system("clear");
            printf("se in una gara sei quarto e superi i primi 2 in che posizione sarai?\n"
                   "a) ultimo\n"
                   "b) io arrivo sempre primo\n"
                   "c) secondo\n");
            
            do
            {
                scanf(" %c", &risposta);
                if((risposta >= 'd' && risposta <= 'z') || (risposta >= 'D' && risposta <= 'Z')) {
                    printf("\nsono accettati valori solo a/b/c \n");
                }
            }while((risposta >= 'a' && risposta <= 'c') || (risposta >= 'A' && risposta <= 'C'));

            if(risposta=='c' || risposta=='C')
            {
               	punteggio++;
            }


            system("clear");

            printf("bravo, hai fatto %d punti\n\n", punteggio);
            printf("premi [ENTER] per continuare\n");
            
            char x = getchar();
            x = getchar();
            
            system("clear");
            
        }
    }while(newGame=='s' || newGame=='S');
    printf("addiosss :)\n\n");

    return 0;
}