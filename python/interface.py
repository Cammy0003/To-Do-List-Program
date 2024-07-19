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
void print_task_list();
""")


def insert_task(task, time):  # string, f32 -> void
    return lib.insert_list(task.encode('utf-8'), time)


def remove_task(task):  # string -> bool
    if lib.remove_list(task.encode('utf-8')) == 0:
        return False
    return True


def find_task(task):  # string -> bool
    if lib.find_task(task.encode('utf-8')) == 0:
        return False
    return True


def print_task_list():  # -> void
    lib.print_task_list()


print_task_list()

'''
# Just testing to see if it works
insert_task("A", 1.00)
insert_task("B", 2.00)
insert_task("C", 3.00)
insert_task("E", 5.00)

print_task_list()

insert_task("D", 4.00)

print_task_list()

remove_task("C")
remove_task("B")

print_task_list()

print("Finding E (True): ", find_task("E"))
print("Finding B (False): ", find_task("B"))
'''