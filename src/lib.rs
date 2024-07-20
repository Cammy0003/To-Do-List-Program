use crate::task_list::TaskList;
use std::sync::Mutex;
use lazy_static::lazy_static;
use std::ffi::{CString, CStr, c_int};
use std::os::raw::c_char;
use std::ptr;

pub mod task;
pub mod task_list;

lazy_static! {
    static ref TASK_LIST: Mutex<TaskList> = Mutex::new(TaskList::new());
}

#[no_mangle]
pub extern "C" fn insert_list(task: *const c_char, time: f32) -> c_int { // type bool essentially
    // int insert_list(const char* task, float time); // as a C function
    // use crate::task_list;
    let task = unsafe {
        assert!(!task.is_null());
        CStr::from_ptr(task)
    };

    let task = match task.to_str() {
        Ok(s) => s,
        Err(_) => return 0, // false
    };

    let mut list = TASK_LIST.lock().unwrap();
    list.insert(task.to_string(), time);

    return 1; // true
}

#[no_mangle]
pub extern "C" fn remove_list(task: *const c_char) -> c_int { // type bool essentially
    // use crate::task_list;
    let task = unsafe {
        assert!(!task.is_null());
        CStr::from_ptr(task)
    };

    let task = match task.to_str() {
        Ok(s) => s,
        Err(_) => return 0,
    };

    let mut list = TASK_LIST.lock().unwrap();
    let check = list.remove(task.to_string());

    if check == true {
        return 1;
    }
    return 0;
}

#[no_mangle]
pub extern "C" fn find_task(task: *const c_char) -> c_int {
    // use crate::task_list;
    let task = unsafe {
        assert!(!task.is_null());
        CStr::from_ptr(task)
    };

    let task = match task.to_str() {
        Ok(s) => s,
        Err(_) => {
            return 0;
        },
    };

    let mut list = TASK_LIST.lock().unwrap();
    let check = list.view_task(task.clone().to_string());

    if check == "NONE" {
        return 0;
    }


    return 1;

}

#[no_mangle]
pub extern "C" fn clear_list() {
    let mut list = TASK_LIST.lock().unwrap();
    list.clear_list();
}

#[no_mangle]
pub extern "C" fn print_task_list() -> *const c_char {
    let list = TASK_LIST.lock().unwrap();
    let printed = list.print_list();

    let c_printed = match CString::new(printed) {
        Ok(c_printed) => c_printed,
        Err(_) => return ptr::null(),
    };

    return c_printed.into_raw() // Rust loses ownership and burrowing rules over this string, it will be freed by free_string(s)
}

#[no_mangle]
pub extern "C" fn free_c_string(s: *const c_char) {
    if s.is_null() {
        return;
    }
    unsafe {
        let x = CString::from_raw(s as *mut c_char); // Rust's ownership takes back c_string s.
    }
}



