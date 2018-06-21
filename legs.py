# Format for the dictionary: {"leg_1":{"knee":{"outwards": (0 , 190)
# left_row["leg_2"]["hip"]["down"]
# would return (4, 390)
# First key defines which leg (ranging from leg_1 to leg_3),
# second key chooses which limb to move
# and third key defines direction on that limb, returning servo-port
# and what value to send for the correct position


# Left row of legs (rotate values are mirrored due to construction)

left = {
"leg_1":
    {
        "knee":
            {
                "inwards": (0, 0, 190),
                "outwards": (0, 0, 390),
                "vertical": (0, 0, 285)},
        "hip":
            {
                "up": (0, 1, 190),
                "down": (0, 1, 390),
                "levelled": (0, 1, 285)},
        "rotate":
            {
                "forward": (0, 2, 390),
                "backwards": (0, 2, 190),
                "right_angel": (0, 2, 285)}
    },

"leg_2":
    {
        "knee":
            {
                "inwards": (0, 3, 190),
                "outwards": (0, 3, 390),
                "vertical": (0, 3, 285)},
        "hip":
            {
                "up": (0, 4, 190),
                "down": (0, 4, 390),
                "levelled": (0, 4, 285)},
        "rotate":
            {
                "forward": (0, 5, 390),
                "backwards": (0, 5, 190),
                "right_angel": (0, 5, 285)}
    },

"leg_3":
    {
        "knee":
            {
                "inwards": (0, 6, 190),
                "outwards": (0, 6, 390),
                "vertical": (0, 6, 285)},
        "hip":
            {
                "up": (0, 7, 190),
                "down": (0, 7, 390),
                "levelled": (0, 7, 285)},
        "rotate":
            {
                "forward": (0, 8, 390),
                "backwards": (0, 8, 190),
                "right_angel": (0, 8, 285)}
    }

}

# Right row of legs

right = {
"leg_1":
    {
        "knee":
            {
                "inwards": (0, 0, 190),
                "outwards": (0, 0, 390),
                "vertical": (0, 0, 285)},
        "hip":
            {
                "up": (1, 0, 190),
                "down": (1, 0, 390),
                "levelled": (1, 0, 285)},
        "rotate":
            {
                "forward": (2, 0, 190),
                "backwards": (2, 0, 390),
                "right_angel": (2, 0, 285)}
    },

"leg_2":
    {
        "knee":
            {
                "inwards": (3, 0, 190),
                "outwards": (3, 0, 390),
                "vertical": (3, 0, 285)},
        "hip":
            {
                "up": (4, 0, 190),
                "down": (4, 0, 390),
                "levelled": (4, 0, 285)},
        "rotate":
            {
                "forward": (5, 0, 190),
                "backwards": (5, 0, 390),
                "right_angel": (5, 0, 285)}
    },

"leg_3":
    {
        "knee":
            {
                "inwards": (6, 0, 190),
                "outwards": (6, 0, 390),
                "vertical": (6, 0, 285)},
        "hip":
            {
                "up": (7, 0, 190),
                "down": (7, 0, 390),
                "levelled": (7, 0, 285)},
        "rotate":
            {
                "forward": (8, 0, 190),
                "backwards": (8, 0, 390),
                "right_angel": (8, 0, 285)}
    }

}