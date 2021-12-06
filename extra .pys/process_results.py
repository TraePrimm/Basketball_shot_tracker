import pandas as pd

linesindoc =[]
picnumber = []
picture = []
classtype = []
conf = []
file=[]
#turns the file into a list
with open('result.json', 'r') as f:
    for line in f:
        linesindoc.append(line)    
#pulls the data that is kept such as filename, img, class, and cf %
for n in range(len(linesindoc)):
    if 'data' in linesindoc[n]:
        #gets img name and img number
        w = linesindoc[n].split('/')
        z = w[2]
        y = z.split()
        my_str =  y[0]
        my_str = my_str[:-1]
        picture.append(my_str)
        my_str = my_str[1:-4]
        picnumber.append(my_str)
        count=n
        if 'Basketball' in linesindoc[count+1] or 'Made_Shot' in linesindoc[count+1]:
            w = linesindoc[count+1].split()
            my_str =  w[0]
            my_str = my_str[:-1]
            classtype.append(my_str)
            #gets cf %
            my_str =  w[1]
            my_str = my_str[:-1]
            conf_to_p = float(my_str)/100
            conf.append(conf_to_p)
        else:
            classtype.append(0)
            conf.append(0)

#creates the dataframe
df = pd.DataFrame(
    {'number': picnumber,
     'picname': picture,
     'Class': classtype,
     'confidence': conf
    })


#organizes and makes it similar to the demo settings
df['number'] = df['number'].astype(int)
df = df.sort_values(by=['number'])
df = df[df.confidence >= .8]
to_drop = ['Basketball']
made_shots = df[~df['Class'].isin(to_drop)]


testlist=made_shots['number'].tolist()

msc = 0
count = 0
listindex = []
#drops the extra frames to just leave 1 frame per made shot and keeps track of false positives
for n in range(len(testlist)-1):
    if testlist[n]+1 == (testlist[n+1]):
        count+=1
    elif testlist[n]+1 != (testlist[n+1]):
        if count>3:
            listindex.append(testlist[n])
            msc+=1
            count=0
        else:
            print('flase pos')
if count >3:
    listindex.append(testlist[-1])
    msc+=1
    count = 0
        


#outputs csvs
df.to_csv('procesed_results.csv', index=False)
made_shots.to_csv('total_made_shots.csv',index=False)
rms = made_shots[made_shots.number.isin(listindex)]
rms.to_csv('reduced_made_shots.csv',index=False)