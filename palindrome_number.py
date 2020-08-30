def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True     

        l = []
        while x > 0:
            remainder = x % 10
            x = x // 10
            l.insert(0, remainder)

        is_even = len(l) % 2 == 0
        low = 0
        high = len(l) - 1

        if is_even:
            print('---Number is Even---')
            left_mid = len(l) / 2 - 1
            right_mid = len(l) / 2 
            
            while high >= right_mid and low <= left_mid:

                print(f'high: {high} || low: {low}')
                print(f'h val: {l[high]} || l val: {l[low]}')
                if l[low] != l[high]:
                    return False
                
                high -= 1
                low  += 1

        else:
            print('---Number is Odd---')
            mid = len(l) // 2
            left_mid  = mid - 1
            right_mid = mid + 1

            while high >= right_mid and low <= left_mid:

                
                print(f'high: {high} || low: {low}')
                print(f'h val: {l[high]} || l val: {l[low]}')
                if l[low] != l[high]:
                    return False
                
                high -= 1
                low  += 1

        return True
