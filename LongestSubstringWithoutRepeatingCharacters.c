#include <stdio.h>
#include <string.h>
int lengthOfLongestSubstring(char *s) {
    int m[129] = {-1};

    memset( m, -1, sizeof(m));
    int i = 0;
    int max = 0;
    int pre = 0;
    int count = 0;

    while( s[i] != '\0'){
        int c = s[i];
        count++;
        if ( m[c] != -1) {
            //printf( "==%d\n", m[c]);
            pre = m[c];
            m[c] = i;
            count = count > i - pre ? i -pre : count;
            //printf( "i %d max %d count %d \n", i, max, count );
        } else{
            m[c] = i;
        }
        i++;
        max = count > max? count : max;
    }
    return max;
}

int main(int argc, const char *argv[])
{
    char *s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ abcdefghijk`]'`]'`]'";
    printf( "%d\n", lengthOfLongestSubstring(s) );
    /*
     *printf( "%d\n", lengthOfLongestSubstring1(s) );
     */
    return 0;
}
