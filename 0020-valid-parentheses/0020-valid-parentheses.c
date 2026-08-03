bool isValid(char* s) {
    char stack[10000];
    int j=0;
    for (int i=0;s[i]!='\0';i++){
        if(s[i]=='(' || s[i]=='[' || s[i]=='{'){
            stack[j++]=s[i];
        }
        else if (s[i]==')'){
            if (j==0){return false;}
            if (stack[j-1]=='('){
                j--;
            }
            else {return false;}
        }
        else if (s[i]==']'){
            if (j==0){return false;}
            if (stack[j-1]=='['){
                j--;
            }
            else {return false;}
        }
        else if (s[i]=='}'){
            if (j==0){return false;}
            if (stack[j-1]=='{'){
                j--;
            }
            else {return false;}
        }
        else {return false;}
    }
    if (j==0){return true;}
    return false;
}