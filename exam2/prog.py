f=open("complete.csv","r")
for lines in f:
   x=lines.rstrip("\n").split(",")
   state=x[1]
   confirmed=x[4]
   death=x[5]
   recoverd=x[6]
   #print(state)
dit={}
if(state not in dit):
    print("invalid")
else:
    dit[state] = {"state": state, "confirmed": confirmed, "death": death, "recoverd": recoverd}

def fetchData(**kwargs):
    if(kwargs["state"] not in dit):
        print("invalid")
    else:
        for i,j in dit.items():
            if(i==kwargs["state"]):
                print("total confirmed",j["confirmed"])
                if("param" in kwargs):
                    value=kwargs["param"]
                if(value=="recovred"):
                    print("recoverd:",j["recoverd"])
                elif(value=="death"):
                    print("death:",j["death"])
fetchData(state="kerala",param="recoverd")









##ate,state,latitude,logitude,toatalconfirm,death,curred,newcase,newdeath