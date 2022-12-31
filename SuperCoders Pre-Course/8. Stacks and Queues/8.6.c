int precedence(char c) {
    if (c == '^') return 3;
    if (c == '*' || c == '/') return 2;
    if (c == '+' || c == '-') return 1;
    return 0;
}
int infixToPostfix(char exp[], char output[]) {
    char stack[100];
    int stack_top = 0;
    int output_length = 0;
    for (int i = 0; i < strlen(exp); i++) {
        char c = exp[i];
        if (c == '(') {
            stack[stack_top++] = c;
        } else if (c == ')') {
            while (stack_top > 0 && stack[stack_top - 1] != '(') {
                output[output_length++] = stack[--stack_top];
            }
            stack_top--;
        } else if (c == '+' || c == '-' || c == '*' || c == '/' || c == '^') {
            while (stack_top > 0 && precedence(stack[stack_top - 1]) >= precedence(c)) {
                output[output_length++] = stack[--stack_top];
            }
            stack[stack_top++] = c;
        } else {
            output[output_length++] = c;
        }
    }
    while (stack_top > 0) {
        output[output_length++] = stack[--stack_top];
    }
    output[output_length] = '\0';
}