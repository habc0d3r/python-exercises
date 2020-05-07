#Todo : Health management system:::
# 1st program will ask if i want log or to retrive
# Write a function that when executed takes as input client name
# then asks for what he wants to log Diet or Exercise
# 3 clients - Udi , Deba , Sam
# Total 6 files for diet and exercise log
# get time
# and write one more function for retrieve exercise or food for any client
# at the end it will say you have successfully wrote
##########~~~~~##########~~~~~############~~~~~~~~~~~~@@@$@@@~~~~~~~~~~~~###########~~~~~############~~~~~~##########

def getdate():
    import datetime
    return datetime.datetime.now()


print("What do you want: ", end=' ~ ')
n = int(input("1.for Log 2.for Retrieve \n"))
if n == 1:
    print("Log")
    c = int(input("For what you want to Log/Retrieve: \n 1.Diet \n 2.Exercise\n"))
    if c == 1:
        client = int(input("For whom ~\n1.Udi\n2.Deba\n3.Sam \n"))
        if client == 1:
            udi = input('=>', )
            with open("udiF.txt", 'a') as f:
                a = f.write(str([str(getdate())])+ ':' + udi + "\n")
            print("Successfully Written")
        elif client == 2:
            deba = input(getdate())
            with open("debaF.txt", 'a') as f:
                a = f.write(str([str(getdate())])+ ':' + deba + "\n")
            print("Successfully Written")
        else:
            sam = input(getdate())
            with open("samF.txt", 'a') as f:
                a = f.write(str([str(getdate())])+ ':' + sam + "\n")
            print("Successfully Written")
    else:
        client = int(input("For whom ~\n1.Udi\n2.Deba\n3.Sam \n"))
        if client == 1:
            udi = input(getdate())
            with open("udiExe.txt", 'a') as f:
                a = f.write(str([str(getdate())])+ ':' + udi + "\n")
            print("Successfully Written")
        elif client == 2:
            deba = input(getdate())
            with open("debaExe.txt", 'a') as f:
                a = f.write(str([str(getdate())])+ ':' + deba + "\n")
            print("Successfully Written")
        else:
            sam = input(getdate())
            with open("samExe.txt", 'a') as f:
                a = f.write(str([str(getdate())])+ ':' + sam + "\n")
            print("Successfully Written")
else:
    print("Retrieve")
    c = int(input("For what you want to Log/Retrieve: \n 1.Diet \n 2.Exercise\n"))
    if c == 1:
        client = int(input("For whom ~\n1.Udi\n2.Deba\n3.Sam \n"))
        if client == 1:
            with open("udiF.txt") as f:
                a = f.read()
                print(getdate(), a)
        elif client == 2:
            with open("debaF.txt") as f:
                a = f.read()
                print(getdate(), a)
        else:
            with open("samF.txt") as f:
                a = f.read()
                print(getdate(), a)
    else:
        client = int(input("For whom ~\n1.Udi\n2.Deba\n3.Sam \n"))
        if client == 1:
            with open("udiExe.txt") as f:
                a = f.read()
                print(getdate(), a)
        elif client == 2:
            with open("debaExe.txt") as f:
                a = f.read()
                print(getdate(), a)
        else:
            with open("samExe.txt") as f:
                a = f.read()
                print(getdate(), a)