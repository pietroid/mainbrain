# What needs to be done

- Create a thread for each unit -> will need to solve the data passing problem
- Create an input queue for each unit and output queue. It can be consumed by other agents that will enqueue it on its queues as well.
- Create the minimal time for processing message: Each unit can just start processing again after some minimal time.
- Use the brains structure and create files to describe examples of brains with different seeds
- Create simple seeds that keep the response very fast and very succint. We want small units for now.
- Test with architecture X -> X <-> X -> X. Two intermediate feedback layers, one receiver and one writer.