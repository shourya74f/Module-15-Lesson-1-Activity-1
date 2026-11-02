n=4
g=input("Total points: 1+2+3+4= ?")
input("Formula: n(n+1)//2, Press enter to run.")
t=n*(n+1)//2
print("Total: ", t)
input("Loop: 1 step at a time, Press enter to run.")
t=0
for i in range(1,n+1):
    t+=i
print("Step: ", i, "Total: ", t)
input("Double Loop: counts each step, Press enter to run.")
t=0
c=0
for i in range(1,n+1):
    for j in range(1,i+1):
        t+=1
        c+=1
print("Step: ", c, "Total: ", t, "Guess: ", g)