# Stack

## Stack using Link List
```c++
struct Node {
    int data;
    Node* next;
    Node(int data, Node* next = nullptr){
        this->data = data;
        this->next = next;
    }
};

class Stack {
    Node* top;

    Node* insert(Node* top,int data){
        Node* newNode = new Node(data);

        // Stack is not empty
        if(top != nullptr)
            newNode->next = top;

        top = newNode;
        return top;
    }

    Node* del(Node* top){
        if(top == nullptr){
            cout<<"Stack Underflow\n";
        } else {
            cout<< "deleted " << top->data << endl;
            top = top->next;
        }
        return top;
    }

    void print(Node* top){
        Node* ptr = top;
        while(ptr != nullptr){
            cout<< ptr->data<<"->";
            ptr = ptr->next;
        }
        cout<<"NULL\n";
    }
};
```