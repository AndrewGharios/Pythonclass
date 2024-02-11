

def valid_password(password:str)->bool:
    '''check password -7 charcs long, one uppercase, one lowercase and one digit'''
    correct_length = False
    has_upper = False
    has_lower = False
    has_digit = False

    if len(password) >= 7:
        for chr in password:
            if chr isupper():
                has_upper = True
            if chr islower():
                has_lower = True
            if chr isdigit():
                has_digit = True
    if correct_lenght and has_upper and has_lower and has_digit:
          is_valid = True
    else:
        is_valid = False
    return is_valid


def main():
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    idnum = input("Enter student id: ")
    print("Your system login name is:")
    print(get_login_name(first,last,idnum))

#get_pass
[len(idnum)-3: ]
    password = input("Enter password")

    while not valid_password(password):
        print("Password not valid")
        password = input ("Enter password")
    print("Valid password")

def get_login_name(first:str,last:str,idnum:str)->str:
    set1 = first[0:3]
    set2 = last[0:3]
    set3 = idnum[-3:]
    print("Your login name is: ", set1+set2+set3




if __name__ == "__main__":
    main()

