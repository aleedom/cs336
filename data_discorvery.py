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
        averages = [0]*7
        query = "select Day,AVG(TicketsSold) from BASKETBALL group by Day"
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        #order the data correcly and make it into a list
        #record starts as a tuple of tuples, becomes a list of integers
        #ordered by day starting with monday
        for record in data:
            averages[day_index.index(record[0])] = int(record[1])
        print("Average price: {}".format(averages))
        return averages



    def scorediff_vs_tickets(self):
        """
        while the data itself isn't very usefull the shape of the data is quite interesting.
        The shape,which is very square, shows that most games sell a minimum amount of tickets (5000),
        most stadiums only seat 10,000 people and that the closest games are housed in the biggest stadiums
        and sell the most tickets.
        """
        #getting the data
        query = "select ABS(BASKETBALL.Score1-BASKETBALL.Score2),TicketsSold from BASKETBALL"
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        #transforming data to be usable from tuple of tuples into a list
        score_diff = []
        tickets_sold = []
        for tup in data:
            score_diff.append(tup[0])
            tickets_sold.append(tup[1])

        #plot the data
        fig1,ax = plt.subplots()
        rects2 = ax.scatter(score_diff,tickets_sold)

        ax.set_xlabel('Score Difference')
        ax.set_ylabel('Tickets Sold')
        ax.set_title('Tickets Sold VS Score Difference')
        plt.show()

    def tickets_vs_day(self):
        """
        As you would expect games which are held on the weekends sell amost 3x more tickets on average than games held during the week
        """
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

    def avggrade_vs_row(self):

        query = "select Seated,Grade from PROFESSOR_MOODY"
        self.cursor.execute(query)
        query_result = self.cursor.fetchall()

        #since grades are alphabetical we take it and map to numers with python
        grade_index = ['F','D','C','B','A']
        level_index = ['front','middle','back']
        grades = [[],[],[]]
        for record in query_result:
            level = level_index.index(record[0])
            num_grade = grade_index.index(record[1])
            grades[level].append(num_grade)
        avg_grades = []
        for i in grades:
            avg_grades.append(sum(i)/float(len(i)))

        ind = np.arange(1,4)
        width = 0.5
        fig,ax = plt.subplots()
        rects1 = ax.bar(ind,avg_grades,width,color='b')

        ax.set_xlabel('Row')
        ax.set_ylabel('Average Grade')
        ax.set_title('Average Grade VS Seating Row')
        ax.set_xticks(ind+width*.5)
        ax.set_xticklabels( ('1st Row','2nd Row','3rd Row') )
        plt.show()

    def avggrade_vs_attitude(self):
        """
        Attutudes: nice, eager, argumentative, arrogant
        """
        query = "select Attitude,Grade from PROFESSOR_MOODY"
        self.cursor.execute(query)
        query_result = self.cursor.fetchall()
        grade_index = ['F','D','C','B','A']
        att_index = ['nice','eager','argumentative','arrogant']
        grades = [[],[],[],[]]
        grade_sum = 0
        num_students = [0,0,0,0,209]
        for record in query_result:
            attitude = att_index.index(record[0])
            num_grade = grade_index.index(record[1])
            grades[attitude].append(num_grade)
            num_students[attitude] += 1
            grade_sum += num_grade
        class_avg = grade_sum/209.
        avg_grades = []
        for i in grades:
            avg_grades.append(sum(i)/float(len(i)))
        avg_grades.append(class_avg)

        print("Class average: {}. num_students: {}".format(class_avg,num_students))
        #graph the data
        ind = np.arange(1,6)
        width = 0.3
        fig,ax1 = plt.subplots()
        rects1 = ax1.bar(ind,avg_grades,width,color='purple')

        ax2 = ax1.twinx()
        rects2 = ax2.bar(ind+width,num_students,width,color='green')

        ax1.set_xlabel('Attitude')
        ax1.set_ylabel('Average Grade')
        ax1.set_title('Average Grade VS Attitude')
        ax1.set_xticks(ind+width)
        ax1.set_xticklabels( ['nice','eager','argumentative','arrogant','class'] )
        ax2.set_ylabel('Number of Students in Catgeory')

        ax1.legend( (rects1[0], rects2[0]), ('Grade','Num Students'))
        plt.show()
class WINEJUNE9(object):
    """
    columns:
        FIXED_ACIDITY -- VOLATILE_ACIDITY -- RESIDUAL_SUGAR -- FREE_SULFUR_DIOXIDE
        -- TOTAL_SULFUR_DIOXIDE -- ALCOHOL -- QUALITY -- COUNTRY -- PRICE_A -- RATE
        -- YEAR -- PH
    """
    def __init__(self,cursor):
        self.cursor = cursor



#a = BASKETBALL(cursor)
#a.tickets_vs_day()
#a.scorediff_vs_tickets()

b = PROFESSOR_MOODY(cursor)
b.avggrade_vs_attitude()
