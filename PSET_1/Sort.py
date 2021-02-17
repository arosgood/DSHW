import time
import random

def insertion_sort(arr):
    for k in range(1, len(arr)): #this loop loops through the entire provided array
        cur = arr[k] #we sent current value to the value in the current index of the array
        j = k 
        while j > 0 and arr[j-1] > cur: #if the value in the index before the current index is greater than the value in the current index
            arr[j]= arr[j-1] #then swap the values, and check if the preceding value is also greater than the value in the new currenty index (1 less)
            j = j - 1 #we continue until we hit the first value in the array (index 0)
            arr[j] = cur

def selection_sort(arr):
    for k in range(len(arr)): #need to loop through the entire array which this loop does
        start = arr[k] #find the first value in the array
        smallest = arr[k] #set the variable that finds the smallest value in the sub-array to the first value in the array
        i = k #set the incrementing value for the loop as the outer loop value so that the inner loop loops through only the sub-array
        while(i < len(arr)): #this is the inner loop to loop through whatever the sub-array is
            if(smallest < arr[i]): #if we already have the smallest value continue through the inner loop
                i += 1
            else:
                smallest = arr[i]  #if we don't, set smallest to the value of the new smallest number
                index_of_smallest = i #set the index_of_smallest to the index of where the new smallest number is in the sub-array
                i += 1 #continue the loop
        arr[k] = smallest #once we are done with the inner loop, set our original starting value equal to the smallest value we found 
        arr[index_of_smallest] = start #swap our starting value with the smallest value and continue with the next value in the outer loop if limit has not yet been reached

if __name__ == '__main__':
#####below are my arrays that I create to test sorting and timing
    ins_test_1 = [-22, -14, 4, -10, -86, 8, -96, 11, 57, -76, 48, 94, 36, 9, -37, -80, 97, -82, 71, -56]
    ins_test_2 = [100, 54, 87, 36, 76, -77, 12, -29, -6, 5, 50, 67, -56, 4, 71, -25, 75, 47, -18, 23]
    ins_test_3 = [98, -55, 78, 2, 88, -9, 42, 26, -33, -28, 60, -36, -24, -79, -69, 35, 37, 100, 62, 18]
    ins_test_4 = [31, 82, -23, 50, -50, 60, 2, -27, -16, -90, 73, -18, -88, -30, 44, -82, -91, -64, -76, -6]
    ins_test_5 = [-100, 86, -25, -11, -14, -61, 100, -46, 21, -96, -28, 2, 42, -5, 5, 57, -86, -39, 1, 37]
    sel_test_1 = [6, -26, 10, 61, 95, -10, 32, -28, 54, 91, -96, -14, 93, -40, 39, 80, 62, -3, 31, 28]
    sel_test_2 = [-69, 5, -58, -76, -19, 59, -73, 35, 10, -57, -91, 48, 43, 28, 47, 8, 81, -47, -61, -71]
    sel_test_3 = [19, -77, 42, 62, 45, -99, 46, 75, 7, -89, 85, 3, 88, -86, -8, 44, -72, -64, -11, -7]
    sel_test_4 = [72, 47, 87, 0, -73, -87, -65, -37, -11, -69, 9, -51, -79, 81, -63, 62, -3, 32, 11, -67]
    sel_test_5 = [-51, 26, -91, -70, -28, -68, -37, 86, 85, -75, -65, -53, 45, 90, -59, 12, 47, 77, 67, 2]

    insertion_sort(ins_test_1)
    print(ins_test_1)
    insertion_sort(ins_test_2)
    print(ins_test_2)
    insertion_sort(ins_test_3)
    print(ins_test_3)
    insertion_sort(ins_test_4)
    print(ins_test_4)
    insertion_sort(ins_test_5)
    print(ins_test_5)

    selection_sort(sel_test_1)
    print(sel_test_1)
    selection_sort(sel_test_2)
    print(sel_test_2)
    selection_sort(sel_test_3)
    print(sel_test_3)
    selection_sort(sel_test_4)
    print(sel_test_4)
    selection_sort(sel_test_5)
    print(sel_test_5)

#####increasing arrays - 1000
    ins_incr_1000_arr = []
    sel_incr_1000_arr = []
    for i in range(1000):
        ins_incr_1000_arr += [i]
    sel_incr_1000_arr = list(ins_incr_1000_arr)

    start = time.clock()
    insertion_sort(ins_incr_1000_arr)
    end = time.clock()
    incr_insertion_1000 = '{:.6f}'.format(end-start)
    print('1000 Increasing Insertion: ' + '{:.6f}'.format(end-start))

    start = time.clock()
    selection_sort(sel_incr_1000_arr)
    end = time.clock()
    incr_selection_1000 = '{:.6f}'.format(end-start)
    print('1000 Increasing Selection: ' + '{:.6f}'.format(end-start))

#####increasing arrays - 2500
    ins_incr_2500_arr = []
    sel_incr_2500_arr = []
    for i in range(2500):
        ins_incr_2500_arr += [i]
    sel_incr_2500_arr = list(ins_incr_2500_arr)

    start = time.clock()
    insertion_sort(ins_incr_2500_arr)
    end = time.clock()
    incr_insertion_2500 = '{:.6f}'.format(end-start)
    print('2500 Increasing Insertion: ' + '{:.6f}'.format(end-start))

    start = time.clock()
    selection_sort(sel_incr_2500_arr)
    end = time.clock()
    incr_selection_2500 = '{:.6f}'.format(end-start)
    print('2500 Increasing Selection: ' + '{:.6f}'.format(end-start))

#####increasing arrays - 5000
    ins_incr_5000_arr = []
    sel_incr_5000_arr = []
    for i in range(5000):
        ins_incr_5000_arr += [i]
    sel_incr_5000_arr = list(ins_incr_5000_arr)

    start = time.clock()
    insertion_sort(ins_incr_5000_arr)
    end = time.clock()
    incr_insertion_5000 = '{:.6f}'.format(end-start)
    print('5000 Increasing Insertion: ' + '{:.6f}'.format(end-start))

    start = time.clock()
    selection_sort(sel_incr_5000_arr)
    end = time.clock()
    incr_selection_5000 = '{:.6f}'.format(end-start)
    print('5000 Increasing Selection: ' + '{:.6f}'.format(end-start))

#####increasing arrays - 7500
    ins_incr_7500_arr = []
    sel_incr_7500_arr = []
    for i in range(7500):
        ins_incr_7500_arr += [i]
    sel_incr_7500_arr = list(ins_incr_7500_arr)

    start = time.clock()
    insertion_sort(ins_incr_7500_arr)
    end = time.clock()
    incr_insertion_7500 = '{:.6f}'.format(end-start)
    print('7500 Increasing Insertion: ' + '{:.6f}'.format(end-start))

    start = time.clock()
    selection_sort(sel_incr_7500_arr)
    end = time.clock()
    incr_selection_7500 = '{:.6f}'.format(end-start)
    print('7500 Increasing Selection: ' + '{:.6f}'.format(end-start))

#####increasing arrays - 10000
    ins_incr_10000_arr = []
    sel_incr_10000_arr = []
    for i in range(10000):
        ins_incr_10000_arr += [i]
    sel_incr_10000_arr = list(ins_incr_10000_arr)

    start = time.clock()
    insertion_sort(ins_incr_10000_arr)
    end = time.clock()
    incr_insertion_10000 = '{:.6f}'.format(end-start)
    print('10000 Increasing Insertion: ' + '{:.6f}'.format(end-start))

    start = time.clock()
    selection_sort(sel_incr_10000_arr)
    end = time.clock()
    incr_selection_10000 = '{:.6f}'.format(end-start)
    print('10000 Increasing Selection: ' + '{:.6f}'.format(end-start))

#####decreasing arrays - 1000
    ins_decr_1000_arr = []
    sel_decr_1000_arr = []
    for i in range(999, -1, -1):
        ins_decr_1000_arr += [i]
    sel_decr_1000_arr = list(ins_decr_1000_arr)

    start = time.clock()
    insertion_sort(ins_decr_1000_arr)
    end = time.clock()
    decr_insertion_1000 = '{:.6f}'.format(end-start)
    print('1000 Decreasing Insertion: ' + '{:.6f}'.format(end-start))

    start = time.clock()
    selection_sort(sel_decr_1000_arr)
    end = time.clock()
    decr_selection_1000 = '{:.6f}'.format(end-start)
    print('1000 Decreasing Selection: ' + '{:.6f}'.format(end-start))

#####decreasing arrays - 2500
    ins_decr_2500_arr = []
    sel_decr_2500_arr = []
    for i in range(2499, -1, -1):
        ins_decr_2500_arr += [i]
    sel_decr_2500_arr = list(ins_decr_2500_arr)

    start = time.clock()
    insertion_sort(ins_decr_2500_arr)
    end = time.clock()
    decr_insertion_2500 = '{:.6f}'.format(end-start)
    print('2500 Decreasing Insertion: ' + '{:.6f}'.format(end-start))

    start = time.clock()
    selection_sort(sel_decr_2500_arr)
    end = time.clock()
    decr_selection_2500 = '{:.6f}'.format(end-start)
    print('2500 Decreasing Selection: ' + '{:.6f}'.format(end-start))

#####decreasing arrays - 5000
    ins_decr_5000_arr = []
    sel_decr_5000_arr = []
    for i in range(4999, -1, -1):
        ins_decr_5000_arr += [i]
    sel_decr_5000_arr = list(ins_decr_5000_arr)

    start = time.clock()
    insertion_sort(ins_decr_5000_arr)
    end = time.clock()
    decr_insertion_5000 = '{:.6f}'.format(end-start)
    print('5000 Decreasing Insertion: ' + '{:.6f}'.format(end-start))

    start = time.clock()
    selection_sort(sel_decr_5000_arr)
    end = time.clock()
    decr_selection_5000 = '{:.6f}'.format(end-start)
    print('5000 Decreasing Selection: ' + '{:.6f}'.format(end-start))

#####decreasing arrays - 7500
    ins_decr_7500_arr = []
    sel_decr_7500_arr = []
    for i in range(7499, -1, -1):
        ins_decr_7500_arr += [i]
    sel_decr_7500_arr = list(ins_decr_7500_arr)

    start = time.clock()
    insertion_sort(ins_decr_7500_arr)
    end = time.clock()
    decr_insertion_7500 = '{:.6f}'.format(end-start)
    print('7500 Decreasing Insertion: ' + '{:.6f}'.format(end-start))

    start = time.clock()
    selection_sort(sel_decr_7500_arr)
    end = time.clock()
    decr_selection_7500 = '{:.6f}'.format(end-start)
    print('7500 Decreasing Selection: ' + '{:.6f}'.format(end-start))

#####decreasing arrays - 10000
    ins_decr_10000_arr = []
    sel_decr_10000_arr = []
    for i in range(9999, -1, -1):
        ins_decr_10000_arr += [i]
    sel_decr_10000_arr = list(ins_decr_10000_arr)

    start = time.clock()
    insertion_sort(ins_decr_10000_arr)
    end = time.clock()
    decr_insertion_10000 = '{:.6f}'.format(end-start)
    print('10000 Decreasing Insertion: ' + '{:.6f}'.format(end-start))

    start = time.clock()
    selection_sort(sel_decr_10000_arr)
    end = time.clock()
    decr_selection_10000 = '{:.6f}'.format(end-start)
    print('10000 Decreasing Selection: ' + '{:.6f}'.format(end-start))

#####random arrays - 1000
    ins_random_1000_arr = []
    sel_random_1000_arr = []
    for i in range(0, 1000):
        ins_random_1000_arr += [(random.randint(-1000, 1000))]
    sel_random_1000_arr = list(ins_random_1000_arr)

    start = time.clock()
    insertion_sort(ins_random_1000_arr)
    end = time.clock()
    random_insertion_1000 = '{:.6f}'.format(end-start)
    print('1000 Random Insertion: ' + '{:.6f}'.format(end-start))

    start = time.clock()
    selection_sort(sel_random_1000_arr)
    end = time.clock()
    random_selection_1000 = '{:.6f}'.format(end-start)
    print('1000 Random Selection: ' + '{:.6f}'.format(end-start))

#####random arrays - 2500
    ins_random_2500_arr = []
    sel_random_2500_arr = []
    for i in range(0, 2500):
        ins_random_2500_arr += [(random.randint(-1000, 1000))]      
    sel_random_2500_arr = list(ins_random_2500_arr)

    start = time.clock()
    insertion_sort(ins_random_2500_arr)
    end = time.clock()
    random_insertion_2500 = '{:.6f}'.format(end-start)
    print('2500 Random Insertion: ' + '{:.6f}'.format(end-start))

    start = time.clock()
    selection_sort(sel_random_2500_arr)
    end = time.clock()
    random_selection_2500 = '{:.6f}'.format(end-start)
    print('2500 Random Selection: ' + '{:.6f}'.format(end-start))

#####random arrays - 5000
    ins_random_5000_arr = []
    sel_random_5000_arr = []
    for i in range(0, 5000):
        ins_random_5000_arr += [(random.randint(-1000, 1000))]
    sel_random_5000_arr = list(ins_random_5000_arr)

    start = time.clock()
    insertion_sort(ins_random_5000_arr)
    end = time.clock()
    random_insertion_5000 = '{:.6f}'.format(end-start)
    print('5000 Random Insertion: ' + '{:.6f}'.format(end-start))

    start = time.clock()
    selection_sort(sel_random_5000_arr)
    end = time.clock()
    random_selection_5000 = '{:.6f}'.format(end-start)
    print('5000 Random Selection: ' + '{:.6f}'.format(end-start))

#####random arrays - 7500
    ins_random_7500_arr = []
    sel_random_7500_arr = []
    for i in range(0, 7500):
        ins_random_7500_arr += [(random.randint(-1000, 1000))]
    sel_random_7500_arr = list(ins_random_7500_arr)

    start = time.clock()
    insertion_sort(ins_random_7500_arr)
    end = time.clock()
    random_insertion_7500 = '{:.6f}'.format(end-start)
    print('7500 Random Insertion: ' + '{:.6f}'.format(end-start))

    start = time.clock()
    selection_sort(sel_random_7500_arr)
    end = time.clock()
    random_selection_7500 = '{:.6f}'.format(end-start)
    print('7500 Random Selection: ' + '{:.6f}'.format(end-start))

#####random arrays - 10000
    ins_random_10000_arr = []
    sel_random_10000_arr = []
    for i in range(0, 10000):
        ins_random_10000_arr += [(random.randint(-1000, 1000))]
    sel_random_10000_arr = list(ins_random_10000_arr)

    start = time.clock()
    insertion_sort(ins_random_10000_arr)
    end = time.clock()
    random_insertion_10000 = '{:.6f}'.format(end-start)
    print('10000 Random Insertion: ' + '{:.6f}'.format(end-start))

    start = time.clock()
    selection_sort(sel_random_10000_arr)
    end = time.clock()
    random_selection_10000 = '{:.6f}'.format(end-start)
    print('10000 Random Selection: ' + '{:.6f}'.format(end-start))





