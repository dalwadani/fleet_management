# Introduction:
This is fleet management app written for [Frappe Framework] (https://github.com/frappe/frappe).

This app is still in **_Alpha_**. Do not use in production.
# Prerequisites:

[This app require installing ERPNEXT](https://github.com/frappe/erpnext)

# Features and To Do:
- [ ] Logging:
  - [x] Odometer
  - [ ] Fuel
- [ ] Scheduling:
  - [ ] Schedule maintenance  every X days or Y KM.
- [ ] Tracking:
  - [ ] The vehicle status:
    - Active (is beeing used right now) 
    - Available. 
    - Out of service
  - [x] The user (The employee who has the keys).
  - [ ] Location:
    - [ ] Automatically, GPS
    - [ ] Manually.
- [ ] Integrate with ERPNEXT:
  - [ ] Add to Chart of accounts as assets.
  - [ ] Maintenance expenses.
  - [ ] Fuel expenses
  - [ ] Insurance expenses

# Installation

[Install via Frappe Bench](https://github.com/frappe/bench)
using the following commands:
```
bench get-app fleet_management https://github.com/dalwadani/fleet_management
bench frappe --install_app fleet_management site1.local
```
