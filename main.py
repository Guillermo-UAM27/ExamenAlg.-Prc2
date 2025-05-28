from collections import deque
from datetime import datetime, date
from typing import List, Optional

class Prescription:
    def __init__(self, medications: List[str], dosage: str, instructions: str, recommendations: str = "", issued_on: Optional[date] = None):
        self.medications = [med.strip() for med in medications if med.strip()]  # Lista de medicamentos
        self.dosage = dosage.strip()
        self.instructions = instructions.strip()
        self.recommendations = recommendations.strip()
        self.issued_on = issued_on or date.today()

    def __repr__(self):
        meds = ", ".join(self.medications)
        result = f"Receta(medicamentos={meds}, dosis={self.dosage}, instrucciones={self.instructions}, fecha={self.issued_on.isoformat()}"
        if self.recommendations:
            result += f", recomendaciones={self.recommendations}"
        result += ")"
        return result

class Patient:
    def __init__(self, patient_id: int, name: str, reason: str):
        self.id = patient_id
        self.name = name.strip()
        self.reason = reason.strip()
        self.prescriptions: List[Prescription] = []

    def add_prescription(self, prescription: Prescription) -> None:
        self.prescriptions.append(prescription)
        print(f"→ Receta agregada para {self.name}: {prescription}")

    def get_history(self) -> List[Prescription]:
        return self.prescriptions

class HealthCenter:
    def __init__(self):
        self.waiting_queue = deque()
        self.attended_patients = {}
        self.patient_id_counter = 1

    def register_patient(self):
        name = input("Nombre del paciente: ").strip()
        if not name:
            print("Error: El nombre no puede estar vacío.")
            return
        reason = input("Motivo de consulta: ").strip()
        if not reason:
            print("Error: El motivo no puede estar vacío.")
            return
        patient = Patient(self.patient_id_counter, name, reason)
        self.waiting_queue.append(patient)
        self.attended_patients[self.patient_id_counter] = patient
        print(f"Paciente '{name}' (ID: {self.patient_id_counter}) registrado en la cola.")
        self.patient_id_counter += 1

    def attend_patient(self):
        if not self.waiting_queue:
            print("No hay pacientes en espera.")
            return
        patient = self.waiting_queue.popleft()
        print(f"Atendiendo a {patient.name} (ID: {patient.id}, Motivo: {patient.reason})")
        meds_input = input("Medicamentos (separados por coma, o presione Enter si no hay receta): ").strip()
        if meds_input:
            medications = [m.strip() for m in meds_input.split(",") if m.strip()]
            if not medications:
                print("Error: Debe ingresar al menos un medicamento válido.")
                return
            dosage = input("Dosis: ").strip()
            if not dosage:
                print("Error: La dosis no puede estar vacía.")
                return
            instructions = input("Instrucciones (opcional): ").strip()
            recommendations = input("Recomendaciones (opcional): ").strip()
            prescription = Prescription(medications, dosage, instructions, recommendations)
            patient.add_prescription(prescription)
        else:
            print("Sin receta registrada.")

    def check_history(self):
        try:
            patient_id = int(input("Ingrese ID del paciente: "))
        except ValueError:
            print("Error: ID inválido. Debe ser un número.")
            return
        patient = self.attended_patients.get(patient_id)
        if not patient:
            print(f"Paciente con ID {patient_id} no encontrado.")
            return
        history = patient.get_history()
        if not history:
            print(f"{patient.name} no tiene recetas registradas.")
        else:
            print(f"\nHistorial de recetas de {patient.name} (ID: {patient_id}):")
            for idx, prescription in enumerate(history, 1):
                print(f"  {idx}. Fecha: {prescription.issued_on.isoformat()}")
                print(f"     Medicamentos: {', '.join(prescription.medications)}")
                print(f"     Dosis: {prescription.dosage}")
                if prescription.instructions:
                    print(f"     Instrucciones: {prescription.instructions}")
                if prescription.recommendations:
                    print(f"     Recomendaciones: {prescription.recommendations}")

    def show_waiting(self):
        if not self.waiting_queue:
            print("No hay pacientes en espera.")
        else:
            print("\nPacientes en espera:")
            for patient in self.waiting_queue:
                print(f"- {patient.name} (ID: {patient.id}, Motivo: {patient.reason})")

    def show_menu(self):
        print("\n=== Centro de Salud ===")
        print("1. Registrar llegada de paciente")
        print("2. Atender siguiente paciente")
        print("3. Consultar historial de recetas")
        print("4. Ver pacientes en espera")
        print("5. Salir")

    def run(self):
        while True:
            self.show_menu()
            option = input("Seleccione una opción [1-5]: ").strip()
            if option == '1':
                self.register_patient()
            elif option == '2':
                self.attend_patient()
            elif option == '3':
                self.check_history()
            elif option == '4':
                self.show_waiting()
            elif option == '5':
                print("Cerrando Centro de Salud. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

def main():
    print("=== Sistema de Gestión de Centro de Salud ===")
    center = HealthCenter()
    center.run()

if __name__ == "__main__":
    main()