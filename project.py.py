#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fun():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    print("Enter 1.Show the sample data safety")
    print("Enter 2.Show the describe sample data safety")
    print("Enter 3.Show the info sample data safety")
    print("Enter 4.Show the null sample data safety")
    print("Enter 5.Show the sum of the null velues of sample data safety")
    print("Enter 6.Show the sum of the total null values of sample data safety")
    print("Enter 7.Number of  unit cost region value ")
    print("Enter 8.Number of Region units value ")
    print("Enter 9.Number of  show boxplot")
    print("Enter 10.Number of  names ")
    print("Enter 11.Number of  names lineplot")
    df=pd.read_csv("D:\\all subject pdf\\Copy of SampleData.csv")
    choice=input("Enter your choice:\n")
    if choice =='1':
        print(df)
    elif choice=='2':
        print(df.info())
    elif choice=='3':
        print(df.describe())
    elif choice=='4':
        print(df.tail(10))
    elif choice=='5':
        print(df=pd.read_csv("D:\\all subject pdf\\Copy of SampleData.csv"))
    elif choice=='6':
        sns.countplot(df["Total"])
    elif choice=='7':
        sns.scatterplot(df["Units"],df["Unit Cost"],df["Region"]) #linearregerresion model
    elif choice=='8':
        print(df["Region"],df["Units"].value_counts())
        print(df["Item"].value_counts())
    elif choice=='9':
        sns.boxplot(df.Units)
    elif choice=='10':
        labels='Binder','Pencil','Pen','Desk','Pen Set'
        sizes=[15,13,5,3,7]
        colors=['yellow','yellowgreen','lightcoral','lightskyblue']
        explode=(0,0,0,0,0)
        plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True)
        plt.axis('equal')
        plt.show()
    elif choice=='11':
        
        sns.lineplot(df["Units"],df["Unit Cost"]) 
    
        
        
        
        
        
        
    #choice=input("Press c for continue and press any key to exit")
    #if choice=='c' or choice=='C':
           #fun()
        
fun()                


# In[ ]:





# In[ ]:





# In[ ]:




