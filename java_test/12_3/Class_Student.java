import java.util.Scanner;

class Student{
		String school_name;
		int number;
		String sex;
		String birthday;
		String name;
		int score;
		void SetName(String _name)
		{
			name = _name;
			System.out.println("姓名："+name);
		}
		void SetScore(int _score)
		{
			score = _score;
			System.out.println("成绩："+score);
		}
}

class Undergraduate extends Student{
	String department;
	String major;
	void SetDepartment(String _dep)
	{
		department = _dep;
		System.out.println("系别："+department);
	}
	void SetMajor(String _maj)
	{
		major = _maj;
		System.out.println("专业："+major);
	}
}
public class Class_Student {
	public static void main(String[] args) {
		Undergraduate ug = new Undergraduate();
		ug.SetDepartment("信息学院");
		ug.SetMajor("软件工程");
		ug.SetName("zhangsan");
		ug.SetScore(100);
	}
}
