# Challenge: Cricket Scorecard

# Write a Python program to generate a Cricket Scorecard.

# Store the following information in variables:
# Batsman Name
# Team Name
# Singles
# Doubles
# Triples
# Fours
# Sixes
# Balls Faced
# Calculate:
# Total Runs Scored
# Total Boundary Runs
# Total Non-Boundary Runs
# Strike Rate
# Percentage of Runs Scored Through Boundaries
# Percentage of Runs Scored Through Running Between the Wickets
# Display the output in a professional scorecard format.
# Constraints
# ✅ Use only:
# Variables
# Arithmetic operators (+, -, *, /)
# print()
# ❌ Do not use:
# input()
# if / else
# Loops
# Functions
# String methods
# Lists, tuples, or dictionaries

batsman_name = "Virat Kohli"
team_name = "India"
balls_faced = 52

singles = 18
doubles = 6
triples = 1
fours = 8
sixes = 3

single_runs = singles * 1
double_runs = doubles * 2
triple_runs = triples * 3
four_runs = fours * 4
six_runs = sixes * 6

total_runs = single_runs + double_runs + triple_runs + four_runs + six_runs
boundary_runs = four_runs + six_runs
running_runs = single_runs + double_runs + triple_runs

strike_rate = (total_runs / balls_faced) * 100
boundary_percentage = (boundary_runs / total_runs) * 100
running_percentage = (running_runs / total_runs) * 100

total_boundaries = fours + sixes
scoring_shots = singles + doubles + triples + fours + sixes
average_runs_per_ball = total_runs / balls_faced
average_runs_per_shot = total_runs / scoring_shots

print("========================================")
print("         CRICKET SCORECARD")
print("========================================")
print("Batsman Name      :", batsman_name)
print("Team Name         :", team_name)
print("Balls Faced       :", balls_faced)

print("\n------------- Scoring ------------------")
print("Singles           :", singles)
print("Doubles           :", doubles)
print("Triples           :", triples)
print("Fours             :", fours)
print("Sixes             :", sixes)

print("\n------------ Statistics ----------------")
print("Total Runs        :", total_runs)
print("Boundary Runs     :", boundary_runs)
print("Running Runs      :", running_runs)
print("Strike Rate       :", strike_rate)
print("Boundary %        :", boundary_percentage)
print("Running %         :", running_percentage)
print("Total Boundaries  :", total_boundaries)
print("Runs/Ball         :", average_runs_per_ball)
print("Runs/Shot         :", average_runs_per_shot)

print("========================================")