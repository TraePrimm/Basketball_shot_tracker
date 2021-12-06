<h1>Intro</h1>
<b1> For this project I want to be able to track as many elements that I can from a basketball game. I think the most important is scoring so that would be a good starting point.</b1>

<br>
<h1>Data</h1>
<b1>

When collecting data I recorded roughly 2 hours of footage to be processed through 
[vid_to_frame.py](https://github.com/TraePrimm/Basketball_shot_tracker/blob/5d6b978afb6ebdcab41c3f926b557aaeed9a4fc0/.py%20files/vid_to_frame.py). From those images I selected 900 of them which can be found in the files and videos folder.
 
![exampledata](https://github.com/TraePrimm/Basketball_shot_tracker/blob/main/images%20and%20videos/unnamed.jpg?raw=true)

</b1>
<br>
<b1> I used <a href="https://github.com/tzutalin/labelImg">labelImg</a> to process all of my images.<br>
 
 ![labelimg screenshot](https://github.com/TraePrimm/Basketball_shot_tracker/blob/74bc7427929bc37344dd4cf3f3fd8f40cab5411b/images%20and%20videos/labelimg.png)</b1>
 
 <h1> Model </h1>
 <b1>
I used darknet for the yolov4 model which can be found <a href="https://github.com/AlexeyAB/darknet">here</a>. </b1>

<b1> This project was used for two of my classes and I can say I am happy about the results and would like to strive to advance this to a more complete system. <br> Here is a snipit from the demo video.<br>
![exampledata](https://github.com/TraePrimm/Basketball_shot_tracker/blob/a0e943562d9f5643fd53f8add920f334d6b92fbb/images%20and%20videos/demo.gif)<br>
</b1>
 <b1>
I was unable to upload the weigt file to github so <a href="https://www.mediafire.com/file/3652vqzgoebdz06/yolov4-basketball_final.weights/file">here</a> is a link to download it.
