#include <stdlib.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// Function prototypes
struct ListNode* newNode(int val);



// Solution function
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* head = NULL;
    struct ListNode* sum = NULL;
    int carry = 0;

    while (l1 != NULL || l2 != NULL || carry > 0) {
        int digit_sum = carry;
        if (l1 != NULL) {
            digit_sum += l1->val;
            l1 = l1->next;
        }
        if (l2 != NULL) {
            digit_sum += l2->val;
            l2 = l2->next;
        }
        carry = digit_sum / 10;

        if (head == NULL) {
            sum = newNode(digit_sum % 10);
            head = sum;
        } else {
            sum->next = newNode(digit_sum % 10);
            sum = sum->next;
        }
    }

    return head;
}



// Function to allocate a new node and handle exceptions
struct ListNode* newNode(int val) {
    struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
    if (node) {
        node->val = val;
        node->next = NULL;
    }
    return node;
}