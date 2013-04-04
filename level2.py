str_input = """{{[{{{{}}{{}}}[]}[][{}][({[(({{[][()()]}}{[{{{}}}]}))][()]{[[{((()))({}(())[][])}][]()]}{()[()]}]})][]]}{{}[]}}"""

reverse = {
    '}': '{',
    ')': '(',
    ']': '[',
    '{': '}',
    '[': ')',
    '(': ']' 
}

open_b = {
    '{': 0,
    '[': 0,
    '(': 0 
}

close_b = {
    '}': 0,
    ']': 0,
    ')': 0 
}

opened = []
for index, value in enumerate(str_input.replace("\n", "")):
    
    if value in open_b.keys():
        opened.append(value)

    if value in close_b.keys():
        if reverse[value] != opened.pop():
            print "Problem found at index: %s" % index;
            break;
