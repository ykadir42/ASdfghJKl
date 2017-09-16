import random

def open_file(): #returns the contents of the occupations.csv file
	source = open( 'occupations.csv', 'rU')
	occupations = source.read()
	source.close()
	return occupations


def make_dict(): #makes a dictionary with occupations as keys and their respective percentages as values
	occupations = open_file()
	occupation_list = occupations.split("\n")
	occupations_dict={}
	for i in occupation_list[1:-2]:
		if(i[0]=='"'):
			occupation = i[1:].split('",')
			occupations_dict[occupation[0]] = float(occupation[1])
		else:
			occupation = i.split(',')
			occupations_dict[occupation[0]] = float(occupation[1])
	return occupations_dict
occupations_dict = make_dict()
#print (make_dict())

def random_occupation():
	i=random.random()*99.800000
	pos=0.0
	for o in occupations_dict.keys():
		if (i >= pos and i<pos+occupations_dict[o]):
			#print i
			#print str(pos)+"-"+str(pos+occupations_dict[o])
			return o
		pos+=occupations_dict[o]

print random_occupation()
