import random
def isValid(s):
    print(f's: {s}')
    op = "("
    ob = "["
    os = "{"
    cp = ")"
    cb = "]"
    cs = "}"
    o_symbols = [op, ob, os]
    c_symbols = [cp, cb, cs]

    # Find easiest subsets first: "()[]{}""
    for symbol in range(0, len(o_symbols)-1):
        if len(s) == 0:
                return True
        elif len(s) == 1:
            return False
        
        print(f'Evaluating: {o_symbols[symbol]}\nSearching for: {c_symbols[symbol]}')
        print('-----------')

        if o_symbols[symbol] == s[0] and c_symbols[symbol] == s[1]:
            print("Found a match pair in the first 2 indices!")
            print(f"Removing '{s[:2]}' from the list")
            s = s[2:]

            if len(s) > 1:  
                print("\nRecursing\n--------")
                return isValid(''.join(s))
    
        # Find more difficult subsets: eg. "({})"
        else:
            for val in range(0, len(s)-1, 1):
                left = s[val]
                right = s[val+1]
                #print(f"left-current: {left} || right-current: {right}")
                if left in o_symbols:
                    if right in c_symbols:
                        idx = o_symbols.index(left)

                        if left == o_symbols[idx] and right == c_symbols[idx]:
                            return isValid(s[:val] + s[val + 2:])
            if len(s) > 1:
                return False
                

### GENERATE TEST CASES ###
possible_values = "([{)]}"
test_case = [random.choice(possible_values) for i in range(100)]
n = 0

while not isValid(test_case):
    test_case = [random.choice(possible_values) for i in range(100)]
    print(isValid(test_case))
    n += 1

"""
'(){{}[}][][]' || False
'()[]{}()[]{}' || True
'()[]{[{}]}{}[]()' || True
()[]{}[] || True 
'()([][{}({})])' || True
"""
















"""
    print(f'Evaluating: {list(s)}')
    l = len(s)
    if l % 2 == 1:
        print('Uneven number of items')
        return False

    if len(s) == 0:
        return True
    
    mp = {'(':')', '[': ']', '{':'}'}

    while len(s) != 0:
        for i in range(0, l):
            for j in range(i + 1, l):

                # Found a possible companion subset
                if mp.get(s[i]) == s[j]:
                    
                    # The second letter is a closing pair match (e.g. '{}')
                    if j == i + 1:
                        print(f'companion index: {s[i:j+1]}')
                        print(f'subset found: {s[i+1:j]}')
                        print(f'second subset: {s[j+1:]}')

                        if (len(s[i + 1:j]) == 0) and (len(s[j+1:]) > 0):
                            return isValid(s[j+1:])

                        elif (len(s[j+1:]) == 0) and (len(s[i + 1:j]) > 0):
                            return isValid(s[i + 1:j])

                        else:
                            return isValid(s[i + 1:j]), isValid(s[j+1:])

                    else:
                        # find valid closing pair
                        first_sub_idx = i + 1
                        last_sub_idx = j
                        subset = s[first_sub_idx:last_sub_idx]

                        found_valid_subset = False
                        while found_valid_subset or (last_sub_idx < (len(s))):
                            print(f'subset: {list(subset)}') 
                            
                            open_brackets = []
                            closed_brackets = []
                            
                            for item in subset:
                                if item in mp.keys():
                                    open_brackets.append(item)
                                if item in mp.values():
                                    closed_brackets.append(item)
                            
                            if len(open_brackets) != len(closed_brackets):
                                last_sub_idx += 1
                                
                                print(f'last_sub_idx = {last_sub_idx} || len(s) = {len(s)}')
                                
                                if last_sub_idx == len(s):
                                    return False
                                
                                subset = s[first_sub_idx: last_sub_idx]
                                

                            else:
                                found_valid_subset = True
                                break

                        print(found_valid_subset)
                        print('I RETURNED')
                        return isValid(s[last_sub_idx+1:])                                 
    """