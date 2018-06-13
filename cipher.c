/*
 * Encode a string using 'The Alphabet Cipher' and a given key
 *
 * https://www.reddit.com/r/dailyprogrammer/comments/879u8b/20180326_challenge_355_easy_alphabet_cipher/
 */

#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    // requires 2 string args - key then message
    const char *key = argv[1];
    char *msg = argv[2];

    size_t key_len = strlen(key);
    int i;

    for (i = 0; msg[i] != '\0'; i++) {
        msg[i] = (msg[i] + key[i % key_len] - 2 * 'a') % 26 + 'a';
    }

    printf("%s\n", msg);

    return 0;
}
