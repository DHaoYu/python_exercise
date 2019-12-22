import java.io.DataInputStream;
import java.io.InputStream;
import java.net.Socket;



public class client {
	public static void main(final String[] args) throws Exception {
        final int c;
        Socket s1;
        InputStream s1In;
        DataInputStream dis;
        s1 = new Socket("localhost", 8080);
        s1In = s1.getInputStream();
        dis = new DataInputStream(s1In);
        final Strig st = new String(dis.readUTF());
      System.out.println(st);
      s1In.close();
      s1.close();
	}

}
