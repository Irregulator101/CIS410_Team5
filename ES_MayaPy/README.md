Eric Schultz
11/2/2015 - 11/9/2015

I think I've been able to identify how MayaPy sends commands to Maya - I'm trying to add my own Lego Animations 
buttons and section to the existing QT interface... I've got all the necessary Python lines (or so I thought) 
but I don't see it show up. Wondering what to do. Will keep exploring. 
Ah, it needs a widget.ui file. Okay. I have to get QT to cooperate with Python it looks like. This should be 
interesting. I'll have to figure this out a bit later.
I've modifed the home widget and created a "Lego Animations" widget ui file.
Using the python code provided for the assignment1 widget, I've managed to create and assign commands to various buttons 
on my lego animations widget. With liberal use of the setKeyframe() command!