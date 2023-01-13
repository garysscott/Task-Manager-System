# A task management system.

# ====sub programs====

# the sub program below enables the user to register a new user to the task_manager.py system.
# it utilises a second sub program called username_check() to ascertain whether a username is unique.

def reg_user():
    name = username_check()
    print(name)
    while True:

        new_pass = input("Please enter the new password: ")
        new_pass2 = input("Please re- enter the new password for confirmation: ")

        if new_pass == new_pass2:
            print("\nPasswords match - your details will be added to the database")

            file = open("user.txt", "a")
            file.write(f"\n{name}, {new_pass}, ")
            file.close()

            print("\n")
            break

        else:
            print("Your password entries do not match - Please try again")


# This procedure ascertains whether the username entered is unique when registering a new user.
def username_check():
    file = open("user.txt", "r")
    lines = file.readlines()
    file.close()

    users = []

    for line in lines:
        temp = line.strip()
        temp = temp.split(",")
        users.append(temp[0])

    while True:
        new_user = input("Please enter the new user name: ")

        if new_user in users:
            print(f"\nIm sorry but the username: {new_user} has already been taken.  Please try again\n")

        else:
            print("User name is unique and not currently in the system\n")
            break

    return(new_user)


# the add_task subprogram allows the user to add a new task
def add_task():
    user = input("Please enter the user that the task will be assigned to: ")
    title = input("Please enter a title for the job: ")
    description = input("Please enter a description for the job: ")
    print("You now need to enter the due date for the task")

    # the code below has been structured to take the day, month and year entries (with some validation) and then
    # combine them all together as a new variable called due_date in the specified format

    day1 = int(input("Enter the day the task is due (ie: 13): "))

    while True:  # to ensure the month is added in the correct format
        month1 = input("Please enter the month the task is due (in three letter format, e.g. Nov): ").capitalize()

        if len(month1) != 3:
            print("The system only accepts the date in three letter format.  Please try again")

        else:
            break

    while True:  # to make sure a 4 digit year is entered
        year1 = input("Please enter the year the task is due (in four digit format, e.g. 2022: ")

        if len(year1) != 4:
            print("The system only accepts the year in four letter format.  Please try again")

        else:
            break

    due_date = str(day1) + " " + month1 + " " + year1 + " "  # the due date is now in the correct format

    # the code below has been structured to take the day, month and year entries (with some validation) and then
    # combine them all together as a new variable called cur_date in the specified format
    # this section works the same as the previous one, so I don't think it needs comments

    print("You now need to enter the current (today's) date")

    day2 = int(input("Enter the day of the month it is (ie: 13): "))

    while True:
        month2 = input("Please enter the current month (in three letter format, e.g. Nov): ").capitalize()

        if len(month2) != 3:
            print("The system only accepts the date in three letter format.  Please try again")

        else:
            break

    while True:
        year2 = input("Please enter the current year (in four digit format, e.g. 2022: ")

        if len(year2) != 4:
            print("The system only accepts the year in four letter format.  Please try again")

        else:
            break

    cur_date = str(day2) + " " + month2 + " " + year2 + " "  # the current date is now in the correct format

    while True:  # this section is for whether the task is complete or not and ensure only 'Yes' or 'No' is added

        complete = input("Is the task complete - enter 'yes' or 'no': ").capitalize()

        if complete == "Yes" or complete == "No":
            break

        else:
            print("You are only able to enter 'yes' or 'no'.  Please try again")

    file = open("tasks.txt", "a")

    # the code below appends the data collected to the tet file in the format specified in the task
    file.write("\n" + user + ", " + title + ", " + description + ", " + due_date + ", " + cur_date + ", " + complete)
    file.close()

    print("\n")


# This sub-program is to allow the user to view all the current jobs in the task_manager.py system
def view_all():
    file = open("tasks.txt", "r")
    lines = file.readlines()
    file.close()  #

    print("TASK LIST #########################################################################################")

    for line in lines:
        temp = line.strip()
        temp = temp.split(", ")
        print(f"Task:\t\t\t {temp[1]}")
        print(f"Username:\t\t {temp[0]}")
        print(f"Date Assigned:\t {temp[3]}")
        print(f"Date Due:\t\t {temp[4]}")
        print(f"Completed:\t\t {temp[5]}")
        print(f"Description:\n {temp[2]}")

        print("___________________________________________________________________________________________________")

    print("\n")


# this sub-program allows the user to check a certain users tasks
def view_mine():
    user_check = input("Please enter the username whose tasks you would like to identify: ")

    file = open("tasks.txt", "r")
    lines = file.readlines()
    file.close()

    counter = 1
    for line in lines:
        temp = line.strip()
        temp = temp.split(", ")
        job_list.append(temp)
        counter += 1

        if temp[0] == user_check:
            print(f"Task Number: {counter - 1}")
            print(f"Task:\t\t\t {temp[1]}")
            print(f"Username:\t\t {temp[0]}")
            print(f"Date Assigned:\t {temp[3]}")
            print(f"Date Due:\t\t {temp[4]}")
            print(f"Completed:\t\t {temp[5]}")
            print(f"Description:\n {temp[2]}")
            print("___________________________________________________________________________________________________")

    print("\n")

    while True:
        choice = int(input('''Choose:
    1 - Edit a task
    2 - Mark a task as complete
    3 - Continue without editing / marking as complete

    Enter a choice: '''))

        if choice == 1:
            edit_task()

        elif choice == 2:
            task_complete()

        elif choice == 3:
            break

        else:
            print("You can only select 1, 2 or 3.  Try again")


# This sub-program is linked to the view_mine() subprogram and allows the user to edit a task
def edit_task():
    while True:
        task_no = int(input("\nWhich task number would you like to edit?: "))

        if task_no in job_list[task_no - 1]:
            decide = int(input('''\nDo you wish to edit:

            1 - Task Description
            2 - User Assigned
            3 - Due Date
            4 - Description
            5 - Go to Menu

            Enter a choice: '''))

            if decide == 1:
                edit_desc()

            elif decide == 2:
                edit_assign()

            elif decide == 3:
                edit_due_date()

            if decide == 4:
                edit_long_desc()

            elif decide == 5:                #
                break

        else:
            print(f"The user {user_check} does not have a task {task_no}")


# this sub program allows the user to edit the job description:
def edit_desc():
    file = open("tasks.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        temp = line.strip()
        temp = temp.split(", ")
        job_list.append(temp)

    desc = input("\nPlease enter the new task description: ")
    job_list[task_no][1] = desc
    print("\nThe task description has now been changed")

    file = open("tasks.txt", "w")
    for x in range(len(job_list)):
        tempa = job_list[x][0]
        tempb = job_list[x][1]
        tempc = job_list[x][2]
        tempd = job_list[x][3]
        tempe = job_list[x][4]
        tempf = job_list[x][5]
        file.write(tempa + ", " + tempb + ", " + tempc + ", " + tempd + ", " + tempe + ", " + tempf + "\n")

    file.close()

    print("\n")


# this sub program allows the user assigned to a task to be edited
def edit_assign():
    file = open("tasks.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        temp = line.strip()
        temp = temp.split(", ")
        job_list.append(temp)

    user_ass = input("\nPlease enter the new user for the task to be assigned to: ")
    job_list[task_no][0] = user_ass
    print("\nThe assigned user has now been changed")

    file = open("tasks.txt", "w")

    for x in range(len(job_list)):
        tempa = job_list[x][0]
        tempb = job_list[x][1]
        tempc = job_list[x][2]
        tempd = job_list[x][3]
        tempe = job_list[x][4]
        tempf = job_list[x][5]
        file.write(tempa + ", " + tempb + ", " + tempc + ", " + tempd + ", " + tempe + ", " + tempf + "\n")

    file.close()


# this sub program allows the user to edit the due date
def edit_due_date():
    file = open("tasks.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        temp = line.strip()
        temp = temp.split(", ")
        job_list.append(temp)

    # the code below has been structured to take the day, month and year entries (with some validation) and then
    # combine them all together as a new variable called due_date in the specified format
    # this section works exactly the same as the commented code in the add_task() sub program so I won't add comments

    day1 = int(input("Enter the day the task is due (ie: 13): "))

    while True:
        month1 = input("Please enter the new month the task is due (in three letter format, e.g. Nov): ").capitalize()

        if len(month1) != 3:
            print("The system only accepts the date in three letter format.  Please try again")

        else:
            break

    while True:
        year1 = input("Please enter the new year the task is due (in four digit format, e.g. 2022: ")

        if len(year1) != 4:
            print("The system only accepts the year in four letter format.  Please try again")

        else:
            break

    new_due_date = str(day1) + " " + month1 + " " + year1 + " "
    job_list[task_no][4] = new_due_date
    print("\nThe due date has now been changed")

    file = open("tasks.txt", "w")

    for x in range(len(job_list)):
        tempa = job_list[x][0]
        tempb = job_list[x][1]
        tempc = job_list[x][2]
        tempd = job_list[x][3]
        tempe = job_list[x][4]
        tempf = job_list[x][5]
        file.write(tempa + ", " + tempb + ", " + tempc + ", " + tempd + ", " + tempe + ", " + tempf + "\n")

    file.close()

    print("\n")


# this sub program allows the user to edit the long job description
def edit_long_desc():
    file = open("tasks.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        temp = line.strip()
        temp = temp.split(", ")
        job_list.append(temp)

    long_desc = input("\nPlease enter the new full task description: ")
    job_list[task_no][2] = long_desc
    print("\nThe task description has now been changed")

    file = open("tasks.txt", "w")

    for x in range(len(job_list)):
        tempa = job_list[x][0]
        tempb = job_list[x][1]
        tempc = job_list[x][2]
        tempd = job_list[x][3]
        tempe = job_list[x][4]
        tempf = job_list[x][5]

        file.write(tempa + ", " + tempb + ", " + tempc + ", " + tempd + ", " + tempe + ", " + tempf + "\n")

    file.close()

    print("\n")


# this sub program allows the user to edit whether the task is complete or not
def task_complete():
    file = open("tasks.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        temp = line.strip()
        temp = temp.split(", ")
        job_list.append(temp)

    complete = int(input("\nPlease enter the task which you want to mark as complete: "))

    if job_list[complete][5] == "No":
        job_list[complete][5] = "Yes"
        print("\nThe task is now marked as complete")

        file = open("tasks.txt", "w")

        for x in range(len(job_list)):
            tempa = job_list[x][0]
            tempb = job_list[x][1]
            tempc = job_list[x][2]
            tempd = job_list[x][3]
            tempe = job_list[x][4]
            tempf = job_list[x][5]
            file.write(tempa + ", " + tempb + ", " + tempc + ", " + tempd + ", " + tempe + ", " + tempf + "\n")

        file.close()

    print("\n")


# this sub program is for the log in system so that only valid users gain entry to the task_manager.py system
def log_in():
    log_on = False
    while log_on == False:
        user_name = input("Please enter your user name: ")
        password = input("Please enter your password: ")

        file = open("user.txt", "r")
        lines = file.readlines()
        file.close()

        list = []

        for line in lines:
            temp = line.strip("\n")
            temp = temp.split(",")
            list.append(temp)

        for x in range(len(list)):
            if list[x][0] == user_name:
                if list[x][1] == " " + password:
                    print(f"\nYour login information has been verified.  Welcome {user_name}\n")
                    log_on = True

        if log_on == False:
            print("\nYour username or password has not been recognised - Please try again\n")


# this sub program generates a task report for the user
def gen_rep():
    file = open("tasks.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        temp = line.strip()
        temp = temp.split(", ")
        job_list.append(temp)

    file = open("task_overview", "w")

    # I have included formatting when writing to the text file to try and produce something that is readable both in
    # the text file itself and in the output that will be printed on screen

    file.write('''
 _______________________________________________________________________
|                                                                       |
|                    T A S K    O V E R V I E W                         |
|                                                                       |
 _______________________________________________________________________
     \n''')

    job_tot = len(job_list)

    file.write(f"The total number of tasks:\t\t\t\t{job_tot}\n")
    file.write(" _______________________________________________________________________\n")
    file.write("Number of complete & incomplete tasks:\n\n")

    comp_tot = 0
    comp_not = 0

    for x in range(len(job_list)):
        if job_list[x][5] == "Yes":
            comp_tot += 1

        elif job_list[x][5] == "No":
            comp_not += 1

    file.write(f"Completed tasks:\t\t\t\t\t\t{comp_tot}\n")
    file.write(f"Incomplete tasks:\t\t\t\t\t\t{comp_not}\n")
    file.write(" _______________________________________________________________________\n")
    file.write("Number of complete & incomplete tasks:\n\n")

    # the perc_calc variables below are used to work out the percentage of complete & incomplete tasks

    perc_calc1 = round((100 / len(job_list) * comp_tot))
    perc_calc2 = round((100 / len(job_list) * comp_not))

    file.write(f"Percentage of complete tasks:\t\t {perc_calc1}%\n")
    file.write(f"Percentage of incomplete tasks:\t\t {perc_calc2}%\n")
    file.write(" _______________________________________________________________________\n")
    file.close()

    print("\nYour report has been generated.  Please open the task_overview.txt file to view or see below:")

    file = open("task_overview.txt", "r")

    lines = file.readlines()
    file.close()

    for line in lines:
        temp = line.strip()
        print(temp)

    print("\n")


# this sub program is used to display user statistics
def disp_stat():
    file = open("user.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        temp = line.strip()
        temp = temp.split(", ")
        user_list.append(temp)

    file = open("tasks.txt", "r")

    lines = file.readlines()
    file.close()

    for line in lines:
        temp = line.strip()
        temp = temp.split(", ")
        job_list.append(temp)

    file = open("user_overview.txt", "w")

    file.write('''
 _______________________________________________________________________
|                                                                       |
|                    U S E R    S T A T I S T I C S                     |
|                                                                       |
 _______________________________________________________________________
 \n''')

    job_tot = len(job_list)

    file.write(f"The total number of tasks: {job_tot}\n")
    file.write(" _______________________________________________________________________\n")
    file.write("Tasks assigned to users:\n\n")

    # the next section of code works out how many jobs each user has.
    # a counter is used to keep check of each users total which is then appended to the user_jobs list for use later

    count = 0
    user_jobs = []

    for x in range(len(user_list)):
        if user_list[x][0] not in user_jobs:
            user_jobs.append(user_list[x][0])

            for y in range(len(job_list)):
                if user_list[x][0] == job_list[y][0]:
                    count += 1

            user_jobs.append(count)
            count = 0


    for x in range(len(user_jobs)):
        file.write(f"{user_jobs[x]}\t\t")
        if x % 2 != 0:
            file.write("\n")

    file.write(" _______________________________________________________________________\n")
    file.write("Percentage of total tasks assigned per user:\n\n")

    counter = 0

    end = len(user_jobs)

    for x in range(0, int(end / 2)):
        user = user_jobs[counter]
        counter += 1
        job_numb = user_jobs[counter]
        calc = (100 / len(job_list)) * job_numb  #

        file.write(f"User: {user}\t\tPercentage of tasks assigned: {round(calc)}%\n")
        counter += 1

    file.write(" _______________________________________________________________________\n")
    file.write("Percentage of completed tasks per user:\n\n")

    # the next section works out the percentage of completed tasks per user
    # it looks to see how many time 'Yes' appears for every job assigned to a specific user
    # the counter is re-set once each user has been checked

    comp_list = []

    for x in range(len(user_list)):
        count = 0
        if user_list[x][0] not in comp_list:
            comp_list.append(user_list[x][0])

            for y in range(len(job_list)):
                if user_list[x][0] == job_list[y][0] and job_list[y][5] == "Yes":
                    count += 1

        comp_list.append(count)  # the number of completed tasks for each user is appended to the list

    completion_list = []

    for x in range(len(user_list)):
        count1 = 0
        count2 = 0

        # checks to see if the user_list[x][0] is NOT already in the completion list

        if user_list[x][0] not in completion_list:
            completion_list.append(user_list[x][0])

            for y in range(len(job_list)):
                if user_list[x][0] == job_list[y][0] and job_list[y][5] == "No":
                    count1 += 1

                if user_list[x][0] == job_list[y][0] and job_list[y][5] == "Yes":
                    count2 += 1

            completion_list.append(count1)
            completion_list.append(count2)


    counter = 0
    counter2 = 0

    end = len(comp_list) + 3  # to allow for a final loop through list (doesn't work properly without the + 3)


    for x in range(0, int(end / 3)):
        user = completion_list[counter]
        counter += 2
        job_numb1 = completion_list[counter]
        counter2 += 2
        job_numb2 = completion_list[counter]

        # this next section checks to see if the number is divisible by 0 to avoid an error
        if job_numb1 > 0:
            calc = (100 / int(job_numb1)) * int(job_numb2)
            file.write(f"User: {user}\t\tPercentage of completed tasks: {round(calc)}%\n")
            counter += 1

        else:
            file.write(f"User: {user}\t\tPercentage of completed tasks: 0%\n")
            counter += 1

    file.write(" _______________________________________________________________________\n")
    file.write("Percentage of incomplete tasks per user:\n\n")

    counter = 0
    counter2 = 1

    for x in range(0, int(end / 3)):
        user = completion_list[counter]
        counter += 2
        job_numb1 = user_jobs[counter2]
        counter2 += 2
        job_numb2 = completion_list[counter]

        if job_numb2 > 0:
            calc = (100 / int(job_numb1)) * int(job_numb2)
            calc2 = 100 - calc
            file.write(f"User: {user}\t\tPercentage of incomplete tasks: {round(calc2)}%\n")
            counter += 1

        else:
            file.write(f"User: {user}\t\tPercentage of incomplete tasks: 100%\n")
            counter +=1

    file.close()

    print("\nYour report has been generated.  Please open the user_overview.txt file to view or see below: ")

    file = open("user_overview.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        temp = line.strip()
        print(temp)

    print("\n")


# ====Login Section====

log_in()

job_list = []

user_list = []

while True:
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'gr':
        gen_rep()

    elif menu == 'ds':
        disp_stat()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
