# the content of the movie database is taken from the textbook Concrete Abstractions: An
# Introduction to Computer Science Using Scheme, by Max Hailperin, Barbara Kaiser, and
# Karl Knight, Copyright (c) 1998 by the authors. Full text is available for free at
from typing import List, Tuple

bands_db: List[Tuple[str, str, int, List[str]]] = [
    (
        "the beatles",  # name
        "rock",  # main genre
        13,  # albums
        [
            "abbey road",
            "magical mystery tour",
            "sgt pepper",
            "The beatles",
            "with the beatles",
            "please please me", 
            "beatles for sale",
            "rubbersoul",
            "help",
            "let it be",
            "a hard day's night",
            "revolver",
            "yellow submarine",
        ],  # albums
    ),
    (
        "The cardigans",
        "pop",
        6,
        [
            "emmerdale",
            "life",
            "first band on the moon",
            "gran turismo",
            "long gone before daylight",
            "super exttra gravity",
        ],
    ),
    (
        "deftones",
        "alternative",
        9,
        [
            "adrenaline",
            "around the fur",
            "white pony",
            "deftones",
            "saturday night wrist",
            "diamond eyes",
            "gore",
            "ohms",
        ],
    ),
    (
        "the smiths",
        "indie rock",
        4,
        [
            "strangeways, here we come",
            "the queen is dead",
            "meat it murder",
            "the smiths",
        ],
    ),
    (
        "the cure",
        "goth",
        13,
        ["three imaginary boys", "seventeen seconds", "faith", "pornography", "the top", "the head on the door", "kiss me, kiss me, kiss me", "disintegration", "wish", "wild mood swings", "bloodflowers", "the cure", "4:13 dream"],
    ),
    (
        "ings",
        "rock",
        7,
        ["wildlife", "red rose speedway", "band in the run", "venus and mars", "wings at the speed of sound", "london town", "back to the egg"],
    ),
    (
        "derek and the dominos",
        "rock",
        1,
        [
            "Layla and other assorted love songs",
        ],
    ),
    (
        "blur",
        "alternative",
        1941,
        [
            "Leisure",
            "modern life is rubbish",
            "parklife",
            "the great escape",
            "blur",
            "13",
            "think tank",
            "the magic whip",
        ],
    ),
    (
        "weezer",
        "alternative",
        15,
        [
            "the blue album",
            "pinkerton",
            "the green album",
            "maladriot",
            "make believe",
            "the red album",
            "raditude",
            "hurley",
            "everything will be alright in the end",
            "the white album",
            "pacific daydream",
            "the black album",
            "the teal album",
            "ok human",
            "van weezer",

        ],
    ),
    (
        "nirvana",
        "alternative",
        3,
        [
            "bleach",
            "nevermind",
            "in utero",
        ],
    ),
    (
        "ten years after",
        "blues rock",
        10,
        [
            "ssssh",
            "stonedhenge",
            "cricklewood green",
            "watt",
            "a space in time",
            "rock and roll music to the world",
            "positive vibrations",
            "about time",
            "now",
            "evolution",
        ],
    ),
    (
        "radiohead",
        "alternative",
        9,
        [
            "pablo honey",
            "the bends",
            "ok computer",
            "kid a",
            "amnesiac",
            "hail to the thief",
            "in rainbows",
            "the king of limbs",
            "a moon shaped pool",
        ],
    ),
    (
        "sonic youth",
        "alternative",
        15,
        [
            "confusion is sex",
            "bad moon rising",
            "evol",
            "sister",
            "daydream nation",
            "goo",
            "dirty",
            "experimental jet set, trash and no star",
            "washing machine",
            "a thousand leaves",
            "nyc ghosts and flowers",
            "murray street",
            "sonic nurse",
            "rather ripped",
            "the eternal",
        ],
    ),
    (
        "kittie",
        "metal",
        7,
        [
            "spit",
            "oracle",
            "until the end",
            "funeral for yesterday",
            "in the black",
            "i've failed you",
            "no so...safe",
        ],
    )

]
