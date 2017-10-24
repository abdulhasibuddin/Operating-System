#Not-Recently-Used Page Replacement Algorithm::

def main():
    pages = raw_input("Pages: ")
    page_list = map(int, pages.split(" "))

    R_bits = raw_input("Reference-bits: ")
    R_bit_list = map(int, R_bits.split(" "))

    M_bits = raw_input("Modification-bits: ")
    M_bit_list = map(int, M_bits.split(" "))

    print "Reference bit:",R_bit_list
    print "Modification bits:",M_bit_list

    no_frames = input("No. of frames: ")
    index = page_hit = hit_count = page_fault = temp = isEmpty = lowest_weight = lowest_weight_pointer = 0

    frame_list = [""]
    weight_list = [""]

    for i in range(1, no_frames):
        frame_list.append("")
    for i in range(1, no_frames):
        weight_list.append("")

    for i in range(0, len(page_list)):
        for j in range(0,len(frame_list)):

            if(frame_list[j] == page_list[i]):
                page_hit = 1
                hit_count += 1
                print "frame_list=",frame_list,"; weight-level=",weight_list
                break

            elif(frame_list[j] == ""):
                frame_list[j] = page_list[i]
                weight_list[j] = R_bit_list[i]*10 + M_bit_list[i]
                page_fault += 1
                isEmpty = 1
                print "frame_list=",frame_list,"; weight-level=",weight_list
                break

        if(page_hit == 1):
            page_hit = 0
            continue
        elif(isEmpty == 1):
            isEmpty = 0
            continue

        lowest_weight = weight_list[0]
        for j in range(0, len(frame_list)):

            if(weight_list[j]<lowest_weight):
                lowest_weight = weight_list[j]
                lowest_weight_pointer = j

        frame_list[lowest_weight_pointer] = page_list[i]
        weight_list[lowest_weight_pointer] = R_bit_list[i]*10 + M_bit_list[i]
        page_fault += 1
        print "frame_list=",frame_list,"; weight-level=",weight_list

    print "page_fault=",page_fault,"; hit_count=",hit_count

if __name__ == '__main__':
    main()
