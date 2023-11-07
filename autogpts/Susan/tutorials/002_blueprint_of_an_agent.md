# AutoGPT Forge Part 2: The Blueprint of an AI Agent

**Written by Craig Swift & [Ryan Brandt](https://github.com/paperMoose)**

*8 min read*  


---

![Header](../../../docs/content/imgs/quickstart/t2_01.png)



Hello there, fellow pioneers of the AI frontier!

If you’ve landed here, chances are you’ve been bitten by the AI bug, eager to harness the incredible power of Large Language Models (LLMs) to build your own intelligent agents, commonly known as AutoGPTs. Remember the thrill when we set up our first project in the initial tutorial? Well, buckle up, because things are about to get even more exciting!

In this tutorial — [the sequel to our AI adventure](https://aiedge.medium.com/autogpt-forge-a-comprehensive-guide-to-your-first-steps-a1dfdf46e3b4) — we're going to embark on a journey into the very heart of an AI agent. Imagine peeling back the layers of an onion, but instead of tears, there’s a wealth of knowledge waiting at each layer. We’ll explore the intricate web of components that make these agents tick, take a guided tour of the revered AutoGPT Forge's project structure, and yes, get our hands back into the coding trenches to enhance the step function.

By the time we wrap up, you won’t just have a working LLM-powered agent; you’ll have one that passes the essential “write file” test, a testament to your growing prowess in the world of AI development.

So, my fellow agent developers, are you ready to leap into this world where code meets cognition? Let the exploration begin!

## What are LLM-Based AI Agents?

Before we add logic to our new agent, we have to understand what an agent actually IS. 

Large Language Models (LLMs) are state-of-the-art machine learning models that harness vast amounts of web knowledge. But what happens when you give the LLM the ability to use tools based on it's output? You get LLM-based AI agents — a new breed of artificial intelligence that promises more human-like decision-making in the real world.  

Traditional autonomous agents operated with limited knowledge, often confined to specific tasks or environments. They were like calculators — efficient but limited to predefined functions. LLM-based agents, on the other hand don’t just compute; they understand, reason, and then act, drawing from a vast reservoir of information.  

![AI visualising AI researchers hard at work](../../../docs/content/imgs/quickstart/t2_02.png)

The [Agent Landscape Survey](https://arxiv.org/abs/2308.11432) underscores this evolution, detailing the remarkable potential LLMs have shown in achieving human-like intelligence. They’re not just about more data; they represent a more holistic approach to AI, bridging gaps between isolated task knowledge and expansive web information.

Further expanding on this, [The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864) portrays LLMs as the foundational blocks for the next generation of AI agents. These agents sense, decide, and act, all backed by the comprehensive knowledge and adaptability of LLMs. It is an incrediable source of knowledge on AI Agent Research with almost 700 papers referenced and organised by reseach area.

## The Anatomy of an LLM-Based AI Agent

Diving deep into the core of an LLM-based AI agent, we find it’s structured much like a human, with distinct components akin to personality, memory, thought process, and abilities. Let’s break these down:  

![The Github repository](../../../docs/content/imgs/quickstart/t2_03.png)
Anatomy of an Agent from the Agent Landscape Survey  

### **Profile**  
Humans naturally adapt our mindset based on the tasks we're tackling, whether it's writing, cooking, or playing sports. Similarly, agents can be conditioned or "profiled" to specialize in specific tasks.

The profile of an agent is it's personality, mindset, and high-level instructions. Research indicates that merely informing an agent that it's an expert in a certain domain can boost its performance.

| **Potential Applications of Profiling** | **Description**                                                                                          |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------|
| **Prompt Engineering**                  | Tailoring agent prompts for better results.                                                              |
| **Memory Adjustments**                  | Modifying how an agent recalls or prioritizes information.                                               |
| **Action Selection**                    | Influencing the set of actions an agent might consider.                                                  |
| **Driving Mechanism**                   | Potentially tweaking the underlying large language model (LLM) that powers the agent.                    |

#### Example Agent Profile: Weather Expert

- **Profile Name:** Weather Specialist
- **Purpose:** Provide detailed and accurate weather information.
- **Preferred Memory Sources:** Meteorological databases, recent weather news, and scientific journals.
- **Action Set:** Fetching weather data, analyzing weather patterns, and providing forecasts.
- **Base Model Tweaks:** Prioritize meteorological terminology and understanding.

### **Memory**  
Just as our memories shape our decisions, reactions, and identities, an agent's memory is the cornerstone of its identity and capabilities. Memory is fundamental for an agent to learn and adapt. At a high level, agents possess two core types of memories: long-term and short-term.

|                   | **Long-Term Memory**                                                                                         | **Short-Term (Working) Memory**                                                                                 |
|-------------------|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| **Purpose**       | Serves as the agent's foundational knowledge base.                                                           | Handles recent or transient memories, much like our recollection of events from the past few days.              |
| **What it Stores**| Historical data and interactions that have taken place over extended periods.                                | Immediate experiences and interactions.                                                                         |
| **Role**          | Guides the agent's core behaviors and understanding, acting as a vast reservoir of accumulated knowledge.   | Essential for real-time tasks and decision-making. Not all these memories transition into long-term storage.     |


### **Planning**  
Planning is essential for agents to systematically tackle challenges, mirroring how humans break down complex problems into smaller tasks.
#### **1. What is Planning?**

- **Concept:** It's the agent's strategy for problem-solving, ensuring solutions are both comprehensive and systematic.
- **Human Analogy:** Just like humans split challenges into smaller, more manageable tasks, agents adopt a similar methodical approach.

#### **2. Key Planning Strategies**

| **Strategy**               | **Description**                                                                                           |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| **Planning with Feedback** | An adaptive approach where agents refine their strategy based on outcomes, similar to iterative design processes.|
| **Planning without Feedback** | The agent acts as a strategist, using only its existing knowledge. It's like playing chess, anticipating challenges and planning several moves ahead. |

### **Action**  
After the introspection of memory and the strategizing of planning, comes the finale: Action. This is where the agent’s cognitive processes manifest into tangible outcomes using the agents Abilities. Every decision, every thought, culminates in the action phase, translating abstract concepts into definitive results.  
Whether it’s penning a response, saving a file, or initiating a new process, the action component is the culmination of the agent’s decision-making journey. It’s the bridge between digital cognition and real-world impact, turning the agent’s electronic impulses into meaningful and purposeful outcomes.  

![t2_agent_flow.png](..%2F..%2F..%2Fdocs%2Fcontent%2Fimgs%2Fquickstart%2Ft2_agent_flow.png)
An example of how a basic agent works
## The Agent Protocol: The Linguistics of AI Communication

After diving deep into the anatomy of an agent, understanding its core components, there emerges a pivotal question: How do we effectively communicate with these diverse, intricately-designed agents? The answer lies in the Agent Protocol.  

### Understanding the Agent Protocol

At its essence, the Agent Protocol is a standardized communication interface, a universal “language” that every AI agent, regardless of its underlying structure or design, can comprehend. Think of it as the diplomatic envoy that ensures smooth conversations between agents and their developers, tools, or even other agents.  

In an ecosystem where every developer might have their unique approach to crafting agents, the Agent Protocol acts as a unifying bridge. It’s akin to a standardized plug fitting into any socket or a universal translator decoding myriad languages.  

## AutoGPT Forge: A Peek Inside the LLM Agent Template

Now we understand the architecture of an agent lets look inside the Forge. It’s a well-organized template, meticulously architected to cater to the needs of agent developers.

#### Forge’s Project Structure: A Bird’s-Eye View
![t2_diagram.png](..%2F..%2F..%2Fdocs%2Fcontent%2Fimgs%2Fquickstart%2Ft2_diagram.png)

The Forge's agent directory structure consists of three parts:
- **agent.py**: The heart of the Forge, where the agent's actual business logic is.  
- **prompts**: A directory of prompts used in agent.py's LLM logic.  
- **sdk**: The boilerplate code and the lower level APIs of the Forge.  

Let’s break them down.

#### Understanding the SDK

The SDK is the main directory for the Forge. Here's a breakdown:

- **Core Components**: These are key parts of the Forge including Memory, Abilities, and Planning. They help the agent think and act.
- **Agent Protocol Routes**: In the routes sub-directory, you'll see the Agent Protocol. This is how the agent communicates.
- **Database (db.py)**: This is where the agent stores its data like experiences and learnings.
- **Prompting Engine (prompting.py)**: This tool uses templates to ask questions to the LLM for consistent interactions.
- **Agent Class**: This connects the agent's actions with the Agent Protocol routes.

#### Configurations and Environment

Configuration is key to ensuring our agent runs seamlessly. The .env.example file provides a template for setting up the necessary environment variables. Before diving into the Forge, developers need to copy this to a new .env file and adjust the settings:  
- **API Key**: `OPENAI_API_KEY` is where you plug in your OpenAI API key.  
- **Log Level**: With `LOG_LEVEL`, control the verbosity of the logs.  
- **Database Connection**: `DATABASE_STRING` determines where and how the agent's data gets stored.  
- **Port**: `PORT` specifies the listening port for the agent's server.  
- **Workspace**: `AGENT_WORKSPACE` points to the agent's working directory.  

## To Recap

- **LLM-Based AI Agents**: 
  - LLMs are machine learning models with vast knowledge. When equipped with tools to utilize their outputs, they evolve into LLM-based AI agents, enabling human-like decision-making.

- **Anatomy of an Agent**: 
  - **Profile**: Sets an agent's personality and specialization.
  - **Memory**: Encompasses the agent's long-term and short-term memory, storing both historical data and recent interactions.
  - **Planning**: The strategy the agent employs to tackle problems.
  - **Action**: The stage where the agent's decisions translate to tangible results.
  
- **Agent Protocol**: 
  - A uniform communication interface ensuring smooth interactions between agents and their developers.

- **AutoGPT Forge**: 
  - A foundational template for creating agents. Components include:
    - **agent.py**: Houses the agent's core logic.
    - **prompts**: Directory of templates aiding LLM logic.
    - **sdk**: Boilerplate code and essential APIs.

Wrapping Up: From Blueprint to Reality
And there we have it — a comprehensive dive into the world of AutoGPTs. We’ve traversed the intricate pathways of agent anatomy, understood how the Agent Protocol fits in, and peeked under the hood of the Forge, understanding its core components and structure.

If this tutorial was a journey, think of it as a hike up a mountain. We started at the base, with a broad view of LLM-based AI agents, understanding their significance and potential. As we climbed, the trail led us to the anatomy of these agents, dissecting their structure and functionality. Nearing the summit, we delved into the Agent Protocol, understanding its pivotal role in standardizing communication. And finally, standing at the peak, we had a bird’s-eye view of the Forge, observing its organized layout and appreciating its design intricacies.

But remember, every mountain peak is the bottom of another adventure. Having grasped the theoretical aspects, it’s time to transition from blueprint to reality. Now the foundations have laid, our next steps involve breathing life into these concepts, turning lines of code into intelligent, responsive agents.

To all the budding agent developers out there, gear up for the next phase of our expedition — the hands-on time! Until then, keep the AI flame burning bright and never stop exploring.

Let's put this blueprint into practice in part 3!