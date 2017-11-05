# Multi-Resource Deadlock Detection Algorithm::

from operator import add # import 'add' from 'operator' module to add elements of two lists
def main():
    num_Processes = input("Number of processes: ") # input number of processes

    Existing_Vector = raw_input("Existing Vector = ") # input elements of 'Existing Vector' of resources
    Existing_Vector = map(int, Existing_Vector.split(" ")) # splitting elements

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

    Available_Vector = [] # initializing 'Available Vector'
    sum = available = 0 # initializing 'sum' with value 0
    # Calculating Available Resources::
    for i in range(0, len(Existing_Vector)):
        for j in range(0, num_Processes):
            sum += Current_Alocation_Matrix[j][i] # Summing up total allocated instances of each resource
        available = Existing_Vector[i] - sum
        Available_Vector.append(available) # Adding available instances of each resource to 'Available Vector'
        sum = 0 # reassigning 0 to variable 'sum'
        available = 0
    print "Available_Vector = ",Available_Vector

    isGreater = 0
    for i in range(0, num_Processes):
        msg = "Request Matrix for process ",i
        Resource_list = raw_input(msg) # input requested resource list by process i
        Resource_list = map(int, Resource_list.split(" "))
        Request_Matrix.append(Resource_list) # appned requested resource list by process i in 'Resource Request Matrix'

    for i in range(0, num_Processes):
        isGreater = 0
        if(Process_Marked[i] == 1): # if i-th process is marked...
            continue # do nothing else and continue for next process
        else:
            for j in range(0,len(Request_Matrix[i])):
                if(Request_Matrix[i][j] > Available_Vector[j]):
                    isGreater = 1
                    break
            if(isGreater == 0): # if requested resources by process i <= available resources...
                Available_Vector = map(add, Available_Vector, Current_Alocation_Matrix[i]) # add currently allocated resouces for process i to available resources
                Process_Marked[i] = 1 # mark process i
    print "Deadlock status:"
    for i in range(0, num_Processes):
        if(Process_Marked.count(0) < 2): # if number of unmarked process is less than 2...
            print "No deadlock detected!" # then there is no deadlock, and so...
            break # break searching
        elif(Process_Marked[i] == 0): # if there exis atleast 2 unmarked processes, then they are in deadlock. So...
            print "Process ",i # print the deadlocked processes.

if __name__ == '__main__':
    main()
