public class Index {
    public static void main(String[] args) {
        int nums[] = {2,3,5,5,5,5,5,7,9,9};
        int size =  nums.length;
        int target = 5;

        int first  = -1, last = - 1;
        int i = 0 , j = size-1;

        while( i < size || j >= 0) {
            if( i < size && nums[i] == target) {
                first = i; i = size;
            }

            if(j >= 0  && nums[j] == target) {
                last = j; j = -1;
            }
        }

        System.out.println(first+" , " +last);
    }
}