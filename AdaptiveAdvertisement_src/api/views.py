from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.core.urlresolvers import reverse
from collections import Counter

import json
import os
import random
import time

from .models import User, Poster, Image

def getImage(request):
    i = Image.objects.all()
    data = serializers.serialize('json', Image.objects.all())
    return HttpResponse(data, content_type = "application/json")
    # return HttpResponse(i.image.read(), content_type = i.mimeType)

def getOne(request,id):
    i = Image.objects.get(poster=id)
    return i
    

@csrf_exempt
def addUser(request):
	print (request)
	print (json.dumps(request.POST))
	user= json.loads(json.dumps(request.POST))
	u=User(username = user['username'],\
		age = user['age'],\
		qatar_resident=user['qatar_resident'],\
		gender= user['gender'],\
		children =user['children']
		)
	u.save()
	data = serializers.serialize('json', User.objects.all())
	return HttpResponse(data, content_type = "application/json")


def showUsers(request):
	data = serializers.serialize('json', User.objects.all())
	return HttpResponse(data, content_type = "application/json")

def count_ages(request):
	list1=User.objects.filter(username__contains="192.168.1")

	ages_result=[]
	for i in range(0, len(list1)):
		answer = (list1[i].age)
		ages_result.append(answer)

	age_list={}
	count51_older=0
	count41_50=0
	count31_40=0
	count21_30=0
	count15_20=0
	for i in range(0, len(ages_result)):
		if ages_result[i]=="51-older":
			count51_older+=1
		if ages_result[i]=="41-50":
			count41_50+=1
		if ages_result[i]=="31-40":
			count31_40+=1
		if ages_result[i]=="21-30":
			count21_30+=1
		if ages_result[i]=="15-20":
			count15_20+=1
	print ("51-older",count51_older)
	print ("41-50",count41_50)
	print ("31-40",count31_40)
	print ("21-30",count21_30)
	print ("15-20",count15_20)
	age_list["group51"]=count51_older
	age_list["group4150"]=count41_50
	age_list["group3140"]=count31_40
	age_list["group2130"]=count21_30
	age_list["group1520"]=count15_20
	print (age_list)

	# data = json.dumps(age_list)
	return age_list

def count_resident(request):
	list1=User.objects.filter(username__contains="192.168.1")
	resident_result=[]
	for i in range(0, len(list1)):
		answer = (list1[i].qatar_resident)
		resident_result.append(answer)

	resident_list={}
	resident=0
	tourist=0
	for i in range(0, len(resident_result)):
		if resident_result[i]=="Yes":
			resident+=1
		if resident_result[i]=="No":
			tourist+=1
	print ("Resident",resident)
	print ("Tourist",tourist)
	resident_list["resident"]=resident
	resident_list["tourist"]=tourist
	print (resident_list)
	# data = json.dumps(resident_list)
	return resident_list


def count_gender(request):
	list1=User.objects.filter(username__contains="192.168.1")

	gender_result=[]
	for i in range(0, len(list1)):
		answer = (list1[i].gender)
		gender_result.append(answer)

	gender_list={}
	male=0
	female=0
	for i in range(0, len(gender_result)):
		if gender_result[i]=="male":
			male+=1
		if gender_result[i]=="female":
			female+=1
	print ("male",male)
	print ("female",female)
	gender_list["male"]=male
	gender_list["female"]=female
	print (gender_list)
	# data = json.dumps(gender_list)
	return gender_list

def count_child(request):
	list1=User.objects.filter(username__contains="192.168.1")

	child_result=[]
	for i in range(0, len(list1)):
		answer = (list1[i].children)
		child_result.append(answer)

	child_list={}
	yes=0
	no=0
	for i in range(0, len(child_result)):
		if child_result[i]=="Yes":
			yes+=1
		if child_result[i]=="No":
			no+=1
	print ("child",yes)
	print ("no child",no)
	child_list["child"]=yes
	child_list["no_child"]=no
	print (child_list)
	# data = json.dumps(child_list)
	return child_list

def analyze1(request):
	list1=User.objects.filter(username__contains="192.168.1")
	Majority={}

	ages_result=[]
	for i in range(0, len(list1)):
		answer = (list1[i].age)
		ages_result.append(answer)

	gender_result=[]
	for i in range(0, len(list1)):
		answer = (list1[i].gender)
		gender_result.append(answer)

	resident_result=[]
	for i in range(0, len(list1)):
		answer = (list1[i].qatar_resident)
		resident_result.append(answer)

	child_result=[]
	for i in range(0, len(list1)):
		answer = (list1[i].children)
		child_result.append(answer)

	Majority['Child'] = child_max(child_result)
	Majority['Resident'] = resident_max(resident_result)
	Majority['Gender'] = gender_max(gender_result)
	Majority['Age'] = ages_max(ages_result)
	print ("result",child_result)
	count_ages(ages_result)
	count_gender(gender_result)
	count_resident(resident_result)
	count_child(child_result)
	print (Majority)
	return Majority

def analyze2(request):
	list1=User.objects.filter(username__contains="192.168.2")
	Majority={}

	ages_result=[]
	for i in range(0, len(list1)):
		answer = (list1[i].age)
		ages_result.append(answer)

	gender_result=[]
	for i in range(0, len(list1)):
		answer = (list1[i].gender)
		gender_result.append(answer)

	resident_result=[]
	for i in range(0, len(list1)):
		answer = (list1[i].qatar_resident)
		resident_result.append(answer)

	child_result=[]
	for i in range(0, len(list1)):
		answer = (list1[i].children)
		child_result.append(answer)

	Majority['Child'] = child_max(child_result)
	Majority['Resident'] = resident_max(resident_result)
	Majority['Gender'] = gender_max(gender_result)
	Majority['Age'] = ages_max(ages_result)

	print (Majority)
	return Majority

def ages_max(ages_result):
	ages = Counter(ages_result)
	ages.most_common()
	maximum, count = ages.most_common()[0]
	return maximum

def gender_max(gender_result):
	gender = Counter(gender_result)
	gender.most_common()
	maximum, count = gender.most_common()[0]
	return maximum

def resident_max(resident_result):
	resident_status = Counter(resident_result)
	resident_status.most_common()
	maximum, count = resident_status.most_common()[0]
	return maximum

def child_max(child_result):
	children = Counter(child_result)
	children.most_common()
	maximum, count = children.most_common()[0]
	return maximum

def address(request):
	data = serializers.serialize('json', User.objects.filter(username__contains="192.168.1"))
	return HttpResponse(data, content_type = "application/json")

def categorize1(request):
	matching_ad_pks=[]
	list_ad=[]
	popular=analyze1(request)
	print(popular)
	adv_list=Poster.objects.all()
	for adv_item in adv_list: #looping through each ad in the dictionary
		dict_temp = adv_item
		id_temp = dict_temp.pk #getting the ID of the ad
		print (id_temp)
		print (adv_item.title)

		age = [] #initializing array
		age_temp = [False, False, False, False, False] #temporary araray with false values onl
		age.append(adv_item.age1520)
		age.append(adv_item.age2130)
		age.append(adv_item.age3140)
		age.append(adv_item.age4150)
		age.append(adv_item.age51)
		male = adv_item.man
		female = adv_item.woman
		resident = adv_item.qatar_resident
		child = adv_item.children

		#getting the max result of each criteria from the current connected user group
		age_maximum = popular['Age']
		gender_maximum = popular['Gender']
		resident_maximum = popular['Resident']
		child_maximum = popular['Child']




		# initializing criteria variables
		age_status = False
		gender_status = False
		resident_status = False
		child_status = False

		#checking & matching the age attribute
		if age_maximum == "15-20" and age[0]:
			age_status = True
		elif age_maximum == "21-30" and age[1]:
			age_status = True
		elif age_maximum == "31-40" and age[2]:
			age_status = True
		elif age_maximum == "41-50" and age[3]:
			age_status = True
		elif age_maximum == "51-older" and age[4]:
			age_status = True
		print("age status", age_status)

		#checking & matching the gender attribute
		if gender_maximum == "male":
			if male == True:
				gender_status = True
		elif gender_maximum == "female":
			if female == True:
				gender_status = True
		print("gender status", gender_status)

		#checking & matching the resident attribute
		if resident_maximum == "Yes":
			if resident == True:
				resident_status = True
		elif resident_maximum == "No":
			if resident == False:
				resident_status = True
		print("resident status", resident_status)

		#checking & matching the child attribute
		if child_maximum == "Yes":
			if child == True:
				child_status = True
		elif child_maximum == "No":
			if child == False:
				child_status = True
		print("child status", child_status)

		age_num=0
		gender_num=0
		resident_num=0
		child_num=0

		#checking if all criteria = true
		if age_status:
			age_num = 1
		if gender_status:
			gender_num=1
		if resident_status:
			resident_num=1
		if child_status:
			child_num=1
		print (age_num)
		print (gender_num)
		print (resident_num)
		print (child_num)

		if age_num + gender_num + resident_num + child_num > 2:
			print (id_temp,"is a matching poster")
			matching_ad_pks.append(id_temp)
		else:
			print (id_temp,"is not matching")
		
	print ("matching id",matching_ad_pks)
	return matching_ad_pks

def categorize2(request):
	matching_ad_pks=[]
	list_ad=[]
	popular=analyze2(request)
	print(popular)
	adv_list=Poster.objects.all()
	for adv_item in adv_list: #looping through each ad in the dictionary
		dict_temp = adv_item
		id_temp = dict_temp.pk #getting the ID of the ad
		print (id_temp)
		print (adv_item.title)

		age = [] #initializing array
		age_temp = [False, False, False, False, False] #temporary araray with false values onl
		age.append(adv_item.age1520)
		age.append(adv_item.age2130)
		age.append(adv_item.age3140)
		age.append(adv_item.age4150)
		age.append(adv_item.age51)
		male = adv_item.man
		female = adv_item.woman
		resident = adv_item.qatar_resident
		child = adv_item.children

		#getting the max result of each criteria from the current connected user group
		age_maximum = popular['Age']
		gender_maximum = popular['Gender']
		resident_maximum = popular['Resident']
		child_maximum = popular['Child']




		# initializing criteria variables
		age_status = False
		gender_status = False
		resident_status = False
		child_status = False

		#checking & matching the age attribute
		if age_maximum == "15-20" and age[0]:
			age_status = True
		elif age_maximum == "21-30" and age[1]:
			age_status = True
		elif age_maximum == "31-40" and age[2]:
			age_status = True
		elif age_maximum == "41-50" and age[3]:
			age_status = True
		elif age_maximum == "51-older" and age[4]:
			age_status = True
		print("age status", age_status)

		#checking & matching the gender attribute
		if gender_maximum == "male":
			if male == True:
				gender_status = True
		elif gender_maximum == "female":
			if female == True:
				gender_status = True
		print("gender status", gender_status)

		#checking & matching the resident attribute
		if resident_maximum == "Yes":
			if resident == True:
				resident_status = True
		elif resident_maximum == "No":
			if resident == False:
				resident_status = True
		print("resident status", resident_status)

		#checking & matching the child attribute
		if child_maximum == "Yes":
			if child == True:
				child_status = True
		elif child_maximum == "No":
			if child == False:
				child_status = True
		print("child status", child_status)

		age_num=0
		gender_num=0
		resident_num=0
		child_num=0

		#checking if all criteria = true
		if age_status:
			age_num = 1
		if gender_status:
			gender_num=1
		if resident_status:
			resident_num=1
		if child_status:
			child_num=1
		print (age_num)
		print (gender_num)
		print (resident_num)
		print (child_num)

		if age_num + gender_num + resident_num + child_num > 2:
			print (id_temp,"is a matching poster")
			matching_ad_pks.append(id_temp)
		else:
			print (id_temp,"is not matching")
		
	print ("matching id",matching_ad_pks)
	return matching_ad_pks




def display1(request):
	list_pk=categorize1(request)
	print("final list",list_pk)
	my_adpk=random.choice(list_pk)
	print(my_adpk)
	# my_ad=getOne(request,my_adpk)
	# return HttpResponse(my_ad.image.read(), content_type = my_ad.mimeType)
	# print("test",my_ad)
	# return my_ad
	target_ad=Poster.objects.filter(pk=my_adpk)
	print(target_ad)

	data = serializers.serialize('json', target_ad)
	return HttpResponse(data, content_type = "application/json")

def display2(request):
	list_pk=categorize2(request)
	print("final list",list_pk)
	my_adpk=random.choice(list_pk)
	print(my_adpk)
	# my_ad=getOne(request,my_adpk)
	# return HttpResponse(my_ad.image.read(), content_type = my_ad.mimeType)

	target_ad=Poster.objects.filter(pk=my_adpk)
	print(target_ad)

	data = serializers.serialize('json', target_ad)
	return HttpResponse(data, content_type = "application/json")

def temporary(request):
	response=display1(request)
	# time.sleep(10)
	print ("response",response)
	return response

def exe(request):
	while True:
		nom=temporary(request)
		print ("nom",nom)
		return HttpResponse(nom.image.read(), content_type = nom.mimeType)

	

def democount(request):
	count_demo={}
	count_demo["Age_count"]=count_ages(request)
	count_demo["Gender_count"]=count_gender(request)
	count_demo["Resident_count"]=count_resident(request)
	count_demo["Child_count"]=count_child(request)
	print (count_demo)

	data = json.dumps(count_demo)
	return HttpResponse(data, content_type = "application/json")
