# Project Week 2 
# You are Hercules, the greatest of the Greek Heroes! You have been tasked by King Eurystheus to 
# slay the vicious Nemean Lion, 
# defeat the impossible nine-headed Lernaean Hydra, 
# and capture the guard dog of the underworld—Cerberus.



print("I am  Hercules, the greatest of the Greek Heroes! I have been tasked by King Eurystheus to slay ...the vicious Nemean Lion, defeat the impossible nine-headed Lernaean Hydra, and capture the guard dog of the underworld—Cerberus.")


def Attack(Hercules_health, enemy_health) :
    if Hercules_health or  enemy_health == False :  
        outcome = print(" Hercules's or Enemy's health reached zero : fight is over ")
    else:
        outcome = print(" Hercules's or Enemy's health is Ok : fighting continues ")
    return outcome


print("Enter Hercules's health level  1 (strong) or 0 (weak) : ")

Hercules_health = int(input())

print("Enter Enemy's health level  1 (strong) or 0 (weak) : ")
Enemy_health = int(input())

Attack_health_result = Attack(Hercules_health, Enemy_health)