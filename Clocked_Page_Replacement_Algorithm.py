#Clocked Page Replacement Algorithm::
def main():
    pages = raw_input("Pages: ")
    page_list = map(int, pages.split(" "))

    R_bits = raw_input("Reference-bits: ")
    R_bit_list = map(int, R_bits.split(" "))

    print "Pages: ",page_list
    print "Reference bit:",R_bit_list

    no_frames = input("No. of frames: ")
    index = page_hit = hit_count = page_fault = temp = isEmpty = lowest_weight = lowest_weight_pointer = 0

    frame_list = [""]
    frame_R_list = [""]

    for i in range(1, no_frames):
        frame_list.append("")
    for i in range(1, no_frames):
        frame_R_list.append("")

    for i in range(0, len(page_list)):
        for j in range(0,len(frame_list)):

            if(frame_list[j] == page_list[i]):
                frame_R_list[j] = 1
                page_hit = 1
                hit_count += 1
                print "block 1: frame_list=",frame_list,"; frame_R_list",frame_R_list
                break

            elif(frame_list[j] == ""):
                frame_list[j] = page_list[i]
                frame_R_list[j] = R_bit_list[i]
                page_fault += 1
                isEmpty = 1
                print "block 2: frame_list=",frame_list,"; frame_R_list",frame_R_list
                break

        if(page_hit == 1):
            page_hit = 0
            continue
        elif(isEmpty == 1):
            isEmpty = 0
            continue

        for j in range(0, len(frame_list)):
            if(index > len(frame_list)-1):
                index = 0
            if(frame_R_list[index] == 0):
                frame_list[index] = page_list[i]
                frame_R_list[index] = R_bit_list[i]
                print "block 3: frame_list=",frame_list,"; frame_R_list",frame_R_list
                page_fault += 1
                index += 1
                break
            elif(frame_R_list[index] == 1):
                frame_R_list[index] = 0
                index += 1
                print "block 4: frame_list=",frame_list,"; frame_R_list",frame_R_list

    print "page_fault=",page_fault,"; hit_count=",hit_count

if __name__ == '__main__':
    main()
