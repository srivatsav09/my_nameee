import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord,Topic,Webpage,User
from faker import Faker

fakegen = Faker()


def populate(N=5):

    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        #new entry
        user = User.objects.get_or_create(first_name = fake_first_name,last_name = fake_last_name,email = fake_email)[0]
        





#topics = ['Search','Social','Marketplace','News','Games']

# def add_topic():
#     t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
#     t.save()
#     return t


# def populate(N = 5):
#     for entry in range(N):
#         top = add_topic()   #get topic for entry
#         fake_url = fakegen.url()  #create fake data for that entry
#         fake_date = fakegen.date()
#         fake_name = fakegen.company()

#         #create a webpage entry
#         webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        
#         #create a fake access record for that webpage
#         acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("populating script")
    populate(20)
    print("populating complete")


