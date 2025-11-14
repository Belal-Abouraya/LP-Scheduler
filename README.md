# 📅 Smart To-Do List Scheduler  

## 📘 Overview  
This project implements a **smart task scheduler** that transforms a set of tasks (with deadlines, durations, and priorities) into an **optimized schedule** using linear programming.

The project includes a **Python user interface (UI)** that allows users to create tasks, define blocked time slots, and visualize the final schedule in a **table**.

---

## ✨ Features  

### 🔢 Optimization Engine  
- Mathematical model for task scheduling  
- Supports task attributes:  
  - Duration  
  - Deadline  
  - Priority weight  
  - Earliest start time 
  - Daily work window  
  - Non-overlapping tasks  
  - Optional maximum continuous work limits

### 🖥️ Python User Interface  
The project includes a custom Python UI that provides:

- Adding new tasks with all required fields  
- Adding **blocked slots** (meetings, classes, etc.)  
- Generating an optimized schedule  
- Displaying the schedule in a **table**

---

## 🧩 Schedule Visualization  
The scheduler outputs a timetable:

- Rows represent **days**  
- Columns represent **slots** 
- Empty slots represent available free time  

This layout helps users easily understand and adjust their plan.

---

## 🔧 Technologies Used  
- **Python**  
- Optimization libraries (PuLP)  
- GUI Framework (PyQt)

---

## 🎯 Optimization Objectives  
The scheduler aims to **maximize the sum of the priorities of the tasks completed before their deadlines**
