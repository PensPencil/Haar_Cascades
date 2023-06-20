# Face Detection using OpenCV

This repository contains a Python script for detecting faces in images and videos using OpenCV's Haar cascades.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:
- OpenCV (`cv2`)
- Python 3.x

You can install OpenCV using pip:

```
pip install opencv-python
```

## Usage

1. Clone this repository:

```bash
git clone https://github.com/PensPencil/Haar_Cascades.git
```

2. Change into the cloned directory:

```bash
cd Haar_Cascades
```

3. Run the script:

```bash
python program.py
```

4. Follow the prompts in the terminal to provide input:

- For image input:
  - Enter 'image' when asked for input type.
  - Enter the path to the input image when prompted.
  
- For video input:
  - Enter 'video' when asked for input type.
  - Enter 'camera' to use your live camera as the video source, or provide the path to a video file.

The script will detect faces in the provided image or video and display the output with rectangles drawn around the detected faces.

**Note**: Press 'q' to exit the video input mode.

## Examples

### Image Input

```bash
Enter 'image' for image input or 'video' for video input: image
Enter the path to the input image: /path/to/your/image.jpg
```

### Video Input

```bash
Enter 'image' for image input or 'video' for video input: video
Enter 'camera' for live video, or video path: camera
```

or

```bash
Enter 'image' for image input or 'video' for video input: video
Enter 'camera' for live video, or video path: /path/to/your/video.mp4
```

## Credits

The face detection algorithm in this script utilizes OpenCV's Haar cascades. The Haar cascades XML file used for face detection can be found in the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
