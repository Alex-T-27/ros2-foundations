# ros2-foundations

ROS 2 Jazzy learning workspace. Four Python packages covering the core
primitives, each with a small working demo using turtlesim for visualization.

## Primitives covered

- [x] Nodes — `Node` subclass, spin event loop, multi-timer
- [x] Topics — publishers, subscribers, transformer (sub + pub) nodes
- [x] Services — synchronous client (Futures) and server callbacks
- [x] Parameters — `declare_parameter` / `get_parameter`, CLI override
- [x] Launch files — Python launch description, remappings, multi-node startup
- [x] Actions — client (goal / feedback / result) and server (Fibonacci)
- [x] tf2 — broadcaster publishing turtle pose as a transform

## Packages

### `topics_demo/`
Publishers, subscribers, parameters, launch files.

- `talker` — publishes `std_msgs/String` on `/shouter`
- `listener` — subscribes to `/shouter` and logs
- `driver` — publishes `geometry_msgs/Twist` on `cmd_vel`, with `linear_speed` and `angular_speed` parameters
- `relay` — transformer: subscribes to `/shouter`, republishes uppercased on `/shouter_upper`
- `launch/turtle_drive.launch.py` — starts `turtlesim_node` and `driver` together, remapping `cmd_vel` → `/turtle1/cmd_vel`

### `services_demo/`
Request / reply.

- `spawn_client` — calls turtlesim's `/spawn` service to add a second turtle
- `spawn_server` — implements `example_interfaces/srv/AddTwoInts` on `/add_two_ints`

### `actions_demo/`
Long-running tasks with feedback.

- `rotate_client` — sends a goal to turtlesim's `/turtle1/rotate_absolute` action, logs feedback (`remaining` angle) and the final delta
- `fib_server` — implements `example_interfaces/action/Fibonacci`, streams the growing sequence as feedback

### `tf_demo/`
Coordinate frames.

- `turtle_broadcaster` — subscribes to `/turtle1/pose` and broadcasts a `world` → `turtle1` transform on `/tf`

## Build

From the workspace root:

```bash
colcon build --symlink-install
source install/setup.bash
```

## Run the demos

### Launch file — turtlesim + parameterized driver in one command
```bash
ros2 launch topics_demo turtle_drive.launch.py
```
Override the speed without rebuilding:
```bash
ros2 run topics_demo driver --ros-args -r cmd_vel:=/turtle1/cmd_vel -p linear_speed:=1.5
```

### Service — spawn a second turtle
```bash
ros2 run turtlesim turtlesim_node    # terminal 1
ros2 run services_demo spawn_client  # terminal 2
```

### Action — Fibonacci with live feedback
```bash
ros2 run actions_demo fib_server     # terminal 1
ros2 action send_goal --feedback /fibonacci \
  example_interfaces/action/Fibonacci "{order: 8}"  # terminal 2
```

### tf2 — verify the broadcast
```bash
ros2 run turtlesim turtlesim_node        # terminal 1
ros2 run turtlesim turtle_teleop_key     # terminal 2 (arrow keys)
ros2 run tf_demo turtle_broadcaster      # terminal 3
ros2 run tf2_ros tf2_echo world turtle1  # terminal 4 — live transform
```
