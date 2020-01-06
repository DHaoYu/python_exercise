class ThreadTest1 extends Thread
{
    private String flag;
    public ThreadTest1(String flag)
    {
        this.flag = flag;
    }
    public void run()
    {
        int i = 0;
        while(true)
        {
            System.out.print(flag + ":" + i + " " + '\t');
            i++;
            if(i > 10)
                break;
        }
    }
}

public class ThreadTest
{
    public static void main(String[] args) 
    {
        ThreadTest1 tt1 = new ThreadTest1("A");
        ThreadTest1 tt2 = new ThreadTest1("B");
        ThreadTest1 tt3 = new ThreadTest1("C");
        tt1.start();
        tt2.start();
        tt3.start();
        //System.out.println("sdf");
    }
}