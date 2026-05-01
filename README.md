# MountainCar-gymnasium: different control policies
This repository contains a project focused on exploring and implementing different control policies for the MountainCar-v0 environment using the Gymnasium library.

The project evaluates the performance of three distinct policies:

Random Policy: An agent that selects actions completely at random.
Simple Greedy Policy: An agent that makes decisions based on the car’s velocity. Specifically, it moves right if velocity is positive, left if negative, and right if velocity is zero.
Semi-Greedy Policy: A more sophisticated policy that combines conditional logic with random exploration. It uses velocity to decide actions in certain ranges but resorts to random action selection in others.
The project involves:

Implementing and evaluating these policies within the MountainCar-v0 environment.
Calculating and visualizing the total reward, average reward, and standard deviation of rewards per episode for each policy.
Analyzing the performance of each policy to determine which one is most effective and understanding the reasons behind their performance differences.
This project provides a practical implementation and comparative analysis of reinforcement learning strategies for a classic control problem.