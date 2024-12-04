import heapq

class binaryTree:
    def _init_(self,value,freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

class huffmanCode:

    def _init_(self,path):
        self.path = path
        self.heap = []
        self.code = {}
    
    def lessThan(self,other):
        return self.freq < other.freq

    def equalTo(self,other):
        return self.freq == other.freq

    def count_freq(self,text):
        freq_count = {}
        for char in text:
            if char in freq:
                freq_count[char] += 1
            else:
                freq_count[char] = 1
        return freq_count

    def build_heap(self,freq_dict):
        for key in freq_dict:
            frequency = freq_dict[key]
            binary_tree_node = binaryTree(key,frequency)
            heapq.heappush(self.heap , binary_tree_node)

    def build_BTree(self):
        while len(self.build_heap) > 1:
            bTree_node1 = heapq.heappop(self.build_heap)
            bTree_node2 = heapq.heappop(self.build_heap)

            # sum freq of both nodes and push back to heap
            sum_n12 = bTree_node1.freq + bTree_node2.freq
            newNode = binaryTree(None,sum_n12)
            newNode.left = bTree_node1
            newNode.right = bTree_node2
        return

    def build_BTree_code_helper(self,root,curr_bits):
        if root is None:
            return
        if root.value is not None:
            self.code[root.value] = curr_bits
            return
        self.build_BTree_code_helper(root.left , curr_bits + '0')
        self.build_BTree_code_helper(root.right , curr_bits + '1')

    def build_BTree_code(self):
        root = heapq.heappop(self.build_heap)
        self.build_BTree_code_helper(self,'')
    
    def build_encoded_text(self,text):
        encoded_text = ""
        for char in text:
            encoded_text += self.code[char]
        return encoded_text

    def compression(self):

        # To access the file and get text of the file
        text = "aguhiwdvawuhfsefuheifjwevdgawfj"

        # Count frequency of each char in text
        freq_dict = self.count_freq(text)

        # Create min heap to extract 2 min freq 
        min_heap = self.build_heap(freq_dict)

        # Create binary Tree from heap
        self.build_BTree()

        # Construct code [left->0 , right->1] and store in dict
        self.build_BTree_code()

        # Build encoded text
        encoded_text = self.build_encoded_text(text)
        
        # Return binary file as output