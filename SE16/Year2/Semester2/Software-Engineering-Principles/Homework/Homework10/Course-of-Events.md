# Course of Events

---

## Course of Event for Create Project

### B Basic Path for Create Project

| Performer | Step | Action |
| :-------: | :--: | :----- |
| User | 1 | Login |
| System | 2 | Authenticate user credentials |
| User | 3 | Select "Create Project" |
| System | 4 | Display project creation form |
| User | 5 | Enter project title, description, and start date |
| User | 6 | Add project members |
| User | 7 | Add initial tasks |
| System | 8 | Save project information |
| System | 9 | Display project dashboard |

### A1 Login failed (Alternative from B.2)

| Performer | Step | Action |
| :-------: | :--: | :----- |
| System | 1 | Display login error message |
| User | 2 | Re-enter username and password |
| System | 3 | Re-authenticate credentials |

### A2 User skips adding tasks (Alternative from B.7)

| Performer | Step | Action |
| :-------: | :--: | :----- |
| User | 1 | Skip task creation |
| System | 2 | Save project without tasks |

### E1 Server Down (Exception)

| Performer | Step | Action |
| :-------: | :--: | :----- |
| System | 1 | Display system error message |

---

## Course of Event for View Project

### B Basic Path for View Project

| Performer | Step | Action |
| :-------: | :--: | :----- |
| User | 1 | Login |
| System | 2 | Authenticate user |
| User | 3 | Select a project |
| System | 4 | Retrieve project data |
| System | 5 | Display project information |

### A1 Project not found (Alternative from B.4)

| Performer | Step | Action |
| :-------: | :--: | :----- |
| System | 1 | Display project not found message |

---

## Course of Event for Assign Tasks

### B Basic Path for Assign Tasks

| Performer | Step | Action |
| :-------: | :--: | :----- |
| Manager | 1 | Login |
| System | 2 | Authenticate manager |
| Manager | 3 | Open project |
| Manager | 4 | Select a task |
| Manager | 5 | Assign task to team member |
| System | 6 | Update task assignment |
| System | 7 | Notify assigned member |

### A1 Member unavailable (Alternative from B.5)

| Performer | Step | Action |
| :-------: | :--: | :----- |
| System | 1 | Display member unavailable message |
| Manager | 2 | Select another member |

---

## Course of Event for View Assigned Tasks

### B Basic Path for View Assigned Tasks

| Performer | Step | Action |
| :-------: | :--: | :----- |
| Team Member | 1 | Login |
| System | 2 | Authenticate user |
| Team Member | 3 | Select "View Assigned Tasks" |
| System | 4 | Retrieve assigned tasks |
| System | 5 | Display task list |

### A1 No tasks assigned (Alternative from B.4)

| Performer | Step | Action |
| :-------: | :--: | :----- |
| System | 1 | Display empty task list |

---

## Course of Event for Manage Tasks

### B Basic Path for Manage Tasks

| Performer | Step | Action |
| :-------: | :--: | :----- |
| Manager | 1 | Login |
| System | 2 | Authenticate manager |
| Manager | 3 | Open project |
| Manager | 4 | Add, edit, or delete tasks |
| System | 5 | Validate task changes |
| System | 6 | Save updated task list |

### A1 Invalid task data (Alternative from B.5)

| Performer | Step | Action |
| :-------: | :--: | :----- |
| System | 1 | Display validation error |
| Manager | 2 | Correct task information |

---

## Course of Event for Edit Diagrams or Gantt Chart

### B Basic Path for Edit Diagrams / Gantt Chart

| Performer | Step | Action |
| :-------: | :--: | :----- |
| Manager | 1 | Login |
| System | 2 | Authenticate manager |
| Manager | 3 | Open project |
| Manager | 4 | Select diagram or Gantt chart |
| Manager | 5 | Edit diagram elements |
| System | 6 | Save updated diagram |

### A1 Edit canceled (Alternative from B.5)

| Performer | Step | Action |
| :-------: | :--: | :----- |
| Manager | 1 | Cancel editing |
| System | 2 | Discard changes |

---

## Course of Event for Update Task Status

### B Basic Path for Update Task Status

| Performer | Step | Action |
| :-------: | :--: | :----- |
| Team Member | 1 | Login |
| System | 2 | Authenticate user |
| Team Member | 3 | Open assigned task |
| Team Member | 4 | Update task status |
| System | 5 | Save task status |
| System | 6 | Notify manager |

### A1 Invalid status update (Alternative from B.4)

| Performer | Step | Action |
| :-------: | :--: | :----- |
| System | 1 | Display invalid status message |
| Team Member | 2 | Select valid status |

---

## Course of Event for Request Review

### B Basic Path for Request Review

| Performer | Step | Action |
| :-------: | :--: | :----- |
| Team Member | 1 | Login |
| System | 2 | Authenticate user |
| Team Member | 3 | Select completed task |
| Team Member | 4 | Request review |
| System | 5 | Send review request to manager |

### A1 Task not completed (Alternative from B.3)

| Performer | Step | Action |
| :-------: | :--: | :----- |
| System | 1 | Display task not completed message |

---

## Course of Event for Receive Notifications

### B Basic Path for Receive Notifications

| Performer | Step | Action |
| :-------: | :--: | :----- |
| System | 1 | Generate notification |
| System | 2 | Send notification to user |
| User | 3 | View notification |
| User | 4 | Mark notification as read |

### A1 Notification delivery failed (Alternative from B.2)

| Performer | Step | Action |
| :-------: | :--: | :----- |
| System | 1 | Retry notification delivery |

