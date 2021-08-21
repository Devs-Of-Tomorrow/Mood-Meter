from django.shortcuts import render
from django.views import View
from Maintain.models import Mooddata


# Create your views here.


class Emphome(View):

    def post(self, request):
        postData = request.POST
        mood1 = request.POST.get('mood1')
        mood2 = request.POST.get('mood2')
        mood3 = request.POST.get('mood3')
        mood4 = request.POST.get('mood4')
        mood5 = request.POST.get('mood5')
        mood6 = request.POST.get('mood6')
        mood7 = request.POST.get('mood7')
        mood8 = request.POST.get('mood8')
        mood9 = request.POST.get('mood9')
        mood10 = request.POST.get('mood10')
        mood = request.POST.get('mood')

        submit = request.POST.get('final')

        if submit:
            postData = request.POST
            d = Mooddata.get_all_mooddata();
            moodnum = 20
            if mood1:
                moodnum = 1
            if mood2:
                moodnum = 2
            if mood3:
                moodnum = 3
            if mood4:
                moodnum = 4
            if mood5:
                moodnum = 5
            if mood6:
                moodnum = 6
            if mood7:
                moodnum = 7
            if mood8:
                moodnum = 8
            if mood9:
                moodnum = 9
            if mood10:
                moodnum = 10

            mood = Mooddata(moodnum=moodnum)
            mood.register()
            data = {}
            data['ds'] = d

            return render(request, 'empind.html', data)

    def get(self, request):
        data = {}
        #print("hiiiiiiiiii", request.session.get('first_name'))
        return render(request, 'emphome.html', data)
