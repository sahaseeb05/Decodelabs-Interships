# 🌿 Iris Herbarium — Live In-Browser KNN Classifier

An elegant, interactive field-guide web application that implements a **K-Nearest Neighbors (KNN)** machine learning classification model completely from scratch in JavaScript. This project is built as part of the **DecodeLabs Artificial Intelligence Internship (Project 2: Data Classification Using AI)**.

---

## 📌 Project Overview

This application serves as an interactive bridge between data science concepts and tangible user interfaces. By leveraging the classic **Iris Dataset** (150 botanical samples), users can adjust floral measurements in real-time and observe how a machine learning model categorizes the specimen using pure algorithmic logic—no external API calls, python servers, or backend frameworks required.

The classification process visualizes the proximity of features using **Standardized Euclidean Distance** to ensure unbiased vector calculations across varying dimensional variances.

---

## 🛠️ Core AI & Machine Learning Concepts Implemented

To deliver precise predictions, the underlying architecture maps directly to core supervised learning workflows:

1. **Feature Vectors:** Represents 4 distinct anatomical measurements: Sepal Length, Sepal Width, Petal Length, and Petal Width.
2. **Feature Scaling (Standardization):** Implements manual `StandardScaler` calculations:
   $$\mu = \frac{1}{N}\sum x_i, \quad \sigma = \sqrt{\frac{1}{N}\sum(x_i - \mu)^2}, \quad z = \frac{x - \mu}{\sigma}$$
   This ensures that features with larger variance (like Petal Length) do not disproportionately dominate features with tighter variance (like Sepal Width).
3. **Distance Metric:** Utilizes the Standardized Euclidean Distance formula across a 4-dimensional hyper-space to evaluate mathematical similarity.
4. **Majority Voting:** Extracts the top $K$ nearest historical vectors, calculates the class distribution tally, and returns the modal species as the final inference verdict along with a confidence percentage.

---

## 🎨 User Interface Design Details

The visual system is designed to evoke a "Botanical Laboratory Field Guide" theme:
* **Vintage Aesthetic:** Features a high-contrast warm paper backdrop (`#F6ECD8`) complemented by a deep espresso type palette for optimal long-session legibility.
* **Dynamic Specimen Sketch:** An integrated live-rendered SVG flower element that morphs and transforms structurally in proportion to the slider values.
* **Mathematical Transparency:** Displays live confidence progress bars and renders a detailed checklist of the exact historical neighbor coordinates used to form the classification vote.

---

## 📂 Project Structure

```bash
├── index.html        # Monolithic file containing Semantic HTML5, CSS3 Variables & Vanilla JS Engine
└── README.md         # Detailed technical project documentation
