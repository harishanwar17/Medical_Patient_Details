medical_cost={}

medical_cost["Frank"]=4907.5
# medical cost of frank in dollars and float

medical_cost["Castle"]=3980.5
#medical cost of casttle in dollars and float

medical_cost["Mathew"]=4690.0
#medical cost of mathew in dollars and float

'''suppose we want to update the value of the costs
example: if they will need more medicines or accomodations
we can update using update method '''

medical_cost.update({("Mathew",5500),('Connie',8870.6)})
'''Here we are updating the value of mathew in order to update his bills'''

print(medical_cost)


total_cost=0
# So, lets calculate the total cost of all bills

for i in medical_cost.values():
    total_cost+=i
    # it continously adds the values i.e bills of all of them

'''so lets calculate the average cost, the logic here is 
to divide the total_cost by the number of patients'''
average_cost=total_cost/len(medical_cost)
# here len will return how many patients were there so we'll get the average


#so lets see how much our average cost is 
print("The Average cost in dollars is:",average_cost)


names=['Frank','Castle','Mathew']
#so here we are creating a names list

ages=[41,39,31]
#here is the ages list of the patients

zipped_ages=zip(names,ages)
#we used zip function to combine the names and ages

names_age_data={}

for name in names:
    for age in ages:
        names_age_data[name]=age
        ages.remove(age)
        break
    '''So here we used a loop to iterate in names and another loop to iterate in ages
    after that we added the names as keys to our dictionary and the age iterator will
    fill the dictionary with values'''

    '''So, lets check if our dictioanry is working'''

    #print(names_age_data)
    #so its working completely fine

    '''So lets try to check our data that if matt is present or not'''
   #Mathew_age=names_age_data.get("Mathew","None")
    #print(f"Mathew's age is: {Mathew_age} years")


    '''So, Lets create a big dictioanry which will contain every detail 
    about the patients at one place'''

    complete_medical_records={}
    #so we initialised the super-dictionary we'll like to create

    complete_medical_records["Frank"]={"age":41 ,"sex":"Male" ,"bmi":30.5 ,"children":2,
                                       "smoker":"non-smoker","insurance_cost":4907.5}
    
    complete_medical_records["Castle"]={"age":44 ,"sex":"Male" ,"bmi":33.6 ,"children":0,
                                       "smoker":"smoker","insurance_cost":3980.5}

complete_medical_records["Mathew"]={"age":31 ,"sex":"Male" ,"bmi":27.5 ,"children":0,
                                       "smoker":"non-smoker","insurance_cost":4907.5}

complete_medical_records["Murdock"]={"age":46 ,"sex":"Male" ,"bmi":29.8 ,"children":2,
                                       "smoker":"non-smoker","insurance_cost":4907.5}

#frank_report=complete_medical_records.get("Frank")
#print(f"Frank's Complete Profile:{frank_report}")
'''Here, we accessed frank records by using get '''

'''
lets assume for an istance that we want only the bmi not other details
so we can use nested dictionary for that'''

#frank_bmi=complete_medical_records["Frank"]["bmi"]
#print(frank_bmi)
'''So, our code until now is error free as it is printing correct values, lets proceed ahead'''

#print(complete_medical_records)

'''if we want to remove someone's information we can simply use
pop() function'''
#complete_medical_records.pop("murdock")

'''So, we want a medical report in simple words and with explanation'''

for i in complete_medical_records:
    print(i,"is a",complete_medical_records[i]["age"],"years old",complete_medical_records[i]["smoker"],"with a bmi of",complete_medical_records[i]["bmi"],"and insurance cost of",complete_medical_records[i]["insurance_cost"])