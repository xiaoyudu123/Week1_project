import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000")

patient_id = 123
data = {
    "blood_pressure": "120/80",
    "heart_rate": 72,
    "blood_sugar": 90
}

if server.receive_patient_data(patient_id, data):
    print("Data sent successfully")
else:
    print("Failed to send data")






