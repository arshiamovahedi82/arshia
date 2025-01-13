while True :
    print ("select your option :\n\t1)Encrypt\n\t2)Decrypt\n\t3)Exit")
    choice = input("your choice : ")
    if choice == "1" :
        plain_text = input("text :")
        encrypt_text = ""
        for c in plain_text :
            x = ord(c) * 2 + 5
            encrypt_text += chr(x)
        print("encrypted text :" , encrypt_text)
        print("*" * 40 + "\n")    
    elif choice == "2" :
        encrypted_text = input("encrypted text :")
        plain_text = ""
        for c in encrypted_text :
            x = (ord(c) - 5) // 2
            plain_text += chr(x)
        print("encrypted text : " , plain_text)
        print("*" * 40 + "\n") 
    elif choice == "3" :
        print("auf widersien!")
        pass
    else :
        print ("your choice is wrong!")