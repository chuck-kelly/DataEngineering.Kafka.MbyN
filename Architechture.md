two producers 
    -one produces small rectangles(1-10 side lenght)
        -list of two intergers , [2,4] or [9,2]
        -and sends that list to the 'small-rectangle size' topic
    -one produced big recrangles (1-20 side lenght)
        -list of two intergers , [12,4] or [9,20]
        -and sends that list to the 'big-rectangle size' topic

six consumers
    -3 for each topic
        -will read in the lastest message sent to the topic they are looking at and will print the rectangle info into the terminal based on the consumer
        -one comsumer finds the area
        -two consumer finds the perimeter
        -three comsumer finds if it is a square

run main.py to launch all consumers and then both producers that produce 20 rectangles
