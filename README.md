# Main Brain

Main Brain is an idea on how to use individual AI units to produce more complex and more humane behavior.

## Unit

Each unit is a single instance of some AI chat interaction. The idea is that it represents some personality, trait or specialized area for some task. Characteristics

- Usually a single conversation, with some history with an AI.
- The history is variable according to the "memory capacity" of the unit
- Each unit receives regular prompts and can give an autocompletion.

### Interaction between units

The units interact solely based on prompts or responses. There is no previous protocol nor any language highly specialized to units to communicate. However, in this process, depending on the "profile" of each unity, it will give completly different responses for the same input.

### Profile of unit

Each unity has some sort of profile, that starts with a seed, e.g. some basic prompt that says something about how the unit should respond. For example, the seed could be something like "You have a highly analtyical skill and is very rational on decisions, demonstrating them in a detailed way.". Based on this, the chat would continue always on the same way, thus it would have some "imbued" profile even if there is no specific model tuning.

### History

The history of each unit is highly important on building a complex and rich profile, because it will provide also past ways to respond to new questions. It has this learning component, where it reinforces its previous response. The history implementation is a queue. So it means, older memories fade away and new memories come and stay for a while. The "while" means how much memory, or what is the size of the history. Obviously it means more computational resources and costs. So it's a tradeoff between complexity and spend. The idea is that more complex units tend to have bigger histories and less complex can survive with just the seed every iteration. It's important to say the seed always remain before the queue, so it always is considered as "first prompt".

## Distribution and decision

One important thing to even consider to start combining two units is how we will distribute information and decide which one will be relevant? It is two units, so the input goes to two units. And each unit produce a response, which also need to be merged. We can simplify and consider distribution as the same. However the merging needs to be done in a way. So the idea is that the merger has this role of merging two or more informations and it will be programmed accordingly. It has similar structure to a multi-layered neural network, where outputs are distributed to a bigger layer, and after that is converged to next neuron, where it will "decide" how to fire. 

### Final decider

The final neuron is the final decider on the process, which we could call "the consciousness" of the brain. It's the most top level which has very clear informations on what to do and how to do. 

### The base "generators"

The generators are the units that have some basic input, coming from sensory level (aka, prompts), and they diverge a lot to try to break in many different ways whay this simple message means. It runs in "parallel" between multiple different "personalities", so each unit can see different attributes from the message. It will then forward to another generators which can also generate more information from that information, giving more specialized information.

### The thought process

The thought process in this model is then a complete circle where it begins on external world (input prompts), this simple information is then complexified by the generators which created a lot of lines of thought. Then the role of the "deciders" is to link those different chaotic thoughts in a coese and good way. The final decider, the consciousness is which produce the final history of the brain's life, and projects action to the external world again. 

### Feedback loops

Some internal units can backfire some information to provide feedback, which is a really important thing for a rational and structured thought. For it to have feedback, basically a layer of neuron must be able to go "back" to previous layer and interfere itself in the future. It's the secret sauce for consciousness and the perception of time: connecting back the generate signal to produce new ideas based on your previous ideas. 

### Units talking

In the end, we can extend further and consider that each unit can talk to each other. But it is as a conversation. It talks and the other answers back. Depending on the answer, the unit itself can understand some way if the information it gave was relevant or not.

## Sample

In practice, we can produce a simple brain with 4 units:

- Listener unit: it will listen anything incoming from world (input)
- 2 middle units: Each unit must be the opposite of the other. The idea is to make a basic polarization.
- Final decider: it will merge the 2 previous units and produce a single response from this.

Those are the main connections, however each one can connect to another in a 2-way conversation. The input and output of the system will be conventioned on two extreme points. 

So in total, it will be 8 connections (two-way). The implementation is very simple: a response from one is a input for the other. Each unit will have a separate chat that means 4 individual chats. In the beginning it will be a very chaotic place but it will tend to converge somewhere in the future, depending on the external stimulus, because each unit will answer one thing to every other unit and will receive 3 different responses which need to understand the feedback.

### The units

Which is the role of the units? Maybe we can identify some basic prompt which can serve to every unit for now. Basically we need to stick to some principles for survival and relevance. The idea is that:

- Each unit wants to keep producing relevant content this means that the feedbacks seems good. If it doesn't seem, it's because the information was irrelevant. To detect if the information was relevant, it needs to understand how much the response was similar to what it said.
- Each unit wants to produce constant information per time, no more no less. It means that if recently it was producing less information or data, it will need to produce more, and vice-versa.
- Each unit must hear and extract what is more relevant, and respond to what it thinks is more relevant for that scenario.

The principles are the basic ones common to every unit. However they can be programmed to have some preponderance for other characteristics such as:

- Everything that comes you must negate it somehow
- You must shorten the content
- You must create new things and ideas from this content.
- You can search in the internet for newest informations about this.

### The collective unconscious

The deepest knowledge present on those models are naturally, what they have been trained for. With a huge corpus of information, basically stored on the whole internet, it can equate to some sort of "collective unconscious" where the machines have some inherited common ground of information to be able at least to understand some core concepts. However, the history and seed and stimulus will effectively determine the speciality of that unit.

## Wrapping it up:

The core of this MainBrain project is

- Each unit corresponds to a single instance of conversation, with some limitation of size. This limitation must be set via parameter.
- Each unit can connect to each other and the output of one goes to another and so on.
- Each unit must have some seed to start with. And this seed must be external to the history queue.