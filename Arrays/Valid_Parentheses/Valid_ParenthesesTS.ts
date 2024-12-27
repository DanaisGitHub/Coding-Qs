const isValidTS = (s: string): boolean => {
    let square = 0,
        curly = 0,
        bracket = 0;
    let booleanResult = false;

    for (let i in s as any) { // i is the index not the character
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
        booleanResult = true;
    } else {
        booleanResult = false;
    }
    return booleanResult;
}

