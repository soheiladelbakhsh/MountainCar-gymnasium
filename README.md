# MountainCar-gymnasium: different control policies
This repository contains a project focused on exploring and implementing different control policies for the classic MountainCar-v0 environment using the Gymnasium library.

The goal is to implement, test, and comparatively analyze the performance of three distinct control strategies to find the most effective method for teaching an agent to reach the goal state (the top of the right hill).

## Policies Implemented
The project evaluates the performance of three different agent behaviors:

### 1. Random Policy
- **Description:** The agent selects actions entirely at random from the set of possible actions.
- **Analysis Goal:** To serve as a baseline for comparison.

### 2. Simple Greedy Policy
- **Description:** An agent that makes deterministic decisions based solely on the car’s velocity:
- If velocity is positive *(v > 0)*, take the Right action.
- If velocity is negative *(v < 0)*, take the Left action.
- If velocity is zero *(v = 0)*, take the Right action.
