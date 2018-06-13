/*
 * Encode string into Rövarspråket
 *
 * https://www.reddit.com/r/dailyprogrammer/comments/341c03/20150427_challenge_212_easy_r%C3%B6varspr%C3%A5ket/
 */

#include <stdio.h>

int isvowel(char c);

int main(int argc, char *argv[])
{
    const char *phrase = argv[1];
    int i;

    for (i = 0; phrase[i] != '\0'; i++) {
        if (isvowel(phrase[i]) || !isalpha(phrase[i]) || isdigit(phrase[i]))
            putchar(phrase[i]);
        else
            printf("%c%c%c", phrase[i], 'o', tolower(phrase[i]));
    }  

    putchar('\n');    

    return 0;
}

int isvowel(char c)
{
    c = tolower(c);

    if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
        return 1;

    return 0;
}
