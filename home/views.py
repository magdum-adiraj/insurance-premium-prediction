from django.shortcuts import render,HttpResponse
import joblib

model = joblib.load('static_files/random_forest_regressor')

# Create your views here.
def index(request):
    return render(request,'index.html')

def prediction(request):
    if(request.method=="GET"):
        return render(request,'prediction.html')
    elif(request.method=="POST"):
        age=int(request.POST.get('age'))
        sex=int(request.POST.get('sex'))
        bmi=int(request.POST.get('bmi'))
        children=int(request.POST.get('children'))
        smoker=int(request.POST.get('smoker'))
        region=int(request.POST.get('region'))
        
        pred=round(model.predict([[age,sex,bmi,children,smoker,region]])[0])
        output={
            "output":pred
        }
        return render(request,'prediction.html',output)
