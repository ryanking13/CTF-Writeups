## Meta Find Me - 70

### Description

Find the location of the flag in the image: image.jpg. Note: Latitude and longitude values are in degrees with no degree symbols,/direction letters, minutes, seconds, or periods. They should only be digits. The flag is not just a set of coordinates - if you think that, keep looking!

### Hint

  - How can images store location data? Perhaps search for GPS info on photos.

### Write up

    $ exiftool image.jpg
    ...
    Comment : "Your flag is flag_2_meta_4_me_<lat>_<lon>_f8ad. Now find the GPS coordinates of this image! (Degrees only please)"
    ...
    GPS Latitude : 91 deg 0' 0.00"
    GPS Longitude : 124 deg 0' 0.00"


> flag_2_meta_4_me_91_124_f8ad
