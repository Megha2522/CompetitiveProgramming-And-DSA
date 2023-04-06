# [String Task](https://codeforces.com/contest/118/problem/A)

```java
import java.util.*;
public class Program
{
    public static void main(String[] args) {

		Scanner sc =new Scanner(System.in);

        String Originalstr,str,newstr="";
        Originalstr=sc.nextLine();

        int l;
        l=Originalstr.length();
        str=Originalstr.toLowerCase();

        for(int i=0;i<l;i++)
        {
            char ch=str.charAt(i);
            if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'||ch=='y')
            newstr=newstr;
            else
            newstr=newstr+"."+ch;
        }
        System.out.println(newstr);
	}
}
```