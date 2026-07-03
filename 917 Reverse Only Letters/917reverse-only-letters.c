char* reverseOnlyLetters(char* s) {
    char temp;
    int i=0,j;
    j=strlen(s)-1;
    while(i<j){
        while(i<j && !((s[i]>='a' && s[i]<='z') || (s[i]>='A' && s[i]<='Z'))){i++;}
        while(i<j && !((s[j]>='a' && s[j]<='z') || (s[j]>='A' && s[j]<='Z'))){j--;}
        if(i<j){
            temp=s[i];
            s[i]=s[j];
            s[j]=temp;
            i++;
            j--;
        }
    }
    return s;
}