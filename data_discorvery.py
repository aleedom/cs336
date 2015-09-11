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

    def get_score_diff(self):
        test = "select ABS(BASKETBALL.Score1-BASKETBALL.Score2),TicketsSold,Day from BASKETBALL"

        #bin1 = "select * from BASKETBALL where ABS(BASKETBALL.Score1-BASKETBALL.Score2) <= 5"
        #bin2 = "select * from BASKETBALL where ABS(BASKETBALL.Score1-BASKETBALL.Score2) > 5 and ABS(BASKETBALL.Score1-BASKETBALL.Score2) <= 10"
        #bin3 = "select * from BASKETBALL where ABS(BASKETBALL.Score1-BASKETBALL.Score2) > 10 and ABS(BASKETBALL.Score1-BASKETBALL.Score2) <= 15"
        #bin4 = "select * from BASKETBALL where ABS(BASKETBALL.Score1-BASKETBALL.Score2) > 15 and ABS(BASKETBALL.Score1-BASKETBALL.Score2) <= 20"
        #bin5 = "select * from BASKETBALL where ABS(BASKETBALL.Score1-BASKETBALL.Score2) > 20 and ABS(BASKETBALL.Score1-BASKETBALL.Score2) <= 25"
        #bin6 = "select * from BASKETBALL where ABS(BASKETBALL.Score1-BASKETBALL.Score2) > 25 and ABS(BASKETBALL.Score1-BASKETBALL.Score2) <= 30"
        #bin7 = "select * from BASKETBALL where ABS(BASKETBALL.Score1-BASKETBALL.Score2) > 30"
        self.cursor.execute(test)
        data = self.cursor.fetchall()
        l = []
        for tup in data:
            l.append(tup[0])
        hist = [0]*60
        for data in l:
            hist[data] += 1

        ind = np.arange(len(hist))
        width = 0.4
        fig,ax = plt.subplots()
        rects1 = ax.bar(ind,hist,width,color='b')

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
a.get_score_diff()
