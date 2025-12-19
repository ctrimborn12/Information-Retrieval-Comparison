def extract_patient_notes(documents):
    #takes a list of documents(as dictionaries) and extracts the patient id's and their clinical notes; returns list of patient notes
    patients = []
    for doc in documents:
        patient_notes_dictionary = {}
        
        #setup new filtered patient dictionary
        pid = doc["patient_id"]
        puid = doc["patient_uid"]
        notes = doc["patient"]
        patient_notes_dictionary["patient_id"] = pid
        patient_notes_dictionary["patient_uid"] = puid
        patient_notes_dictionary["notes"] = notes

        #add record to the list of patients 
        patients.append(patient_notes_dictionary)
    return patients