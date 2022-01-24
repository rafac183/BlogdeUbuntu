class Main {
  public static void showSubstrings(String text, int start, int end) {
    System.out.println(text.substring(start,end));
  }
  
  public static void main(String[] args) {
    String text = "LasFloresAzules";
    showSubstrings(text, 3, 9);
  }
}