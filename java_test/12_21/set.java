import java.util.HashSet;

class set
{
    public static void main(String args[])
    {
        /*
        String s = "32154";
        System.out.print(s);
        Arrays.sort(s);
        System.out.print(Arrays.toString(s));
        */
        HashSet<String> hs = new HashSet<String>();
        hs.add("Tom");
        hs.add("jane");   

        System.out.println("Tom is in set:  " + hs.contains("Tom"));
        System.out.println("Jack is in set:  " + hs.contains("Jack"));
        for(String s : hs)
            System.out.print(s + " ");
    }
}