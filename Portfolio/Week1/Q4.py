# In a long career for Yorkshire, Geoffrey Boycott played 609 matches, 
#batted 1014 times, was not out 162 times, and scored 48426 runs. Write a 
#program to calculate and display Boycott's batting average. 
#Note: A batting average is the number of runs scored divided by the number
#of completed innings (i.e. the total times batted minus the times not out).
def calculate_batting_average(runs, times_batted, not_out):
    completed_innings = times_batted - not_out
    batting_average = runs / completed_innings
    return batting_average

# Geoffrey Boycott's statistics
runs_scored = 48426
times_batted = 1014
not_out = 162

# Calculate and display batting average
batting_average = calculate_batting_average(runs_scored, times_batted, not_out)
print(f"Geoffrey Boycott's batting average: {batting_average:.2f}")