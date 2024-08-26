

char * mergeAlternately(char * word1, char * word2){
    int len1 = strlen(word1);
    int len2 = strlen(word2);
    int totalLength = len1 + len2;
    char* str = (char*)malloc((totalLength + 1) * sizeof(char));
    int i=0,j=0,k=0;
    while(i<len1&&j<len2){
        str[k] = word1[i];
        k++;
        i++;
        str[k] = word2[j];
        k++;
        j++;
    }
    while(i<len1){
        str[k] = word1[i];
        k++;
        i++;
    }
    while(j<len2){
        str[k] = word2[j];
        k++;
        j++;
    }
    str[k] = '\0';
    return str;
}