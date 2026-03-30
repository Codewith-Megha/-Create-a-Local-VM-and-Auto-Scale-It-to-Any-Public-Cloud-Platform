import os

os.system("""
gcloud compute instances create auto-instance \
--zone=asia-south1-a \
--machine-type=e2-micro \
--image-family=debian-11 \
--image-project=debian-cloud
""")