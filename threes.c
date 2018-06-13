/*
 * Play 'A Game of Threes' by repeadetly dividing a number by 3 until you get 1
 *
 * https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/ 
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    long num = strtol(argv[1], NULL, 10);

    while (num > 1) {
        printf("%d\n", num = num % 3 == 0 ? num / 3 : (num % 3 == 1 ? (num--) / 3 : (num++) / 3));
    }    

    return 0;
}
