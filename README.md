# To Do List
2024-07

This was a personal **To Do List** project that has a **RUST Backend** and a **Python Frontend**.

### Objective:
To create a **to-do list** in which users can create a list of tasks to complete, and **set a 
time** to complete them. 

This app is to be very primitive and not very competitive to any real to do list application that's out there, but the main
purpose of this program was to gain a better understanding of Rust, as well as understand interops between languages. Also
practicing the `tkinter` library GUI in Python, was another interest.

### Progression:
The tasks where established as a nodes in a linked list, where each Task Node, contained a task and time
parameter, as well as a **next** parameter for the next node in the list. **RUST** was used for
implementing and handling these linked lists, as it should allow for a faster program overall, and it
was also a good challenge. 

With `Rust`, I utilized a `lazy-static` dependency in order to save the list data structure, that the python 
functions access through `C`. Types in `Rust` are very picky to a `Rust` compiler. As a result, I spent a lot of time doing do-overs, and having
dragging conversations with Chat-GPT to understand where I was going wrong. With all of this having to eventually be
compatible with `Python` as well, required that I be very careful with code I added, or got rid of.

Currently `Python` script is implemented, where through the use of `cffi` and the many crates used in rust (refer 
to "lib.rs" file), I was able to have `Python` call to `Rust` **functions** made public. If you notice in the 
"interface.py" file, there is a `ffi.cdef()` function, which was a necessary `C` language buffer for `Rust` to 
communicate to. This implied that the `Rust` functions needed to be established as `C` like, where through the many crates in "lib.rs", 
I could return `C` `types` instead of `Rust` `types` for the functions in "lib.rs". Luckily I have experience in `C`, so that was not too tricky 
for me to implement.

Finally, `Python` utilizes these `C` functions through a user interface. If you run `python python/ui.py`, you will find
a working To Do List application. Granted it does look pretty ugly, but it's my first time playing with `tkinter` so cut
me a break would ya. Anyway, the hardest part in all of that was printing the list. Printing the list, required that 
I design Rust's `print_list()` function, to return a long string that alternates between a "Task:" and "Time:" substring,
preceding the corresponding task and time substring. This was done to allow python to process the string more easily and to
determine the actual tasks and times, to then print in the ui. interface.py did the processing of that, and returned a tuple 
(task, time), that the ui.py `process_print_task()` function would deal with.

Anyway, all done now!! I have not done any rigorous testing, so there may be some bugs unknown, but currently, everything
seems fine.

### Completed: (2024-07-17)
I have established a user interface with `tkinter`. Currently, everything seems to work correctly. 
 

### How to Run
Within the project directory, type the following into the terminal:
```commandline
python python/ui.py
```



