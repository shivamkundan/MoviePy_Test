
# Google Roads API key AIzaSyDWfgw7VvZqrMW0neLvY0e7u5qOgxZL6uY
# https://developers.google.com/maps/documentation/roads/speed-limits
# https://wcedmisten.fyi/post/dashcam-to-speed-limits/
# https://github.com/wcedmisten/piofo  -- cool


# need:
# valid bit        [RMC]
# epoch/Timestamp  [RMC]
# (lat, long)	   [RMC]
# speed kts -> mph [RMC]
# true heading (?) [RMC]
# num satellites   [GSV]

# HDOP,VDOP,PDOP   [GSA]

# ==== calc these ==== #
# trip start time
# gps sig start time
# trip end time
# total trip time
# total driving time
# total stopping/waiting time
# distance traveled -> calc from (lat, long)
# num of stops
# avg/median/min/max time stopped

# ==================================================================================================== #
# ==================================================================================================== #
# ----------------------------------------------------------------------------------------------------
# GPGLL
# 1    5133.81   Current latitude
# 2    N         North/South
# 3    00042.25  Current longitude
# 4    W         East/West
# 5    *75       checksum
GPGLL_headers=["epoch","code","latitude","N/S","longitude","E/W","timestamp","validity","","Checksum"]

# ----------------------------------------------------------------------------------------------------
# GPRMC
# KTS  to MPH: for an approximate result, multiply the speed value by 1.151
# KTS to KMPH: multiply the speed value by 1.852
# KMPH to MPH: for an approximate result, divide   the speed value by 1.609
# MPH to m/s: divide the speed value by 2.237


# 1   220516     Time Stamp
# 2   A          validity - A-ok, V-invalid
# 3   5133.82    current Latitude
# 4   N          North/South
# 5   00042.24   current Longitude
# 6   W          East/West
# 7   173.8      Speed in knots
# 8   231.8      True course
# 9   130694     Date Stamp
# 10  004.2      Variation
# 11  W          East/West
# 12  *70        checksum

# -------------
# $GPRMC,210230,A,3855.4487,N,09446.0071,W,0.0,076.2,130495,003.8,E*69
# The sentence contains the following fields:
# Epoch
# Code/The sentence type
# Current time (if available; UTC)
# Position status (A for valid, V for invalid)
# Latitude (in DDMM.MMM format)
# Latitude compass direction
# Longitude (in DDDMM.MMM format)
# Longitude compass direction
# Speed (in knots per hour)
# Heading
# Date (DDMMYY)
# Magnetic variation
# Magnetic variation direction
# The checksum validation value (in hexadecimal)

GPRMC_headers=["epoch","code","timestamp","validity","latitude","N/S","longitude","E/W",\
				"Speed (kts)","Heading","Date Stamp","Mag Variation","Mag Variation Dir","valid?","Checksum"]

# ----------------------------------------------------------------------------------------------------
# GPVTG
# 054.7,T      True track made good
# 034.4,M      Magnetic track made good
# 005.5,N      Ground speed, knots
# 010.2,K      Ground speed, Kilometers per hour
GPVTG_headers=["epoch","code","True track made good"," Magnetic track made good","Speed (kts)","Speed (kmph)"]

# ----------------------------------------------------------------------------------------------------
# GPGSV
# 1    = Total number of messages of this type in this cycle
# 2    = Message number
# 3    = Total number of SVs in view
# 4    = SV PRN number
# 5    = Elevation in degrees, 90 maximum
# 6    = Azimuth, degrees from true north, 000 to 359
# 7    = SNR, 00-99 dB (null when not tracking)
# 8-11 = Information about second SV, same as field 4-7
# 12-15= Information about third SV, same as field 4-7
# 16-19= Information about fourth SV, same as field 4-7

# -------------
# $GPGSV,2,1,08,02,74,042,45,04,18,190,36,07,67,279,42,12,29,323,36*77
# $GPGSV,2,2,08,15,30,050,47,19,09,158,,26,12,281,40,27,38,173,41*7B

# The GSV sentence contains the following fields:

# The sentence type
# The number of sentences in the sequence
# The number of this sentence
# The number of satellites
# The satellite number, elevation, azimuth, and signal to noise ratio for each satellite
# The checksum validation value (in hexadecimal)

GPGSV_headers=["epoch","code","#MSGS","MSG_NUM","#SVs","SV PRN#","ELV","AZM","SNR","","","","","","","","","","","","",""]


# ----------------------------------------------------------------------------------------------------
# GPGSA
# 1    = Mode:
#        M=Manual, forced to operate in 2D or 3D
#        A=Automatic, 3D/2D
# 2    = Mode:
#        1=Fix not available
#        2=2D
#        3=3D
# 3-14 = IDs of SVs used in position fix (null for unused fields)
# 15   = PDOP
# 16   = HDOP
# 17   = VDOP
GPGSA_headers=["epoch","code","manual/auto","mode"]

