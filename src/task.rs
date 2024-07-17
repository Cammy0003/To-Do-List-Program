#[derive(Clone)]
pub struct TaskNode {
    pub task: String,
    pub time: f32,
    pub next: Option<Box<TaskNode>>,
}

impl TaskNode {
    pub fn new(task: String, time: f32) -> Self {
        TaskNode {
            task,
            time,
            next: None,
        }
    }
}