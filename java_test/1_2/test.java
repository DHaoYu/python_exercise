import java.util.*;

class test
{
    public static int max(List<Integer> list) {
        int maxValue = list.get(0);
        for (int i = 1; i < list.size(); ++i)
           if(list.get(i) > maxValue) 
             maxValue = list.get(i);
        return maxValue;
    }
    public static void main(String[] args)
    {
        List<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(5);
        list.add(3);
        list.add(4);
        System.out.println(max(list));
    }    
}