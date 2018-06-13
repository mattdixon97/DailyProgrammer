/*
 * Tally occurrences of lower case vs upper case letters
 *
 * https://www.reddit.com/r/dailyprogrammer/comments/8jcffg/20180514_challenge_361_easy_tally_program/
 */

#include <stdio.h>

#define NUM_PLAYERS 5

int main(int argc, char *argv[]) 
{
    const char *s = argv[1];
    int scores[NUM_PLAYERS] = {0};
    int i, j;
    char c;

    for (i = 0; isalpha(s[i]); i++) {
        j = tolower(s[i]) - 'a';
        scores[j] += isupper(s[i]) ? -1 : 1;
    }

    for (c = 'a'; c < ('a' + NUM_PLAYERS); c++) {
        printf("%c: %d%s ", c, scores[c-'a'], (c-'a') == (NUM_PLAYERS-1) ? "\n" : ", ");
    }

    return 0;
}
