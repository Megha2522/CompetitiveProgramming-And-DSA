# 1] MAP ,2] DICT
map<int, string> myMap;
unordered_map<int, string> myDict;
### PUSH     
myMap[1] = "One";
### REMOVE
myMap.erase(1);
### EDIT
myMap[2] = "Two Updated";
### PRINT
for(auto i : myMap)
    i.first , i.second

# SET
set<int> mySet;
unordered_set<int> s;
### PUSH
mySet.insert(10);
### REMOVE
mySet.erase(10);
### EDIT
s.find(key) == s.end() // key doesnot exist
### PRINT
for (int element : mySet) 
    cout << element << " ";

# PAIR
pair<int, string> myPair = make_pair(1, "One");
pair<int, string> p1 = {1, "Geeks"};
vector<pair<int, string>> vec = {{1, "Apple"}, {2, "Banana"}};
### PUSH
myPair.first = 2;
myPair.second = "Two";
vectorName.push_back({element1, element2});
               or 
vectorName.push_back(make_pair(element1, element2));
### PRINT
myPair.first , myPair.second

# VECTOR
vector<int> myVector;
vector<int> v1 = {1, 4, 2, 3, 5};
vector<int> v2(5, 9); // output 9 9 9 9 9
### PUSH
myVector.push_back(10);
v.insert(v.begin() + 1, 'c'); // Inserting 'c' at index 1
### REMOVE
v.pop_back(); // Deleting last element 
v.erase(find(v.begin(), v.end(), 'f')); // Deleting element 'f'
v.erase(v.begin() + 2); // Deleting element at index '2'
### EDIT
myVector[0] = 25;
### PRINT

# SORT
sort(myVector.begin(), myVector.end());
