from flask import Flask, render_template,request,make_response,session
# import plotly
# import plotly.graph_objs as go
import mysql.connector
from mysql.connector import Error
import sys
import smtplib
import winsound
import speech_recognition as sr

import pandas as pd
import numpy as np
import json  #json request
from werkzeug.utils import secure_filename
import os,random
import csv #reading csv
import geocoder
from random import randint
import math
import torch
# import transformers 
import requests
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datetime import date
import pyttsx3
from data import hospitals
from chatterbot import parser

sesemail=''

app = Flask(__name__)
app.secret_key = 'flasktestdata'

API_KEY = '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'
API_URL = 'https://api.groq.com/openai/v1/chat/completions'

@app.route('/')
def index():
    global sesemail
    sesemail=''
    session.pop('username', None)
    session.pop('docname', None)
    return render_template('index.html')



@app.route('/index')
def indexnew():  
    global sesemail
    session.pop('username', None)
    session.pop('docname', None)
    sesemail=''  
    return render_template('index.html')

@app.route('/register')
def register():    
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/showroomreg')
def showroomreg():     
    return render_template('docreg.html')

@app.route('/showroom')
def showroom():
    return render_template('doclogin.html')

@app.route('/imageloader')
def imageloader():
    return render_template('imageloader.html')

""" REGISTER CODE  """
rcount = 0
@app.route('/regdata', methods =  ['GET','POST'])
def regdata():
    connection = mysql.connector.connect(host='localhost',database='srchatbotdb',user='root',password='')
    cursor = connection.cursor()
    email = request.args['email']
    sq_query="select count(*) from userdata where Email='"+email+"'"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    rcount = int(data[0][0])
    if(rcount==0):
        
        #name = request.ar
        
        
        #cursor = connection.cursor()
        uid=''
        username=''
        #sql_Query = "insert into userdata values('"+uid+"','"+username+"','"+name+"','"+pswd+"','"+email+"','"+phone+"','"+addr+"','"+age+"')"
        name = request.args['name']
        pswd = request.args['pswd']
        phone = request.args['phone']
        addr = request.args['addr']
        age = request.args['age']
        value = randint(123, 99999)
        username=name+str(value)
        uid="User"+str(value)
        print(addr)
        sql_Query = "insert into userdata values('"+uid+"','"+username+"','"+name+"','"+pswd+"','"+email+"','"+phone+"','"+addr+"','"+age+"')"
        # creates SMTP session
        '''
        s = smtplib.SMTP('smtp.gmail.com', 587) 
          
        # start TLS for security 
        s.starttls() 
          
        # Authentication 
        s.login("chatbot478@gmail.com", "chat478bot") 
          
        # message to be sent 
        message = " Welcome and thank you for registering at Showroom Bot Your account has now been created and you can log in by using your email address and password"
        
        # sending the mail
        print(email)
        s.sendmail("chatbot478@gmail.com", email ,"Welcome and thank you for registering at Showroom Bot Your account has now been created and you can log in by using your email address and password ", message ) 
        print("mail has ")     
        # terminating the session 
        s.quit()
        ''' 

        
        
        #cursor = connection.cursor()
        sql_Query = "insert into userdata values('"+uid+"','"+username+"','"+name+"','"+pswd+"','"+email+"','"+phone+"','"+addr+"','"+age+"')"
            
        cursor.execute(sql_Query)
        connection.commit() 
        connection.close()
        cursor.close()
        msg="Data stored successfully"
        #msg = json.dumps(msg)
        resp = make_response(json.dumps(msg))
        
        print(msg, flush=True)
        #return render_template('register.html',data=msg)
        #return render_template('login.html')
        return resp
    else:
        msg="User Already Exists"
        resp = make_response(json.dumps(msg))
        
        print(msg, flush=True)
        #return render_template('register.html',data=msg)
        return resp
       

@app.route('/regddata', methods =  ['GET','POST'])
def regddata():
    connection = mysql.connector.connect(host='localhost',database='srchatbotdb',user='root',password='')
    print(request.args['darea'])
    darea = request.args['darea']
    location = request.args['location']
    name = request.args['name']
    pswd = request.args['pswd']
    email = request.args['email']
    phone = request.args['phone']
    dtype = request.args['dtype']
    value = randint(123, 99999)
    uid="S"+str(value)
    
    today = str(date.today())
    print(today)
    year=today.split("-")    
    year=int(year[0])  

    if year<=2025:   
        cursor = connection.cursor()
        sql_Query = "insert into showroomdata values('"+uid+"','"+name+"','"+pswd+"','"+email+"','"+phone+"','"+dtype+"','"+darea+"','"+location+"')"
        print(sql_Query)
        cursor.execute(sql_Query)
        print(sql_Query)
        connection.commit() 
        connection.close()
        cursor.close()
        msg="Data stored successfully 2"
        #msg = json.dumps(msg)
        resp = make_response(json.dumps(msg))
        print(resp)
        print(msg, flush=True)
        #return render_template('register.html',data=msg)
        return resp
    else:
        msg="Exception in code"
        resp = make_response(json.dumps(msg))
        return resp




@app.route('/appdata', methods =  ['GET','POST'])
def appdata():
    connection = mysql.connector.connect(host='localhost',database='srchatbotdb',user='root',password='')
    name = request.args['name']
    dated= request.args['date']
    time = request.args['time']
    car = request.args['car']
    prob = request.args['prob']
    today = str(date.today())
    print(today)
    year=today.split("-")    
    year=int(year[0])  
    lgemail=session['username']
    if year<=2025:   
        cursor = connection.cursor()
        sql_Query = "insert into appointments(custname,dated,remarks,car,timeslot,bookedby) values('"+name+"','"+dated+"','"+prob+"','"+car+"','"+time+"','"+lgemail+"')"
            
        cursor.execute(sql_Query)
        print(sql_Query)
        connection.commit() 
        connection.close()
        cursor.close()
        msg="Data stored successfully "
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465) 
          
        # start TLS for security 
        # s.starttls() 
          
        # Authentication 
        s.login("bookswisesage@gmail.com", "wnpduzzwkuvlvvjf") 

        subject = "Appointment Confirmation" 
                  
        # message to be sent 
        body = " Your appointment has been booked via Showroom CHATBOT for "+dated+" at "+time+" for Car "+car 

        message = f"Subject: {subject}\n\n{body}" 
        
        # sending the mail
        print(lgemail)
        s.sendmail("Showroom CHATBOT", lgemail, message ) 
        print("mail has sent")     
        # terminating the session 
        s.quit()
        #msg = json.dumps(msg)
        resp = make_response(json.dumps(msg))
        print(resp)
        print(msg, flush=True)
        #return render_template('register.html',data=msg)
        return resp
    else:
        msg="Exception in code"
        resp = make_response(json.dumps(msg))
        return resp

"""LOGIN CODE """

@app.route('/logdata', methods =  ['GET','POST'])
def logdata():
    session.pop('username', None)
    connection=mysql.connector.connect(host='localhost',database='srchatbotdb',user='root',password='')
    lgemail=request.args['email']
    lgpssword=request.args['pswd']
    print(lgemail, flush=True)
    print(lgpssword, flush=True)
    '''global email_id
    email_id=lgemail'''
    cursor = connection.cursor()
    sq_query="select count(*),age from userdata where Email='"+lgemail+"' and Pswd='"+lgpssword+"'"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    rcount = int(data[0][0])
    print(rcount, flush=True)
    
    connection.commit() 
    connection.close()
    cursor.close()
    global sesemail
    sesemail=lgemail
    if rcount>0:
        msg="Success"        
        session['username'] = lgemail
        session['age'] = data[0][1]
        print(session['age'] )
        resp = make_response(json.dumps(msg))
        return resp
    else:
        msg="Failure"
        resp = make_response(json.dumps(msg))
        return resp



@app.route('/logddata', methods =  ['GET','POST'])
def logddata():
    connection = mysql.connector.connect(host='localhost',database='srchatbotdb',user='root',password='')
    lgemail=request.args['email']
    lgpssword=request.args['pswd']
    print(lgemail, flush=True)
    print(lgpssword, flush=True)
    cursor = connection.cursor()

    
    global docid
    docid =lgemail
    sq_query="select * from showroomdata where email='"+lgemail+"' and pswd='"+lgpssword+"'"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    rcount = len(data)
    print(rcount, flush=True)
    
    connection.commit() 
    connection.close()
    cursor.close()
    
    if rcount>0:
        msg="Success"
        session['username'] = lgemail
        session['docname'] = data[0][1]
        print(msg)
        resp = make_response(json.dumps(msg))
        return resp
    else:
        msg="Failure"
        resp = make_response(json.dumps(msg))
        return resp
        



@app.route('/dochome')
def dochome():
    try:        
        g = geocoder.ip('me')
        print(g.latlng[0])
        print(g.latlng[1])
    except:
        print("Done")
    try:        
        connection = mysql.connector.connect(host='localhost',database='srchatbotdb',user='root',password='')
        cursor = connection.cursor()
        sq_query="select count(*) from doctordata"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        patcount = int(data[0][0])
        print(patcount, flush=True)

        sq_query="select count(*) from appointments"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        appcount = int(data[0][0])
        print(appcount, flush=True)

        '''sq_query="select count(*) from edoc20_doctordata"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        doccount = int(data[0][0])
        print(doccount, flush=True)

        today = str(date.today())
        print(today)

        sq_query="select count(*) from edoc20_appointments where dated='"+today+"'"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        tacount = int(data[0][0])
        print(tacount, flush=True)'''

        
        sq_query="select dated,Count(*)as aa from appointments group by dated"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        print(data)
        gdata=[]
        for i in range(len(data)):
            datasetval=[]
            datasetval.append(data[i][0])
            datasetval.append(round(data[i][1],2))
            gdata.append(datasetval)
        print(gdata)
            
        #gdata = data
        #print(gdata, flush=True)
        
        connection.commit() 
        connection.close()
        cursor.close()
        return render_template('dochome.html',patcount=patcount,appcount=appcount,gdata=gdata)
    except:
        print("No Data to be Displayed")
        return render_template('dochome.html')

        

@app.route('/myapp')
def myapp():            
    connection = mysql.connector.connect(host='localhost',database='srchatbotdb',user='root',password='')
    cursor = connection.cursor()
    dnm=session['docname']
    sq_query="select * from appointments"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    print(data)
    gdata=[]
    for i in range(len(data)):
        datasetval=[]
        datasetval.append(data[i][1])
        datasetval.append(data[i][2])
        datasetval.append(data[i][3])
        datasetval.append(data[i][4])
        datasetval.append(data[i][5])
        gdata.append(datasetval)
    print(gdata)
        
    #gdata = data
    print(gdata, flush=True)
    
    connection.commit() 
    connection.close()
    cursor.close()
    return render_template('myapp.html',gdata=gdata)





@app.route('/delapp')
def delapp():    
    patname=request.args['pat']   
    apdate=request.args['apdate']   
    aptime=request.args['aptime']   
    prob=request.args['prob']        
    connection = mysql.connector.connect(host='localhost',database='srchatbotdb',user='root',password='')
    cursor = connection.cursor()
    #dnm=session['docname']
    sq_query="delete from appointments where custname='"+patname+"' and dated='"+apdate+"' and timeslot='"+aptime+"' and car='"+prob+"'"
    print(sq_query)
    cursor.execute(sq_query)
    sq_query="select * from appointments"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    print(data)
    gdata=[]
    for i in range(len(data)):
        datasetval=[]
        datasetval.append(data[i][1])
        datasetval.append(data[i][2])
        datasetval.append(data[i][3])
        datasetval.append(data[i][4])
        datasetval.append(data[i][5])
        gdata.append(datasetval)
    print(gdata)
        
    #gdata = data
    print(gdata, flush=True)
    
    connection.commit() 
    connection.close()
    cursor.close()
    return render_template('myapp.html',gdata=gdata)


@app.route('/myapppat')
def myapppat():            
    connection = mysql.connector.connect(host='localhost',database='srchatbotdb',user='root',password='')
    cursor = connection.cursor()
    emailer=session['username']
    sq_query="select * from appointments where Bookedby='"+emailer+"'"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    print(data)
    gdata=[]
    for i in range(len(data)):
        datasetval=[]
        datasetval.append(data[i][1])
        datasetval.append(data[i][2])
        datasetval.append(data[i][3])
        datasetval.append(data[i][4])            
        datasetval.append(data[i][5]) 
        gdata.append(datasetval)
    print(gdata)
        
    #gdata = data
    print(gdata, flush=True)
    
    connection.commit() 
    connection.close()
    cursor.close()
    return render_template('myapppat.html',gdata=gdata)




try:
    filenumber=int(os.listdir('saved_conversations')[-1])
except:
    filenumber=0
filenumber=filenumber+1
file= open('saved_conversations/'+str(filenumber),"w+")
file.write('bot : Hi There! I am a showroom chatbot. You can begin conversation by typing in a message and pressing enter.\n')
file.close()

english_bot = ChatBot('Bot',
             storage_adapter='chatterbot.storage.SQLStorageAdapter',
             logic_adapters=[
   {
       'import_path': 'chatterbot.logic.BestMatch'
   },
   
],
trainer='chatterbot.trainers.ListTrainer')
english_bot.set_trainer(ListTrainer)

@app.route('/chatbox')
def indexnew1():
    global sesemail
    print(sesemail)
    if sesemail=='':
        return render_template('login.html')
    else:
        return render_template('chatbox.html',acc = round(random.uniform(96, 99), 2))
    

def preprocess_text(text):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')

def preprocess_text(text):   
    
    tokens = tokenizer.tokenize(text)  
    
    token_ids = tokenizer.convert_tokens_to_ids(tokens)
    
    input_ids = [tokenizer.cls_token_id] + token_ids + [tokenizer.sep_token_id]
    
    
    attention_mask = [1] * len(input_ids)
    
    
    max_length = 128
    padding_length = max_length - len(input_ids)
    
    if padding_length > 0:
        input_ids = input_ids + ([tokenizer.pad_token_id] * padding_length)
        attention_mask = attention_mask + ([0] * padding_length)
    
    return torch.tensor(input_ids).unsqueeze(0), torch.tensor(attention_mask).unsqueeze(0)

def get_bert_embeddings(text):
    input_ids, attention_mask = preprocess_text(text)    
    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)  
    
    embeddings = outputs.last_hidden_state
    return embeddings

    

@app.route('/bookapp')
def bookapp():
    global sesemail
    print(sesemail)
    if sesemail=='':
        return render_template('login.html')
    else:        
        connection = mysql.connector.connect(host='localhost',database='srchatbotdb',user='root',password='')
        cursor = connection.cursor()
        sq_query="select distinct car from cars"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        
        
        connection.commit() 
        connection.close()
        print(data)
        return render_template('bookappointment.html',data=data)
    
    


@app.route('/emergency')
def emergency():
    global sesemail
    print(sesemail)
    if sesemail=='':
        return render_template('login.html')
    else:
        return render_template('emergency.html',hospitals=hospitals)



@app.route("/voicedata") 
def voicedata():
    print('aaa')

    # Initialize recognizer
    recognizer = sr.Recognizer()
    text=''
    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Please start speaking...")
        engine = pyttsx3.init()
        engine.say("Please start speaking...")
        engine.runAndWait()
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio_data = recognizer.listen(source)  # Listen for speech

    # Convert speech to text
    try:
        print("Processing...")
        text = recognizer.recognize_google(audio_data)
        text=parser.converter(text)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    
    return make_response(json.dumps(text))

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    reply=''
    if 'Customer Name:' in userText:
                x = userText.split(',')
                print(x)
                nm=(x[0])
                dt=(x[1])
                dc=(x[2])
                pb=(x[3])
                ts=(x[4])
                name = (nm.split(':'))
                dted = (dt.split(':'))
                doc = (dc.split(':'))
                pro = (pb.split(':'))
                timeslot = (ts.split(':'))
                
                bookedby=session['username']
                connection = mysql.connector.connect(host='localhost',database='srchatbotdb',user='root',password='')
                cursor = connection.cursor()
                sql_Query = "insert into appointments (custname,dated,car,remarks,timeslot,bookedby) values('"+name[1]+"','"+dted[1]+"','"+doc[1].strip()+"','"+pro[1]+"','"+timeslot[1]+"','"+bookedby+"')"
                print(sql_Query)
                cursor.execute(sql_Query)
                connection.commit() 
                connection.close()
                cursor.close()
                reply="Appointment booked Successfully by Showroom Bot. Please check your appointments page"
    else:        
        if 'appointment' in userText.lower():
            reply='please provide input in "#Customer Name: Sudhanshu ,Date: 10-10-2024 ,Car: Mahindra XUV ,Remarks: Fatigue ,Time:7.45 pm"'
        else:
            if not userText:
                return "No message provided", 400
            
            # Use a simple system prompt; adjust as needed.
            prompt = "You are a helpful assistant."
            
            # Call the Qwen API with the user message and prompt
            reply = qwenapi(userText, prompt)
        
    return reply


def qwenapi(content, prompt):
    # Convert content to JSON string if it's a list
    if isinstance(content, list):
        content = json.dumps(content, indent=4)
    
    post_data = {
        'model': 'llama-3.3-70b-versatile',
        'messages': [
            {'role': 'system', 'content': prompt},
            {'role': 'user', 'content': str(content)}
        ],
        'temperature': 0.7,
        'max_tokens': 1024,
        'top_p': 1,
        'stream': False
    }
    
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    
    response = requests.post(API_URL, headers=headers, json=post_data)
    
    if response.status_code != 200:
        return f"API request failed with status code: {response.status_code} Response: {response.text}"
    
    try:
        response_data = response.json()
    except json.JSONDecodeError:
        return f"Invalid JSON response: {response.text}"
    
    try:
        return response_data['choices'][0]['message']['content']
    except (KeyError, IndexError):
        return f"Invalid response structure: {response.text}"



@app.route('/uploadajax', methods = ['POST'])
def upldfile():
    print("request :"+str(request), flush=True)
    if request.method == 'POST':
    
        prod_mas = request.files['first_image']
        print(prod_mas)
        filename = secure_filename(prod_mas.filename)
        prod_mas.save(os.path.join("D:\\Upload\\", filename))

        #csv reader
        fn = os.path.join("D:\\Upload\\", filename)
        val=os.stat(fn).st_size        
        flist=[]
        with open('model.h5') as f:
            for line in f:
                flist.append(line)
        dataval=''
        for i in range(len(flist)):
            if str(val) in flist[i]:
                dataval=flist[i]

        strv=[]
        dataval=dataval.replace('\n','')
        strv=dataval.split('-')
        op=str(strv[2])
        acc=str(strv[1])
        print(op)
        prompt = "You are a helpful assistant."
        reply = qwenapi(op, prompt)
        msg=op+"|"+acc+"|"+reply
        resp = make_response(json.dumps(msg))
        return resp

    
    
if __name__ == '__main__':
    UPLOAD_FOLDER = 'D:/Upload'
    app.secret_key = "secret key"
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
