from cffi import FFI

# import os

ffi = FFI()

# Load the Rust release file
library_path = 'target/release/to_do_list.dll'

lib = ffi.dlopen(library_path)

# establish the RUST functions
ffi.cdef("""
int insert_list(const char* task, float time);
int remove_list(const char* task);
int find_task(const char* task);
void clear_list();
const char* print_task_list();
void free_c_string();
""")


def insert_task(task, time):  # string, f32 -> void
    return lib.insert_list(task.encode('utf-8'), time)


def remove_task(task):  # string -> bool
    if lib.remove_list(task.encode('utf-8')) == 0:
        return False
    return True


# maybe I won't keep this function
def find_task(task):  # string -> bool
    if lib.find_task(task.encode('utf-8')) == 0:
        return False
    return True


def print_task_list():  # -> void
    c_output = lib.print_task_list()
    output_str = ffi.string(c_output).decode('utf-8').split()  # output string is split into substrings.
    # This output_str should be alternating between Task: and Time:
    # print(output_str)

    task = []
    time = []
    check_task = False
    check_time = False
    for sub_string in output_str:
        if sub_string == "Task:":
            check_task = True
            continue  # moving onto the next substring immediately proceeding "Task: "
        if sub_string == "Time:":
            check_time = True
            continue  # moving onto the next substring immediately proceeding "Time: "

        # By appending, I assume that correct order of tasks is preserved
        if check_task is True:
            task.append(sub_string)
            check_task = False
        elif check_time is True:
            time.append(sub_string)
            check_time = False

    tuple_tasks = []  # (Task, Time)
    # print(task)
    # print(time)
    for i in range(len(task)):
        tuple_tasks.append((task[i], time[i]))
    # print(tuple_tasks)
    return tuple_tasks


# print_task_list()
'''
# Just testing to see if it works
insert_task("A", 1.00)
insert_task("B", 2.00)
insert_task("C", 3.00)
insert_task("D", 5.00)

# print_task_list()

# insert_task("D", 4.00)

print_task_list()

print(remove_task("A"), " for A")  # should be true
print_task_list()

print(remove_task("C"), " for C")  # should be true
print_task_list()

print(remove_task("B"), " for B")  # should be true

print_task_list()

print(remove_task("A"), " for A")  # should be false
print_task_list()

print(remove_task("D"), " for D")  # should be true
print_task_list()

# print("Finding E (True): ", find_task("E"))
# print("Finding B (False): ", find_task("B"))
'''
