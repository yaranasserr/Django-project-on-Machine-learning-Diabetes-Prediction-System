
from django.shortcuts import render
from joblib import load
from .forms import PredictionForm

# Load the saved model from a file
loaded_model = load('./savedModels/model.joblib')

# Create your views here.
def home(request):
    return render(request,'home.html')

def predict(request):
    return render(request,'predict.html')

# def predict_view(request):
#     if request.method == 'POST':
#         form = PredictionForm(request.POST)
#         if form.is_valid():
#             # Get the input values from the form
#             pregnancies = form.cleaned_data['pregnancies']
#             glucose = form.cleaned_data['glucose']
#             blood_pressure = form.cleaned_data['blood_pressure']
#             skin_thickness = form.cleaned_data['skin_thickness']
#             insulin = form.cleaned_data['insulin']
#             bmi = form.cleaned_data['bmi']
#             diabetes_pedigree_function = form.cleaned_data['diabetes_pedigree_function']
#             age = form.cleaned_data['age']
            
#             # Call your prediction function with the input values
#             result = loaded_model (pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age)
            
#             # Render the result template with the result
#             return render(request, 'result.html', {'result': result})
#     else:
#         form = PredictionForm()
#     return render(request, 'predict.html', {'form': form})
def result(request):
    val1=float(request.GET['n1'])
    val2=float(request.GET['n2'])
    val3=float(request.GET['n3'])
    val4=float(request.GET['n4'])
    val5=float(request.GET['n5'])
    val6=float(request.GET['n6'])
    val7=float(request.GET['n7'])
    val8=float(request.GET['n8'])
    pred=loaded_model.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])
    result1=''
    if pred==[1]:
        result1 ="Positive"
    else:
        result1="Negative"
        
    return render(request,'predict.html',{"result2":result1})

#     val1=request.GET['n1']
#     val2=request.GET['n2']
#     val3=request.GET['n3']
#     val4=request.GET['n4']
#     val5=request.GET['n5']
#     val6=request.GET['n6']
#     val7=request.GET['n7']
#     val8=request.GET['n8']

# val1=float(request.GET['n1'])
#     val2=float(request.GET['n2'])
#     val3=float(request.GET['n3'])
#     val4=float(request.GET['n4'])
#     val5=float(request.GET['n5'])
#     val6=float(request.GET['n6'])
#     val7=float(request.GET['n7'])
#     val8=float(request.GET['n8'])