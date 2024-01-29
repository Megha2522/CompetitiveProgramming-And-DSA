# [ZigZag Tree Traversal](https://www.geeksforgeeks.org/problems/zigzag-tree-traversal/1)

```c++
class Solution{
    public:
    //Function to store the zig zag order traversal of tree in a list.
    vector <int> zigZagTraversal(Node* root)
    {
    	vector<int> res;
    	queue<Node*> q;
    	int level = 0;
    	
    	if(root == nullptr) return res;
    	
    	q.push(root);
    	
    	while(!q.empty()){
    	    
    	    vector<int> temp;
    	    int len = q.size();
    	    
    	    for(int i=0 ; i<len ; i++){
    	        Node* node = q.front();
    	        temp.push_back(node->data);
    	        q.pop();
    	   
    	        if(node->left != nullptr) q.push(node->left);
                if(node->right != nullptr) q.push(node->right);
                
    	    }
    	    
    	    if(level%2 == 0){
        	    for(int j=0 ; j<temp.size() ; j++){
        	        res.push_back(temp[j]);
        	    }
    	    }
    	    else{
    	        for(int j=temp.size()-1 ; j >= 0 ; j--){
        	        res.push_back(temp[j]);
        	    }
    	    }
    	    level++;

    	}
    	return res;
    }
};
```