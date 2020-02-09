from functions import organize, re_format
from vars import my_destination

m, i, d = organize(my_folder_list, my_target, my_destination, my_ignore)
print_data(m, i, d)

# re_format(my_destination, 3)
