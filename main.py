class Patient:
  def __init__(self, name, age, contact_info):
    self.name = name
    self.age = age
    self.contact_info = contact_info
    self.appointments = []

  def make_schedule_appointment(self, doctor : object, date : str, time : str):
    if doctor.availability:
      doctor.availability = False
      self.appointments.append({"doctor" : doctor, "date" : date, "time" : time})
      print("Appointment scheduled successfully!")
    else:
       print("Sorry, the doctor is not available at that date and time.")

  def cancel_appointment(self, doctor, date, time):
    for appointment in self.appointments:
      if appointment["doctor"] == doctor and appointment["date"] == date and appointment["time"] == time:
        self.appointments.remove(appointment)
        print("Appointment canceled succesfully!")
      else:
        print("Appointment not found")
        
        