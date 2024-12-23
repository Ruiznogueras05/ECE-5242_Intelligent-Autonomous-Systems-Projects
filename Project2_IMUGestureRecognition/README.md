# Project 2: IMU-Based Gesture Recognition with Hidden Markov Models (HMMs)

This project was developed as part of the **Intelligent Autonomous Systems** course at Cornell Tech in Spring 2024. The objective was to create a robust system for recognizing arm motion gestures using data from gyroscopes and accelerometers in an Inertial Measurement Unit (IMU). By employing Hidden Markov Models (HMMs), this project classified time-series sensor data into distinct gestures, laying the groundwork for real-time human-computer interaction systems and gesture-based interfaces.

---

## Project Description

The project aimed to process IMU data and apply machine learning techniques to classify arm gestures accurately. The core of this system utilized a custom implementation of the Baum-Welch algorithm to train the HMMs and K-means clustering to discretize raw sensor data into observable states. The system was validated using unseen data to demonstrate its generalization and accuracy.

### Key Features
- **IMU Data Processing:** Collected and preprocessed IMU data for gesture recognition.
- **Custom HMM Implementation:** Trained Hidden Markov Models using the Baum-Welch algorithm for gesture classification.
- **K-Means Clustering:** Discretized continuous IMU sensor data into observable states for HMM training.
- **Robust Testing and Validation:** Tested on multiple datasets to evaluate model accuracy and generalization.

---

## Getting Started

### Prerequisites
1. **Hardware Requirements:**
   - Access to an Inertial Measurement Unit (IMU) for collecting gesture data.
   
2. **Software Requirements:**
   - Python 3.7+.
   - Required libraries: `numpy`, `sklearn`, `pandas`, `matplotlib`, and `seaborn`.

### How to Use
1. **Prepare the Dataset:**
   - Ensure you have the following folders:
     - `RepeatedGestureTraining`: Contains repeated gesture data for HMM training.
     - `SingleGestureTraining`: Contains single gesture data for testing the HMM models.

2. **Update File Paths:**
   - Modify file paths in the `GestureRecognition.ipynb` notebook to point to your dataset directories. Look for comments marked `##IMPORTANT TO CHANGE##`.

3. **Run the Notebook:**
   - Execute the `GestureRecognition.ipynb` notebook step-by-step:
     - **Cell 1:** Load and visualize the IMU data.
     - **Cell 2:** Discretize raw sensor data using K-means clustering.
     - **Cell 3:** Initialize HMM parameters.
     - **Cell 4:** Implement and train HMM models using the Baum-Welch algorithm.
     - **Cell 5:** Plot the log-likelihood over iterations.
     - **Cell 6-7:** Preprocess test data and evaluate models.

4. **Save and Load Trained Models:**
   - Save trained HMM models to the `trained_models` folder for reuse.
   - Apply saved models to new test data without re-training.

---

## Files Included

### Scripts
- **`GestureRecognition.ipynb`**: Python notebook containing the entire workflow for training, testing, and evaluating HMM models on gesture data.

### Data
- **Training and Test Data:**
  - `RepeatedGestureTraining`: Training data for HMM models.
  - `SingleGestureTraining`: Testing data for evaluation.

### Additional
- **Trained Models Folder:** Contains saved HMM models and their respective log-likelihoods.
- **README.txt:** Original documentation.

---

## Project Report

For a detailed explanation of the methodology, results, and insights from this project, please refer to the **[Project 2 Report](https://github.com/Ruiznogueras05/ECE-5242_Intelligent-Autonomous-Systems-Projects/blob/main/Project2_IMUGestureRecognition/media/Project%202%20Report.pdf)**.

---

## Reflections and Future Enhancements

### Achievements
- Successfully classified gestures with high accuracy using HMMs.
- Demonstrated the generalization of the model on unseen test data.
- Developed a complete pipeline for IMU data processing and gesture recognition.

### Future Enhancements
- **Expanded Dataset:** Collect more diverse gestures to improve model robustness.
- **Real-Time Testing:** Adapt the system for real-time gesture recognition.
- **Improved Feature Engineering:** Incorporate additional features from IMU data to enhance classification accuracy.
