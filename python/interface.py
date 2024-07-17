from cffi import FFI
import os

ffi = FFI()

# Load the Rust shared library
current_dir = os.path.dirname(os.path.abspath(__file__))
library_path = ffi.dlopen(current_dir, '..', 'target', 'release', 'to_do_list.dll')
# the above is done to ensure that the correct path is dynamically provided regardless of device.
# else I could have just done 'target/release/to_do_list.dll', but that maybe problematic...idk

lib = ffi.dlopen(library_path)

# establish the RUST functions
ffi.cdef("""
typdef struct {
    const char* task;
    float time;
} TaskResult;

TaskResult creat_task_result(const char* task, float time);

int insert_list(const char* task, float time);
int remove_list(const char* task);
TaskResult view_task(cont char* task);
void clear_list();
""")



