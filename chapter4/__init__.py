for pic_id1 in range(1, 1000):
    search_list = range(max((pic_id1 - 10), 1), pic_id1) + \
                  range(pic_id1 + 1, min((pic_id1 + 16), 1000 + 1))
    # print(pic_id1, search_list)
import numpy as np
print(np.arange(9))