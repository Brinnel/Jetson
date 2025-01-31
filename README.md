# Jetson
## WEBSITE:
https://www.jetson-ai-lab.com/  
**https://www.jetson-ai-lab.com/initial_setup_jon.html**  


## INTRODUCTION:

- Kit to start your journey of local generative AI evaluation and development  


### APPLICATIONS:
#### LLM (Large language Models):
- Software that understands texts and languages
- Generates human like responses
- Eg: ChatGPT, Copilot, Gemini.

#### VLM (Visual language Models):
- Software that understands texts and Images.
- Used for image captioning, text to image generation.


#### ViTs (Vision Transformers)
- Image recognition neural network
- Image classification and detection
- Used in self driving cars, medical imaging.


### STORAGE:
- NVMe SSD for the OS and data, then you need to use **SDK Manager** to flash the latest JetPack on the NVMe SSD.
- In case you have an x86 PC running Ubuntu 22.04 or 20.04, then you can flash your Jetson Orin Nano Developer Kit with the latest firmware and JetPack all at once using **NVIDIA SDK Manager**.

<img src="Storage.png" alt="Storage" width="900" />

Here we have NVMe SSD, hence we need **NVIDIA SDK Manage**

https://www.youtube.com/watch?v=FX2exKW_20E


SSD(Solid State Drives):  
SDK MANAGER to boot JetPack  
need to download SDK Manager  
Need UBUNTU 20.04 OR 22.04  

SSD Manager Download:  
https://www.youtube.com/watch?v=BaRdpSXU6EM&t=418s  
22:52  
29:49
https://www.jetson-ai-lab.com/initial_setup_jon_sdkm.html#overall-flow-sdk-manager-method

JetsonZoo  
For all the tutorials and links for Python library downlaod.


Advantages of SSD over micro SD:
-Faster
- Larger Capcity
- Cheaper
- Reiable

<img src="SSD.png" alt="Storage" width="600" />


There are 2 types of SSD:
1. NVMe - Supports
2. SATA - Doesnt Support

<img src="NVME_SATA.png" alt="Storage" width="600" />


### SDK Manager  
NVIDIA SDK Manager as a one-stop shop that helps set up all the software you need to work with NVIDIA hardware (like Jetson Orin, GPUs, etc.).

Imagine you're building a gaming PC. Instead of searching for each driver, tool, or setting manually, you use a single program that installs everything in one go. That’s what the SDK Manager does for developers—it downloads, installs, and sets up the required software and tools automatically.

It saves time, reduces errors, and ensures everything is properly configured for development on NVIDIA platforms.

### PACKING LIST:
- Jetson Orin NX core module
- Cooling fan
- Network card antenna
- Jetson Orin NX expansion board
- Power supply


## SET UP:

### CASING:
1. https://www.youtube.com/watch?v=zxMn6U1DauE  (Board)
2. https://www.youtube.com/watch?v=fliiLNNoIWM  (Camera)
3. https://www.youtube.com/watch?v=tTHzI6u2lmE  (Anttena)

### COONECTION:

1. Fix the Antenna and Camera
2. Remove the HDMI connected from Monitor screen to CPU and connect it to Jetson
3. Remove the Keyboard and mouse connected from Monitor screen to CPU and connect it to Jetson
4. Connect the ethernet wire from CPU to the Jetson
5. Connect the Power Supply
6. 


## REFERENCE:
https://www.youtube.com/watch?v=-PjMC0gyH9s  
https://www.jetson-ai-lab.com/initial_setup_jon.html  
**http://www.yahboom.net/study/Jetson-Orin-NX**  
