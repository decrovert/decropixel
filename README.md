# Decropixel

## Overview
Decropixel is an artificial intelligence
which draws simple pixel art and
uses feedback to improve its neural network.

## Technical details
The neural network contains an **input layer**,
an **output layer** and some **layers in between**.
Layers are no more than **arrays** of **neuron structures**.
Each **neuron** has a **connection** to
every other neuron in the next and previous layers,
if these exist.

Neurons can be **stimulated** with a certain level of stimulus.
When a neuron is fired,
it **passes** its stimulation
to all the neurons it has a connection to
in the next layer.
However, passing the stimulation value alone
**does not** provide the artificial intelligence with
the ability to **learn**.
In fact, if the stimuli were
the only fuel powering the behaviour of the neural network,
for the same stimuli,
it would **always** produce the same behaviour.
Therefore, this is where the other factors come into play.

First, there are **connection strengths**.
These will determine **how much** of the stimulus will
actually be passed onto the next neuron.
Each connection has a certain strength associated with it,
which can be **adjusted** to be stronger or weaker,
depending on the **feedback** given
to the artificial intelligence.

Then, there are **biases**.
Each neuron has a certain bias,
which represents a value that is
**added or subtracted** from the stimulus
(depending on whether it's positive or negative).
These can also be **adjusted** with relation to
the feedback received.

The neurons, their biases
and the connections they form between each other
form the **neural network** itself.
A simple, but complex, system that allows a machine to learn.

## License
The license must be included with
each distribution of this software
in the form of a `LICENSE` file.
