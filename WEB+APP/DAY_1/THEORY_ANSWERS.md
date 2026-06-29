# Part A — Theory Questions & Answers

Day 1: Introduction to Web and Mobile App Development

---

## 1. Software vs. Hardware

**Hardware** is the physical, touchable parts of a computer — the actual machinery. **Software** is the set of instructions and programs that tell the hardware what to do; you cannot physically touch it.

- **Hardware examples:** keyboard, hard drive (or RAM, monitor).
- **Software examples:** Google Chrome browser, Microsoft Word (or Windows, a mobile app).

In short: hardware is the body, software is the brain that runs on it.

---

## 2. Internet vs. World Wide Web (Analogy)

The **Internet** is the global network of physical cables, routers, and connected computers — think of it as the **road and railway system** that connects every city in the world.

The **World Wide Web (WWW)** is just one service that travels on those roads — the collection of websites and web pages you visit through a browser. Think of it as the **cars and trucks** carrying goods along the roads.

So the Internet is the infrastructure; the Web is one thing that uses it (email, online games, and streaming use the same roads but are not the Web).

---

## 3. The Request–Response Cycle

The request–response cycle is the back-and-forth conversation that happens every time you open a web page:

1. The **user** types a web address or clicks a link.
2. The **browser** turns that action into a request and sends it out.
3. The request travels across the **internet** to find the right computer.
4. The **server** receives the request and figures out what was asked for.
5. The server may ask the **database** for stored information (e.g., your profile).
6. The server packages a **response** (the web page/data) and sends it back through the internet to the browser, which displays it.

**The five players:** User → Browser → Internet → Server → Database.

---

## 4. Frontend vs. Backend Development

**Frontend** is everything the user sees and interacts with in the browser (the "client side"). **Backend** is the behind-the-scenes logic, servers, and databases that the user never sees (the "server side").

**Frontend responsibilities:**
- Building the layout and visual design of pages (buttons, menus, colors).
- Handling user interactions (clicks, form input, animations).

**Backend responsibilities:**
- Storing, retrieving, and managing data in databases.
- Handling business logic, security, and user authentication (logins, payments).

---

## 5. HTML, CSS, and JavaScript (House Analogy)

- **HTML** is the **structure of the house** — the walls, rooms, doors, and foundation. It defines what content exists (headings, paragraphs, images).
- **CSS** is the **decoration and style** — the paint, furniture, and interior design. It controls how things look (colors, fonts, spacing, layout).
- **JavaScript** is the **electricity and plumbing** — it makes things work and respond. It adds behavior and interactivity (a light switch that turns on, a doorbell that rings).

Together: HTML builds it, CSS beautifies it, JavaScript brings it to life.

---

## 6. What is an API? (Real-World Example)

An **API (Application Programming Interface)** is a set of rules that lets two different software programs talk to each other without knowing how the other works internally.

**Example — a power socket / wall outlet:** When you plug any device into a wall socket, you don't need to know how the power plant generates electricity. The socket is a standard "interface": you follow its rules (the plug shape and voltage), and you get power. Similarly, an API gives you a standard way to request a service (like getting weather data or making a payment) without needing to know the complex code behind it.

---

## 7. Native vs. Cross-Platform Mobile Development

**Native development** means building an app separately for each platform using that platform's own language and tools — for example, Kotlin/Java for Android and Swift for iOS. Native apps usually give the best performance and full access to device features, but you must build and maintain two separate codebases, which costs more time and money.

**Cross-platform development** means writing one codebase that runs on both Android and iOS using frameworks like Flutter or React Native. This is faster and cheaper to maintain, though it can sometimes be slightly less performant or limited when accessing very specific device hardware. The choice depends on the budget, timeline, and performance needs of the project.

---

## 8. Flutter — Advantages and Limitations

**Three advantages:**
1. **Single codebase** — write once and run on Android, iOS, web, and desktop.
2. **Fast development** — "Hot Reload" lets you see code changes instantly without restarting the app.
3. **Beautiful, consistent UI** — rich set of customizable widgets that look the same across devices.

**Two limitations:**
1. **Large app size** — Flutter apps tend to be bigger than native apps.
2. **Smaller talent/library pool** — fewer third-party libraries and developers compared to long-established native ecosystems.

---

## 9. Git vs. GitHub

**Git** is a *version control tool* installed on your own computer. It tracks changes to your code, lets you save snapshots (commits), and lets you go back to earlier versions or work on different branches — all locally.

**GitHub** is an *online website/service* that hosts Git repositories in the cloud. It lets you store your Git projects online, share them, and collaborate with other people.

In short: **Git** is the tool that tracks your code; **GitHub** is the online place where you store and share that code with others.

---

## 10. The Seven Stages of the Software Development Life Cycle (SDLC)

1. **Planning** — Define the project's goals, scope, budget, and timeline. Decide what problem the software will solve.
2. **Requirement Analysis** — Gather and document exactly what the software must do (the features and needs of users).
3. **Design** — Create the blueprint: system architecture, user interface mockups, and database structure.
4. **Implementation (Coding)** — Developers write the actual code to build the software based on the design.
5. **Testing** — Check the software for bugs and errors, and make sure it meets all requirements and works correctly.
6. **Deployment** — Release the finished software to users / launch it in the live (production) environment.
7. **Maintenance** — Fix bugs, release updates, and improve the software over time after it is live.
