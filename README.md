# Audio Splitter

This repository contains methods and tools for audio separation and manipulation, designed for use in the EGR 334 Final Project. Below is an overview of the project structure, requirements, and usage instructions.

---

## Project Structure

### **Method 1 - Instrument Separation**
Tools and scripts for separating audio tracks by instrument (e.g., vocals, drums, bass). This is ideal for creating backing tracks or isolating specific parts of an audio recording for analysis.

#### **Requirements**:
- **numpy**: For numerical operations and data handling.
- **librosa**: For audio analysis and processing.

  ```bash
  pip install librosa numpy spleeter
  ```

---

### **Method 2 - Lows, Mids, Highs**
This method splits audio into frequency ranges—lows, mids, and highs. It is commonly used for equalization analysis or creative audio remixing.

#### **Requirements**:
- **scipy**: For signal processing and transformations.
- **numpy**: For numerical operations and frequency computations.
- **matplotlib**: For visualizing frequency spectrums.

  ```bash
  pip install matplotlib numpy scipy
  ```

---

### **Trying Existing Libraries**
This section explores third-party libraries for audio splitting and manipulation, serving as an evaluation of alternative approaches.

#### **Requirements**:
- **ffmpeg**: A powerful tool for handling audio and video files. Install it from the [official website](https://ffmpeg.org/).
- **pydub**: For simple and high-level audio editing. Install with:
  ```bash
  pip install pydub demuc ffmpeg
  ```

---

## Installation Instructions

1. Ensure you have **Python 3.7 or higher** installed.
2. Install dependencies for each method using the provided commands under their respective sections.
3. Verify that additional tools like **FFmpeg** are installed and accessible via your system's PATH if using third-party libraries.

---

## Usage Instructions

1. **Instrument Separation (Method 1)**:
   - Navigate to the `Method 1 - Instrument Separation` directory.
   - Run the provided script(s) to process your audio file.
   - Refer to the comments within the scripts for input/output details.

2. **Frequency Splitting (Method 2)**:
   - Navigate to the `Method 2 - Lows, Mids, Highs` directory.
   - Execute the appropriate script to split your audio file into frequency bands.
   - Follow script instructions for further analysis or export.

3. **Using Existing Libraries**:
   - Explore the `Trying Existing Libraries` folder for experiments and additional insights.
   - Install the necessary tools and libraries before running the scripts.
  
---

ReadMe written with help of OpenAI. (2024). ChatGPT [Large language model]. https://chatgpt.com