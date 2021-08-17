# Song-generator
<h>program that can generate songs to an output file with random notes, find the note in the input file, change the notes in the input file, and print out the song in dictionary format with the input file.</h>
<p><b>random_song(filename, tempo, tuning, num_measures)</b><p>
<p>Description: Uses the random module to write song made of random notes to a file given the name of the song
to write to, the desired tempo, and the desired tuning frequency, and the number of measures this song is. We
want to make sure that the song you generate would be a valid song in terms of beats in measures, so you are
going to pick random notes using the following algorithm:</p>
<p>1. Loop as long as you have not completed the number of measures that is being asked for, then build the next
measure by doing the following:<p>
<p>a. Pick a random valid index in this exact list:
["Sixteenth", "Eighth", 'Quarter', 'Half','Whole']
b. If this note type at the index that you pick can fit in this measure (the number of beats it requires
is less than or equal to the number of beats left in the measure) then:</p>
<p>i. Select a random index in this exact list:
["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
ii. Select a random octave from 1 to 7 (we're ignoring the incomplete octaves 0 and 8)
iii. join the note type, note, and octave together, and write this as a line in the output file</p>
<p>c. If the note duration selected doesn't fit in the measure, throw away this note and try again in the
next iteration of the loop, to pick a new random index to try until a note type that fits is selected.</p>
<p>Parameters: filename (string) the name of the output file to write to, tempo (int) the BPM of the song, tuning
(float) the base frequency to use for the note A4, and num_measures (int) the number of measure of song to write</p>
<p>Return value: None (all output goes to a file)</P>


