// 1. The username is between 4 and 25 characters.
// 2. It must start with a letter.
// 3. It can only contain letters, numbers, and the underscore character.
// 4. It cannot end with an underscore character.


class App {

  public static boolean CodelandUsernameValidation(String str) {
    // code goes here
    if (str.length() < 4 || str.length() > 25) {
        return false;
    }

    if (!Character.isLetter(str.charAt(0))) {
        return false;
    }

    if ( str.endsWith("_")) {
        return false;
    }

    for (int i = 0; i < str.length(); i++) {
      if (Character.isLetter(str.charAt(i)) || Character.isDigit(str.charAt(i)) || str.charAt(i) == '_'){
        continue;
      }
      else {
        return false;
      }
    }
    return true;
  }

  public static void main (String[] args) {
    // keep this function call here
    String str = "aaaaaaaaaa";
    System.out.println(CodelandUsernameValidation(str));
    System.out.println();


  }

}