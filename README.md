
# spotify-to-stl
spotify-to-stl is a python command-line based program designed to get .stl file of 'spotify code' based on spotify url.

# Installation
For usage of this program you need those 5 files: `spotify-to-stl.py`, `get_svg_file.py`, `parse_svg.py`, `template17.stl`, `chromedriver.exe`  
And you have to have installed:
- `pip install numpy`
- `pip install numpy-stl`
- `pip install selenium`  
# Usage
`spotify-to-stl.py [spotify-url]` <br><br>

# Example
You start by copying spotify song url as below.
![alt text](https://github.com/Silvesterrr/spotify_song_to_stl/blob/main/example.jpg?raw=true)

Than you run python file from console <br>
`spotify-to-stl.py spotify:track:5W3cjX2J3tjhG8zb6u0qHn`  
And after this we get something like this:<br>
![alt text](https://github.com/Silvesterrr/spotify-to-stl/blob/main/examples/1.PNG?raw=true)
![alt text](https://github.com/Silvesterrr/spotify-to-stl/blob/main/examples/IMG_20210322_135852.jpg?raw=true)
And mostly that's it.

# Requirements and Other
- You have to have python installed.  
- Make sure that `chromedriver` added in the files is in thesame folder as python file
- Make sure that you have chrome browser installed.
- If the `chromedriver` added in the files won't work download it from this webside https://chromedriver.chromium.org/downloads (version equal to your chrome version).  

### Common problems
I found out that slicing with PrusaSlicer can cause some problem as below:  
![alt text](https://github.com/Silvesterrr/spotify-to-stl/blob/main/examples/2.PNG?raw=true)
I just run the .stl file through repair webside (https://www.formware.co/onlinestlrepair) and the problem **dissapeard**  
<br>
Hope You like it.  
If you want to make new template I suggest editing existing one. I recomend to contact with me, I will explain how stuff works.  
If you have any problems, or you have any suggestions feel free to contact me at: `sylwesterjarosz50@gmail.com`
