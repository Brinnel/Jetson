# Jetson
## WEBSITE:
https://www.jetson-ai-lab.com/  
**https://www.jetson-ai-lab.com/initial_setup_jon.html**  


## INTRODUCTION:

- Kit to start your journey of local generative AI evaluation and development  

### PACKING LIST:
- Jetson Orin NX core module
- Cooling fan
- Network card antenna
- Jetson Orin NX expansion board
- Power supply

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

<img src="Images/Storage.png" alt="Storage" width="900" />

Here we have NVMe SSD, hence we need **NVIDIA SDK Manage**

https://www.youtube.com/watch?v=FX2exKW_20E


SSD(Solid State Drives):  
SDK MANAGER to boot JetPack  
need to download SDK Manager  
Need UBUNTU 20.04 OR 22.04  

SSD Manager Download:  
https://www.youtube.com/watch?v=BaRdpSXU6EM&t=418s  
22:52  
https://www.jetson-ai-lab.com/initial_setup_jon_sdkm.html#overall-flow-sdk-manager-method


Advantages of SSD over micro SD:
-Faster
- Larger Capcity
- Cheaper
- Reiable

<img src="Images/SSD.png" alt="Storage" width="600" />


There are 2 types of SSD:
1. NVMe - Supports
2. SATA - Doesnt Support

<img src="Images/NVME_SATA.png" alt="Storage" width="600" />


## REFERENCE:
https://www.youtube.com/watch?v=-PjMC0gyH9s  
https://www.jetson-ai-lab.com/initial_setup_jon.html  
**http://www.yahboom.net/study/Jetson-Orin-NX**  
