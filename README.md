# ImageSequenceFill
A small python program to fill in missing images (pngs currently) from an image sequence with blank images for easy importing and use in video editing software.
If you have an image sequence that is missing frames (for example test101.png-test201.png and then a gap of frames, and then test301.png-test501.png), this program will fill those missing frames with blank frames, allowing for easy importing into video editors like Adobe Premiere and/or After Effects. 
## Requirments
You'll need to make sure python is installed and you have a working pillow or PIL installation.

# How to run
Firstly, copy and paste the python script into the directory you want to fill in the gaps.
Then, edit the python file so that the name and numbering scheme matches the scheme of the 
files. (Ex: change match = re.match(r"default_image_name(\d+)\.png", file) to match = re.match(r"name_of_desired_image(\d+)\.png", file))
Change the directories as well in the fill_gaps function, and change the first file's name and numbering to match your desired format/name
Then run the program (python fill_gaps.py)
It should have added empty image files in between the rendered images.
