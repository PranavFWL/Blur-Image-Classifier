**Blur Image Classifier**

Blur Image Classifier is a simple Python tool that helps you determine whether an image is blurry. It includes a sample image for testing and a Python script that analyzes and displays the blur level of the image.

**What’s inside the project**

* A sample image to try out the blur detection
* A Python script named `blurshow.py` that you can run to see how the blur classification works

**Purpose**

This project is designed to demonstrate a basic method for detecting blur in images. It’s a starting point for anyone working on image processing or computer vision tasks related to image quality. The `blurshow.py` script reads the image, applies a blur detection algorithm, and outputs visual results or blur scores to help you see how blurry the image is.

**How to set it up**

1. Clone the repository and navigate into the project folder
2. Make sure you have Python installed on your system
3. If needed, install any dependencies—typically OpenCV or similar libraries—for image handling
4. Place your own image in the folder if you wish to test beyond the provided sample image

**How to use it**

* Run the `blurshow.py` script from the command line
* The script will load the sample image (or any image you choose), process it, and output the blur score or show the processed result on screen
* Look at the output to understand whether the image is classified as sharp or blurry based on the algorithm used

**Possible future improvements**

You could expand this into a more robust blur detector by:

* Using more advanced blur detection techniques like Laplacian variance or machine learning
* Extending support to batch-process image folders
* Automating threshold settings to separate sharp from blurry images more effectively
* Adding visual overlays or GUI elements to illustrate blur regions
* Integrating it into a broader image quality analysis toolkit or embedding it in a web or desktop application

**Contributing**

If you’d like to contribute, feel free to:

* Fork the repository
* Experiment with new blur detection methods
* Test and refine thresholds or algorithms
* Submit your improvements via a pull request with a clear description of your changes


