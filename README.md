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

- ## ⏲️ Step 5: Crontab Automation

To ensure the Flask application runs continuously and recovers automatically, a cron-based automation was set up.

### ✅ 1. Created Automation Script

Wrote a shell script `start_flask.sh` in the home directory:

```bash
#!/bin/bash
cd /home/ubuntu/flask_app
/usr/bin/python3 app.py >> flask_output.log 2>&1
```

Made the script executable:

```bash
chmod +x start_flask.sh
```

### ✅ 2. Tested the Script Manually

Ran it manually to verify the app launches:

```bash
./start_flask.sh
```

Checked that Flask app was accessible on port 5000.

### ✅ 3. Scheduled It with Crontab

Opened crontab editor:

```bash
crontab -e
```

Added the following entry to run the script every 5 minutes (for testing purpose):

```bash
*/5 * * * * /home/ubuntu/start_flask.sh
```

Redirected logs to `flask_output.log` for troubleshooting.

Verified cron was registered:

```bash
crontab -l
```

### ✅ Outcome

Flask app auto-starts every 5 minutes.

Helps in ensuring the app restarts if it stops for any reason.

Can later adjust frequency or integrate with a proper `systemd` service for production.


---
