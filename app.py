from flask import Flask,render_template

app = Flask (__name__)

# sum of digits of a number until it becomes one!

def num2digit(sum):
    temp = 0
    while sum > 0:
        temp = temp + sum%10
        sum = sum//10
    if temp>9:
        return num2digit(temp)
    else:
        return temp

# simple function to count the sum of the alphabets in a word

def numerology(name): 
    sum=0
    for i in range(len(name)):      
        if name[i] in ['a','r','s']:
            sum+=1
        elif name[i] in ['b','q','t']:
            sum+=2
        elif name[i] in ['c','p','u']:
            sum+=3
        elif name[i] in ['d','o','v']:
            sum+=4
        elif name[i] in ['e','n','w']:
            sum+=5
        elif name[i] in ['f','m','x']:
            sum+=6
        elif name[i] in ['g','l','y']:
            sum+=7
        elif name[i] in ['h','k','z']:
            sum+=8
        elif name[i] in ['i','j']:
            sum+=9
        else:
            sum = -9999
    if sum > 0:
        sum = num2digit(sum)

    # Giving some random messages for a digit

    if (sum==1):
        message = "You are a sad person"
    elif (sum==2):
        message = "You are an angry person"
    elif (sum==3):
        message = "An introvert"
    elif (sum==4):
        message = "You have a golly nature"
    elif (sum==5):
        message = "You like to party"
    elif (sum==6):
        message = "Your revenge is bitter"
    elif (sum==7):
        message = "A nerd"
    elif (sum==8):
        message = "too much attitude"
    elif (sum==9):
        message = "you are a shy person"
    else:
        message = "I know who you are. THE ROBOT :P"
    return message


@app.route('/')  # main page
def hello():
    return render_template('index.html',message="hello brother, Lets have some fun!!",imgname="hello")

@app.route('/<username>') # dynamic route
def hello_user(username):
    username=username.lower()
    result = numerology(username)
    return render_template('index.html',message=username+": "+result,imgname="jenkins")

if __name__ == '__main__':
    app.run(host='0.0.0.0')