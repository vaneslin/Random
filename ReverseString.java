
public class ReverseString {
    /*** basic string reversion ***/

    public static void main(String[] args){
        String reversed = reverseString("I am MWPSB Enforcer, Kougami Shinya");
        System.out.println(reversed);
    }

    private static String reverseString(String in){
        String rev = "";
        for (int i = in.length(); i > 0; i--){
            rev+=in.substring(i-1, i);
        }
        return rev;
    }
}
