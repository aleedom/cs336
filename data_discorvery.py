import MySQLdb as msdb
from operator import itemgetter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#pandas config
pd.set_option('display.width', 1000000)


db_host = "cs336-1.c28ltethrrc0.us-east-1.rds.amazonaws.com"
db_port = 3306
db_user = "student"
db_pass = "student"
db_db = "DiscoveryChallenge"


conn = msdb.connect(host=db_host,user=db_user,passwd=db_pass,db=db_db)

cursor = conn.cursor()


class BASKETBALL(object):
    """
    columns:
        FirstTeam -- SecondTeam -- Score1 -- Score2 -- TicketsSold -- Day
    """
    def __init__(self,cursor):
        self.cursor = cursor
        self.avg_price = self.get_avg_price()
    def get_avg_price   (self):
        day_index=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        averages = []
        for day in day_index:
            query = "select TicketsSold from BASKETBALL where BASKETBALL.Day='{}'".format(day)
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            s = 0
            for tup in data:
                s += tup[0]
            avg = s/(len(data))
            averages.append(avg)
        return averages

    def score_diff(self):
        test = "select ABS(BASKETBALL.Score1-BASKETBALL.Score2),TicketsSold,Day from BASKETBALL"

        self.cursor.execute(test)
        data = self.cursor.fetchall()
        score_diff = []
        tickets_sold = []
        for tup in data:
            score_diff.append(tup[0])
            tickets_sold.append(tup[1])
        hist = [0]*60
        for data in score_diff:
            hist[data] += 1


        fig1,ax = plt.subplots()
        rects2 = ax.scatter(score_diff,tickets_sold)
        plt.show()

    def tickets_vs_day(self):
        #plot
        ind = np.arange(1,8)
        width = 0.75
        fig,ax = plt.subplots()
        rects1 = ax.bar(ind,self.avg_price,width,color='b')

        ax.set_xlabel('Days')
        ax.set_ylabel('Avg Tickets Sold')
        ax.set_title('Tickets Sold VS Day')
        ax.set_xticks(ind+width*.5)
        ax.set_xticklabels( ('Mon','Tue','Wed','Thu','Fri','Sat','Sun'))
        plt.show()

    def tickets_vs_scoredif(self):
        """
        hello world
        """

class DOGOWNERS(object):
    """
    columns:
        First -- Last -- Personality -- Dog -- Trait -- Dog_Age
    """
    def __init__(self,cursor):
        self.cursor = cursor


class HAPPY(object):
    """
    columns:
        Born -- Lives -- Happiness
    """
    def __init__(self,cursor):
        self.cursor = cursor


class PROFESSOR_MOODY(object):
    """
    columns:
        Lname -- Fname -- Percentile -- Grade -- Attitude -- Seated
    """
    def __init__(self,cursor):
        self.cursor = cursor


class WINEJUNE9(object):
    """
    columns:
        FIXED_ACIDITY -- VOLATILE_ACIDITY -- RESIDUAL_SUGAR -- FREE_SULFUR_DIOXIDE
        -- TOTAL_SULFUR_DIOXIDE -- ALCOHOL -- QUALITY -- COUNTRY -- PRICE_A -- RATE
        -- YEAR -- PH
    """
    def __init__(self,cursor):
        self.cursor = cursor



a = BASKETBALL(cursor)
#a.tickets_vs_day()
a.score_diff()
