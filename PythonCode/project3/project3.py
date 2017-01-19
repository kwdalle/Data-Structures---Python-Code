# project3.py
# Kevin Dalle
# kdalle1@stu.parkland.edu
# CSC 220, Spring 2015

from heap_priority_queue import *
from sys import argv


def readinfile(ifilename, queue=HeapPriorityQueue()):
    ifile = open(ifilename, "r")
    for line in ifile:
        temp = line.split(',')
        if temp[1] != "PRIORITY":
            key = int(temp[1])
            del temp[1]
            temp[1] = int(temp[1])  # converts the length to an integer for
            # processing later
            queue.add(key, temp)


def processjobs(jobqueue=HeapPriorityQueue()):
    job = jobqueue.min()
    jobqueue.remove_min()
    job2 = jobqueue.min()
    while len(jobqueue) != 0 or job[1][1] != 0:  # either the queue is empty
        # and the current job is done or it will continue to process
        if job[1][1] <= 0:
            job = jobqueue.min()
            jobqueue.remove_min()
            if len(jobqueue)!=0:
                job2 = jobqueue.min()
        if job[0] == job2[0] and job2[1][1] < job[1][1]:
            job, job2 = job2, job  # swaps the two if they are equal and the
            # second has a shorter time
            jobqueue.remove_min()  # removes the second job from the queue
            jobqueue.add(job2[0], job2[1])  # re-adds the first job back to
            # the queue
        job[1][1] -= 1
        print('Current Job:', job[1][0], "Priority:", job[0], "Time Left: ",
              job[1][1], "\n")
        job = newjob(jobqueue, job)
        jobqueue, job = halt(jobqueue, job)


def newjob(jobqueue=HeapPriorityQueue(), currentjob=tuple()):
    question = input("Would you like to add a new job? Y/N\n")
    if question == 'y' or question == 'Y':
        name = input("What is the name of the new job?\n")
        priority = input("What is the priority of the new job?\n")
        length = input("What is the length of the new job?\n")
        data = [name, int(length)]
        newjob = (int(priority), data)
        if currentjob[0] == newjob[0] and newjob[1][1] < currentjob[1][1]:
            jobqueue.add(currentjob[0], currentjob[1])
            return newjob
        elif currentjob[0] > newjob[0]:
            job1, job2 = newjob, currentjob
            jobqueue.add(job2[0], job2[1])
            return job1
        else:
            jobqueue.add(int(priority), data)
            return currentjob
    else:
        return currentjob


def halt(jobqueu=HeapPriorityQueue(), currentjob=tuple()):
    question = input("Would you like to halt the current job? Y/N \n")
    cjob = currentjob
    if question == "Y" or question == "y":
        joblist = HeapPriorityQueue()
        print("Job:", currentjob[1][0], "Priority:", currentjob[0],
              "Time Remaining:", currentjob[1][1], "\n")
        joblist.add(currentjob[0], currentjob[1])
        while len(jobqueu) != 0:
            currentjob = jobqueu.min()
            jobqueu.remove_min()
            joblist.add(currentjob[0], currentjob[1])
            print("Job:", currentjob[1][0], "Priority:",
                  currentjob[0],
                  "Time Remaining:", currentjob[1][1], "\n")
        question = input("Would you like to reassign a priority to a job? "
                         "Y/N\n")
        if question == 'Y' or question == 'y':
                question2 = input("What is the name of the job?\n")
                newpriority = int(input("What is the new priority?\n"))
                jobqueu, cjob = reassign(jobqueu, joblist, cjob, currentjob,
                                 newpriority,
                         question2)
        else:
            while len(joblist) != 0:
                currentjob = joblist.min()
                if currentjob[1][0] != cjob[1][0]:
                    jobqueu.add(currentjob[0], currentjob[1])
                joblist.remove_min()
    return jobqueue, cjob

def comparisons(jobqueu=HeapPriorityQueue(), joblist=HeapPriorityQueue(),
                cjob=tuple(), currentjob=tuple(), newpriority=int()):
    if cjob[0] == newpriority and currentjob[1][1] < cjob[1][1]:
        jobqueu.add(cjob[0], cjob[1])
        cjob = (newpriority, [currentjob[1][0], currentjob[
                1][1]])
        joblist.remove_min()
    elif cjob[0] > newpriority:
        joblist.remove_min()
        jobqueu.add(cjob[0], cjob[1])
        cjob = (newpriority, [currentjob[1][0], currentjob[
                1][1]])
    elif currentjob[0] < newpriority and currentjob[1][0] == cjob[1][0]:
        jobqueu.add(newpriority, currentjob[1])
        joblist.remove_min()
        cjob = joblist.min()
    else:
        jobqueu.add(newpriority, [currentjob[1][0],currentjob[1][1]])
        joblist.remove_min()
    return jobqueu, cjob

def reassign(jobqueu=HeapPriorityQueue(), joblist=HeapPriorityQueue(),
             cjob=tuple(), currentjob=tuple(), newpriority=int(),
             question2=str()):
    while len(joblist) != 0:
        currentjob = joblist.min()
        if currentjob[1][0] == question2:
            jobqueu, cjob = comparisons(jobqueu,joblist,cjob,currentjob,
                                        newpriority)
        elif currentjob[1][0] != cjob[1][0]:
            jobqueu.add(currentjob[0], currentjob[1])
            joblist.remove_min()
        else:
            joblist.remove_min()
    return jobqueu, cjob


if __name__ == "__main__":
    ifilename = argv[1]
    jobqueue = HeapPriorityQueue()
    readinfile(ifilename, jobqueue)
    processjobs(jobqueue)
