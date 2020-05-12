#read 2 sets of student names
#android students and java students
#display all names, common names

jstud=set()
astud=set()
reply='y'
while reply=='y':
                m = (input('Enter java students names '))
                jstud.add(m)
                reply = input ('Do yo wish to add  more y/n ')

reply='y'
while reply=='y':
                m = (input('Enter android students names '))
                astud.add(m)
                reply = input ('Do yo wish to add  more y/n ')

allname=jstud|astud
comname=jstud&astud

print("All names are",allname,"\ncommon names are",comname)
