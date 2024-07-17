#ifndef MY_PROJECT_H
#define MY_PROJECT_H

#include <stdarg.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

typedef struct TaskResult {
  const char *task;
  float time;
} TaskResult;

bool insert_list(const char *task, float time);

struct TaskResult view_task(const char *task);

#endif /* MY_PROJECT_H */
