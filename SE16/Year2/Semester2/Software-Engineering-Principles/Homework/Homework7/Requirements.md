# PEPE Requirements

[[toc]]

## EARN Requirements

__**User Requirements**__

_*Functional*_

- The software must allow users to create, view, edit and delete desired 
projects.
- The software must allow users to create tasks, assign them to team 
members and set deadlines.
- The software must allow users to update their task status such as in
progress, completed, etc.
- The software must allow users to view project timeline in a Gantt Chart.
- The software must allow users to collaborate and receive notifications
for task update.

_*Non-Functional*_

- The software must be accessible by normal web browser without requiring
additional installation from the users.
- The software must display clear visual indicators for task status and
progress
- The software must be user-friendly and not requiring users a lot of
learning to perform basic actions.
- The software must provide error messages when invalid input occurs.
- The software must allow users to complete common actions with as
minimal steps as possible.

__**System Requirements**__

_*Functional*_

- The system must generate and update Gantt charts automatically based
on the task schedule.
- The system must authenticate users before grating access to protected
features.
- The system must send real time notifications to users.
- The system must store project, task, user, role and comment data in
a database.
- The system must validate user input before saving data to the database.

_*Non-Functional*_

- The system must be scalable to support increasing number of users and
projects.
- The system must protect users data against unauthorized access or
modification for security.
- The system must prevent data loss during updates or failures for
reliability.
- The system must be available during normal working hours.
- The system should support on Docker container.

## Pangya Requirements

__**User Requirements**__

_*Functional*_

- The program shall allow users to create an account and authenticate
securely.
- The program shall allow users to create projects and assign tasks to
team members.
- The program shall allow users to assign roles (manager, back-end
engineer, etc.) and apply their restrictions for other users in the project.
- The program shall allow team members to view, update, and tag tasks
with statuses (e.g., To Do, In Progress, Done).
- The program shall provide a feature for users to mention or tag other
users within tasks or projects.
- The program shall allow the users to view project metadata, including
deadlines, task status, and assigned members.
- The program shall provide features for users to create, modify, and
view project timelines and planning artifacts such as Gantt charts and
diagrams.

_*Non-Functional*_

- The application shall provide real-time responsiveness with no more
than 1 second latency for collaborative actions, including modifications
of the charts and diagrams.
- The system shall be accessible through modern web browsers without
requiring additional plugins.
- The user interface shall be intuitive and easy to navigate for both
managers and team members.
- The system shall ensure data consistency and prevent unauthorized
access to project data.
- The application shall maintain availability during concurrent usage
by multiple users.

__**System Requirements**__

_*Functional*_

- The system shall provide a frontend implemented using React with
TypeScript, enabling dynamic rendering of project boards, tasks, and
project views without full page reloads.
- The system shall expose RESTful APIs implemented using Django and 
Django REST Framework (DRF) to handle user authentication, project
management, task assignment, and metadata retrieval.
- The system shall support real-time communication using Django Channels 
and WebSockets, allowing instant synchronization of task updates,
assignments, mentions, and notifications across connected clients.
- The system shall persist structured application data—including users, 
projects, tasks, roles, and permissions—using PostgreSQL, accessed through 
the Django ORM.
- The system shall implement role-based access control (RBAC) using 
Django’s authentication and permission framework to enforce manager and 
team member privileges.
- The system shall support storage and retrieval of project metadata
and design artifacts (e.g., diagrams, timelines) using JSON fields in 
PostgreSQL.
- The system shall provide endpoints for frontend integration of project
planning tools, such as Gantt charts and interactive diagrams, rendered 
client-side using React-compatible libraries.
- The system shall log application errors, security events, and system
activity using Django’s logging framework for monitoring and debugging.

_*Non-Functional*_

- The system shall maintain low-latency real-time updates, with WebSocket
message propagation handled via Django Channels backed by Redis as
a message broker.
- The system shall secure all client-server communication using HTTPS
and secure WebSocket (WSS) protocols, with reverse proxy support provided
by Nginx.
- The system shall be scalable to support multiple concurrent users by
utilizing ASGI servers (e.g., Uvicorn/Daphne) and stateless backend services.
- The system shall ensure data integrity and transactional consistency
through PostgreSQL ACID-compliant transactions.
- The system shall be maintainable through a modular Django app structure
and strongly typed frontend code using TypeScript.

## Pottarr Requirements

__**User Requirements**__

_*Functional*_

- The app shall create the diagrams in 2 main methods, writing it with
the mermaid markdown syntax or drag and drop.
- The program shall export to `SVG` or `PNG` file and paste into any kind of
document file (i.e. Google Doc, MS Word,LibreOffice Document Latex,
MS PowerPoint).
- The program shall let users to edit tasks via markdown rendering.
- The program shall let users create a project schedule Gantt Chart and
calculate the critical path for the project to finish.

_*Non-Functional*_

- The program shall be able to be used on every desktop platform through
browser and on mobile devices.
- The program shall be able to sync real-time with other users in the
team.
- The program shall preview task which is currently editing in real-time.
- The app shall be able to handle at least 50 or more objects being
generated in the canvas.
- The app shall support editing the tasks through VS-Code.
- The project owner shall use this program and set the roles to others
team members.

__**System Requirements**__

_*Functional*_

- The program shall use both `WebSocket` and `REST API`
- The program shall edit the tasks by the editor package available in
npm.
- The program shall be able see only the project they are assigned to
by filtering in the database table.
- The frontend shall render the markdown syntax with the npm package
named `React Markdown`.
- The app shall compute the critical path with Dijkstra Algorithm

_*Non-Functional*_
- The program shall be able log errors in the logging system.
- The app shall run on any mobile platform by porting into mobile with
React Native.
- The Database shall be normalized to the fifth normal form to prevent
the `INSERT` and `DELETE` problem in the relational database.
- The frontend shall be designed with OOP paradigm for more scalability.
- The backend system shall be able to handle load balancing through Nginx.
