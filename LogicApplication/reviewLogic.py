from LogicApplication.DB_connector import *
import mysql.connector

def getLikesListForThisFilmReviews(idFilm):
    con = createConnection()
    cur = con.cursor()
    sqlGetLikesListForThisFilmID = """
    SELECT rs.id_user, rs.id_review, rs.score FROM films_review
    JOIN review_score rs
    ON films_review.id = rs.id_review
    WHERE id_films = %s;"""
    cur.execute(sqlGetLikesListForThisFilmID, (idFilm,))
    exe = cur.fetchall()
    return exe

def deleteReviewVoteForThisUser(idUser, idReview, con = createConnection()):
    cur = con.cursor()
    sql = """
    DELETE FROM review_score WHERE id_user = %s AND id_review = %s"""
    cur.execute(sql, (idUser, idReview))

def updateReviewVoteForThisUser(idUser, idReview, score, con = createConnection()):
    cur = con.cursor()
    sql = """
    UPDATE review_score SET score = %s WHERE id_user = %s AND id_review = %s"""
    cur.execute(sql, (score, idUser, idReview))

def insertReviewVoteForThisUser(idUser, idReview, score, con = createConnection()):
    cur = con.cursor()
    sql = """
    INSERT INTO review_score (score, id_user, id_review) VALUES (%s, %s, %s)"""
    cur.execute(sql, (score, idUser, idReview))

def reviewScoreButton(idUser, idReview, score, likesReviewsListForThisFilm):
    con = createConnection()
    cur = con.cursor()
    check = 0
    for i in likesReviewsListForThisFilm:
        if (i[0] == idUser and i[1] == idReview):
            if (i[2] == score):
                deleteReviewVoteForThisUser(idUser, idReview, con)
                check = 1
                print("Already exists, deleting...")
            elif(i[2] == -score):
                updateReviewVoteForThisUser(idUser, idReview, score, con)
                check = 1
                print("Already exists separate one, updating...")
    if check == 0:
        insertReviewVoteForThisUser(idUser, idReview, score, con)
        print("Not exists, creating...")
    con.commit()