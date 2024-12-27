function isValid(s) {
  let square = 0,
    curly = 0,
    bracket = 0;
  let isValid = false;

  for (const i in s) { // i is the index not the character
    switch (s[i]) {
      case "(":
        bracket++;
        break;
      case "{":
        curly++;
        break;
      case "[":
        square++;
        break;
      case ")":
        bracket--;
        break;
      case "}":
        curly--;
        break;
      case "]":
        square--;
        break;
    }
  }

  if (curly === 0 && square === 0 && bracket === 0) {
    isValid = true;
  } else {
    isValid = false;
  }
  return isValid;
}

console.log(isValid("()()())"));
