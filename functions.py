import os
import shutil
import pathlib


HOME = pathlib.Path.home()


def goto(given_folder):
    os.chdir(given_folder)


def files():
    return os.listdir()


def file_type(file_name):
    given_file = file_name.lower().split(".")
    if file_name[0] == ".":
        type_ = "hidden"
    elif file_name[0] == "_":
        type_ = "ignore"
    elif given_file[0] == given_file[-1]:
        type_ = "folder"
    else:
        type_ = given_file[-1]
    return type_.lower()


def re_format(target_folder, case=1):
    case = case % 5
    os.chdir(target_folder)
    list_ = os.listdir()
    if case == 1:
        for i in list_:
            number = 0
            while True:
                try:
                    if number == 0:
                        os.rename(i, i.title())
                    else:
                        os.rename(i, f"{i.title()}-{number}")
                    break
                except OSError:
                    number += 1
                except Exception as e:
                    print(e)
    elif case == 2:
        for i in list_:
            number = 0
            while True:
                try:
                    if number == 0:
                        os.rename(i, i.upper())
                    else:
                        os.rename(i, f"{i.upper()}-{number}")
                    break
                except OSError:
                    number += 1
                except Exception as e:
                    print(e)
    elif case == 3:
        for i in list_:
            number = 0
            while True:
                try:
                    if number == 0:
                        os.rename(i, i.lower())
                    else:
                        os.rename(i, f"{i.lower()}-{number}")
                    break
                except OSError:
                    number += 1
                except Exception as e:
                    print(e)
    elif case == 4:
        for i in list_:
            number = 0
            while True:
                try:
                    if number == 0:
                        os.rename(i, i.capitalize())
                    else:
                        os.rename(i, f"{i.capitalize()}-{number}")
                    break
                except OSError:
                    number += 1
                except Exception as e:
                    print(e)


def create_folder(name):
    new_name = name.lower()
    try:
        os.mkdir(new_name)
    except FileExistsError:
        pass
    return new_name


def organize(given_folder_list, given_target, given_destination, given_ignore):
    moved = 0
    ignored = 0
    for folder in given_folder_list:
        main = f"{given_target}/{folder}"
        goto(main)
        for f in files():
            t = file_type(f)
            if t not in given_ignore:
                goto(given_destination)
                new_destination = create_folder(t)
                goto(main)
                shutil.move(f"{main}/{f}",
                            f"{given_destination}/{new_destination}/{f}")
                # print(f"{f} moved !!")
                moved += 1
            else:
                # print(f"{f} is {t}")
                ignored += 1
    return moved, ignored, given_destination


def print_data(moved, ignored, destination, gap=0):
    print("\n" * gap, end="")
    print(f"Summery:\n\t"
          f"{moved} files Organized\n\t"
          f"{ignored} files Ignored\n\t"
          f"Destination: \"{destination}\"")
