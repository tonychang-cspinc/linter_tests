def find_most(arr: list, top_num: int):
    '''
    Returns to top_num elements in an array

        Parameters:
            arr (list) : a list of integers
            top_num (int) : an integer

        Returns:
            z (list) : a list of most elements in list arr
    '''
    ht = {k:arr.count(k) for k in set(arr)}
    z = []
    z.append(max(ht))
    for i in range(top_num):
        ht.pop(z[0], None)
        z.append(max(ht))
    return z

if __name__ == "__main__":
    arr = ['a', 'b', 'c', 'd', 'e', 'e', 'a']
    k = 2
    most = find_most(arr, k)
    print(most)

