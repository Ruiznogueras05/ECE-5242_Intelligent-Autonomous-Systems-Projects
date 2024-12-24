# Project 4: Reinforcement Learning for Markov Decision Processes (MDPs)

This project was developed as part of the **Intelligent Autonomous Systems** course at Cornell Tech in Spring 2024. The objective was to apply reinforcement learning algorithms to solve decision-making tasks in various Markov Decision Process (MDP) environments, including a maze, Acrobot-v1, and MountainCar-v0. This work explored and implemented Q-learning, REINFORCE, and Value Iteration, providing insights into the adaptability and limitations of reinforcement learning in discrete and continuous state spaces.

---

## Project Description

The project involved designing and testing reinforcement learning strategies in diverse environments to optimize navigation and control policies. Tasks ranged from finding the shortest path in a maze to balancing and swinging up the Acrobot-v1, and navigating sparse-reward challenges in MountainCar-v0.

### Key Features
- **Value Iteration:** Optimized navigation in a custom maze environment, generating Q-tables and visualizing the optimal policies.
- **Q-Learning:** Refined policies in continuous and discrete state spaces, with applications in maze navigation and MountainCar-v0.
- **REINFORCE Algorithm:** Trained a policy network to master the Acrobot-v1 environment using gradient-based methods.
- **Performance Metrics:** Evaluated algorithms through Root Mean Square Error (RMSE), cumulative rewards, and visualization of learning curves.

---

## Getting Started

### Prerequisites

1. **Software Requirements:**  
   - Python 3.7+  
   - Required libraries: `numpy`, `matplotlib`, `gym`, and `tensorflow` for neural network implementation.  

2. **File Dependencies:**  
   - Ensure the following external files are in the same directory as `RLearning.ipynb`:  
     - `evaluation.py`  
     - `maze.py`  
   - Include the `Optimal_Q_table.npy` file for pre-trained Q-table access.

---

### How to Use

1. **Prepare the Environment:**  
   - Place `evaluation.py`, `maze.py`, and `Optimal_Q_table.npy` in the project directory.  

2. **Run the Notebook:**  
   - Open and execute `RLearning.ipynb` step-by-step:
     - **Cell 1:** Implements value iteration to generate and visualize the Q-table for the maze environment.  
     - **Cell 2:** Uses the Q-table from Cell 1 to simulate and visualize an episode in the maze.  
     - **Cell 3:** Implements Q-learning for the maze and MountainCar-v0 environments, visualizing performance metrics.  
     - **Cell 4:** Applies the REINFORCE algorithm to train a policy network for Acrobot-v1.  

3. **Adjust Parameters:**  
   - Update file paths and tune hyperparameters (e.g., learning rates, exploration rates) in the notebook for specific experiments.  

4. **Visualize Results:**  
   - Render outputs for Acrobot-v1 and MountainCar-v0, and analyze performance metrics plotted in the notebook.

---

## Files Included

### Scripts
- **`RLearning.ipynb`**: Jupyter Notebook with reinforcement learning workflows, including Q-learning, REINFORCE, and Value Iteration.  

### Data
- **Pre-trained Q-Table:**  
  - `Optimal_Q_table.npy`: Pre-computed Q-table for the maze environment.

### External Files
- `evaluation.py` and `maze.py`: Required Python scripts for the maze environment setup and evaluation.

---

## Project Report

For a detailed explanation of the methodology, results, and insights from this project, please refer to my **[Project 4 Report](https://github.com/Ruiznogueras05/ECE-5242_Intelligent-Autonomous-Systems-Projects/blob/main/Project4_ReinforcementLearning/media/Project%204%20Report.pdf)**.

---

## Reflections and Future Enhancements

### Achievements
- Successfully applied reinforcement learning to diverse MDP environments.  
- Implemented and evaluated Q-learning, Value Iteration, and policy gradient methods.  
- Visualized performance metrics and learning curves to gain critical insights into algorithm behavior.  

### Future Enhancements
- **Multi-Agent RL:** Explore reinforcement learning in multi-agent environments.  
- **Transfer Learning:** Apply learned policies to new but similar tasks for efficiency.  
- **Dynamic Exploration Strategies:** Improve exploration-exploitation trade-offs in sparse reward environments.  
