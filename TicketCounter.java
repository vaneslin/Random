public class TicketCounter {
    /*** let [d, v] represent a ticket with 'd' digits (0 - 9) that add up to a sum of 'v'. Calculates # of total possible tickets ***/

    public static void main(String [] args){
        int digits = 8;
        int value = 20;

        /*
        * Test cases
        * [3 12] = 73
        * [4 22] = 540
        * [6 46] = 1287
        * [8 20] = 732474
        * [10 61] = 96130540
        */

        int answer = ticketCounter(digits, value);

        System.out.println("Tickets: " + answer);
    }

    private static int ticketCounter(int dig, int val){
        int count = 0;
        if (dig == 1){
            return 1;  //base case: i.e. [1 3], [1 9], or [1 2] only has one possible ticket solution
        } else {
            /*** Methodology: group all possible solutions by first digit, and then find each group separately
             valid tickets for [dig val] =
             valid tickets for [dig-1 val] (where first digit is 0 in [dig val])
             + valid tickets for [dig-1 val] (where first digit is 1 in [dig val])
             + valid tickets for [dig-1 val] (where first digit is 2 in [dig val])
             ...
             + valid tickets for [dig-1 val] (where first digit is 8 in [dig val])
             + valid tickets for [dig-1 val] (where first digit is 9 in [dig val]) ***/

            for (int num = 0; num <=9; num ++){  //num represents first digit in ticket
                if (val - num >= 0 && val - num <= 9*(dig-1)){  //checks if [dig-1 val] is a valid ticket i.e. [2 43] is impossible
                    count += ticketCounter(dig-1, val - num);
                }
            }
        }
        return count;
    }
}
