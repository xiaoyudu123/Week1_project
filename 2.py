from xmlrpc.server import SimpleXMLRPCServer

def receive_patient_data(patient_id, data):
    print(f"Received data from patient {patient_id}: {data}")
    return True

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(receive_patient_data, "receive_patient_data")
server.serve_forever()