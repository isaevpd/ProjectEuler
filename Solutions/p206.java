public class p206
{
    private static String nthdigit(int x, int n)
    {
        while (n > 0)
        {
            n--;
            x /= 10;
        }
        return (x % 10) + "0";
    }
    public static void main(String[] args)
    {
        System.out.println(p206.nthdigit(12, 1));
    }
}