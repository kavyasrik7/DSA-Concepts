//                                                 Doublelinked.cpp
// A Doubly Linked List is a linear data structure made up of nodes where each node is connected to both its previous and next node.
// It allows traversal in both forward and backward directions — unlike a singly linked list which only moves forward.

// Structure of a Node
// Each node has three parts:
// Prev → Pointer to the previous node
// Data → Actual value stored in the node
// Next → Pointer to the next node
    // Example structure:
    // [ prev | data | next ]

// Example Diagram
//NULL ← [Prev|10|Next] ⇄ [Prev|20|Next] ⇄ [Prev|30|Next] → NULL
//Here:

// 10 is the first node (head)
// 30 is the last node (tail)
// Each node points to the one before and after it


//    Code

#include <iostream>
using namespace std;

// Node structure for Doubly Linked List
class Node {
public:
    int data;//value of the node
    Node* prev;//pointer to the previous node
    Node* next;//pointer to the next node

    Node(int val) {//constructor to initialize a new node
        data = val;//set the data
        prev = NULL;//set previous pointer to NULL
        next = NULL;//set next pointer to NULL
    }
};

// Doubly Linked List class
class DoublyLinkedList {
private:
    Node* head;//pointer to the first node
    Node* tail;//pointer to the last node

public:
    DoublyLinkedList() {
        head = NULL;//initialize head pointer
        tail = NULL;
    }

    // Insert at beginning
    void insertAtBeginning(int val) {
        Node* newNode = new Node(val);
        if (!head) { // empty list
            head = tail = newNode;
        } else {
            newNode->next = head;//link new node to current head
            head->prev = newNode;//link current head back to new node
            head = newNode;//update head to new node
        }
    }

    // Insert at end
    void insertAtEnd(int val) {
        Node* newNode = new Node(val);
        if (!tail) { // empty list
            head = tail = newNode;
        } else {
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
    }

    // Insert at specific position (1-based index)
    void insertAtPosition(int pos, int val) {
        if (pos <= 1) {
            insertAtBeginning(val);
            return;
        }

        Node* temp = head;
        for (int i = 1; i < pos - 1 && temp; i++)
            temp = temp->next;

        if (!temp || !temp->next) {
            insertAtEnd(val);
            return;
        }

        Node* newNode = new Node(val);
        newNode->next = temp->next;//link new node to next node
        newNode->prev = temp;//link new node back to current node
        temp->next->prev = newNode;//link next node back to new node
        temp->next = newNode;//link current node to new node
    }

    // Delete from beginning
    void deleteFromBeginning() {
        if (!head) {
            cout << "List is empty!\n";
            return;
        }

        Node* temp = head;
        if (head == tail) { // single node
            head = tail = NULL;
        } else {
            head = head->next;
            head->prev = NULL;
        }
        delete temp;
    }

    // Delete from end
    void deleteFromEnd() {
        if (!tail) {
            cout << "List is empty!\n";
            return;
        }

        Node* temp = tail;
        if (head == tail) {
            head = tail = NULL;
        } else {
            tail = tail->prev;
            tail->next = NULL;
        }
        delete temp;
    }

    // Delete from specific position
    void deleteFromPosition(int pos) {
        if (pos <= 1) {
            deleteFromBeginning();
            return;
        }

        Node* temp = head;//start from head
        for (int i = 1; i < pos && temp; i++)
            temp = temp->next;

        if (!temp) {
            cout << "Position out of range!\n";
            return;
        }

        if (temp == tail) {
            deleteFromEnd();
            return;
        }

        temp->prev->next = temp->next;
        temp->next->prev = temp->prev;
        delete temp;
    }

    // Display list forward
    void displayForward() {
        Node* temp = head;
        cout << "Forward: ";
        while (temp) {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }

    // Display list backward
    void displayBackward() {
        Node* temp = tail;
        cout << "Backward: ";
        while (temp) {
            cout << temp->data << " ";
            temp = temp->prev;
        }
        cout << endl;
    }
};

// Main function for testing
int main() {
    DoublyLinkedList dll;

    dll.insertAtEnd(10);
    dll.insertAtEnd(20);
    dll.insertAtEnd(30);
    dll.displayForward();

    dll.insertAtBeginning(5);
    dll.displayForward();

    dll.insertAtPosition(3, 15);
    dll.displayForward();
    dll.displayBackward();

    dll.deleteFromPosition(2);
    dll.displayForward();

    dll.deleteFromEnd();
    dll.displayForward();

    dll.deleteFromBeginning();
    dll.displayForward();

    return 0;
}

//Output
//Forward: 10 20 30
//Forward: 5 10 20 30
//Forward: 5 10 15 20 30

//Backward: 30 20 10 5
//Backward: 30 20 15 10 5





// Advantages of Doubly Linked List

// 1.Bidirectional traversal:
// You can move both forward and backward easily.
// 2.Easier deletion:
// Deleting a node is simpler — no need to track the previous node separately as in singly linked lists.
// 3.Efficient insertion/deletion in middle:
// Faster than arrays because you don’t need to shift elements.
// 4.Flexible memory usage:
// Size can grow/shrink dynamically.


// Disadvantages of Doubly Linked List
// 1.Extra memory:
// Each node requires additional memory for the previous pointer.
// 2.Complex implementation:
// More pointers to manage (next and prev), making the code more complex.
