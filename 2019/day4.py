def main():
    count = 0
    for i in range(168630, 718099):
        if check_password(str(i)):
            count += 1
    print(count)

def check_password(passw):
    return passw == "".join(sorted(passw)) and only_double_is_present(passw)

def double_is_present(string):
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            return True
    return False

def only_double_is_present(string):
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            right = True
            if i < len(string) - 2:
                right = string[i] != string[i+2]
            left = True
            if 0 < i:
                left = string[i-1] != string[i]
            if left and right:
                return True
    return False

main()
