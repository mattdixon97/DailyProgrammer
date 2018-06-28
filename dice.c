/*
 *  Given inputs as NdM, roll an M-sided die N times and sum their rolls
 *
 *  https://www.reddit.com/r/dailyprogrammer/comments/8s0cy1/20180618_challenge_364_easy_create_a_dice_roller/
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void rollDice(int num_rolls, int num_sides);

int main()
{
    int rolls, sides;
    srand(time(NULL));

    while (scanf("%dd%d", &rolls, &sides) == 2) {
        rollDice(rolls, sides);
    }
    
    return 0;
}

void rollDice(int num_rolls, int num_sides)
{
    int i, j;
    int sum = 0;
    int rolls[num_rolls];

    for (i = 0; i < num_rolls; i++) {
        rolls[i] = rand() % num_sides + 1;
        sum += rolls[i];    
    }
    
    printf("%d:", sum);
    for (j = 0; j < num_rolls; j++) {
        printf(" %d", rolls[j]);
    }
    printf("\n");
}
