import psutil
import time
import os

THRESHOLD = 75
VM_NAME = "auto-scale-vm-2"

def check_cpu():
    return psutil.cpu_percent(interval=2)

while True:
    cpu = check_cpu()
    print(f"CPU Usage: {cpu}%")

    if cpu > THRESHOLD:
        print("⚠️ CPU > 75%! Triggering scaling...")

        os.system(f"""
        gcloud compute instances create {VM_NAME} \
        --zone=asia-south1-a \
        --machine-type=e2-micro \
        --image-family=debian-11 \
        --image-project=debian-cloud
        """)

        print("✅ New VM created in GCP!")
        break

    time.sleep(5)
