# Traffic Cone Detection and Distance Estimation Using GMM

## Project Overview  
This project involved designing and implementing an image processing system to detect traffic cones in images and estimate their real-world distances using **Gaussian Mixture Models (GMM)**. The system was developed as part of the **Intelligent Autonomous Systems** course at Cornell Tech, during Spring 2024. This project aimed to apply computer vision techniques and statistical modeling to enable accurate object detection and distance estimation, crucial for autonomous navigation applications.

### Task and Goal  
The main objectives of this project were:
- **Traffic Cone Detection:** Classify pixels corresponding to traffic cones in images and isolate them from the background.  
- **Distance Estimation:** Calculate the real-world distance to detected traffic cones using camera calibration and projective geometry.  
- **GMM Implementation:** Replace the built-in GMM library with a custom implementation for increased control and accuracy.

### System Highlights:
- **Color-Based Segmentation:** Utilized the HSV color space for robust segmentation of traffic cones under varying lighting conditions.  
- **Custom GMM Algorithm:** Developed a Gaussian Mixture Model to classify cone pixels and generate bounding boxes around detected cones.  
- **Precise Distance Calculations:** Applied projective geometry principles and camera calibration to ensure accurate distance measurements.  
- **Applications:** The system demonstrated potential for autonomous vehicles, robotics, and traffic monitoring.

---

## How To Use

### Prerequisites
Ensure you have the following:
1. **Folders:**  
   - **ECE5242Proj1-test:** Contains the test data set provided by the course. Ensure all file names are consistent with the naming convention required by the code.
   - **Proj1TrainImages:** Contains the training images used to develop and test the GMM algorithm.
2. **Dependencies:**  
   - Python 3.7+  
   - Required libraries: `OpenCV (cv2)`, `NumPy`, and `Matplotlib`.  

### Instructions
1. **Update File Paths:**  
   Open the script or notebook and ensure the file paths for the training and test datasets match your local directory structure. Modify paths under the comment **`##IMPORTANT TO CHANGE##`** to ensure proper execution.  

2. **Run the Pipeline:**  
   - Open and execute the Jupyter Notebook or Python script (`trainingImages.ipynb`) to run the GMM training and segmentation process.  
   - The script will process the training images, classify cone pixels, and generate bounding boxes.  

3. **Evaluate the Results:**  
   - Use the output distance measurements and visualized bounding boxes to assess the system’s performance.  
   - The system provides annotated images highlighting detected cones and the corresponding calculated distances.  

---

## Project Report
For a detailed explanation of the methodology, results, and insights from this project, please refer to the **[Project 1 Report](Project1_TrafficConeDetection/media/Project%201%20Report.pdf)**.

---

## Files Included
- **`labeling.py`**: Python script for labeling and segmenting cone images using GMM.  
- **`trainingImages.ipynb`**: Jupyter Notebook implementing the entire pipeline for GMM training, segmentation, and evaluation.  
- **`results.txt`**: Output file containing the calculated distances and performance metrics for the test data.  
- **`Proj1TrainImages/`**: Directory containing the training images used for GMM development.  
- **`ECE5242Proj1-test/`**: Directory containing the test images for evaluating the system.  

---

## Reflections and Future Enhancements
### Achievements:
- Developed a robust image processing pipeline for traffic cone detection and distance estimation.  
- Validated the system’s performance on diverse test data, demonstrating adaptability to varying lighting conditions.  

### Future Improvements:
- **Enhanced Distance Estimation:** Incorporate advanced camera calibration techniques for increased accuracy.  
- **3D Object Detection:** Extend the system to detect cones in three-dimensional space for real-world robotics applications.  
- **Real-Time Performance:** Optimize the implementation to process frames in real-time for autonomous navigation systems.  
