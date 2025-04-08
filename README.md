----------------------------------------------------------

#  **DevOps Internship Assignment – Final Report**

------------------------------------------------------------

## Project Title


 ###  DevOps Infrastructure Automation & Monitoring Using Proxmox, Terraform, Jenkins, and Prometheus


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

## ⚙️ Architecture

1. **Infrastructure Provisioning**
   - A VM is provisioned on **Proxmox VE** using **Terraform**.
   - Optional: Containers (LXC or Docker) can also be provisioned via Terraform or manually.

2. **Networking**
   - VM and Container are configured with **static IPs** on a **virtual bridge** (`vmbr0`).
   - They can **communicate with each other** and access the internet.

3. **Flask Application Deployment**
   - A simple Flask app is deployed inside the VM.
   - It exposes:
     - `/` → returns a greeting.
     - `/compute` → performs a CPU-intensive task.
   - The app is run using **Gunicorn**, reverse-proxied by **Nginx**.
   - A **SystemD service** keeps the app running on VM reboot.

4. **Automation with Crontab**
   - A **cron job** runs every minute to hit the `/compute` endpoint using `curl`.

5. **CI/CD with Jenkins**
   - Jenkins pipeline:
     - Clones the Flask repo.
     - Sets up Python environment.
     - Installs dependencies.
     - Restarts Flask app SystemD service.
     - Verifies deployment via test curl request.
     - Setup the webhook
