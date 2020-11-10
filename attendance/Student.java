package attendance;
/* Written by Matthew Korfhage 11/9/20
Last updated --/--/--
Nicolet High School - Fabrication Capstone
==========================================
This class stores and modifies student data. It contains methods for retrieving this data 
in memory along with constructors for creating new students during admission cycles or when
enrollment of an individual is changed. Currently needs to implement arrays to access the "Student"
objects easier.
==========================================*/
public class Student{
    private String firstName = "John";
    private String lastName = "Doe";
    private int id = 00000;
    boolean isTardy;
    boolean isAbsent;
    int numOfPeriods;
//This adds a new student to the database in memory
    public Student(String studentFirst, String studentLast, int studentID){
        firstName = studentFirst;
        lastName = studentLast;
        id = studentID;
    }
//This modifies the first name of a student
    public void changeFirst(String newName){
        firstName = newName;
    }
//This modifies the last name of a student
    public void changeLast(String newName){
        lastName = newName;
    }
//This modifies the ID of a student
    public void changeID(int newID){
        id = newID;
    }
//This returns a value of true or false depending on if a student is on time or not
//A value of "false" means the stdent isn't on time.
    public boolean onTimeQuery(){
        if(isTardy==true || isAbsent == true){
            return false;
        }
        else{
            return true;
        }
    }
//Calling this allows you to retrieve or view a student's info by printing the Student
//object directly from the main function i.e. "System.out.println(student1);"
    public String toString(){
        return lastName + ", " + firstName + " ID#: " + id;
    }
}