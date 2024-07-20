use crate::task::TaskNode;

pub struct TaskList {
    head: Option<Box<TaskNode>>,
}

impl TaskList {
    pub fn new() -> Self {
        TaskList {head: None}
    }

    pub fn insert(&mut self, task: String, time: f32) {
        let mut new_node = Box::new(TaskNode::new(task, time));

        // self.head should be taken as a reference at first, since we merely wish to know what's in it
        if self.head.is_none() || self.head.as_ref().unwrap().time >= time {
            new_node.next = self.head.take();
            self.head = Some(new_node);
            return;
        }

        // self.head.as_mut() ensures that changes to current, apply to the list that head contains
        let mut current = self.head.as_mut();

        while let Some(node) = current {
            if node.next.is_none() || node.next.as_ref().unwrap().time >= time {
                new_node.next = node.next.take();
                node.next = Some(new_node);
                return;
            }
            current = node.next.as_mut();
        }
    }

    pub fn remove(&mut self, task: String) -> bool {
        if let Some(node) = self.head.as_mut() { // check head node
            if node.task == task {
                self.head = node.next.take(); // take what proceeds (next) head, and give it to
                return true;
            }
        }

        let mut current = self.head.as_mut();

        while let Some(node) = current {
            if let Some(check) = node.next.as_mut() {
                if check.task == task {
                    node.next = check.next.take();
                    return true;
                }
            }

            current = node.next.as_mut();
        }

        return false; // never found the specified task
    }

    pub fn change_time(&mut self, task: String, new_time: f32) -> bool {
        let mut current = self.head.as_mut();

        while let Some(node) = current {
            if node.task == task {
                self.remove(task.clone());
                self.insert(task.clone(), new_time);
                return true;
            }
            current = node.next.as_mut();
        }

        return false; // never found the specified task
    }

    pub fn change_task(&mut self, task: String, new_task: String) -> bool {
        if self.view_task(task.clone()) != "NONE" {
            let time = self.view_time(task.clone());
            self.remove(task);
            self.insert(new_task, time);
            return true;
        }
        return false; // never found the specified task
    }

    pub fn view_task(&self, task: String) -> String {
        let mut current = self.head.as_ref();

        while let Some(node) = current {
            if node.task == task {
                return node.task.to_string();
            }
            current = node.next.as_ref();
        }
        return "NONE".to_string(); // never found the specified task
    }

    pub fn view_time(&self, task: String) -> f32 {
        let mut current = self.head.as_ref();

        while let Some(node) = current {
            if node.task == task {
                return node.time;
            }
            current = node.next.as_ref();
        }

        return -1.0; // never found the specified task
    }

    pub fn print_list(&self) -> String { // mostly used to trouble shoot TaskList within RUST only
        let mut s = String::new();
        println!("BEGIN"); // So python knows where to begin when capturing output
        let mut current = self.head.as_ref();

        while let Some(node) = current {
            s.push_str("Task: ");
            s.push_str(&node.task);
            s.push_str("Time: ");
            s.push_str(&format!("{:.2}", node.time));
            // println!("Task: {}\nTime: {:.2}\n", node.task, node.time);
            current = node.next.as_ref();
        }

        // s.push_str("\nEND"); // Don't think I need to push END cause python can determine when there is nothing left in a string itself

        return s;
        // println!("END"); // So python knows where to end
    }

    pub fn is_empty(&self) -> bool {
        return if let Some(_) = self.head.as_ref() {
            false
        } else {
            true
        }
    }

    pub fn clear_list(&mut self) {
        self.head = None;
    }
}

