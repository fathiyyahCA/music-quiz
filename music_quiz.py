name=str
password=str
name=input("Hello!Please enter your name!")

password="secret" #the password to guess

for i in range(3):

    user_password=input("Please enter your password")
    if user_password==password:
        print("Authentication successful!")
        break
    else:
        print("Incorrect password.Please try again.")

else:
    print("you have exceeded the maximum number of tries. Access denied")
    exit()


print("hello",name ,"lets start the quiz!")

#my list !!
songs=[("butterfly","BTS","this song was released in 2015")]


score=0


for songs,artist,info in songs:
    print(f"Guess the artist for the songs:{songs}")
    for i in range(3):
        guess=input("Enter your guess:")
        if guess.lower()==artist.lower():
            print("you got it right!")
            if i==0:
                score+=1
            break
        else:
            if i==2:
                print(f"sorry,you didnt get it right .The artist for the song {song} is {artist}")
            else:
                print("sorry,try again.")

print(f"your final score is {score}.well done !!:-))")
