# [Petya and strings](https://codeforces.com/contest/112/problem/A)

```java
import java.util.*;
public class Program
{
    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        String str1,str2;
        int len;
        str1=sc.nextLine();
        str1=str1.toLowerCase();
        str2=sc.nextLine();
        str2=str2.toLowerCase();

        if(str1.compareTo(str2)==0)
        System.out.println(0);

        if(str1.compareTo(str2)>0)
        System.out.println(1);
             
        if(str1.compareTo(str2)<0)
        System.out.println(-1);
        
	}
}s
```