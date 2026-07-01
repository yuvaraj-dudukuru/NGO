# Day 8 — Theory Questions & Answers

Introduction to Mobile Apps and Cross-Platform Development

---

### 1. What is a mobile app, and three ways it differs from a web app?

A **mobile app** is a software application built to run directly on a mobile device's operating
system (Android or iOS), installed from an app store and able to use the device's hardware and
features. It differs from a **web app** in that:

1. **Installation & access** — a mobile app is downloaded and installed from an app store and lives
   on the device, while a web app runs in a browser at a URL with nothing to install.
2. **Device access** — a mobile app can directly use device features (camera, GPS, sensors, push
   notifications, offline storage), whereas a web app has limited, permission-gated access.
3. **Performance & offline use** — a mobile app runs natively and can work offline, while a web app
   generally needs an internet connection and depends on the browser, so it can feel slower.

---

### 2. The four layers of the mobile ecosystem and how they interact

1. **Hardware** — the physical device (screen, processor, camera, sensors, battery).
2. **Operating System** — Android or iOS, which manages the hardware and provides services to apps.
3. **Applications** — the apps users install and run, built on top of the OS.
4. **App Stores / Distribution** — the Google Play Store and Apple App Store, through which apps are
   published, discovered, downloaded, and updated.

**How they interact:** the OS sits on top of the hardware and controls it; apps run on the OS and
request hardware access through it; the app stores are the channel that delivers apps to the device.
A user downloads an app from the store, the OS installs and runs it, and the app uses the OS to
reach the hardware.

---

### 3. Android vs iOS — openness, market share, development

- **Openness:** Android is **open source** and more flexible — multiple manufacturers, customizable,
  apps can be sideloaded. iOS is **closed/proprietary** — Apple controls hardware, software, and
  distribution tightly.
- **Market share:** Android has the **larger global market share** (especially in Asia, Africa, and
  developing markets); iOS has a smaller share but is dominant in markets like the US and tends to
  have higher-spending users.
- **Development:** Android apps are traditionally built in **Kotlin/Java** using Android Studio and
  run on many devices (more fragmentation to test). iOS apps are built in **Swift/Objective-C** using
  Xcode (Mac required) for a smaller, more uniform set of devices, with a stricter App Store review.

---

### 4. The four types of mobile apps and their trade-offs

1. **Native apps** — built specifically for one platform (Swift for iOS, Kotlin for Android). *Best
   performance and full device access, but expensive — you build and maintain two separate codebases.*
2. **Web apps** — websites that run in the browser and look app-like. *Cheap, instantly updated, work
   everywhere, but limited device access, need internet, and aren't in app stores.*
3. **Hybrid apps** — web code (HTML/CSS/JS) wrapped in a native container (e.g. Cordova/Ionic).
   *One codebase across platforms, but performance can lag and the experience may feel less native.*
4. **Cross-platform apps** — one codebase compiled to run natively on both platforms (e.g. Flutter,
   React Native). *Near-native performance and big time/cost savings, with some dependence on the
   framework and occasional need for platform-specific code.*

---

### 5. Difference between hybrid and cross-platform apps

A **hybrid app** is essentially a web app (HTML/CSS/JavaScript) running inside a native "wrapper"
(a WebView), so the UI is rendered as web content. A **cross-platform app** is written once in a
single language/framework (e.g. Dart with Flutter) that compiles to **actual native components or
native machine code**, giving performance and a look-and-feel much closer to native. In short:
hybrid wraps web code in a shell; cross-platform produces genuinely native output from one codebase.

---

### 6. Why cross-platform development exists and why businesses prefer it

It exists to solve the high cost of building and maintaining **two separate native apps** (one for
iOS, one for Android), which doubles development time, teams, and effort. Cross-platform frameworks
let teams write **one codebase that runs on both platforms**. Businesses prefer it because it means
**lower cost, faster time-to-market, easier maintenance** (fix once, deploy everywhere), a smaller
team, and **consistent behavior** across platforms — while still delivering near-native quality.

---

### 7. The three layers of mobile app architecture

1. **Presentation layer (UI)** — what the user sees and interacts with: screens, buttons, lists,
   forms. It handles input and displays data.
2. **Business logic layer** — the "brain" of the app: it processes input, applies rules, makes
   decisions, and coordinates what happens (e.g. validating a form, calculating a total).
3. **Data layer** — where data is stored and retrieved: local databases, device storage, and remote
   APIs/servers.

The presentation layer passes user actions to the business logic, which processes them and asks the
data layer to store or fetch data; results flow back up to be displayed. Separating them keeps the
app organized, testable, and easier to maintain.

---

### 8. Difference between UI and UX

**UI (User Interface)** is the *look* — the visual elements the user interacts with: layout, colors,
typography, buttons, icons. **UX (User Experience)** is the *feel* — the overall experience of using
the app: how easy, logical, fast, and satisfying it is to accomplish goals. UI is one part of UX: a
beautiful UI (good UI) can still be frustrating to use (bad UX), and good UX depends on flow,
usability, and accessibility, not just appearance.

---

### 9. Difference between authentication and authorization

**Authentication** verifies **who you are** — confirming identity, e.g. logging in with a username
and password or biometrics. **Authorization** determines **what you are allowed to do** — which
features, data, or actions you have permission to access once your identity is confirmed.
Authentication always comes first; authorization happens afterward. (E.g. logging in proves you're a
user = authentication; whether you can access the admin panel = authorization.)

---

### 10. The complete mobile app development workflow

1. **Planning** — define the problem statement, features (prioritized), screens, user flow, and
   wireframes (the blueprint, before any code).
2. **Design** — turn wireframes into detailed UI/UX designs (visuals, layout, navigation).
3. **Development** — write the code: build the UI, business logic, and data layer.
4. **Testing** — check for bugs and verify the app works correctly across devices.
5. **Deployment** — publish the app to the Google Play Store and Apple App Store.
6. **Maintenance** — fix bugs, release updates, add features, and respond to user feedback.

This is an iterative cycle: feedback from maintenance and testing feeds back into planning and
development for future versions. Planning first makes every later stage far smoother.
