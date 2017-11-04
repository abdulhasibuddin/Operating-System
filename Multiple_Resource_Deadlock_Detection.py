# Multi-Resource Deadlock Detection Algorithm::

from operator import add # import 'add' from 'operator' module to add elements of two lists

def main():
    num_Processes = input("Number of processes: ") # input number of processes

    Existing_Vector = raw_input("Existing Vector = ") # input elements of 'Existing Vector' of resources
    Existing_Vector = map(int, Existing_Vector.split(" ")) # splitting elements

    Available_Vector = raw_input("Available Vector = ") # input elemets of 'Available Vector' of resources
    Available_Vector = map(int, Available_Vector.split(" ")) # splitting elements

    num_Resources =len(Existing_Vector) # getting number of resources
    Current_Alocation_Matrix = [] # initializing list for 'Current Allocation Matrix'
    Request_Matrix = [] # initializing list for 'Resource Request Matrix'
    Process_Marked = [] # this list contains marking status of the processes

    for i in range(0, num_Processes):
        msg = "Current Alocation Matrix for process ",i
        Resource_list = raw_input(msg) # input currently allocated resource list for process i
        Resource_list = map(int, Resource_list.split(" "))
        Current_Alocation_Matrix.append(Resource_list) # appned currently allocated resource list for process i in 'Current Allocation Matrix'
        Process_Marked.append(0) # initially all processes are unmarked

    for i in range(0, num_Processes):
        msg = "Request Matrix for process ",i
        Resource_list = raw_input(msg) # input requested resource list by process i
        Resource_list = map(int, Resource_list.split(" "))
        Request_Matrix.append(Resource_list) # appned requested resource list by process i in 'Resource Request Matrix'

    for i in range(0, num_Processes):
        if(Process_Marked[i] == 1): # if i-th process is marked...
            continue # do nothing else and continue for next process
        elif(Request_Matrix[i] <= Available_Vector): # if requested resources by process i <= available resources...
            Available_Vector = map(add, Available_Vector, Current_Alocation_Matrix[i]) # add currently allocated resouces for process i to available resources
            Process_Marked[i] = 1 # mark process i

    for i in range(0, num_Processes):
        if(Process_Marked.count(0) < 2): # if number of unmarked process is less than 2...
            print "No deadlock detected!" # then there is no deadlock, and so...
            break # break searching
        elif(Process_Marked[i] == 0): # if there exis atleast 2 unmarked processes, then they are in deadlock. So...
            print i," " # print the deadlocked processes.

if __name__ == '__main__':
    main()
