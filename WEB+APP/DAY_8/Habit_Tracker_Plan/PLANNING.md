# Habit Tracker — Design Challenge Plan (Day 8)

> The **Day 8 Design Challenges** deliverable. A complete app plan for a **Daily Habit Tracker**,
> covering all five challenges: problem statement, prioritized features (MVP), user flow,
> wireframes, and navigation structure.

---

## Challenge 1 — Problem Statement

People who want to build good habits (drinking water, exercising, reading, studying) often
struggle to stay consistent. They start with good intentions but forget to follow through, lose
motivation when they can't see their progress, and give up after a few days.

The **Habit Tracker** solves this by giving users a simple place to create daily habits, check
them off each day, and visualize their streaks and progress — turning small daily wins into
lasting motivation.

---

## Challenge 2 — Feature List (MVP)

| Feature                     | Priority      | Description                                          |
| --------------------------- | ------------- | --------------------------------------------------- |
| Add a habit                 | Must-have     | Create a new habit with a name                       |
| View all habits             | Must-have     | See the list of habits for today                     |
| Mark a habit done           | Must-have     | Check off a habit as completed for the day           |
| Track streaks               | Must-have     | Show how many days in a row a habit was completed     |
| Delete a habit              | Must-have     | Remove a habit                                       |
| Set a reminder time         | Nice-to-have  | Get a daily notification for a habit                  |
| Progress charts / history   | Nice-to-have  | Visualize completion over weeks/months               |
| Habit categories & icons    | Nice-to-have  | Group and personalize habits (health, study, etc.)   |

**MVP scope (v1):** the **five must-have** features. A reliable app that lets users add habits,
check them off, and see their streaks is genuinely useful on its own. *Start small and iterate.*

---

## Challenge 3 — User Flow (Main Task: Completing a Habit)

```
[Home / Today's Habits]
        |
        |  user taps the checkbox next to a habit
        v
[Home / Today's Habits]   (habit marked done; streak count increases)
```

### Secondary flow — Adding a habit
```
[Home / Today's Habits]
        |
        |  user taps the "+" (Add) button
        v
[Add Habit screen]
        |
        |  user enters a name (and optional reminder), taps "Save"
        v
[Home / Today's Habits]   (new habit appears in today's list)
```

---

## Challenge 4 — Wireframes

### Home / Today's Habits Screen
```
+-------------------------------+
|  Today's Habits        [Menu] |  <- header with title
+-------------------------------+
|  [x] Drink water    🔥 5 days |  <- habit item (check + name + streak)
|  [ ] Exercise       🔥 2 days |
|  [x] Read 10 pages  🔥 9 days |
|  [ ] Study Flutter  🔥 1 day  |
|                               |
|                          (+)  |  <- floating "Add" button
+-------------------------------+
```

### Add Habit Screen
```
+-------------------------------+
|  < Back    Add Habit          |  <- header with back navigation
+-------------------------------+
|  Habit name:                  |
|  [_________________________]  |  <- text input
|                               |
|  Reminder (optional):         |
|  [  Set time          v ]     |  <- time picker
|                               |
|  Repeat:                      |
|  ( ) Daily  ( ) Weekdays      |  <- options
|                               |
|        [   Save Habit   ]     |  <- button
+-------------------------------+
```

### Habit Details Screen
```
+-------------------------------+
|  < Back    Habit Details      |
+-------------------------------+
|  Read 10 pages                |  <- habit name
|                               |
|  Current streak:  9 days 🔥   |
|  Best streak:    14 days      |
|  This week:  [x][x][x][ ][ ]  |  <- weekly progress
|                               |
|  [ Mark Done Today ]          |  <- action button
|                               |
|  [ Edit ]  [ Delete ]         |
+-------------------------------+
```

---

## Challenge 5 — Navigation Structure

```
              [Home / Today's Habits]
                /                \
     tap "+"  /                    \  tap a habit
             v                      v
       [Add Habit]           [Habit Details]
             |                      |
     (save returns           (edit/delete returns
      to Home)                to Home)
```

**Explanation:** The Home screen is the hub, listing today's habits with their streaks. The "+"
button opens the Add Habit form; tapping a habit opens its Details (streak history + edit/delete).
Both return to Home. This is **stack navigation** — screens stack on top and "back" returns to the
previous one. Simple, logical, and easy for users to follow.

---

## Design Challenge Checklist

- [x] Complete problem statement
- [x] Prioritized feature list defining the MVP (5 must-haves)
- [x] User flow for the main task
- [x] Wireframes for 3 screens
- [x] Navigation structure connecting all screens
