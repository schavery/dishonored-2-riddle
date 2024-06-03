# Solving the Dishonored 2 riddle

My first thought was to try to create the constraint functions and test all possible combinations
in the solution space.

However, my computer choked to produce the initial list. It's too big. 

Then I attempted to use the OR Tools package so the constraints would be applied to 
the solution space before the solutions are generated.

It was easy until trying to apply the constraints that state things about neighbors.
Eg, the lady wearing green sat next to someone wearing purple.

There's got to be some improved error handling in OR Tools, because when you write bad
constraints, you completely crash python. I've never seen a library do that before.

After a few rounds attempting to format the neighbor rules, I realized that without the 
neighbor rules there were only 2016 solutions being generated. An easy search space.

So, I reused the constraint functions from earlier, and ran the list through these, and then
there were 4 solutions left.

The first one in the list opened the door. Success.

The final code is in solver.py. It should produce the output when run directly with `poetry run python solver.py`

You'll need to install OR Tools with `poetry run pip install requirements.txt`

