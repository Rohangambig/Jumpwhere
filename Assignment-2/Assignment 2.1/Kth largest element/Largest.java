import java.util.Arrays;

public class Largest {
    public static void main(String[] args) {
        int arr[] = new int[] {4,2,9,7,5,6,7,1,3};
        int k = 4;
        
        Arrays.sort(arr);
        System.out.println(arr.length-k);
    }    
}
