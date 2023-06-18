# Coin Detecting & Stealing Money Box
  * **2023-Spring Semester Yonsei University**
  * **IoT & Robotics Project**
  * **연세대학교 [IoT와 로보틱스] 프로젝트**
    - [작동 영상]

       https://github.com/dn0908/CoinStealingBox/assets/94898107/72dbe31f-9078-4505-980b-bd1d0e629edd

## Software Specifications
  - Window10 & Python 3.8
  - PyModi API
 
  **Image(Video) Preprocessed by OpenCV**
  ![image](https://github.com/dn0908/CoinStealingBox/assets/94898107/6bee7946-5452-4a82-a377-77d363c31b0e)



## Hardware Specifications
- PyMODI kit : LED, Button, Dial, Speaker, Display, SerialCommunication Module used
- Arduino UNO
- L9110 / HG7881 2 Channel Motor Driver
- TT Motor DC Gearbox Motor Dual Shaft 200RPM DC 3-6V
- 65mm Diameter White Wheel
- VISVI STUDY9 Webcam
  
  ### Circuit Diagram for UNO
    ![image](https://github.com/dn0908/CoinStealingBox/assets/94898107/2c0b0ed1-2d21-4af3-8d55-aba2a4def061)

  ### Circuit Diagram for MODI
    ![image](https://github.com/dn0908/CoinStealingBox/assets/94898107/65a91ab4-e5b1-414c-b0a1-f0d146d108b4)

## How to RUN
1. Run main.py to run Professor Box. (Running code on ProfessorBox.py)
    * Video Port
        ```
        python3 main.py
        ```
2. If using labtop's camera, change as below
        ```
        cam = cv2.VideoCapture(0) # 0 for default camera, 1,2 for additionally plugged in cameras...
        ```
