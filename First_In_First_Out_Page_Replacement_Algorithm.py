#First-In-First-Out Page Replacement Algorithm::

def main():
    page_frames = input("No. of page frames: ")
    pages_required = raw_input("Pages required: ")
    pages_required_list = map(int, pages_required.split(" "))

    page_fault = page_hit = hit_count = 0
    page_replacement_point = 0
    page_frame_list = [page_frames]

    for i in range(0, page_frames-1):
        page_frame_list.append("")

    for i in range(0, len(pages_required_list)):

        for j in range(0, len(page_frame_list)):

            if(pages_required_list[i] == page_frame_list[j]):
                page_hit = 1
                hit_count += 1
                break

        if(page_hit == 1):
            page_hit = 0
        else:
            page_frame_list[page_replacement_point] = pages_required_list[i]
            page_fault = page_fault + 1

            if(page_replacement_point == page_frames-1):
                page_replacement_point = 0
            else:
                page_replacement_point = page_replacement_point + 1

        print page_frame_list
    print "Page faults = ", page_fault, "\nPage hit = ", hit_count

if __name__ == '__main__':
    main()
