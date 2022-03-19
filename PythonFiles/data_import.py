import numpy as np
import pandas as pd

filenames = ['chefmozaccepts.csv', 'chefmozcuisine.csv', 'chefmozhours4.csv', 'chefmozparking.csv', 'geoplaces2.csv',
             'rating_final.csv', 'usercuisine.csv', 'userpayment.csv', 'userprofile.csv']

cleaned_filenames = []

for i in filenames:
  cleaned_filenames.append(i.replace(".csv",""))

for i in range(len(filenames)):
  print("=== Loading file ",filenames[i], " ===")
  exec('%s = pd.read_csv("./Database/%s", encoding="ISO-8859-1")'%(cleaned_filenames[i],filenames[i]))
  print("=== File loaded ===\n")
