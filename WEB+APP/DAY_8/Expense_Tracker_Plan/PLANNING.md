# Personal Expense Tracker — App Planning Document

> **Day 8 Lab — Mobile Development Workflow.** A planning exercise (no code). This applies the
> full process from Section 28 to produce a buildable blueprint for a Personal Expense Tracker.

---

## Step 1 — Problem Statement

People often struggle to keep track of where their money goes day to day. They lose receipts,
forget small purchases, and reach the end of the month surprised by how much they spent and
unsure what they spent it on.

The **Personal Expense Tracker** solves this by giving users a quick, simple place to record
each expense with an amount, category, and date, then see clear totals and a breakdown of their
spending — so they always know where their money is going and can make better decisions.

---

## Step 2 — Features (Prioritized)

| Feature                       | Priority      | Description                                       |
| ----------------------------- | ------------- | ------------------------------------------------- |
| Add an expense                | Must-have     | Record amount, category, and date of a purchase   |
| View all expenses             | Must-have     | See a list of all recorded expenses               |
| See total spending            | Must-have     | View the running total of what's been spent        |
| Delete an expense             | Must-have     | Remove an incorrect or unwanted entry             |
| Categorize expenses           | Must-have     | Tag each expense (food, transport, bills, etc.)   |
| Spending by category          | Nice-to-have  | Breakdown / chart of spending per category        |
| Monthly budget & alerts       | Nice-to-have  | Set a budget and get warned when nearing it       |
| Export / backup data          | Nice-to-have  | Export expenses to a file (CSV) or cloud backup   |

**MVP scope (v1):** the **five must-have** features above. A working app that records and totals
expenses reliably beats an unfinished app crammed with charts and budgets. *Start small, iterate.*

---

## Step 3 — Screens

| Screen                   | Purpose                                             |
| ------------------------ | --------------------------------------------------- |
| Home / Expense List      | Main screen — shows total + list of expenses        |
| Add Expense screen       | A form to record a new expense                       |
| Expense Details screen   | Shows one expense's full details; delete            |
| Summary screen *(opt)*   | Spending breakdown by category (nice-to-have)        |

---

## Step 4 — User Flow (Main Task: Recording an Expense)

```
[Home / Expense List]
        |
        |  user taps the "+" (Add) button
        v
[Add Expense screen]
        |
        |  user enters amount, picks category & date, taps "Save"
        v
[Home / Expense List]   (new expense appears in the list; total updates)
```

### Secondary flow — Reviewing & deleting an expense
```
[Home / Expense List]
        |
        |  user taps an expense
        v
[Expense Details]
        |
        |  user taps "Delete"
        v
[Home / Expense List]   (expense removed; total updates)
```

---

## Step 5 — Navigation Structure

```
              [Home / Expense List]
                /              \
     tap "+"  /                  \  tap an expense
             v                    v
     [Add Expense]         [Expense Details]
             |                    |
     (save returns          (delete returns
      to Home)               to Home)
```

**Explanation:** The Home screen is the hub showing the total and the expense list. The "+"
button opens the Add Expense form; tapping any expense opens its Details. Both return to Home.
This is **stack navigation** — screens stack on top and "back" returns to the previous one.
Simple and predictable for the user.

---

## Step 6 — Wireframes

### Home / Expense List Screen
```
+-------------------------------+
|  My Expenses           [Menu] |  <- header with title
+-------------------------------+
|  Total spent:        $342.50  |  <- running total
+-------------------------------+
|  Lunch        Food     -$8.00 |  <- expense item (name + category + amount)
|  Bus pass     Transit -$25.00 |
|  Groceries    Food    -$54.20 |
|  Electricity  Bills   -$60.00 |
|                               |
|                          (+)  |  <- floating "Add" button
+-------------------------------+
```

### Add Expense Screen
```
+-------------------------------+
|  < Back    Add Expense        |  <- header with back navigation
+-------------------------------+
|  Amount:                      |
|  [ $ ______________________ ] |  <- number input
|                               |
|  Category:                    |
|  [  Food              v ]     |  <- dropdown
|                               |
|  Date:                        |
|  [  Select date       v ]     |  <- date picker
|                               |
|       [   Save Expense   ]    |  <- button
+-------------------------------+
```

### Expense Details Screen
```
+-------------------------------+
|  < Back    Expense Details    |
+-------------------------------+
|  Groceries                    |  <- the expense title
|                               |
|  Amount:   $54.20             |
|  Category: Food               |
|  Date:     29 Jun 2026        |
|                               |
|  [ Delete ]                   |  <- action button
+-------------------------------+
```

---

## Lab Completion Checklist

- [x] Problem statement
- [x] Prioritized feature list (MVP defined — 5 must-haves)
- [x] User flow for the main task
- [x] Navigation structure
- [x] Wireframes for the main screens (3)

A complete, professional app plan — taking an idea from concept to a buildable blueprint, exactly
what professionals produce before writing any code.
