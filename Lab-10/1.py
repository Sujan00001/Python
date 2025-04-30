import csv
with open("demo.csv",'w+',newline='')as f1:
    wri=csv.writer(f1)

    str1=[['Roll No','Name','Mark1','Mark2','Mark3','Total'],
      ['24BCP193','Rana',20,22,43,84],
      ['24BCP191','Jack',21,20,44,82],
      ['24BCP195','Rusi',22,23,45,80]]

    wri.writerows(str1) 
f1.close()
  
