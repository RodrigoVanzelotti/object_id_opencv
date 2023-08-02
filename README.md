## Object Recognition Project

Object Recognition Project using some well-known libs:

- MediaPipe
- OpenCV
- Numpy

That's just the beggining of the project, the rest of it can't be shown or shared because it's a corporate project. Hope you enjoy

### Models
----

The Object Detector API requires an object detection model to be downloaded and stored in your project directory. [Here's the default directory - EfficientDet-Lite0 model](https://developers.google.com/mediapipe/solutions/vision/object_detector#efficientdet-lite0_model_recommended)

That's the recommended model because it's balanced between latency and accuracy. It's both accurate and lightweight enough for many use cases.

### Model Requirements and metadata
----
| Input         | Shape                                 | Description           |
|---------------|--------------------------------------|-----------------------|
| Input image   | Float32 tensor of shape [1, height, width, 3] | The normalized input image. |

| Output             | Shape                                  | Description                            |
|--------------------|---------------------------------------|----------------------------------------|
| detection_boxes    | Float32 tensor of shape [1, num_boxes, 4] | Box location of each detected object. |
| detection_classes  | Float32 tensor of shape [1, num_boxes]     | Indices of the class names for each detected object. |
| detection_scores   | Float32 tensor of shape [1, num_boxes]     | Prediction scores for each detected object. |
| num_boxes          | Float32 tensor of size 1                    | The number of detected boxes.          |



### Annotations and Learnings
----

- **running_mode**: IMAGE, VIDEO, LIVE_STREAM **[DEFAULT SET]**

- **display_names**: Default is en for english. Sets the language of the model **[DEFAULT SET]**

- **max_results**: "Defines the maximum number of returns given the top scores (-1 returns everything) **[DEFAULT SET]**

- **score_threshold**: Score Threshold, results below T are rejected.

- **category_allow_list**: Sets the optional list of allowed category names

- **category_deny_list**: Sets the optional list of category names that are not allowed


**It is not possible to use category_allow_list and category_deny_list simultaneously.**