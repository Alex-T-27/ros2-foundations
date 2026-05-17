# ros2-foundations

Personal ROS 2 (Jazzy) learning workspace. Working through the core primitives
one at a time, skeleton-with-TODO style.

## Progress

- [x] Nodes — spin event loop, ros2 CLI, remapping, log levels, multi-timer
- [ ] Topics — in progress
  - [x] talker / listener pair (`std_msgs/String`)
  - [x] Twist driver wired up to turtlesim (`geometry_msgs/Twist` → `/turtle1/cmd_vel`)
  - [ ] transformer node (sub + pub in one node)
- [ ] Services
- [ ] Parameters
- [ ] Actions
- [ ] Launch files
- [ ] Custom msg / srv / action interfaces
- [ ] tf2

## Packages

- `src/topics_demo/` — talker, listener, driver (Twist publisher)
- `src/param_demo/` — early scratch, kept for reference

## Build

```bash
colcon build --packages-select topics_demo --symlink-install
source install/setup.bash
ros2 run topics_demo talker
```
