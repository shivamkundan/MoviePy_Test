# MoviePy_Test

## About
Video compositing and rendering using Python. Supplement to my dash cam visualization project.

### Work Flow
The following pipelined flowchart depicts how input is processed. Pipeline stages are represented by the variable ***T***. Tasks in the same stage can be executed in parallel.

<p align="center">
  <img src="flowchart.png" alt="flowchart" width="70%" height="70%"/>
</p>

#### ***T***=0 
I have raw video recordings from my dash cam's front and rear channels. Currently both are set to record at 1080@30fps, which results in considerable file size.

#### ***T***=1
Both front and rear videos have GPS and (and accelerometer) readings embedded in the .mp4 files. 

I use the unix *strings* command to convert files to text. The resulting GPS data is in NMEA format, which is further processed and stored in an excel file.

#### ***T***=2
Advanced processing of the data such as lat/long conversion, unix epoch conversion, distance calculation, etc.

If initial parsing from T=1 was successful, the video combiner/cropper can begin execution in parallel. This is helpful since each 3-minute long video is in 1080p@30FPS, which makes rendering a long process.


