# To Do List
2024-07

This was a personal **To Do List** project that has a **RUST Backend** and a **Python Frontend**.

### Objective:
To create a **to-do list** in which users can create a list of tasks to complete, and **set a 
time** to complete them. 

### Progress:
The tasks where established as a nodes in a linked list, where each Task Node, contained a task and time
parameter, as well as a **next** parameter for the next node in the list. **RUST** was used for
implementing and handling these linked lists, as it should allow for a faster program overall, and it
was also a good challenge. 

Types in `Rust` are very picky to a `Rust` compiler. As a result, I spent a lot of time doing do-overs, and having
dragging conversations with Chat-GPT to understand where I was going wrong. With all of this having to eventually be
compatible with `Python` as well, required that I be very careful with code I added, or got rid of.

Currently `Python` script is implemented, where through the use of `cffi` and the many crates used in rust (refer 
to "lib.rs" file), I was able to have `Python` call to `Rust` **functions** made public. If you notice in the 
"interface.py" file, there is a `ffi.cdef()` function, which was a necessary `C` language buffer for `Rust` to 
communicate to. This implied that the `Rust` functions needed to be `C` like, where through the many crates in "lib.rs", 
I could return `C` `types` instead of `Rust` `types`. Luckily I have experience in `C`, so that was not too tricky 
for me to implement.

##### NOTE: what is written below has yet to be implemented (it's the plan)...
Eventually, **Python** is to be used to handle **user interaction** through `Tkinter`, a Python `GUI`. This repository
will be updated soon once that has been completed. 


