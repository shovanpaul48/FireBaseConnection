from django.shortcuts import render, redirect
from .forms import DataForm
import pyrebase

config = {
    "apiKey": "AIzaSyBMKgJ1_r_2BFBhoWG9g_ViG_XLtW85lbA",
    "authDomain": "firestoretest-a5aa5.firebaseapp.com",
    "databaseURL": "https://firestoretest-a5aa5-default-rtdb.firebaseio.com/",
    "projectId": "firestoretest-a5aa5",
    "storageBucket": "firestoretest-a5aa5.appspot.com",
    "messagingSenderId": "1005206559993",
    "appId": "1:1005206559993:web:b0713596dd21316b3b1628",
    "measurementId": "G-DQPPQTXE5N"
}
# config = {
#     "apiKey": "AIzaSyBMKgJ1_r_2BFBhoWG9g_ViG_XLtW85lbA",
#     "authDomain": "YOUR_AUTH_DOMAIN",
#     "databaseURL": "https://firestoretest-a5aa5-default-rtdb.firebaseio.com/",
#     "projectId": "YOUR_PROJECT_ID",
#     "storageBucket": "YOUR_STORAGE_BUCKET",
#     "messagingSenderId": "YOUR_MESSAGING_SENDER_ID",
#     "appId": "YOUR_APP_ID"
# }

firebase = pyrebase.initialize_app(config)
database = firebase.database()


def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            # Save form data to the database
            form_data = form.save(commit=False)
            form_data.save()

            # Push form data to Firebase without the file field
            data = {
                'title': form_data.title,
                'description': form_data.description,
                'links': form_data.links,
                # You can include other fields here if needed
            }
            database.child("data").push(data)

            return redirect('index')
    else:
        form = DataForm()
    return render(request, 'index.html', {'form': form})