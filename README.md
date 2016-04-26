

Graham Scan
===========

CLRS Ch. 33. Graham’s scan finds the smallest bounding polygon among a set of points!

basically, it finds the lowest (and then lowest left in case of tie) point and then does a counterclockwise rotational sweep to make sure that it gets each vertex, removing anything it comes across that require non-left turns. The result comes out like this:

![Graham's scan bounding box plotted in matplotlib](https://41.media.tumblr.com/2d26693c2dd940186203a9676c808e66/tumblr_inline_o66n5nilmN1tewibc_1280.png)

:wq,
--ankeet
