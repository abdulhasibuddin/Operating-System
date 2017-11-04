#Not-Recently-Used Page Replacement Algorithm::

def main():
    pages = raw_input("Processes: ") #input processed that are required
    page_list = map(int, pages.split(" ")) #splitting processes and assigning into a list

    no_frames = input("No. of frames: ") #frame list of size no. of frames
    index = page_hit = hit_count = page_fault = temp = isEmpty = lowest_weight = lowest_weight_pointer = M_bit = R_bit = 0

    frame_list = [""]
    weight_list = [""]

    #Note: weight = reference bit * 10 + modification bit

    #initially appending empty elements into frame list and weight::
    for i in range(1, no_frames):
        frame_list.append("")
    for i in range(1, no_frames):
        weight_list.append("")

    for i in range(0, len(page_list)): #traversing required processes
        for j in range(0,len(frame_list)): #traversing through frame list

            if(frame_list[j] == page_list[i]): #if process already exists into the frame list

                #print "Page hit for process ", page_list[i]
                page_hit = 1 #flag indicating a page hit is set high
                hit_count += 1 #increament hit count by 1
                print frame_list,"\n"
                break #break traversing frame list

            elif(frame_list[j] == ""): #if frame list is empty...

                frame_list[j] = page_list[i] #insert process in the empty position of frame list
                #print "Process ", page_list[i], "is placed on frame position ", j
                page_fault += 1  #increament page fault counting by 1
                isEmpty = 1 #set empty flag high
                print frame_list,"\n"
                break #break traversing frame list

        if(page_hit == 1):
            page_hit = 0
            continue
        elif(isEmpty == 1):
            isEmpty = 0
            continue

        #print "Reference-bits for", frame_list, " = "
        R_bits = raw_input() #input reference bits for each corresponding frame process
        R_bit_list = map(int, R_bits.split(" ")) #splitting list

        #print "Modification-bits for", frame_list, " = "
        M_bits = raw_input() #input modification bits for each corresponding frame process
        M_bit_list = map(int, M_bits.split(" ")) #splitting list

        #print "Current reference-bits for frame processes =",R_bit_list
        #print "Current modification-bits for frame processes =",M_bit_list

        for j in range(0, len(frame_list)):
            weight_list[j] = R_bit_list[j]*10 + M_bit_list[j]
        #print "Current weight list:", weight_list

        lowest_weight = weight_list[0]
        lowest_weight_pointer = 0
        for j in range(0, len(frame_list)):

            if(weight_list[j]<lowest_weight):
                lowest_weight = weight_list[j]
                lowest_weight_pointer = j

        frame_list[lowest_weight_pointer] = page_list[i]
        page_fault += 1
        print frame_list,"\n"

    print "\npage_fault=",page_fault#,"; hit_count=",hit_count

if __name__ == '__main__':
    main()
