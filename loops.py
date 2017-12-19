student_names = ["James", "Katarina", "Jessica", "Mark", "Bort", "Frank Grimes"]

for name in student_names:
    if name == "Mark":
        print("found him")
        break
    print("Currently testing {0}".format(name))