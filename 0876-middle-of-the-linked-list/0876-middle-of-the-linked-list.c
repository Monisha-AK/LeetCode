/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    int c=0;
    struct ListNode *temp=head,*p=head;
    while(temp!=NULL){
        c++;
        temp=temp->next;
    }
    if (c%2==0)
        c=c/2+1;
    else 
        c=(c+1)/2;
    for(int i=1;i<c;i++){p=p->next;}
    return p;
}