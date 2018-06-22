# Format for the dictionary: {"leg_1":{"knee":{"outwards": (0 , 200)
# left_row["leg_2"]["hip"]["down"]
# would return (4, 300)
# First key defines which leg (ranging from leg_1 to leg_3),
# second key chooses which limb to move
# and third key defines direction on that limb, returning servo-port
# and what value to send for the correct position


# Left row of legs (rotate values has to be mirrored due to construction)

left = {
"leg_1":
    {
        "knee":
            {
                "inwards": (0, 0, 200),
                "outwards": (0, 0, 300),
                "vertical": (0, 0, 400)},
        "hip":
            {
                "up": (1, 0, 200),
                "down": (1, 0, 300),
                "levelled": (1, 0, 400)},
        "rotate":
            {
                "forward": (2, 0, 200),
                "backwards": (2, 0, 300),
                "right_angel": (2, 0, 400)}
    },

"leg_2":
    {
        "knee":
            {
                "inwards": (3, 0, 200),
                "outwards": (3, 0, 300),
                "vertical": (3, 0, 400)},
        "hip":
            {
                "up": (4, 0, 200),
                "down": (4, 0, 300),
                "levelled": (4, 0, 400)},
        "rotate":
            {
                "forward": (5, 0, 200),
                "backwards": (5, 0, 300),
                "right_angel": (5, 0, 400)}
    },

"leg_3":
    {
        "knee":
            {
                "inwards": (6, 0, 200),
                "outwards": (6, 0, 300),
                "vertical": (6, 0, 400)},
        "hip":
            {
                "up": (7, 0, 200),
                "down": (7, 0, 300),
                "levelled": (7, 0, 400)},
        "rotate":
            {
                "forward": (8, 0, 200),
                "backwards": (8, 0, 300),
                "right_angel": (8, 0, 400)}
    }

}

# Right row of legs

right = {
"leg_1":
    {
        "knee":
            {
                "inwards": (0, 0, 200),
                "outwards": (0, 0, 300),
                "vertical": (0, 0, 400)},
        "hip":
            {
                "up": (1, 0, 200),
                "down": (1, 0, 300),
                "levelled": (1, 0, 400)},
        "rotate":
            {
                "forward": (2, 0, 200),
                "backwards": (2, 0, 300),
                "right_angel": (2, 0, 400)}
    },

"leg_2":
    {
        "knee":
            {
                "inwards": (3, 0, 200),
                "outwards": (3, 0, 300),
                "vertical": (3, 0, 400)},
        "hip":
            {
                "up": (4, 0, 200),
                "down": (4, 0, 300),
                "levelled": (4, 0, 400)},
        "rotate":
            {
                "forward": (5, 0, 200),
                "backwards": (5, 0, 300),
                "right_angel": (5, 0, 400)}
    },

"leg_3":
    {
        "knee":
            {
                "inwards": (6, 0, 200),
                "outwards": (6, 0, 300),
                "vertical": (6, 0, 400)},
        "hip":
            {
                "up": (7, 0, 200),
                "down": (7, 0, 300),
                "levelled": (7, 0, 400)},
        "rotate":
            {
                "forward": (8, 0, 200),
                "backwards": (8, 0, 300),
                "right_angel": (8, 0, 400)}
    }

}
