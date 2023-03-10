
from LogicApplication.userDataValidation import *

from LogicApplication.getDataFromIMDB import *
from LogicApplication.getAndSetDataFilmStatusUser import *


def addFavorite(name,fav,userid,lat,his):
    userid1 = re.sub("[^0-9]", "", userid.text())

    without_brackets =re.sub(r"[\(\)]","", str(name.text()))

    a=getFilmID(str(without_brackets[:-4]),str(without_brackets[-4:]))
    favorite=getUsersFavoriteFilms(userid1)

    watcghedLater=getUsersWatchLaterFilms(userid1)
    watched=getUsersWatchedFilms(userid1)
    fav.setStyleSheet('background-color: #696d6d')
    if a in favorite:
        fav.setStyleSheet('background-color:rgb(42, 54, 63)')

    elif a in watcghedLater:
        lat.setStyleSheet('background-color:rgb(42, 54, 63)')
    elif a in watched:
        his.setStyleSheet('background-color:rgb(42, 54, 63)')

    addUserFavoriteFilm(userid1, a, favorite, watched, watcghedLater)

def addLater(name,lat,userid,fav,his):
    userid1 = re.sub("[^0-9]", "", userid.text())

    without_brackets = re.sub(r"[\(\)]", "", str(name.text()))

    a = getFilmID(str(without_brackets[:-4]), str(without_brackets[-4:]))
    favorite = getUsersFavoriteFilms(userid1)
    print(favorite)
    watcghedLater = getUsersWatchLaterFilms(userid1)
    watched = getUsersWatchedFilms(userid1)
    lat.setStyleSheet('background-color: #696d6d')
    if a in favorite:
        fav.setStyleSheet('background-color:rgb(42, 54, 63)')

    elif a in watcghedLater:
        lat.setStyleSheet('background-color:rgb(42, 54, 63)')
    elif a in watched:
        his.setStyleSheet('background-color:rgb(42, 54, 63)')

    addUserWatchLaterFilm(userid1, a, favorite, watched, watcghedLater)


def addwatched(name,lat,userid,fav,his):
    userid1 = re.sub("[^0-9]", "", userid.text())

    without_brackets = re.sub(r"[\(\)]", "", str(name.text()))

    a = getFilmID(str(without_brackets[:-4]), str(without_brackets[-4:]))
    favorite = getUsersFavoriteFilms(userid1)
    print(favorite)
    watcghedLater = getUsersWatchLaterFilms(userid1)
    watched = getUsersWatchedFilms(userid1)
    his.setStyleSheet('background-color: #696d6d')
    if a in favorite:
        fav.setStyleSheet('background-color:rgb(42, 54, 63)')
    elif a in watcghedLater:
        lat.setStyleSheet('background-color:rgb(42, 54, 63)')
    elif a in watched:
        his.setStyleSheet('background-color:rgb(42, 54, 63)')

    addUserWatchedFilm(userid1, a, favorite, watched, watcghedLater)


