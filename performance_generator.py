n=int(input("enter number for student:"))
with open(r"C:\Users\shivani\OneDrive\Desktop\names.txt","w") as f:
    for i in range(n):
        name=input("enter name of the student:")
        mark=input("enter mark of the student:")
        f.write(name+':'+mark+'\n')

from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client=Groq(api_key=os.getenv('GROQ_API_KEY'))



with open(r"C:\Users\shivani\OneDrive\Desktop\names.txt","r") as f:
    s=f.readlines()
    for i in s:
        part=i.split(':')
        name=part[0]
        mark=part[1]
        prompt=f"generate performance report on the student called {name} who scored {mark} out of hundered"
        response=client.chat.completions.create(
            model="llama-3.3-70b-versatile" ,
            messages=[{'role':'user','content':prompt}])
        result=response.choices[0].message.content

        print("Processing:", name)
        print(result)
        print("---")

        with open("performance.txt","a") as f:
            f.write(result)
    







    
    
        
