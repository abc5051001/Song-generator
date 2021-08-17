
#import the random module
import random

#seed the random number generator so that 
#the randomness is the same each time you
#run the file. you can change this number 
#to get your code to match individual tests
random.seed(0)
def generate_durations(base_tempo):
	dictionary = {'Whole': 4.0, 'Half': 2.0, 'Quarter': 1.0,
	'Eighth': 0.5, 'Sixteenth': 0.25}
	x = ['Whole','Half','Quarter','Eighth','Sixteenth']
	for i in x:
		if i in dictionary:
# get each beat
			dictionary[i] = ((60/base_tempo)*dictionary[i])
# change to the value corresponding to base tempo
	return dictionary
def generate_frequencies(base_freq):
	dictionary = {}
	x = ['C','C#','D','D#','E','F', 'F#','G','G#','A','A#','B']
	y = ['A0','A#0','B0']
	for i in range(1,8):
		for j in x:
			y.append(j+str(i))
# append the full octaves from 1-7 to y
	y.append('C8')
	A4 = y.index('A4')
# set A4 as the center
	for k in range(len(y)):
		n = k - A4
		F = base_freq * 2**(n/12)
		d1 = {y[k]:F}
		dictionary.update(d1)
# calculate the frequency based on the distance from A4
	return dictionary
def find_note(filename, highest_or_lowest):
	dictionary = {}
	tracker = 0
	x = ['C','C#','D','D#','E','F', 'F#','G','G#','A','A#','B']
	y = ['A0','A#0','B0']
	for i in range(1,8):
		for j in x:
			y.append(j+str(i))
	y.append('C8')
# same process to get a list of 88 notes
	file = open(filename)
	lines = file.read()
	all_notes=[]
	notes = lines.split('\n')
# this list contains all the lines
	for i in range(2,len(notes)-1):
		note = notes[i].split(',')[0]
		all_notes.append(y.index(note))
# after splitting take the notes
	if highest_or_lowest == True:
		max = all_notes[0]
		for h in all_notes:
			if max < h:
				max = h
		return y[max]
# check max
	if highest_or_lowest == False:
		min= all_notes[0]
		for h in all_notes:
			if min>h:
				min = h
		return y[min]
# check min
def random_song(filename, tempo, tuning, num_measures):
	file = open(filename,"w")
	dictionary = {"Sixteenth" : 0.25, "Eighth" : 0.5, 
	"Quarter" : 1.0, "Half" : 2.0, "Whole" : 4.0}
	list_ = ["Sixteenth", "Eighth", 'Quarter', 'Half','Whole']
	notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
	octave = [1,2,3,4,5,6,7]
	measure = 4
	write_list=[]
	write_list.append(str(tempo)+"\n")
	write_list.append(str(tuning)+"\n")
# append the first two lines into list
	while num_measures > 0:
# do this loop until all the measures are fulfilled
			random_tempo = random.choice(list_)
			value = dictionary[random_tempo]
# get the value from dictionary based on the random choice
			if measure - value >= 0:
# until this 4 beats are filled
				measure = measure - value
				random_notes = random.choice(notes)
				random_octave = random.choice(octave)
				write_list.append(str(random_notes)+str(random_octave
				)+","+random_tempo+"\n")
# take the random notes and append to this list
				if measure == 0:
					num_measures = num_measures -1 
					measure = 4
# total number of measure goes down by 1 
# and reset when one measure is filled
	file.writelines(write_list)
def change_notes (filename, changes, shift):
	x = ['C','C#','D','D#','E','F', 'F#','G','G#','A','A#','B']
	y = ['A0','A#0','B0']
	for i in range(1,8):
		for j in x:
			y.append(j+str(i))
	y.append('C8')
# y = the list of all the notes
# this part is just the same as the others
	file = open(filename)
	whole_text = file.read()
	lines = whole_text.split('\n')
	all_notes=[]
	all_beats = []
	ans_list = []
	ans_list.append(lines[0]+'\n')
	ans_list.append(lines[1]+'\n')
# get first two lines to list
	for i in range(2,len(lines)):
		if len(lines[i]) > 0:
			note=lines[i].split(',')[0]
			beat=lines[i].split(',')[1]
			all_notes.append(note)
			all_beats.append(beat)
# index 0 is the note and 1 is the beat
# so put them to lists
	for q in range(len(all_notes)):
		index_get = y.index(all_notes[q])
# get the index of the note in the 88notes list
		if index_get + shift <0:
			index_changed = index_get
		elif index_get + shift >(len(y)-1):
			index_changed = index_get
# exceeding cases stay the same
		else:
			index_changed = index_get + shift
		new_note = y[index_changed]	
# get this changed note
		if y[index_get] in changes:
			new_note = changes[y[index_get]]
# change case
		ans_list.append(new_note+','+str(all_beats[q])+'\n')

	new_file_list = filename.split('.')
	new_file_list[0] = new_file_list[0]+'_changed'
	new_file_name = '.'.join(new_file_list)
# new file name
	new_file = open(new_file_name, 'w')
	new_file.writelines(ans_list)
	new_file.close()
def song_as_dict(filename):
	dictionary = {'tempo':0,'tuning':0,'notes':{},'types':{}}
	octave = []
	num_octave=[]
	file = open(filename)
	whole_text = file.read()
	lines = whole_text.split('\n')
	dictionary['tempo'] = int(lines[0])
	dictionary['tuning'] = float(lines[1])
# get these two lines to the dictionary
	for i in range(2,len(lines)):
		if len(lines[i]) > 0:
			note=lines[i].split(',')[0]
			beat=lines[i].split(',')[1]
			note_only = note[:-1]
			note_num = int(note[-1])
# get only the note and only the number
			if note_only not in dictionary['notes'].keys():
				dictionary['notes'][note_only] = {int(note_num):1}
# check if the note is the key of 'notes'
# if not have it to get the key and value becomes 1
			else:
				if note_num not in dictionary['notes'][note_only].keys():
					dictionary['notes'][note_only][int(note_num)] = 1
# check if the number is the key of 'notes''note_only'
				else:
					dictionary['notes'][note_only][int(note_num)] += 1
# add one is its in there	
	for i in range(2,len(lines)):
		if len(lines[i]) > 0:
			note=lines[i].split(',')[0]
			beat1=lines[i].split(',')[1]
			beat = beat1.strip()
			if beat not in dictionary['types'].keys():
				dictionary['types'][beat]=1
			else:
				dictionary['types'][beat]+=1
# same idea for types
	return dictionary
			


			
			
	
