% This file provides some model parameters that students can use to
% simulate the experiment

K = 0.01;
tau = 2;

% In Simulink, create a Transfer Function block to get a transfer function
% of the motor position: K/(tau * s + 1)
% The parameters will be generated in the workspace when you run this file
% so that your system transfer function is valid.

input_freq = 0.05; % NOTE: this frequency is in Hz. 

% Add a "signal generator" block. Set the input to "square" to get step
% responses. Then, set the frequency to input_freq value. You are allowed
% to change the frequency to observe longer/shorter runs.

input_amplitude = 0.01; % use a gain block to set the amplitude of the input

% Create a "Subsystem block" with two inputs: x_desired, and x_current
% this is similar to how the position control model is setup
% experimentally.

% Use gain blocks and summer blocks to create the PID controller.

% Using trial and error find the values and set the following in your
% workspace
kp = 0 % you must find a value that works well for proportional gain
ki = 0 % you must find a value that works well for integrator gain
kd = 0 % you must find a value that works well for derivative gain
disp("Set the values in your workspace, then run your Simulink model.")
