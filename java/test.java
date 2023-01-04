class test {
    public static void main(String[] args) {
        System.out.println("Hello");
        System.out.println("Jack");
    }
}
class Exer_2 {
    public static void main(String[] args) {
        System.out.print(74 + 36);
    }
}
class Exer_3 {
    public static void main(String[] args) {
        System.out.print(50/3);
    }
}
class Exer_4 {
    public static void main(String[] arg) {
        System.out.println(-5 + 8 * 6);
        System.out.println((55+9) % 9);
        System.out.println(20 + -3*5 / 8);
        System.out.println(5 + 15 / 3 * 2 - 8 % 3);
    }
}
class Exer_5 {
    public double multiply(int a, int b) {
        return (a*b);
    }
    public static void main(String[] arg) {
        Exer_5 tester = new Exer_5();
        System.out.println(tester.multiply(5, 25));
    }
}
class InsertionSort {
    private int[] arry = new int[] {3,4,2,7,9,12,10,6,5,1,8};
    public InsertionSort() {}
    public void sortArry() {
        int n = arry.length;
        for (int i = 1; i < n; ++i) {
            int key = arry[i];
            int j = i - 1;
            while (j >= 0 && arry[j] > key) {
                arry[j + 1] = arry[j];
                j = j - 1;
            }
            arry[j + 1] = key;
        }
    }
    public void printArry() {
        for (int i: arry) {
            System.out.print(i + " ");
        }
    }
    public static void main(String[] args) {
        InsertionSort s = new InsertionSort();
        s.sortArry();
        s.printArry();
    }
}
class MergeSort {
}