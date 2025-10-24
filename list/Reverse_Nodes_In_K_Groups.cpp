/**
 REVERSE NODES IN K-GROUP
 
 Problem: Given the head of a linked list, reverse the nodes of the list k at a time, 
 and return the modified list.
 
 LeetCode: https://leetcode.com/problems/reverse-nodes-in-k-group/
 Difficulty: Hard
 
 Example:
 Input: head = [1,2,3,4,5], k = 2
 Output: [2,1,4,3,5]
 
 Input: head = [1,2,3,4,5], k = 3
 Output: [3,2,1,4,5]
 
 Intuition:
 My first thought was that reversing exactly k nodes at a time in a linked list 
 seemed tricky because I can't just reverse a "middle" part of a linked list directly.
 
 The approach:
 1. Identify the k-th node from the current position
 2. Cut the list at that point (so this part becomes a smaller standalone linked list)
 3. Reverse this smaller list
 4. Reconnect it with the previous part of the list and continue with the rest
 
 Time Complexity: O(n) - We visit each node exactly once
 Space Complexity: O(k) due to recursion stack, O(1) if iterative reversal
 */

#include <iostream>
#include <vector>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    // Helper Function to get the kth node from the current node
    ListNode* getKthNode(ListNode* temp, int k) {
        k -= 1;
        while (temp && k > 0) {
            k--;
            temp = temp->next;
        }
        return temp;
    }

    // Function to reverse a linked list
    ListNode* reverseLL(ListNode* head) {
        if (!head || !head->next) return head;

        ListNode* newHead = reverseLL(head->next);
        ListNode* front = head->next;
        front->next = head;
        head->next = NULL;
        return newHead;
    }

    // Main function to reverse nodes in groups of k
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* temp = head;
        ListNode* prev = NULL;

        while (temp) {
            ListNode* kthNode = getKthNode(temp, k);
            if (!kthNode) {
                if (prev) prev->next = temp;
                break;
            }

            ListNode* nextNode = kthNode->next;
            kthNode->next = NULL;

            // Reverse the current k-group
            ListNode* newHead = reverseLL(temp);

            if (temp == head)
                head = newHead;
            else
                prev->next = newHead;

            prev = temp;
            temp = nextNode;
        }
        return head;
    }
};

// Utility functions for testing
ListNode* createLinkedList(vector<int> arr) {
    if (arr.empty()) return NULL;
    ListNode* head = new ListNode(arr[0]);
    ListNode* current = head;
    for (int i = 1; i < arr.size(); i++) {
        current->next = new ListNode(arr[i]);
        current = current->next;
    }
    return head;
}

void printLinkedList(ListNode* head) {
    while (head) {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;
}
int main() {
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 8};
    int k = 3;

    ListNode* head = createLinkedList(arr);
    cout << "Original List: ";
    printLinkedList(head);

    Solution sol;
    head = sol.reverseKGroup(head, k);

    cout << "Reversed in groups of " << k << ": ";
    printLinkedList(head);

    return 0;
}

//output:
// Original List: 1 2 3 4 5 6 7 8   
// Reversed in groups of 3: 3 2 1 6 5 4 7 8
