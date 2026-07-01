# Student Task Manager — App Planning Document

> **Project type:** Planning project (no code). This is the blueprint for the Flutter app
> to be built from Day 9 onward. Professional developers always plan before coding.

---

## Step 1 — Problem Statement

Students often struggle to keep track of their assignments, deadlines, and study tasks.
They forget due dates, lose track of what needs doing, and feel disorganized and stressed.

The **Student Task Manager** app solves this by giving students a simple, organized place to
add tasks, set priorities and due dates, mark tasks complete, and see everything they need to
do at a glance.

---

## Step 2 — Features (Prioritized)

| Feature                  | Priority      | Description                          |
| ------------------------ | ------------- | ------------------------------------ |
| Add a task               | Must-have     | Create a new task with a title       |
| View all tasks           | Must-have     | See a list of all tasks              |
| Mark task complete       | Must-have     | Check off finished tasks             |
| Delete a task            | Must-have     | Remove tasks                         |
| Set a due date           | Must-have     | Add a deadline to a task             |
| Set priority             | Nice-to-have  | Mark tasks as high / medium / low    |
| Categories               | Nice-to-have  | Group tasks by subject               |
| Reminders/notifications  | Nice-to-have  | Get alerts before due dates          |

**Scope for v1:** build the **must-have** features first. A working app that does a few things
well beats an unfinished app that tries to do everything. *Start small and iterate.*

---

## Step 3 — Screens

| Screen                  | Purpose                                   |
| ----------------------- | ----------------------------------------- |
| Home / Task List screen | Shows all tasks; the main screen          |
| Add Task screen         | A form to create a new task               |
| Task Details screen     | Shows one task's full details; edit/delete |
| Settings screen *(opt)* | App preferences                           |

---

## Step 4 — User Flows

### Adding a task
```
[Home / Task List screen]
        |
        |  user taps the "+" (Add) button
        v
[Add Task screen]
        |
        |  user enters a title, due date, taps "Save"
        v
[Home / Task List screen]   (the new task now appears in the list)
```

### Completing a task
```
[Home / Task List screen]
        |
        |  user taps the checkbox next to a task
        v
[Home / Task List screen]   (the task is marked complete)
```

---

## Step 5 — Wireframes

### Home / Task List Screen
```
+-------------------------------+
|  My Tasks              [Menu] |  <- header with title
+-------------------------------+
|  [x] Math homework    (today) |  <- task item (checkbox + title + due)
|  [ ] Read chapter 5   (Fri)   |  <- a list
|  [ ] Submit project   (Mon)   |
|  [ ] Study for exam   (next)  |
|                               |
|                               |
|                          (+)  |  <- floating "Add" button
+-------------------------------+
```

### Add Task Screen
```
+-------------------------------+
|  < Back    Add Task           |  <- header with back navigation
+-------------------------------+
|  Title:                       |
|  [_________________________]  |  <- text input (form)
|                               |
|  Due date:                    |
|  [  Select date          v ]  |  <- date picker
|                               |
|  Priority:                    |
|  ( ) High ( ) Medium ( ) Low  |  <- options
|                               |
|       [   Save Task   ]       |  <- button
+-------------------------------+
```

### Task Details Screen
```
+-------------------------------+
|  < Back    Task Details       |
+-------------------------------+
|  Math homework                |  <- the task title
|                               |
|  Due: Today                   |
|  Priority: High               |
|  Status: Not complete         |
|                               |
|  [ Mark Complete ]            |  <- action buttons
|                               |
|  [ Edit ]  [ Delete ]         |
+-------------------------------+
```

---

## Step 6 — Navigation Structure

```
            [Home / Task List]
              /            \
   tap "+"  /                \  tap a task
           v                  v
     [Add Task]         [Task Details]
           |                  |
   (save returns      (edit/delete returns
    to Home)           to Home)
```

**Explanation:** The Home screen is the hub. From it, the "+" button leads to the Add Task
screen, and tapping a task leads to its Details screen. Both lead back to Home. This is
**stack navigation** — screens stack on top, and "back" returns to the previous one. Simple,
logical, and easy for users to understand.

---

## Interview Tip

> **"How do you plan a mobile app?"** — I start with a clear problem statement defining what
> the app solves and for whom. Then I list features, prioritizing must-haves over nice-to-haves
> to keep the first version focused. I identify the screens the app needs, design the user flow
> showing how users move between screens to accomplish goals, create wireframes sketching each
> screen's layout, and define the navigation structure connecting the screens. This planning
> produces a blueprint that makes building far easier and prevents costly mistakes.
