import java.util.Arrays;
import java.util.Scanner;

public class Test{
    /*
    //
    public static void main(String[] args)
    {
        int i, j, k;
        for(int n = 100; n <= 999; n++)
        {
            i = n % 10;
            j = n / 10 % 10;
            k = n / 100;
            if(i*i*i + j*j*j + k*k*k == n)
                System.out.print(n + "\t");
        }
    }
    */
    /*
    //count
    public static void main(String[] args)
    {
        int countP = 0, countN = 0;
        int num;
        Scanner sc = new Scanner(System.in);
        do{
            num = sc.nextInt();
            if(num > 0)
                countP++;
            else if(num < 0)
                countN++;
        }while(num != 0);
        System.out.println("postive count: " + countP);
        System.out.println("negitive count: " + countN);
    }
    */
    /*
    public static void main(String[] args)
    {
        /*
        int[] arr = new int[10];
        arr[0] = 1;
        arr[1] = 2;
        System.out.println(arr[0]);
        */
        /*
        Integer[] arr = {4, 5, 3, 1};
        //Arrays.fill(arr, 10);
        Arrays.sort(arr);
        System.out.println(Arrays.toString(arr));
        for(int num : arr)
        {
            System.out.print(num +" ");
        }
        int ret = Arrays.binarySearch(arr, 4);
        System.out.print(ret + " " + arr[ret]);
    }
    */
    /*
    public static int romanToInt(String s)
    {
        char[] ch = s.toCharArray();
        int result = 0;
        for(int i = 0; i < ch.length; ++i)
        {
            switch(ch[i])
            {
                case 'M':result += 1000;break;
                case 'D':result += 500;break;
                case 'L':result += 50;break;
                case 'V':result += 5;break;
                case 'I':
                if(i + 1 < ch.length && (ch[i+1] == 'V' || ch[i+1]=='X'))
                {
                    result -= 1;
                }
                else
                {
                    result += 1;
                }
                break;
                case 'X':
                if(i + 1 < ch.length && (ch[i+1] == 'L' || ch[i+1] == 'C'))
                {
                    result -=10;
                }
                else
                {
                    result += 10;
                }
                break;
                case 'C':
                if(i + 1 < ch.length && (ch[i+1] == 'D' || ch[i+1] == 'M'))
                {
                    result -=100;
                }
                else
                {
                    result += 100;
                }
                break;
            }
        }
        return result;
    }
    public static void main(String[] args)
    {
        System.out.println(romanToInt("MCMXCIV"));
        System.out.println(romanToInt("LVIII"));
        
    }
    */
    /*
    public static void main(String[] args)
    {
        System.out.println(Integer.toString(100));
        System.out.println(Integer.toBinaryString(100));
    }    
    */
}
