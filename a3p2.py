
from bands import bands_db
from match import match
from typing import List, Tuple, Callable, Any

def get_name(band: Tuple[str, str, int, List[str]]) -> str:
    return band[0]


def get_genre(band: Tuple[str, str, int, List[str]]) -> str:
    return band[1]


def get_albumnum(band: Tuple[str, str, int, List[str]]) -> int:
    return band[2]


def get_albums(band: Tuple[str, str, int, List[str]]) -> List[str]:
    return band[3]



def genre_by_name(matches: List[str]) -> List[str]:
  
    result = []
    for band in band_db:
        if get_genre(band) == matches[0]:
            result.append(get_genre(band))
    
    return result 




def name_by_genre(matches: List[str]) -> List[str]:

    result = []
    for band in band_db:
        if get_genre(band) == matches[0]:
            result.append(get_name(band))
    
    return result 


def albums_by_name(matches: List[str]) -> List[str]:
    
    result = []
    for band in band_db:
        if get_name(band) == matches[0]:
            result = get_albums(band)
    
    return result




def albumnum_by_name(matches: List[str]) -> List[int]:
  
    result = []
    for band in band_db:
        if get_name(band) == matches[0]:
            result.append(get_albumnum(band))
    
    return result




def name_by_albums(matches: List[str]) -> List[str]:
    
    result = []
    for band in band_db:
        if matches[0] in get_albums(band):
            result.append(get_name(band))
    
    return result 




# dummy argument is ignored and doesn't matter
def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt


# The pattern-action list for the natural language query system A list of tuples of
# pattern and action It must be declared here, after all of the function definitions
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [

    (str.split("what genre is %"), genre_by_name),
    (str.split("what bands are %"), name_by_genre),
    (str.split("what albums were made by %"), albums_by_name),
    (str.split("how many albums has % made"), albumnum_by_name),
    (str.split("what band has the % album"), name_by_albums),
    (["bye"], bye_action),
]


def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    for pat, act in pa_list:
        mat = match(pat, src)
        if mat is not None:
            answer = act(mat)
            # print(answer)
            return answer if answer else ["No answers"]   
    return ["I don't understand"]



def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the movie database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")


