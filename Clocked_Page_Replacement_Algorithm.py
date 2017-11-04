#Clocked Page Replacement Algorithm::

def main():
    pages = raw_input("Processes: ")
    page_list = map(int, pages.split(" "))
    #print "Required process list=",page_list

    no_frames = input("No. of frames: ")
    index = page_hit = hit_count = page_fault = temp = isEmpty = 0

    frame_list = [""]
    frame_R_list = [""]

    for i in range(1, no_frames):
        frame_list.append("")
    for i in range(1, no_frames):
        frame_R_list.append("")

    for i in range(0, len(page_list)):
        for j in range(0,len(frame_list)):

            if(frame_list[j] == page_list[i]):
                #print "Page hit for process ", page_list[i]
                page_hit = 1
                hit_count += 1
                print frame_list,"\n"
                break

            elif(frame_list[j] == ""):
                frame_list[j] = page_list[i]
                #print "Process ",page_list[i],"is placed on frame position ",j
                page_fault += 1
                isEmpty = 1
                print frame_list,"\n"
                break

        if(page_hit == 1):
            page_hit = 0
            continue
        elif(isEmpty == 1):
            isEmpty = 0
            continue

        #print "Reference-bits for", frame_list, " = "
        R_bits = raw_input() #input reference bits for each corresponding process
        frame_R_list = map(int, R_bits.split(" ")) #splitting list
        #print "Current reference-bits for frame processes =",frame_R_list

        index = 0 #ensuring the search starts from a fixed frame position
        for j in range(0, len(frame_list)+1):
            if(index > len(frame_list)-1): #ensuring circular move through frame list
                index = 0

            if(frame_R_list[index] == 0):
                frame_list[index] = page_list[i]
                print frame_list,"\n"
                page_fault += 1
                index += 1
                break
            elif(frame_R_list[index] == 1):
                frame_R_list[index] = 0
                #print "Reference bit for existing process ",frame_list[j]," is converted to 0. Updated reference list=",frame_R_list,". Moving to next frame position..."
                index += 1
                print frame_list,"\n"

            if(j == len(frame_list)-1):
                j = 0

    print "page_fault=",page_fault#,"; hit_count=",hit_count

if __name__ == '__main__':
    main()
