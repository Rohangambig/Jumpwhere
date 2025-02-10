import java.util.Arrays;
public class Anagram
{
	public static void main(String[] args) {
		String string1 = "danger";
        String string2 = "garden";

        char[] char1 = string1.toCharArray();
        char[] char2 = string2.toCharArray();

        if(char1.length != char2.length) {
            System.out.println("Given string is not a anagram");
            System.exit(0);
        }
        
        
        Arrays.sort(char1);
        Arrays.sort(char2);


        if (Arrays.equals(char1, char2)) {
            System.out.println("Given strings are anagrams");
        } else {
            System.out.println("Given strings are not anagrams");
        }
	}
}
