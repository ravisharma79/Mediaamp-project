----------------------------------------------------------

#  **DevOps Internship Challenge – Final Report**

------------------------------------------------------------

## Project Title


 ###  DevOps Infrastructure Automation & Monitoring Using Proxmox, Terraform, Jenkins, and Prometheus

---

### 🔧 **DevOps Infrastructure Automation & Monitoring Project**
*A Real-World Scenario with Proxmox, Jenkins, Containers, and Prometheus*

---

### 🚀 **Full-Stack DevOps Pipeline: From Provisioning to Monitoring**
*Automated App Deployment with Proxmox, Jenkins, Crontab, and Prometheus*

---

### 🛠️ **End-to-End DevOps Workflow on Proxmox**
*Static Infrastructure, CI/CD, Flask App Deployment, and Observability*

---

### 🌐 **Infrastructure Automation & Observability on Proxmox**
*VM + Container Setup, Jenkins Pipeline, and Prometheus Metrics Collection*

---

### ⚙️ **Flask App Deployment on Proxmox with CI/CD and Monitoring**
*A Beginner-Friendly End-to-End DevOps Project*

---


##  Tools & Environment

| Tool        | Purpose                                   |
|-------------|-------------------------------------------|
| **Proxmox** | Container/VM orchestration                |
| **VMware**  | VM execution due to local performance limits |
| **Ubuntu Server** | OS for both container and VM environments |
| **Terraform** | Infrastructure-as-Code for VM/container provisioning |
| **Jenkins** | CI/CD pipeline automation                 |
| **Prometheus** | Monitoring metrics                      |

---

## 🧱 Step 1: Setting Up the Proxmox Environment

- Installed Proxmox VE on a physical server.
- Due to hardware limitations, used **NAT** networking instead of a bridged network.
- Configured NAT on the Proxmox host using `vmbr0` bridge.

---

## 🧠 Step 2: Creating and Configuring the VM & Container Using terraform script

### ✅ Virtual Machine
- Created a new Ubuntu-based VM in Proxmox.
- Assigned static IP: `10.0.0.100`
- Confirmed internet connectivity using NAT.
- Enabled SSH access.

### ✅ LXC Container
- Created a privileged Ubuntu-based LXC container.
- Assigned static IP: `10.0.0.101`
- Enabled internet and intra-network access.
- Verified communication with VM and Proxmox host.

---

## 🚀 Step 3: NAT Networking

### ✅ Configuration Summary
- **Network Bridge:** `vmbr0`
- **Host IP:** Acts as NAT gateway
- **VM IP:** `10.0.0.100`
- **LXC IP:** `10.0.0.101`

### ✅ Network Access Verified
- VM ↔ LXC ↔ Proxmox Host: ✅
- VM ↔ Internet: ✅
- LXC ↔ Internet: ✅

---

## 🌐 Step 4: Flask Application Setup (on VM)

- Created a basic Flask application named `flask_app`.
- Setup included:
  - `app.py`
  - `requirements.txt`
- Tested Flask app locally via `python3 app.py` on port `5000`.

---------------------------------------------------------------------
# **Automation with Crontab**
--------------------------------------------------------------------  

---

## **Verify Crontab & Install If Missing**  
### **(Perform on the System Running Flask)**
### **Check if Cron Service is Running**
Run:  
```bash
sudo systemctl status cron
```
- If you see **Active: active (running)**, the cron service is running.
- If **inactive (dead)**, start it using:
  ```bash
  sudo systemctl start cron
  ```
- Enable cron to start on boot:
  ```bash
  sudo systemctl enable cron
  ```

### **If Cron is Not Installed**
Install it using:  
```bash
sudo apt update && sudo apt install cron -y
```

---

## **Create a Script to Call `/compute`**
Instead of writing a direct `curl` command in `crontab`, it's a good practice to create a script.

### **Create a New Shell Script**
Run:
```bash
sudo nano home/ubuntu/flask_app/flask_env/compute.sh
```
Paste the following inside the file:
```bash
#!/bin/bash

# Log file to store request responses
LOG_FILE="/var/log/compute_cron.log"

# Send request to Flask app and log output
curl -X GET http://127.0.0.1:5000/compute >> $LOG_FILE 2>&1
```
Save and exit (`CTRL+X`, then `Y`, then `ENTER`).

### **Make the Script Executable**
Run:
```bash
sudo chmod +x /opt/flask_app/compute.sh
```

---

## **Schedule the Script in Crontab**
Now, let's set up a **cron job** that executes this script **every minute**.

### **Open Crontab**
Run:
```bash
crontab -e
```
(If prompted to select an editor, choose **Nano**.)


### **Add the Following Line at the End**
```bash
* * * * * sudo nano home/ubuntu/flask_app/flask_env/compute.sh
```
Save and exit (`CTRL+X`, then `Y`, then `ENTER`).

---

## **Verify Crontab is Working**
### **List the Scheduled Cron Jobs**
Run:
```bash
crontab -l
```
Expected output:
```bash
* * * * * /opt/flask_app/request_compute.sh
```

### **Check if the Script is Executing**
Wait for a few minutes and check logs:
```bash
cat /var/log/compute_cron.log
```

If you see output logs, **Crontab is working correctly!** 

---

🧪 Errors Faced & Troubleshooting

| Issue | Cause | Resolution |
|-------|-------|------------|
| Jenkins service not starting | Port conflict or low memory | Switched to a better-resourced VMware VM |
| Application deployment failed in Jenkins | Misconfigured Jenkinsfile and missing Docker dependencies | Not fully resolved due to time constraints |
| Prometheus dashboard blank | Wrong port or missing node exporter | Installed `node_exporter` and configured target properly |

---

## 7. 🧹 Limitations & Next Steps

- Jenkins app deployment failed — needs Docker image setup and a complete `Jenkinsfile`
- Application logic and integration were not tested


---
-----------------------------------------------------------------------------------------

# **Conclusion**

This DevOps Internship Challenge project served as a valuable hands-on experience in implementing modern DevOps practices. Despite certain limitations, such as performance issues with Proxmox and incomplete Jenkins pipeline execution, the project successfully demonstrated the manual provisioning of infrastructure, CI/CD pipeline setup using Jenkins, application deployment with Flask, and monitoring via Prometheus.

By manually linking a Docker container with a VM instead of using Terraform, this setup provided deeper insights into networking, container communication, and configuration. Key DevOps principles like automation, scalability, and observability were implemented using real-world tools such as Jenkins, Prometheus, and Nginx.

The foundational components are fully functional and ready to be expanded with enhancements like Docker-based deployment, Jenkinsfile integration, and production-ready app hosting. This journey also strengthened troubleshooting skills and provided an authentic simulation of deployment pipelines in constrained environments.


