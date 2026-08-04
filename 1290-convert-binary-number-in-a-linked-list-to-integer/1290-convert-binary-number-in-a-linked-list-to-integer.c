/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <math.h>
int getDecimalValue(struct ListNode* head) {
    int i=0,a[30],n=-1,ans=0,j=0;
    struct ListNode *temp;
    temp=head;
    while(temp!=NULL){
        a[i++]=temp->val;
        temp=temp->next;
        n++;
    }
    for(i=n;i>=0;i--){
        ans+=a[i]*(pow(2,j));
        j++;
    }
    return ans;
}