/*
 * Check if a word follows the 'i before e except after c' rule
 *
 * https://www.reddit.com/r/dailyprogrammer/comments/8q96da/20180611_challenge_363_easy_i_before_e_except/
 */

#include <stdio.h>

int check(const char *word);

int main(int argc, char *argv[])
{
    const char *word = argv[1];;

    printf("\"%s\": %s\n", word, check(word) ? "true" : "false");

    return 0;
}

int check(const char *word)
{
    int i;

    for (i = 0; word[i] != '\0'; i++) {
        if (i >= 1 && word[i] == 'i') {
            if (word[i-1] == 'e' && (i < 2 || word[i-2] != 'c'))
                return 0;
            if (word[i+1] == 'e' && word[i-1] == 'c')
                return 0;
        }
    }

    return 1;
}
