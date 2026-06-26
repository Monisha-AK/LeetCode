int maximumWealth(int** accounts, int accountsSize, int* accountsColSize) {
    int max=0,c,i,j;
    for(i=0;i<accountsSize;i++){
        c=0;
        for(j=0;j<accountsColSize[i];j++){
            c+=accounts[i][j];
        }
        if(c>max){
            max=c;
        }
    }
    return max;
}