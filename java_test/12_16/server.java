import java.io.DataOutput;
import java.io.DataOutputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class server {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		ServerSocket s = null;
		Socket s1;
		String sendString = "Hello Net Word!";
		OutputStream slout;
		DataOutput dos;
		try{
			s = new ServerSocket(8080);
		}catch(Exception e){
			e.printStackTrace();
		}
		
		while(true){
			try{
				s1 = s.accept();
				slout = s1.getOutputStream();
				dos =  new DataOutputStream(slout);
				dos.writeUTF(sendString);
				slout.close();
				s1.close();
			}catch(Exception e){
				e.printStackTrace();
			}
		}

	}
}
