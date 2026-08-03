/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode *temp,*p,*s;
    temp=head;
    if (head==NULL || head->next==NULL){return head;}
    p=head->next;
    while(p!=NULL){
        if(temp->val==p->val){
            s=p;
            p=p->next;
            temp->next=p;
            free(s);
        }
        else{
        temp = temp->next;
        p=p->next;}
    }
    return head;
}