# Sprite format definition

The definition was created by SAP Commerce and just documented here for a
better understanding.

There are 5 images inside the sprite, each one in a different color. The sprite
is 80x16 pixels, so every image inside is 16x16. Structure:

```
   16px
  -------
  |  1  | 16px
  -------
  |  2  | 16px
  -------
  |  3  | 16px
  -------
  |  4  | 16px
  -------
  |  5  | 16px
  -------
```

The colors used in the different images have the following HEX values:

 - Image 1: #7F90A5 (grey)
 - Image 2: #55667A (dark grey)
 - Image 3: #0486E0 (blue)
 - Image 4: #0486E0 (blue)
 - Image 5: #BEC4D1 (light grey)

Final result of the sprite:

![sprite image](../exampleIcons/backoffice-star.png)