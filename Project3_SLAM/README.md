# Project 3: Simultaneous Localization and Mapping (SLAM)

This project was developed as part of the **Intelligent Autonomous Systems** course at Cornell Tech in Spring 2024. The objective was to construct accurate 2D occupancy grid maps of indoor environments while simultaneously localizing a mobile robot within the map. By leveraging wheel odometry, LiDAR sensor data, and particle filters, this project demonstrated enhanced mapping accuracy, robust trajectory tracking, and effective handling of noisy sensor data.

---

## Project Description

The SLAM project focused on integrating sensor data and implementing a particle filter-based SLAM algorithm to create detailed maps and localize the robot within the environment. This system allowed the robot to autonomously navigate and refine its understanding of the surroundings iteratively, demonstrating the potential for autonomous navigation and robotic applications.

### Key Features
- **Wheel Odometry and LiDAR Integration:** Combined wheel encoder and LiDAR sensor data for precise localization and mapping.  
- **Particle Filter Algorithm:** Used particle filters to estimate the robot’s pose and iteratively refine the map.  
- **Occupancy Grid Mapping:** Created 2D maps with marked free spaces, obstacles, and unknown regions.  
- **Visualization Tools:** Provided enhanced visualizations for debugging and performance analysis.  
- **Parameter Tuning:** Optimized computational efficiency and algorithm robustness for various datasets.

---

## Getting Started

### Prerequisites

1. **Software Requirements:**  
   - Python 3.7+  
   - Required libraries: `numpy`, `scipy`, `matplotlib`, `seaborn`, and `scipy.io` (for `.mat` file handling).  

2. **Data Requirements:**  
   - Datasets containing `.mat` files for LiDAR, encoder, and IMU data.  

3. **File Dependencies:**  
   - `load_data.py` and the `MapUtilsCython` folder containing `MapUtils_fclad.pyx` must be in the same directory as the main notebook.

---

### How to Use

1. **Prepare the Environment:**  
   - Place the provided datasets (`.mat` files) in a directory accessible by the notebook.  
   - Ensure `load_data.py` and `MapUtilsCython/MapUtils_fclad.pyx` are in the same directory as the notebook.  

2. **Update File Paths:**  
   - Modify the data directory paths in `SLAM.ipynb` to point to the `.mat` file locations.  

3. **Run the Notebook:**  
   - Execute the `SLAM.ipynb` notebook step-by-step:  
     - **Cell 1:** Initialize path tracing using wheel odometry measurements.  
     - **Cell 2:** Visualize raw LiDAR data points on a 2D map.  
     - **Cell 3:** Generate an occupancy grid map.  
     - **Cell 4:** Implement the full SLAM algorithm using particle filters.  
     - **Cell 5-12:** Refine and test the SLAM algorithm on additional datasets and unknown environments.  

4. **Adjust Parameters:**  
   - Tune map resolution and noise parameters in the notebook for your environment and datasets.

---

## Files Included

### Scripts
- **`SLAM.ipynb`**: Jupyter Notebook with the complete SLAM workflow, including data preprocessing, particle filter implementation, and mapping.

### Data
- **Sensor Data:** Required `.mat` files for LiDAR, encoder, and IMU data.  

---

## Project Reports

### Preliminary Writeup Checkup
For an early overview of the project’s progress, initial methodology, and foundational work, refer to the **[Preliminary Report](https://github.com/Ruiznogueras05/ECE-5242_Intelligent-Autonomous-Systems-Projects/blob/main/Project3_SLAM/media/Preliminary%20Report.pdf)**.

### Final Project Report
For a comprehensive explanation of the methodology, results, and insights from this project, refer to the **[Project 3 Report](https://github.com/Ruiznogueras05/ECE-5242_Intelligent-Autonomous-Systems-Projects/blob/main/Project3_SLAM/media/Project%203%20Report.pdf)**.

---

## Reflections and Future Enhancements

### Achievements
- Successfully developed a particle filter-based SLAM algorithm for accurate mapping and localization.  
- Demonstrated the effectiveness of integrating wheel odometry and LiDAR data in noisy environments.  
- Enhanced algorithmic efficiency and visualization tools for better performance analysis.  

### Future Enhancements
- **3D SLAM Implementation:** Extend the algorithm to support 3D environments.  
- **Dynamic Mapping:** Incorporate dynamic obstacles and real-time map updates.  
- **Enhanced Localization:** Explore advanced techniques for improved pose estimation accuracy.
