import zipfile ,itertools ,os ,time

def main():
    all_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_@.'
    num = '1234567890'
    alph = 'abcdefghijklmnopqrstuvwxyz'
    cap_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    password_type = input (
                            "Choose your password type : \n \
                            All characters (-_@.)          : 1 \n \
                            Alphabetic only                : 2 \n \
                            Capital letter alphabetic only : 3 \n \
                            Numbers only                   : 4 \n \
                            Alphabetic + Numbers           : 5 \n \
                            All characters - (-_@.)        : 6 \n \
                                Your Choise : "
                            )
    input_list = [str(i) for i in range(7)]
    while password_type not in input_list :
        password_type = input ("Please select in range : ")
    types = {
                "1":all_char ,
                "2":alph ,
                "3":cap_alph ,
                "4":num  ,
                "5":alph+num ,
                "6":alph+num+cap_alph
                }
    string = types[password_type]
    min_lenght = input ("Min lenght of password : ")
    try :
        min_lenght = int(min_lenght)
    except :
        print (
                "Invalid entry . \n \
                Auto set min lenght of password == 6 " 
                )
        min_lenght = 6
    max_lenght = input ("Max lenght of password : ")
    try :
        max_lenght = int (max_lenght)
    except :
        print (
                "Invalid entry . \n \
                Auto set max lenght of password == 8 " 
                )
        max_lenght = 9
    print_mod = input (
                        "Do you want to see wrong passwords ? \n \
                        This will increase the running time of the program [yes/any] : "
                        )
    def password(string) :
        for i in range (min_lenght ,max_lenght+1) :
            res = itertools.product(string ,repeat=i)
            for i in res: 
                password =''.join(i)
                password = bytes(password ,"utf-8")
                yield password

    loop = True
    while loop :
        path = input ("Your Zipfile path : ")
        try :
            f = zipfile.ZipFile(path,"r")
            loop = False
        except :
            print ("File not Found")
    path_unzip = os.getcwd() + "/unzip_file" 
    s = time.time()
    while True  :
        for password in password(string) :
            try :
                f.extractall(path=path_unzip , pwd=password)
                print(f"your password is : {password}")
                complete = True
                break
            except:
                if print_mod :
                    print (f"{password} is not the password" )
                else : pass
        if complete :
            final_time = int(time.time() - s)
            if  final_time < 60 : print(f"time to find password : {final_time} sec" )
            else : print(f"time to find password : {final_time / 60} min ") 
            break 
if __name__ == "__main__":
    main()
             