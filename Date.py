'''
Created on 4/25/2022
@author:   JIanfei Li
Pledge:    I pledge that I have done the homework by myself
CS515 - Hw 12 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
        self.day == d2.day
        
    def tomorrow(self):
        """changes the calling object so that it represents one calendar day after the date it originally represented. """
        if self.day < DAYS_IN_MONTH[self.month]:
            self.day += 1
        elif self.isLeapYear() and self.day < 29 and self.month == 2:
            self.day += 1
        elif self.month < 12:
            self.day = 1
            self.month += 1
        else:
            self.day = 1
            self.month = 1
            self.year += 1
            
    def yesterday(self):
        """changes the calling object so that it represents one calendar day before the date it originally represented. """
        if self.day > 1:
            self.day -= 1
        else:
            if self.isLeapYear() and self.day == 1 and self.month == 3:
                self.day = 29
                self.month = 2
            elif self.month == 1 and self.day == 1:
                self.day = DAYS_IN_MONTH[12]
                self.month = 12
                self.year -= 1
            else:
                self.day = DAYS_IN_MONTH[self.month - 1]
                self.month -= 1
    
    def addNDays(self, N):
        """changes the calling object so that it represents N calendar days after the date it originally represented."""
        for i in range(N):
            print(self)
            self.tomorrow()
        print(self)
    
    def subNDays(self, N):
        """changes the calling object so that it represents N calendar days before the date it originally represented."""
        for i in range(N):
            print(self)
            self.yesterday()
        print(self)
        
    def isBefore(self, d2):
        """This method should return True if the calling object is a calendar date before the input named d2 
        (which will always be an object of type Date). If self and d2 represent the same day, 
        this method should return False. Similarly, if self is after d2, this should return False"""
        if self.year == d2.year and self.month == d2.month:
            if self.day < d2.day:
                return True
        if self.year < d2.year:
            return True
        elif self.year == d2.year and self.month < d2.month:
            return True
        return False
    
    def isAfter(self, d2):
        """This method should return True if the calling object is a calendar date after the input named d2 
        (which will always be an object of type Date). If self and d2 represent the same day, 
        this method should return False. Similarly, if self is before d2, this should return False"""
        if self.equals(d2):
            return False
        else:
            return not self.isBefore(d2)
    
    def diff(self,d2):
        """This method should return an integer representing the number of days between self and d2. """
        count = 0
        day1 = self.copy()
        day2 = d2.copy()
        if day2.isBefore(day1):
            while day2.isBefore(day1):
                day2.tomorrow()
                count += 1
        if day1.isBefore(day2):
            while day2.isAfter(day1):
                day1.tomorrow()
                count -= 1
        return count
    
    def dow(self):
        """This method should return a string that indicates the day of the week"""
        DOW = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']
        d2 = Date(11,9,2011)
        return DOW[self.diff(d2) % 7]
