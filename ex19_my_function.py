# ex19_my_function.py

## this function will determine how many flex box hours you have left in the day, week, month
# define the total number of flex boxes each person claims to have available per week
# define the total hours per flex box that the person wants to use
# 

#### there is an error in this formula because I used %r instead of %d, which is used for integers(?) 
def count_boxes(today_rem, weekly_rem, month_rem):
	print "You have %r number of boxes left to choose from TODAY." % (today_rem)
	print "You have %r number of boxes left to choose from THIS WEEK." % (weekly_rem)
	print "You have %r number of boxes left to choose from THIS MONTH." % (month_rem)

#prompt1 = ("Waiting... Press ENTER to continue")
	
hours_in_day = raw_input("How many hours do you have per day for flex boxes? ")
hours_in_week = (int(hours_in_day) * 7)
hours_in_month = (int(hours_in_day) * 30)

print "Great, that's %r hours PER WEEK, and %r hours PER MONTH that you can spend on flex boxes." % (hours_in_week, hours_in_month)

hrs_per_box = raw_input("How many hours per box? ")	
 	
raw_input("When you are ready to enter your first box, press ENTER, to quit press CRTL-C")

task1 = raw_input("How many flex boxes did you spend on your first task? ")
	 
task2 = raw_input("How many flex boxes did you spend on your second task? ")

task3 = raw_input("How many flex boxes did you spend on your third task? ")

count_boxes(int(hours_in_day) - int(task1) - int(task2) - int(task3), int(hours_in_week) - int(task1) - int(task2) - int(task3), int(hours_in_month) - int(task1) - int(task2) - int(task3))
