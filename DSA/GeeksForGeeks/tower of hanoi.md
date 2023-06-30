# [Tower of Hanoi](https://practice.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1)
```java
class Hanoi {

    public long toh(int N, int from, int to, int aux) {
        // base condition 
        if(N==0) return 0;
        //step 1
        long left = toh(N-1,from,aux,to);
        //step 2
        System.out.println("move disk " + N + " from rod " + from + " to rod "+ to);
        //step 3
        long right = toh(N-1,aux,to,from);
        
        return left+right+1;
    }
}
```