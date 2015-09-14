import MySQLdb as msdb
import pandas as pd


def queries():
    """
    1.  Drinkers who  do not frequent Seven Bamboo
    2.  Drinkers who frequent only Blue Angel
    3.  Drinkers who frequent exactly two bars
    4.  Drinkers who frequent at least two bars
    5.  Drinkers who frequent all bars
    6.  Drinkers who frequent bars which serve some beer they like
    7.  Drinkers who only frequent bars which serve beers they like
    8.  Drinkers who like every beer served by Caravan
    9.  Beers that are served at exactly two bars
    10. Beers served for exactly $5 at either Cabana or The B-Hive, or both
    11. Find the average price of all beer served at Cabana
    12. Bars that serve some beer that is served only by itself
    13. Bars that are frequented by both Mike and John
    14. Bars that sell the beer Budweiser for $5 or less
    15. Bars that do not sell any beers for exactly $5
    16. Bars that serve Budweiser and are frequented by at least one customer who likes Blue Moon

    """


    def q1():
        """ Drinkers who  do not frequent Seven Bamboo """
        q = "SELECT distinct(Drinker) FROM BarBeerDrinker.frequents WHERE Drinker not in \
                (Select Drinker FROM BarBeerDrinker.frequents WHERE bar = 'Seven Bamboo')"
        cursor.execute(q)
        data = cursor.fetchall()

        df = pd.DataFrame( [[ij for ij in i] for i in data] )

        #df.rename(columns = {0:'Drinker',1:'Bar'},inplace=True)
        print(df)

    def q2():
        """ Drinkers who frequent only Blue Angel """
        q = "SELECT DISTINCT(Drinker) FROM BarBeerDrinker.frequents WHERE bar = 'Blue Angel' and Drinker not in \
                (Select Drinker FROM BarBeerDrinker.frequents WHERE bar != 'Blue Angel')"
        cursor.execute(q)
        data = cursor.fetchall()

        df = pd.DataFrame( [[ij for ij in i] for i in data] )

        #df.rename(columns = {0:'Drinker',1:'Bar'},inplace=True)
        print(df)

    def q3():
        """ Drinkers who frequent exactly two bars """
        q = "SELECT Drinker,Count(*) FROM BarBeerDrinker.frequents GROUP BY Drinker Having Count(*)=2"
        cursor.execute(q)
        data = cursor.fetchall()

        df = pd.DataFrame( [[ij for ij in i] for i in data] )
        df.rename(columns = {0:'Drinker',1:'Count'},inplace=True)
        df = df.sort(['Drinker'], ascending=[1])
        #df.rename(columns = {0:'Drinker',1:'Bar'},inplace=True)
        print(df)

    def q4():
        """ Drinkers who frequent at least two bars """
        q = "SELECT Drinker,Count(*) FROM BarBeerDrinker.frequents GROUP BY Drinker Having Count(*)>=2"
        cursor.execute(q)
        data = cursor.fetchall()

        df = pd.DataFrame( [[ij for ij in i] for i in data] )
        df.rename(columns = {0:'Drinker',1:'Count'},inplace=True)
        df = df.sort(['Count'], ascending=[1])
        #df.rename(columns = {0:'Drinker',1:'Bar'},inplace=True)
        print(df)

    def q5():
        """ Drinkers who frequent all bars """
        q = "SELECT Drinker,Count(*) as c1 FROM BarBeerDrinker.frequents GROUP BY Drinker Having c1 = (Select Count(*) FROM bars)"
        cursor.execute(q)
        data = cursor.fetchall()

        df = pd.DataFrame( [[ij for ij in i] for i in data] )

        #df.rename(columns = {0:'Drinker',1:'Bar'},inplace=True)
        print(df)

    def q6():
        """ Drinkers who frequent bars which serve some beer they like """
        q = "SELECT distinct(f.Drinker) FROM BarBeerDrinker.frequents AS f,BarBeerDrinker.sells AS s,BarBeerDrinker.likes AS l WHERE \
                f.Drinker = l.Drinker AND \
                l.beer = s.beer AND \
                s.bar = f.bar"


        cursor.execute(q)
        data = cursor.fetchall()

        df = pd.DataFrame( [[ij for ij in i] for i in data] )

        #df.rename(columns = {0:'Drinker',1:'Bar'},inplace=True)
        print(df)

    def q7():
        """ Drinkers who only frequent bars which serve some beer they like """
        q = "SELECT DISTINCT f.drinker FROM frequents as f WHERE NOT EXISTS ( \
                SELECT 1 FROM frequents WHERE NOT EXISTS \
                        (SELECT 1 FROM sells as s WHERE s.bar=f.bar AND \
                                s.beer IN (SELECT l.beer FROM likes as l WHERE l.drinker=f.drinker) ) \
                                        AND f.drinker=f.drinker )"

        cursor.execute(q)
        data = cursor.fetchall()

        df = pd.DataFrame( [[ij for ij in i] for i in data] )

        #df.rename(columns = {0:'Drinker',1:'Bar'},inplace=True)
        print(df)

    def q8():
        """ Drinkers who like every beer served by Caravan
        """
        q = "SELECT l.Drinker \
                FROM BarBeerDrinker.likes as l ,BarBeerDrinker.sells as s \
                WHERE s.bar='Caravan' and s.beer=l.beer \
                group by l.Drinker \
                having count(l.beer) = (\
                SELECT Count(*) FROM BarBeerDrinker.sells where sells.bar='Caravan')"


        cursor.execute(q)
        data = cursor.fetchall()

        df = pd.DataFrame( [[ij for ij in i] for i in data] )

        #df.rename(columns = {0:'Drinker',1:'Bar'},inplace=True)
        print(df)
    def q9():
        """ Beers that are served at exactly two bars """
        q = "SELECT s.beer \
                FROM BarBeerDrinker.sells as s \
                GROUP BY s.Beer\
                having count(s.Bar)=2"

        cursor.execute(q)
        data = cursor.fetchall()

        df = pd.DataFrame( [[ij for ij in i] for i in data] )

        #df.rename(columns = {0:'Drinker',1:'Bar'},inplace=True)
        print(df)

    def q10():
        """ Beers served for exactly $5 at either Cabana or The B-Hive, or both """
        q = "SELECT s.Beer \
                FROM BarBeerDrinker.sells as s\
                WHERE price = 5.00 and (s.bar = 'Cabana' or s.bar='The B-Hive')"

        cursor.execute(q)
        data = cursor.fetchall()

        df = pd.DataFrame( [[ij for ij in i] for i in data] )

        #df.rename(columns = {0:'Drinker',1:'Bar'},inplace=True)
        print(df)

    def q11():
        """ Find the average price of all beer served at Cabana """
        q = "SELECT AVG(price) \
                FROM BarBeerDrinker.sells as s\
                WHERE s.bar = 'Cabana'\
                GROUP BY bar"

        cursor.execute(q)
        data = cursor.fetchall()

        df = pd.DataFrame( [[ij for ij in i] for i in data] )

        #df.rename(columns = {0:'Drinker',1:'Bar'},inplace=True)
        print(df)

    def q12():
        """ Bars that serve some beer that is served only by itself """
        q = "SELECT s.bar,count(s.beer)\
                FROM BarBeerDrinker.sells as s\
                GROUP BY bar\
                HAVING count(s.beer) = 1"
        cursor.execute(q)
        data = cursor.fetchall()

        df = pd.DataFrame( [[ij for ij in i] for i in data] )

        #df.rename(columns = {0:'Drinker',1:'Bar'},inplace=True)
        print(df)

    def q13():
        """ Bars that are frequented by both Mike and John """
        q = "SELECT DISTINCT(f1.Bar) \
                FROM BarBeerDrinker.frequents as f1,BarBeerDrinker.frequents as f2\
                WHERE f1.Drinker='Mike' and f2.Drinker='John'"

        cursor.execute(q)
        data = cursor.fetchall()

        df = pd.DataFrame( [[ij for ij in i] for i in data] )

        #df.rename(columns = {0:'Drinker',1:'Bar'},inplace=True)
        print(df)

    def q14():
        """ Bars that sell the beer Budweiser for $5 or less """
        q = "SELECT s.Bar \
                FROM BarBeerDrinker.sells as s\
                WHERE beer = 'Budweiser' and price<=5\
                GROUP BY bar"

        cursor.execute(q)
        data = cursor.fetchall()

        df = pd.DataFrame( [[ij for ij in i] for i in data] )

        #df.rename(columns = {0:'Drinker',1:'Bar'},inplace=True)
        print(df)

    def q15():
        """ Bars that do not sell any beers for exactly $5 """
        q = "SELECT DISTINCT(s.bar) \
                FROM BarBeerDrinker.sells as s\
                WHERE bar not in (\
                    Select s2.bar \
                        FROM BarBeerDrinker.sells as s2\
                        WHERE price = 5\
                )"
        cursor.execute(q)
        data = cursor.fetchall()

        df = pd.DataFrame( [[ij for ij in i] for i in data] )

        #df.rename(columns = {0:'Drinker',1:'Bar'},inplace=True)
        print(df)

    def q16():
        """ Bars that serve Budweiser and are frequented by at least one customer who likes Blue Moon """
        q = "SELECT s.bar \
                FROM BarBeerDrinker.sells as s,BarBeerDrinker.frequents as f,BarBeerDrinker.likes as l\
                WHERE s.beer='Budweiser' and f.bar = s.bar and f.Drinker=l.Drinker and l.beer='Blue Moon'"
        cursor.execute(q)
        data = cursor.fetchall()

        df = pd.DataFrame( [[ij for ij in i] for i in data] )

        #df.rename(columns = {0:'Drinker',1:'Bar'},inplace=True)
        print(df)

    return q16



db_host = "cs336-2.c28ltethrrc0.us-east-1.rds.amazonaws.com"
db_port = 3306
db_user = "student"
db_pass = "student"
db_db = "BarBeerDrinker"

conn = msdb.connect(host=db_host,user=db_user,passwd=db_pass,db=db_db)
cursor = conn.cursor()
a = queries();
a()
conn.close()
