FROM python:3.11-alpine

# Step 2: Set the isolated working directory inside the container
WORKDIR /app

# Step 3: Copy your 4 clean, structured asset tiers into the container image
COPY 1_inventory/ /app/1_inventory/
COPY 2_dealerships/ /app/2_dealerships/
COPY 3_crm_and_history/ /app/3_crm_and_history/
COPY 4_finance/ /app/4_finance/

# Step 4: Copy your main engine script into the container workspace
COPY app.py /app/app.py

# Step 5: Inform Docker that the container will listen on web port 8080
EXPOSE 8080

RUN adduser -D devopsuser && chown -R devopsuser:devopsuser /app
USER devopsuser


# Step 6: Start your python web application
CMD ["python", "app.py"]

