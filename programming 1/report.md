**Daim Bin Khalid - 251686775**
**Syeda Manal Ammad - 251606966**

Ma’am Umber Nisar
Programming 1

26th January 2022


# Report : Object Detection

## Object:

In our project we selected a horse as an object for detection.

## Details:

We used 80 images for training and 20 images for testing. Each was converted to .jpg format to run the process smoothly.

## [Google collab notebook link](https://colab.research.google.com/drive/1MqZ4brh5JrrL6YTma6tHHGYnDcmaOZYg?usp=sharing )
(colab notebook also submitted as a file alongside report)


## [Tutorial link](https://medium.com/swlh/tensorflow-2-object-detection-apiwith-google-colab-b2af171e81cc)


## Process:

We downloaded 100 images from google and labeled them using LabelImg software. We then divided them into two parts and used 80 of them for model training and 20 for testing. We made a label_map.pbtxt file for our dataset according to our object. We downloaded a pre-trained model provided by TensorFlow for training and a script(generate_tfrecords.py) to convert the annotations into the TFRecord format. Following the tutorial provided to us we made the required directory structure on Google Drive and added all the collected files to their respective directories. After that, we downloaded the colab notebook containing all the steps and relevant codes and loaded it on google colab. We then followed the tutorial and executed required cells which trained the model and detected the images of horses as objects successfully.
