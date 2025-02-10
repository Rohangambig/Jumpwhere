import java.util.ArrayList;
public class GenerateParanthesis {
        public static void Helper(ArrayList<String> arr,int left,int right,int n,String str) {
            if(str.length() == n * 2) {
                arr.add(str);
                return;
            }
    
            if(left < n) Helper(arr,left+1,right,n,str + '(');
            if(right < left) Helper(arr,left,right+1,n,str + ')');
        }
    
        public static void main(String[] args) {
            int n = 4;
            ArrayList<String> ans = new ArrayList<String>();
            Helper(ans,0,0,n,"");
            
            for(String str:ans) {
                System.out.print(str+" ");
            }
        }

}
